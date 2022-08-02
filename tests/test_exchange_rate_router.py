from fastapi import status
from fastapi.testclient import TestClient
from routers.exchange.rate import coin_api
from main import app

client = TestClient(app)


def test_list_currencies(mocker, db_session):
    params = {"from_currency": "BTC", "to_currency": "USD"}
    mocker.patch.object(coin_api, "exchange_rates_get_specific_rate", return_value={"rate": 1})
    response = client.get("/v1/exchange/rate", params=params)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"from_currency": "BTC", "to_currency": "USD", "rate": 1}
