from fastapi import status
from fastapi.testclient import TestClient
from routers.currency.list import Currency
from main import app


client = TestClient(app)


def test_list_currencies(mocker):
    mocker.patch.object(Currency, "to_dict", return_value={"name": "bitcoin", "symbol": "BTC"})
    mocker.patch("routers.currency.list.select", return_value=[Currency])
    response = client.get("/v1/currency")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{"name": "bitcoin", "symbol": "BTC"}]
