from fastapi import APIRouter, Depends, HTTPException, status
from exceptions.auth import AuthError
from exceptions.not_found import UserNotFound

from schemas.auth import LoginRequest, LoginResponse
from schemas.rate import ExchangeRate
from utils import auth
from utils.coin_api import coin_api


router = APIRouter(prefix='/v1/exchange', tags=['token'])


@router.get(
    path='/rate',
    response_model=ExchangeRate,
    description='Get the exchange rate of two currencies'
)
def get_exchange_rate(from_currency: str, to_currency: str, current_user: Depends(auth.get_current_user)):
    response = coin_api.exchange_rates_get_specific_rate(from_currency, to_currency)
    return ExchangeRate(
        from_currency=from_currency,
        to_currency=to_currency,
        rate=response["rate"]
    )