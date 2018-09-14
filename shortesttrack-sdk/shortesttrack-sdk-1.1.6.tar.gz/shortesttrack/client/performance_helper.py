import requests
from urlobject import URLObject

from shortesttrack.utils import getLogger

logger = getLogger(__name__)


def _post(url, headers, body: dict = None) -> None:
    body = body if body else {}
    logger.info(f'request POST: {url} {body}')
    logger.debug(f'request POST: {url} {headers} {body}')

    response = requests.post(url=url, headers=headers, json=body)
    logger.info(f'response: {response.status_code} {response.content}')

    if response.status_code != 200:
        raise Exception(response.status_code)


class PerformanceHelper:
    def __init__(self, performance_id: str, config_id: str, host: str) -> None:
        logger.info(f'PerformanceHelper performance_id: {performance_id} sec_id: {config_id} host: {host}')
        self._config_id = config_id
        self.host = host
        self._performance_id = performance_id

    def send_success(self, access_token: str) -> None:
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = URLObject(self.host).add_path(
            f'api/exec-scheduling/v1/sec/{self._config_id}/performances/{self._performance_id}/success/'
        )
        _post(url=url, headers=headers)

    def send_failed(self, access_token: str) -> None:
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = URLObject(self.host).add_path(
            f'api/exec-scheduling/v1/sec/{self._config_id}/performances/{self._performance_id}/failed/'
        )
        _post(url=url, headers=headers)

    def write_parameter(self, parameter_id: str, parameter_value: str, host: str, access_token: str) -> None:
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = URLObject(host).add_path(
            f'api/execution-metadata/v2/performances/{self._performance_id}/output-parameters/{parameter_id}/value/'
        )
        body = {
            'value': parameter_value
        }
        _post(url=url, headers=headers, body=body)



