# FastAPI
from fastapi import APIRouter, Depends

# Pony
from pony.orm import db_session

# Models
from models import User

# Schemas
from schemas import UserResponse

# Utils
from utils import auth, permission


router = APIRouter(prefix="/v1/user", tags=["user"])


@router.get(
    path="/{id:int}",
    description="Retrieve an user instance",
    response_model=UserResponse,
)
def get_user(id: int, current_user: User = Depends(auth.get_current_user)):
    """Retrieve an user.

    Args:

    Returns:
    - UserResponse: user. With the following structure:
        - email: EmailStr
        - first_name: str
        - last_name: str
        - active: bool
    """
    with db_session:
        user = User.get(id=id)
        permission.is_same_user(current_user, user)
        return UserResponse(**user.to_dict())


@router.delete(
    path="/{id:int}", description="Delete an user", response_model=UserResponse
)
def delete_user(id: int, current_user: User = Depends(auth.get_current_user)):
    with db_session:
        user = User.get(id=id)
        permission.is_same_user(current_user, user)
        user.active = False
        return UserResponse(**user.to_dict())
