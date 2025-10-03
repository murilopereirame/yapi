import yfinance as yf
from yfinance import Ticker
from app.models import TickerInfo

def fetch_tickers(tickers: list[str]) -> dict[str, TickerInfo]:
    tickers_data = yf.Tickers(str.join(" ", tickers))
    tickers_dict: dict[str, TickerInfo] = {}

    for symbol in tickers_data.tickers:
        tk: Ticker = tickers_data.tickers[symbol]
        tk_info = TickerInfo(symbol=symbol, price=tk.info.get('currentPrice'))

        tickers_dict[symbol] = tk_info

    return tickers_dict