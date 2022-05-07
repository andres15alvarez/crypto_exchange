# Python
from typing import List
# FastAPI
from fastapi import APIRouter, Depends, Request, status
# Pony
from pony.orm import select, db_session
# Models
from models import User
# Schemas
from schemas import UserResponse, UserRequest
# Utils
from utils import crypt, auth


router = APIRouter(prefix='/v1/user', tags=['user'])


def get_currenct_user(request: Request) -> User:
    authorization = request.headers['Authorization']
    return auth.validate_access_token(authorization)

@router.get(
    path='',
    description="Retrieve all users registered",
    response_model=List[UserResponse]
)
def list_users(current_user: User = Depends(get_currenct_user)):
    """Retrieve all users.

    Args:

    Returns:
    - list: users. With the following structure:
        - email: EmailStr
        - first_name: str
        - last_name: str
        - active: bool
    """
    with db_session:
        users = select(user for user in User)
        return [UserResponse(**user.to_dict()) for user in users]


@router.post(
    path='',
    description="Create a new user",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserRequest):
    """Create a new user.

    Args:
        user (UserRequest): user's data. With the following structure:
            - first_name (str, Optional): user's first name. Defaults None.
            - last_name (str, Optional): user's last name. Defaults None.
            - email (str): user's email, this field is unique.
            - password (str): user's password.

    Returns:
        UserResponse: user. With the following structure:
        - email: EmailStr
        - first_name: str
        - last_name: str
        - active: bool
    """
    user.password = crypt.hash_password(user.password)
    with db_session:
        User(**user.dict())
        return user
