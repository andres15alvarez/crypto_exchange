import pytest
from fastapi.testclient import TestClient
from exceptions.auth import AuthError
from exceptions.not_found import UserNotFound
from utils import auth
from main import app


client = TestClient(app)


@pytest.fixture
def token():
    return (
        "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjODM1Yzg2Ny1hYjg5LTRlMjYtOWUyOC1kZmNhZWNjYTl"
        "mYmEiLCJzdWIiOiJhZDE1ZDU4MS0wY2QwLTQyYmItYjQ5OS0zNmEyYWM2Yjg3MTkiLCJzY3AiOiJ"
        "hcGlfY2xpZW50IiwiYXVkIjpudWxsLCJpYXQiOjE2NTkxMTYwMzgsImV4cCI6MTY1OTIwMjQzOH0"
        ".BvWfGdQQ3bD3KRaQu08Hnh2gK6RcTtK4WvMVZ3d9V78"
    )


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


def test_login_success(mocker, token):
    user = mocker.Mock()
    user.id = 1
    mocker.patch("routers.auth.login.auth.verify_login_user", return_value=(True, user))
    mocker.patch("routers.auth.login.auth.create_access_token", return_value=token)
    response = client.post(
        "/v1/token", json={"email": "andres15alvarez@gmail.com", "password": "holahola"}
    )
    assert response.status_code == 201
    assert response.json() == {"token": token, "id": 1}


def test_login_invalid_credentials(mocker):
    user = mocker.Mock()
    user.id = 1
    mocker.patch(
        "routers.auth.login.auth.verify_login_user", return_value=(False, user)
    )
    response = client.post(
        "/v1/token", json={"email": "andres15alvarez@gmail.com", "password": "holahola"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}


def test_login_user_not_active(mocker):
    user = mocker.Mock()
    user.id = 1
    mocker.patch(
        "routers.auth.login.auth.verify_login_user",
        side_effect=AuthError("User is not active"),
    )
    response = client.post(
        "/v1/token", json={"email": "andres15alvarez@gmail.com", "password": "holahola"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "User is not active"}


def test_login_user_not_found(mocker):
    user = mocker.Mock()
    user.id = 1
    mocker.patch(
        "routers.auth.login.auth.verify_login_user",
        side_effect=UserNotFound("User not found"),
    )
    response = client.post(
        "/v1/token", json={"email": "andres15alvarez@gmail.com", "password": "holahola"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
