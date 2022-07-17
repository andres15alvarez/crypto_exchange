from fastapi import status
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_list_currencies():
    params = {"from_currency": "BTC", "to_currency": "USD"}
    response = client.get("/v1/exchange/rate", params=params)
    assert response.status_code == status.HTTP_200_OK
