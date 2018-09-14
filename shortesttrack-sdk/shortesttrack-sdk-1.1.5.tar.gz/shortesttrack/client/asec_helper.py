from urlobject import URLObject
import requests
import json

from shortesttrack.utils import getLogger

logger = getLogger()


class ASECHelper:
    def __init__(self, config_id: str) -> None:
        logger.info(f'ASECHelper {config_id}')
        self._config_id = config_id

    def get_asec(self, host: str, access_token: str) -> dict:
        url = URLObject(host).add_path('api/execution-metadata/v2/iservice-asec/{}'.
                                       format(self._config_id))

        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        logger.info(f'GET ASEC:'
                    f'URL: {url}'
                    f'HEADERS: {headers}')

        response = requests.get(url, headers=headers)
        logger.info(f'RESPONSE CODE: {response.status_code}')

        if response.status_code != 200:
            raise Exception(response.status_code)

        logger.info(f'RESPONSE CONTENT: {response.content.decode()}')
        return json.loads(response.content)
