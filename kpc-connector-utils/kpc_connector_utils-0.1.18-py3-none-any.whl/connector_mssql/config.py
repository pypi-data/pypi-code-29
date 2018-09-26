from kpc_connector_utils.pusher_s3.config import BasePutS3Config
from kpc_connector_utils.common.base64 import base64_encode as encode

import json


class ConnectorMSSql(BasePutS3Config):
    def __init__(self, mssql_connector_env):
        super().__init__(mssql_connector_env)

        self._hostname = None
        self._username = None
        self._password = None
        self._database = None
        self._port = None
        self._query_string = None

    def __str__(self):
        data_dict = {
            'hostname': self._hostname,
            'username': self._username,
            'password': self._password,
            'database': self._database,
            'port': self._port,
            'query_string': self._query_string,
            'puts3_config': self.get_data_dict()
        }

        value = {'MSSQLConnectorEvent': data_dict}

        return json.dumps(value)

    def set_hostname(self, value):
        self._hostname = encode(value)
        return self

    def set_username(self, value):
        self._username = encode(value)
        return self

    def set_password(self, value):
        self._password = encode(value)
        return self

    def set_database(self, value):
        self._database = encode(value)
        return self

    def set_port(self, value):
        port = value
        if not isinstance(port, int):
            try:
                port = int(port)
            except Exception:
                raise ValueError('Port value should be integer')

        self._port = encode(port)
        return self

    def set_query_string(self, value):
        self._query_string = encode(value)
        return self

    def set_by_dict(self, config: dict):

        if config.get('hostname'):
            self.set_hostname(config.get('hostname'))

        if config.get('username'):
            self.set_username(config.get('username'))

        if config.get('password'):
            self.set_password(config.get('password'))

        if config.get('database'):
            self.set_database(config.get('database'))

        if config.get('port'):
            self.set_port(config.get('port'))

        if config.get('query_string'):
            self.set_query_string(config.get('query_string'))

        if config.get('puts3_config'):
            super().set_by_dict(config.get('puts3_config'))

        return self
