import requests
import json

from shortesttrack.client.utils import getLogger

logger = getLogger()
logger.setLevel('DEBUG')


class ISSConnector:
    def __init__(self, url: str, auth_custom_token: str = None) -> None:
        self._url = url
        logger.info(f'CONNECT ISERVICE: {url}')
        self._auth_custom_token = auth_custom_token
        logger.info(f'AUTH CUSTOM TOKEN: {auth_custom_token}')

    def send(self, msg: dict) -> bytes:
        header = {}
        if self._auth_custom_token is not None:
            header = {'Auth-Custom-Token': self._auth_custom_token}

        r = requests.post(self._url, json=msg, headers=header)

        logger.info(f'SEND MESSAGE(RESPONSE): {r.status_code}')
        if r.status_code != 200:
            raise Exception(r.status_code)

        logger.info(f'SEND MESSAGE(CONTENT): {r.content}')
        return r.content

    def is_health(self) -> bool:
        try:
            r = requests.get(self._url.replace('iter', 'healthz'))
            return json.loads(r.content.decode())['message'] == 'OK'
        except:
            return False

    def is_ready(self) -> bool:
        try:
            r = requests.get(self._url.replace('iter', 'readyz'))
            return json.loads(r.content.decode())['message'] == 'OK'
        except:
            return False
