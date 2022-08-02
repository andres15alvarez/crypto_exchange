# FastAPI
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

# Pony
from pony.orm import db_session, select
from models import User, Transaction, Currency, Account
from schemas.transaction import TransactionRequest, TransactionResponse
from utils import auth
from utils.coin_api import coin_api


router = APIRouter(prefix="/v1/transaction", tags=["transaction"])


@router.post(
    path="",
    description="Create a new exchange transaction",
    response_model=TransactionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_transaction(
    transaction: TransactionRequest, current_user: User = Depends(auth.get_current_user)
):
    with db_session:
        from_currency = Currency.get(symbol=transaction.from_currency)
        to_currency = Currency.get(symbol=transaction.to_currency)
        transaction.from_currency = from_currency.id
        transaction.to_currency = to_currency.id
        exchange_rate = coin_api.exchange_rates_get_specific_rate(
            from_currency.symbol, to_currency.symbol
        )["rate"]
        account_from_currency = Account.get(user=current_user, currency=from_currency)
        if account_from_currency is None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Balance insufficient"
            )
        if account_from_currency.amount < transaction.quantity:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Balance insufficient"
            )
        transaction_created = Transaction(
            **transaction.dict(), user=current_user.id, exchange_rate=exchange_rate
        )
        account = Account.get(user=current_user, currency=to_currency)
        if account is None:
            Account(
                user=current_user,
                currency=to_currency,
                amount=exchange_rate * transaction_created.quantity,
            )
        else:
            account.amount += exchange_rate * transaction_created.quantity
        return TransactionResponse(**transaction_created.to_dict())


@router.get(
    path="",
    description="Retrieve all transactions made by the user.",
    response_model=List[TransactionResponse],
    status_code=status.HTTP_200_OK,
)
def list_transactions(current_user: User = Depends(auth.get_current_user)):
    with db_session:
        transactions = select(t for t in Transaction if t.user == current_user)
        return [TransactionResponse(**t.to_dict()) for t in transactions]
