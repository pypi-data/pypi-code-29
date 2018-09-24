import os

from shortesttrack.client import AuthHelper, ASECHelper, ISSConnector
from shortesttrack.library.script_configuration import ScriptConfiguration
from shortesttrack.utils import getLogger

logger = getLogger()


class ISSConnectionInfo:
    def __init__(self, info: dict) -> None:
        self.url = info.get('url')
        self.url = self.url if self.url[-1] != '/' else self.url[0:-1]
        self.auth_custom_token = info.get('auth_custom_token')
        self.id = info.get('iscript_service_id')


class AnalyticScriptConfiguration(ScriptConfiguration):
    def __init__(
            self, asec_id: str = os.getenv('ASEC_ID'), host: str = os.getenv('HOST', 'https://shortesttrack.com'),
            refresh_token: str = os.getenv('SEC_REFRESH_TOKEN')
    ) -> None:
        logger.info(f'AnalyticScriptConfiguration {asec_id} {host} {refresh_token}')
        if not asec_id:
            raise Exception('No ASEC found')

        self.asec_id = asec_id
        self._host = host
        self._refresh_token = refresh_token
        self._access_token = AuthHelper(self._host).get_access_token_from_refresh_token(self._refresh_token)
        self._asec = ASECHelper(self.asec_id).get_asec(self._host, self._access_token.get())
        super().__init__(self._asec['configuration_id'], host, refresh_token)

    def __str__(self):
        return f'ASEC({self.asec_id})'

    def get_iss_connection_info(self) -> list:
        return [ISSConnectionInfo(info) for info in self._asec['relations']]

    @staticmethod
    def get_iss_connector(connection_info: ISSConnectionInfo) -> ISSConnector:
        return ISSConnector(
            url=connection_info.url, auth_custom_token=connection_info.auth_custom_token
        )
