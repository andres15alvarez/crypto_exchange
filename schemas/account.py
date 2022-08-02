from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, validator
from models.currency import Currency
from schemas.currency import CurrencySchema


class AccountResponse(BaseModel):
    amount: Decimal = Field(description="Amount of the currency")
    currency: CurrencySchema = Field(description="Currency of the account")
    created_at: datetime = Field(description="Datetime when the transaction was made")

    class Config:
        schema_extra = {
            "example": {
                "currency": {"name": "dolar", "symbol": "USD"},
                "amount": 20_000.00,
                "created_at": "2022-07-17T12:44:33.137017",
            }
        }

    @validator("currency", pre=True)
    def convert_currency_to_dict(cls, currency: int):
        if isinstance(currency, dict):
            return currency
        if not isinstance(currency, int):
            raise ValueError("currency must be an integer")
        currency = Currency.get(id=currency)
        return currency.to_dict()
