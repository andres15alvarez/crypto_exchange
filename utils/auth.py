from datetime import datetime
from fastapi import Request
# Pony
from pony.orm import db_session
from jose import ExpiredSignatureError, JWTError, jwt
# Settings
from settings import JWT_LIFE_TIME, JWT_ALGORITHM, SECRET_KEY
# Models
from models import User
# Utils
from utils import crypt


class AuthError(Exception):
    """Authentication error"""


def verify_login_user(email: str, password: str) -> bool:
    """Verify is the credentials are valid.

    Args:
        - email (str): email of the user.
        - password (str): raw password of the user.

    Returns:
        - bool: if the credentials are valid.
    """
    with db_session:
        user = User.get(email=email)
        return crypt.verify_password(password, user.password)


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
    authorization = request.headers['Authorization']
    return validate_access_token(authorization)
