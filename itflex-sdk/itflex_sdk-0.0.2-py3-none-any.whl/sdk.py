import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from itflex_sdk.auth.auth import Auth
from itflex_sdk.openvpn.openvpn import Openvpn
from itflex_sdk.requester import Requester


class Sdk:
    def __init__(
        self,
        host,
        username=None,
        password=None,
        apikey=None,
        verify_ssl=True,
        requester=None,
    ):
        if not verify_ssl:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        self.requester = requester
        if not requester:
            self.requester = Requester(
                host=host,
                username=username,
                password=password,
                apikey=apikey,
                verify_ssl=verify_ssl,
            )
        self._auth = None
        self._openvpn = None

    @property
    def auth(self):
        if not self._auth:
            self._auth = Auth(self.requester)
        return self._auth

    @property
    def openvpn(self):
        if not self._openvpn:
            self._openvpn = Openvpn(self.requester)
        return self._openvpn
