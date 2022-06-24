from fastapi import APIRouter, HTTPException, status
from exceptions.auth import AuthError
from exceptions.not_found import UserNotFound

from schemas.auth import LoginRequest, LoginResponse
from utils import auth


router = APIRouter(prefix="/v1/token", tags=["token"])


@router.post(
    path="",
    response_model=LoginResponse,
    status_code=status.HTTP_201_CREATED,
    description="Login and create token to made request",
)
def create_token(login: LoginRequest):
    """Login.

    Args:
        -login (LoginRequest): data to login. With the following structure:
            - email (str): user's email.
            - password (str): user's password.

    Raises:
        HTTPException: Invalid credentials.

    Returns:
        - LoginResponse: token as string.
    """
    try:
        is_user_logged, user = auth.verify_login_user(login.email, login.password)
    except AuthError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    except UserNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    if not is_user_logged:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    token = auth.create_access_token(login.email)
    return LoginResponse(token=token, id=user.id)
