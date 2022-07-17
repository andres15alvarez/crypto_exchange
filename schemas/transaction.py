from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, validator
from models.currency import Currency
from schemas.currency import CurrencyResponse


class TransactionRequest(BaseModel):
    from_currency: str = Field(description="Currency symbol to exchange")
    to_currency: str = Field(description="Currency symbol to receive")
    quantity: Decimal = Field(description="Quantity in from_currency to exchange")

    class Config:
        schema_extra = {
            "example": {
                "from_currency": "USD",
                "to_currency": "BTC",
                "quantity": 20_000.00
            }
        }


class TransactionResponse(TransactionRequest):
    exchange_rate: Decimal = Field(description="Exchange rate")
    from_currency: CurrencyResponse = Field(description="Currency exchanged")
    to_currency: CurrencyResponse = Field(description="Currency received")
    created_at: datetime = Field(description="Datetime when the transaction was made")

    class Config:
        schema_extra = {
            "example": {
                "from_currency": {
                    "name": "dolar",
                    "symbol": "USD"
                },
                "to_currency": {
                    "name": "bitcoin",
                    "symbol": "BTC"
                },
                "quantity": 20_000.00,
                "exchange_rate": 0.00005,
                "created_at": "2022-07-17T12:44:33.137017",
            }
        }

    @validator("from_currency", pre=True)
    def convert_from_currency_to_dict(cls, from_currency: int):
        if isinstance(from_currency, dict):
            return from_currency
        if not isinstance(from_currency, int):
            raise ValueError("from_currency must be an integer")
        from_currency = Currency.get(id=from_currency)
        return from_currency.to_dict()

    @validator("to_currency", pre=True)
    def convert_to_currency_to_dict(cls, to_currency: int):
        if isinstance(to_currency, dict):
            return to_currency
        if not isinstance(to_currency, int):
            raise ValueError("to_currency must be an integer")
        to_currency = Currency.get(id=to_currency)
        return to_currency.to_dict()
