import json
import requests
from requests.exceptions import HTTPError, Timeout, RequestException, ConnectionError


class HttpRequest:
    def __init__(self, url):
        self.__url = url

    def get_response(self, method, params={}):
        url = self.__url + method
        try:
            result = requests.post(url, data=params).text
        except (HTTPError, ConnectionError, Timeout, RequestException, ConnectionError) as e:
            result = {"status": 500, "data": e}

        return result

    @staticmethod
    def json_parse(json_str):
        try:
            result = json.loads(json_str)
        except Exception:
            result = False

        return result
