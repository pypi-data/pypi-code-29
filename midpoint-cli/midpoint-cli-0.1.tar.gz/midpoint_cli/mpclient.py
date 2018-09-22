from argparse import Namespace
from urllib.parse import urlparse


class RestApiClient:
    def __init__(self, url: str, username: str, password: str):
        self.url = self.sanitize_url(url)
        self.username = username
        self.password = password

    def sanitize_url(self, url: str) -> str:
        parsed_url = urlparse(url)
        return parsed_url


class MidpointClient:

    def __init__(self, ns: Namespace):
        self.api_client = RestApiClient(ns.url, ns.username, ns.password)
