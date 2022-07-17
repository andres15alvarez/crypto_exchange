from fastapi import status
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_list_currencies():
    response = client.get("/v1/currency")
    assert response.status_code == status.HTTP_200_OK
