import requests
from datetime import date


class PolygonApiClient:
    def __init__(self, host, api_key):
        self.__host = host
        self.__api_key = api_key
        self.__default_header = {
            "Content-Type": "application/json",
        }
        self.__query_param = {
            "apiKey": self.__api_key,
        }

    def get_open_close_data(self, ticker: str, data: date):
        url = self.__host + f'/v1/open-close/{ticker}/{data.isoformat()}'
        response = requests.get(url, params=self.__query_param)
        if response.status_code == 200:
            return response.json()
        return {}
