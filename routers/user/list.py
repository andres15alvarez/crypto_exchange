from typing import List
from fastapi import APIRouter, status
from pony.orm import select, db_session
from models import User
from schemas import UserResponse, UserRequest
from utils import crypt


router = APIRouter()


@router.get('/user', tags=['user'], response_model=List[UserResponse])
def list_users():
    with db_session:
        users = select(user for user in User)
        return [UserResponse(**user.to_dict()) for user in users]


@router.post(
    '/user',
    tags=['user'],
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserRequest):
    user.password = crypt.hash_password(user.password)
    with db_session:
        User(**user.dict())
        return user
