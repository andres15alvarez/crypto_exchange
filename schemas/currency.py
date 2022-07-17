from pydantic import BaseModel, Field


class CurrencyResponse(BaseModel):
    name: str = Field(description="Cryptocurrency name")
    symbol: str = Field(description="Cryptocurrency symbol")

    class Config:
        schema_extra = {"example": {"symbol": "BTC", "name": "bitcoin"}}
