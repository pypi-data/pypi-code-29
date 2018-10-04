from shortesttrack_tools.functional import cached_property

from shortesttrack.client import SECHelper, PerformanceHelper
from shortesttrack.utils import getLogger, APIClient

logger = getLogger()


class ScriptConfiguration:
    def __init__(self, sec_id=APIClient.CONFIGURATION_ID):
        logger.info(f'ScriptConfiguration {sec_id}')
        if not sec_id:
            raise Exception(f'SEC invalid configuration: {sec_id}')

        self._sec_id = sec_id
        self.helper = SECHelper(self._sec_id)
        self.sec = self.helper.sec
        self._matrices_names = {}
        self._matrices_lists_names = {}

        for mat in self.sec.get('matrices', []):
            self._matrices_names[mat['id']] = mat['matrixId']

        for matrix_list in self.sec.get('matricesLists', []):
            self._matrices_lists_names[matrix_list['id']] = matrix_list['matricesListId']

    def __str__(self):
        return f'SEC({self._sec_id})'

    @cached_property
    def parameters(self) -> dict:
        return {
            p['id']: p.get('value') for p in self.sec.get('parameters', [])
        }

    def write_parameter(self, parameter_id, parameter_value, performance_id: str = APIClient.PERFORMANCE_ID):
        performance = PerformanceHelper(
            sec_id=self._sec_id, performance_id=performance_id
        )
        performance.write_parameter(
            parameter_id=parameter_id, parameter_value=parameter_value
        )

    def read_matrix(self, matrix_id) -> dict:
        if not self._matrices_names.get(matrix_id):
            return {}

        return self.helper.get_matrix(
            matrix_id=self._matrices_names[matrix_id]
        )

    def write_matrix(self, matrix_id: str, matrix: dict) -> None:
        if not self._matrices_names.get(matrix_id):
            return

        return self.helper.insert_matrix(
            matrix_id=self._matrices_names[matrix_id], matrix=matrix
        )
