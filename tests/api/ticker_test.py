import unittest
from collections import namedtuple
from unittest.mock import patch
from fastapi.testclient import TestClient

from app.main import app

class TickerTest(unittest.TestCase):
    client = TestClient(app)

    MockTickers = namedtuple("Tickers", "tickers")
    MockTicker = namedtuple("Ticker", "symbol info")

    mock_info = {"currentPrice": 200.0}
    mock_yfinance = MockTickers(tickers={"AAPL": MockTicker(symbol="AAPL", info=mock_info)})

    def test_fetch_tickers(self):
        """Test fetching ticker data"""
        with patch('yfinance.Tickers', return_value=self.mock_yfinance):
            response = self.client.get("/tickers?symbols=AAPL")
            assert response.status_code == 200

            response_json = response.json()
            self.assertEqual(response_json["AAPL"]["symbol"], "AAPL")
            self.assertEqual(response_json["AAPL"]["price"], self.mock_info["currentPrice"])

    def test_missing_args(self):
        """Test missing query parameters"""
        response = self.client.get("/tickers")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'detail': [{'input': None, 'loc': ['query', 'symbols'], 'msg': 'Field required', 'type': 'missing'}]})