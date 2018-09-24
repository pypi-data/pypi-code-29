import os

from shortesttrack.client import AuthHelper, SECHelper, PerformanceHelper
from shortesttrack.utils import getLogger

logger = getLogger()


class ScriptConfiguration:
    def __init__(self, sec_id: str = os.getenv('CONFIGURATION_ID'),
                 host: str = os.getenv('HOST', 'https://shortesttrack.com'),
                 refresh_token: str = os.getenv('SEC_REFRESH_TOKEN')) -> None:
        logger.info(f'ScriptConfiguration {sec_id} {host} {refresh_token}')
        if not sec_id or not refresh_token:
            raise Exception(f'SEC invalid configuration: {sec_id} {refresh_token}')

        self._sec_id = sec_id
        self._host = host
        self._refresh_token = refresh_token
        self._access_token = AuthHelper(self._host).get_access_token_from_refresh_token(self._refresh_token)
        self._sec = SECHelper(self._sec_id, self._host).get_sec(self._access_token.get())
        self._matrices_names = {}
        for mat in self._sec.get('matrices', []):
            self._matrices_names[mat['id']] = mat['matrixId']

    def __str__(self):
        return f'SEC({self._sec_id})'

    def read_parameters(self) -> dict:
        return {
            p['id']: p.get('value') for p in self._sec.get('parameters', [])
        }

    def write_parameter(self, parameter_id, parameter_value, performance_id: str = os.getenv('PERFORMANCE_ID')):
        performance = PerformanceHelper(
            config_id=self._sec_id, performance_id=performance_id, host=self._host
        )
        performance.write_parameter(
            parameter_id=parameter_id, parameter_value=parameter_value, host=self._host,
            access_token=self._access_token.get()
        )

    def read_matrix(self, matrix_id) -> dict:
        if not self._matrices_names.get(matrix_id):
            return {}

        return SECHelper(self._sec_id, self._host).get_matrix(
            matrix_id=self._matrices_names[matrix_id], access_token=self._access_token.get()
        )

    def write_matrix(self, matrix_id: str, matrix: dict) -> None:
        if not self._matrices_names.get(matrix_id):
            return

        return SECHelper(self._sec_id, self._host).insert_matrix(
            matrix_id=self._matrices_names[matrix_id], matrix=matrix, access_token=self._access_token.get()
        )
