import unittest
from collections import namedtuple
from unittest.mock import patch

from app.services import fetch_tickers

class TickerFetcherTests(unittest.TestCase):
    def test_fetch_tickers(self):
        """Test fetching ticker data"""
        self.shortDescription()
        MockTickers = namedtuple("Tickers", "tickers")
        MockTicker = namedtuple("Ticker", "symbol info")

        mock_info = { "currentPrice": 200.0 }
        mock_yfinance = MockTickers(tickers={"AAPL": MockTicker(symbol="AAPL", info=mock_info)})

        with patch('yfinance.Tickers', return_value=mock_yfinance):
            info = fetch_tickers(tickers=["AAPL"])
            self.assertEqual(info["AAPL"].symbol, "AAPL")
            self.assertEqual(info["AAPL"].price, 200.0)