import os

from client.auth_helper import AuthHelper
from client.asec_helper import ASECHelper
from client.iss_connector import ISSConnector
from library.script_configuration import ScriptConfiguration


class ISSConnectionInfo:
    def __init__(self, info: dict) -> None:
        self.url = info.get('url')
        self.url = self.url if self.url[-1] != '/' else self.url[0:-1]
        self.auth_custom_token = info.get('auth_custom_token')


class AnalyticScriptConfiguration(ScriptConfiguration):
    def __init__(self, asec_id: str = os.getenv('ASEC_ID'),
                 host: str = os.getenv('HOST', 'https://shortesttrack.com'),
                 refresh_token: str = os.getenv('SEC_REFRESH_TOKEN')) -> None:

        self._isasec_id = asec_id
        self._host = host
        self._refresh_token = refresh_token
        self._access_token = AuthHelper(self._host).get_access_token_from_refresh_token(self._refresh_token)
        self._asec = ASECHelper(self._isasec_id).get_asec(self._host, self._access_token.get())
        super().__init__(self._asec['configuration_id'], host, refresh_token)

    def get_iss_connection_info(self) -> list:
        result = []
        for info in self._asec['relations']:
            result.append(ISSConnectionInfo(info))
        return result

    def get_iss_connector(self, connection_info: ISSConnectionInfo) -> ISSConnector:
        connector = ISSConnector(url=connection_info.url,
                                 auth_custom_token=connection_info.auth_custom_token)

        return connector
