import time

from pydantic import BaseModel, Field, validator

class TickerInfo(BaseModel):
    price: float | None = Field(None, gt=0, description='Price of one share at query date.')
    query_date: int = Field(default=int(time.time()), description='Date when the ticker was queried (in seconds).')
    symbol: str = Field("", description='Symbol of the ticker.')

    class Config:
        extra = "forbid"
        frozen = True