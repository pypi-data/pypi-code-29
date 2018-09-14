import os

from client.auth_helper import AuthHelper
from client.sec_helper import SECHelper
from client.performance_helper import PerformanceHelper


class ScriptConfiguration:
    def __init__(self,
                 sec_id: str = os.getenv('CONFIGURATION_ID'),
                 host: str = os.getenv('HOST', 'https://shortesttrack.com'),
                 refresh_token: str = os.getenv('SEC_REFRESH_TOKEN')) -> None:
        self._sec_id = sec_id
        self._host = host
        self._refresh_token = refresh_token
        self._access_token = AuthHelper(self._host).get_access_token_from_refresh_token(self._refresh_token)
        self._sec = SECHelper(self._sec_id).get_sec(self._host, self._access_token.get())
        self._matrices_names = {}
        for mat in self._sec['matrices']:
            self._matrices_names[mat['id']] = mat['matrixId']

    def read_parameters(self):
        result = {}
        params = self._sec['parameters']
        for p in params:
            result[p['id']] = p.get('value')

        return result

    def write_parameter(self, parameter_id, parameter_value):
        performance = PerformanceHelper(config_id=self._sec_id,
                                        performance_id=os.getenv('PERFORMANCE_ID'))

        performance.write_parameter(parameter_id=parameter_id,
                                    parameter_value=parameter_value,
                                    host=self._host,
                                    access_token=self._access_token.get())

    def read_matrix(self, matrix_id):
        return SECHelper(self._sec_id).get_matrix(matrix_id=self._matrices_names[matrix_id],
                                                  host=self._host, access_token=self._access_token.get())

    def write_matrix(self, matrix_id: str, matrix: dict):
        return SECHelper(self._sec_id).insert_matrix(matrix_id=self._matrices_names[matrix_id],
                                                     matrix=matrix,
                                                     host=self._host, access_token=self._access_token.get())







