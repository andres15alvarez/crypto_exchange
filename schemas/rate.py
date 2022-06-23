from pydantic import BaseModel, Field


class ExchangeRate(BaseModel):
    from_currency: str = Field(description="Cryptocurrency symbol")
    to_currency: str = Field(description="Cryptocurrency symbol")
    rate: float = Field(description="Exchange rate")

    class Config:
        schema_extra = {
            'example': {
                'from_currency': "BTC",
                'to_currency': "ETH",
                'rate': 20_000
            }
        }
