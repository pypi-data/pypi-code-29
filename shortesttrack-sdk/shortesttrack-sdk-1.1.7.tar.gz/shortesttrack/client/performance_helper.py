from urlobject import URLObject

from shortesttrack.utils import getLogger, do_post

logger = getLogger(__name__)


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
        do_post(url=url, headers=headers)

    def send_failed(self, access_token: str) -> None:
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = URLObject(self.host).add_path(
            f'api/exec-scheduling/v1/sec/{self._config_id}/performances/{self._performance_id}/failed/'
        )
        do_post(url=url, headers=headers)

    def write_parameter(self, parameter_id: str, parameter_value: str, host: str, access_token: str) -> None:
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = URLObject(host).add_path(
            f'api/execution-metadata/v2/performances/{self._performance_id}/output-parameters/{parameter_id}/value/'
        )
        body = {
            'value': parameter_value
        }
        do_post(url=url, headers=headers, body=body)



