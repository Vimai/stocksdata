from unittest import TestCase
from datetime import datetime
from stocksdata.PolygonApiClient import PolygonApiClient


class TestPolygonApiClient(TestCase):
    def test_get_open_close_data(self):
        client = PolygonApiClient("https://api.polygon.io", "")
        data = datetime.strptime("2023-01-09", "%Y-%m-%d").date()
        response = client.get_open_close_data("AAPL", data)
        assert (type(response) == dict)
