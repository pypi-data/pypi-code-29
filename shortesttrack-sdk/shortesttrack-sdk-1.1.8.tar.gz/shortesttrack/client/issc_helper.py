import json

from urlobject import URLObject

from shortesttrack.utils import getLogger, do_get

logger = getLogger()


class ISSCHelper:
    def __init__(self, config_id: str) -> None:
        logger.info(f'ISSC_ID: {config_id}')
        self._config_id = config_id

    def get_issc(self, host: str, access_token: str) -> dict:
        url = URLObject(host).add_path('api/execution-metadata/v2/issc/{}'.
                                       format(self._config_id))
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        response = do_get(url=url, headers=headers)

        return json.loads(response.content)
