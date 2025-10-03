from fastapi import APIRouter, HTTPException

from app.models import TickerInfo
from app.services import fetch_tickers

router = APIRouter(prefix="/tickers", tags=["Ticker"])

@router.get("", response_model=dict[str, TickerInfo])
def tickers(symbols: str) -> dict[str, TickerInfo]:
    ticker_list: list[str] = []

    for ticker in symbols.split(","):
        if not ticker == "":
            ticker_list.append(ticker)

    if len(ticker_list) == 0:
        raise HTTPException(status_code=400, detail="At least one ticker symbol is required")

    return fetch_tickers(ticker_list)