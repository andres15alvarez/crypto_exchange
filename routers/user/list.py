# FastAPI
from fastapi import APIRouter, status

# Pony
from pony.orm import db_session

# Models
from models import User

# Schemas
from schemas import UserResponse, UserRequest

# Utils
from utils import crypt


router = APIRouter(prefix="/v1/user", tags=["user"])


@router.post(
    path="",
    description="Create a new user",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
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
        - created_at: datetime
    """
    user.password = crypt.hash_password(user.password)
    with db_session:
        user = User(**user.dict())
        return UserResponse(**user.to_dict())
