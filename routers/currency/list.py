# FastAPI
from typing import List
from fastapi import APIRouter, status

# Pony
from pony.orm import db_session, select

# Models
from models import Currency

# Schemas
from schemas import CurrencyResponse


router = APIRouter(prefix="/v1/currency", tags=["currency"])


@router.get(
    path="",
    description="Retrieve all available currencies in the platform",
    response_model=List[CurrencyResponse],
    status_code=status.HTTP_200_OK,
)
def list_currency():
    """Retrieve all available currencies in the platform.

    Returns:
        [CurrencyResponse]: list of currencies. With the following structure:
        - name: str
        - symbol: str
    """
    with db_session:
        currencies = select(currency for currency in Currency)
        return [CurrencyResponse(**currency.to_dict()) for currency in currencies]
