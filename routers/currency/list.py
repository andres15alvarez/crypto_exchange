# FastAPI
from typing import List
from fastapi import APIRouter, status

# Pony
from pony.orm import db_session, select

# Models
from models import Currency

# Schemas
from schemas import CurrencySchema


router = APIRouter(prefix="/v1/currency", tags=["currency"])


@router.get(
    path="",
    description="Retrieve all available currencies in the platform",
    response_model=List[CurrencySchema],
    status_code=status.HTTP_200_OK,
)
def list_currency():
    """Retrieve all available currencies in the platform.

    Returns:
        [CurrencySchema]: list of currencies. With the following structure:
        - name: str
        - symbol: str
    """
    with db_session:
        currencies = select(currency for currency in Currency)
        return [CurrencySchema(**currency.to_dict()) for currency in currencies]


@router.post(
    path="",
    description="Register a currency",
    response_model=CurrencySchema,
    status_code=status.HTTP_201_CREATED,
)
def create_currency(currency: CurrencySchema):
    """Create new currency.

    Returns:
        [CurrencySchema]: list of currencies. With the following structure:
        - name: str
        - symbol: str
    """
    with db_session:
        currency = Currency(**currency.dict())
        return CurrencySchema(**currency.to_dict())
