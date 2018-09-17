import json

from urlobject import URLObject

from shortesttrack.utils import getLogger, do_get, do_post

logger = getLogger(__name__)


class SECHelper:
    def __init__(self, config_id: str, host: str) -> None:
        logger.info(f'sec_id: {config_id} host: {host}')
        self._config_id = config_id
        self.host = host

    def get_sec(self, access_token: str) -> dict:
        url = URLObject(self.host).add_path(f'api/metadata/script-execution-configurations/{self._config_id}')
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        logger.info(f'get_sec {self._config_id}')
        response = do_get(url, headers)

        return json.loads(response.content)

    def get_script_content(self, access_token: str) -> bytes:
        url = URLObject(self.host).add_path(
            f'api/data/script-execution-configurations/{self._config_id}/script/content'
        )
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        logger.info(f'get_script_content {self._config_id}')
        return do_get(url, headers).content

    def get_matrix(self, matrix_id: str, access_token: str) -> dict:
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = URLObject(self.host).add_path(
            f'/api/data/script-execution-configurations/{self._config_id}/matrices/{matrix_id}/data'
        )

        logger.info(f'get_matrix {matrix_id}')
        response = do_get(url, headers)
        response = json.loads(response.content.decode())
        fields = response['schema']['fields']

        matrix = []
        if None is not response.get('rows'):
            for f in response['rows']:
                row = []
                for v in f['f']:
                    row.append(v.get('v'))
                matrix.append(row)

        return {
            'fields': fields,
            'matrix': matrix
        }

    def insert_matrix(self, matrix_id: str, matrix: dict, access_token: str) -> None:
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = URLObject(self.host).add_path(
            f'/api/data/script-execution-configurations/{self._config_id}/matrices/{matrix_id}/insert'
        )

        logger.info(f'push matrix {matrix_id}')
        insert_rows = []
        for row in matrix.get('matrix'):
            tmp = {}
            for k, v in zip(matrix['fields'], row):
                tmp[k['name']] = v
            insert_rows.append({"json": tmp})

        body = {'rows': insert_rows}

        logger.info(f'request POST {url} {headers} {body}')
        response = do_post(url=url, headers=headers, body=body)

        logger.info(f'success matrix push {matrix_id} {insert_rows}: {response.content}')
