from typing import List
from fastapi import APIRouter, Depends, status
from pony.orm import db_session, select
from models import User, Account
from schemas.account import AccountResponse
from utils import auth, permission


router = APIRouter(prefix="/v1/user/{id:int}/account", tags=["user"])


@router.get(
    path="",
    description="Retrieve all accounts by the user.",
    response_model=List[AccountResponse],
    status_code=status.HTTP_200_OK,
)
def list_accounts(id: int, current_user: User = Depends(auth.get_current_user)):
    with db_session:
        user = User.get(id=id)
        permission.is_same_user(current_user, user)
        accounts = select(a for a in Account if a.user == current_user)
        return [AccountResponse(**a.to_dict()) for a in accounts]
