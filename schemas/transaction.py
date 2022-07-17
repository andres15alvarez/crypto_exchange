from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field

from schemas.user import UserResponse


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
    user: UserResponse = Field(description="User whom exchange the currency")
    exchange_rate: Decimal = Field(description="Exchange rate")
    created_at: datetime = Field(description="Datetime when the transaction was made")

    class Config:
        schema_extra = {
            "example": {
                "from_currency": "USD",
                "to_currency": "BTC",
                "quantity": 20_000.00,
                "user": {
                    "active": True,
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "johndoe@email.com",
                    "password": "password",
                },
                "exchange_rate": 0.00005,
                "created_at": "2022-06-23 16:00:00",
            }
        }
