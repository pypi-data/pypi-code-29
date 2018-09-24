import json

from urlobject import URLObject

from shortesttrack.utils import getLogger, do_get

logger = getLogger()


class ASECHelper:
    def __init__(self, config_id: str) -> None:
        logger.info(f'ASECHelper {config_id}')
        self._config_id = config_id

    def get_asec(self, host: str, access_token: str) -> dict:
        url = URLObject(host).add_path(f'api/execution-metadata/v2/iservice-asec/{self._config_id}')
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        response = do_get(url, headers=headers)

        return json.loads(response.content)
