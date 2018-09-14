import requests
import json

from shortesttrack.utils import getLogger

logger = getLogger()


class ISSConnector:
    def __init__(self, url: str, auth_custom_token: str = None) -> None:
        self._url = url
        logger.info(f'ISSConnector {url} {auth_custom_token}')
        self._auth_custom_token = auth_custom_token

    def send(self, msg: dict) -> bytes:
        headers = {'Auth-Custom-Token': self._auth_custom_token} if self._auth_custom_token else {}

        logger.info(f'request POST {self._url} {msg}')
        r = requests.post(self._url, json=msg, headers=headers)

        logger.error(f'response {r.status_code} {r.content}')
        if r.status_code != 200:
            raise Exception(f'Error send message {msg}: {r.status_code}')

        return r.content

    def is_health(self) -> bool:
        try:
            r = requests.get(self._url.replace('iter', 'healthz'))
            return json.loads(r.content.decode())['message'] == 'OK'
        except:
            logger.exception(f'Service {self._url} is not healthy')
            return False

    def is_ready(self) -> bool:
        try:
            r = requests.get(self._url.replace('iter', 'readyz'))
            return json.loads(r.content.decode())['message'] == 'OK'
        except:
            logger.exception(f'Service {self._url} is not ready')
            return False
