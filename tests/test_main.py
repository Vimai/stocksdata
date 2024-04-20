from http import HTTPStatus
from unittest import TestCase

from starlette.testclient import TestClient

from stocksdata.main import app


class Test(TestCase):

    def test_create_stock(self):
        client = TestClient(app)

        response = client.post(
            '/stock/AAPL',
            json={
                'amount': 5
            },
        )
        assert response.status_code == HTTPStatus.CREATED
        assert response.json() == {
            'amount': 5,
            'ticker': 'AAPL'
        }
