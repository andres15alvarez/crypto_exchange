import pytest
from exceptions.auth import AuthError
from utils import auth


def test_create_access_token():
    email = "andres15alvarez@gmail.com"
    token = auth.create_access_token(email)
    assert isinstance(token, str)


def test_check_invalid_access_token():
    token = "hellohello"
    with pytest.raises(AuthError):
        auth.validate_access_token(token)


def test_check_invalid_bearer_token():
    token = "Bearer hellohello"
    with pytest.raises(AuthError):
        auth.validate_access_token(token)
