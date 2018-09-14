import json
import requests

from urlobject import URLObject

from shortesttrack.client.utils import getLogger

logger = getLogger()
logger.setLevel('DEBUG')


class ISSCHelper:
    def __init__(self, config_id: str) -> None:
        logger.info(f'ISSC_ID: {config_id}')
        self._config_id = config_id

    def get_issc(self, host: str, access_token: str) -> dict:
        url = URLObject(host).add_path('api/execution-metadata/v2/issc/{}'.
                                       format(self._config_id))
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        logger.info(f'GET ISSC:'
                    f'URL: {url}'
                    f'HEADERS: {headers}')

        response = requests.get(url, headers=headers)
        logger.info(f'RESPONSE CODE: {response.status_code}')

        if response.status_code != 200:
            raise Exception(response.status_code)

        logger.info(f'RESPONSE CONTENT: {response.content.decode()}')
        return json.loads(response.content)
