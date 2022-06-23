from datetime import datetime
from typing import Tuple
from fastapi import Request
# Pony
from pony.orm import db_session
from jose import ExpiredSignatureError, JWTError, jwt
# Settings
from settings import JWT_LIFE_TIME, JWT_ALGORITHM, SECRET_KEY
# Models
from models import User
# Exceptions
from exceptions.auth import AuthError
from exceptions.not_found import UserNotFound
# Utils
from utils import crypt


def verify_login_user(email: str, password: str) -> Tuple[bool, User]:
    """Verify is the credentials are valid.

    Args:
        - email (str): email of the user.
        - password (str): raw password of the user.

    Returns:
        - bool: if the credentials are valid.
        - User: user instance
    """
    with db_session:
        user = User.get(email=email)
        if user is None:
            raise UserNotFound("User not found")
        if not user.active:
            raise AuthError("User is not active")
        return crypt.verify_password(password, user.password), user


def create_access_token(email: str) -> str:
    """Create jwt.

    Args:
        email (str): email of the user.

    Returns:
        - str: bearer jwt
    """
    data = {'sub': email, 'exp': datetime.utcnow() + JWT_LIFE_TIME}
    return jwt.encode(data, SECRET_KEY, algorithm=JWT_ALGORITHM)


def validate_access_token(token: str) -> User:
    """Validate the bearer token.

    Args:
        - token (str): jwt to validate.

    Raises:
        - AuthError: Invalid token
        - AuthError: JWTError

    Returns:
        - User: object.
    """
    parts = token.split(' ')
    if parts[0] != 'Bearer':
        raise AuthError('Invalid token')
    try:
        data = jwt.decode(parts[1], SECRET_KEY, algorithms=JWT_ALGORITHM)
    except (JWTError, ExpiredSignatureError) as e:
        raise AuthError(str(e))
    with db_session:
        try:
            return User.get(email=data.get('sub'))
        except User.ObjectNotFound:
            raise AuthError('Invalid token')

def get_current_user(request: Request) -> User:
    """Get the user object from the authorization token.

    Args:
        - request (Request): object.

    Returns:
        - User: user instance
    """
    if 'Authorization' not in request.headers:
        raise AuthError('Authorization is required')
    authorization = request.headers['Authorization']
    return validate_access_token(authorization)
