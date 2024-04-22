import requests
from datetime import date
import urllib.parse


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
        path = f'/v1/open-close/{ticker}/{data.isoformat()}'
        url = urllib.parse.urljoin(self.__host, path)
        url += "?" + urllib.parse.urlencode(self.__query_param)
        response = requests.get(
            url,
            headers=self.__default_header,
        )

        if response.status_code == 200:
            return response.json()
        return {}
