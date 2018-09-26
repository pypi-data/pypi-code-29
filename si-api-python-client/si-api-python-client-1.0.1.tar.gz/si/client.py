from requests_toolbelt import sessions
from si.trademark import Trademark
import os
import logging


SI_GRAPHQL_URL = os.getenv('SI_API_URL', 'https://app.trademark-ai.com/_api/')
AUTHORIZATION_HEADER_ID = 'apiKey'


class BaseClient:
    def __init__(self, access_token, url=None):
        self._url = SI_GRAPHQL_URL if url is None else url
        self._access_token = access_token

        logging.debug('Using base_url=%s', self._url)
        self._session = sessions.BaseUrlSession(base_url=self._url)
        self.set_auth(self._access_token)

    def set_auth(self, access_token):
        self._access_token = access_token
        self._session.headers.update({
            'Authorization': '%s %s' % (AUTHORIZATION_HEADER_ID, self._access_token)
        })

    def update_headers(self, headers):
        self._session.headers.update(headers)


class Client(BaseClient):
    def __init__(self, access_token, url=None):
        super().__init__(access_token, url)

        # attach trademark service
        self.trademark = Trademark(self._session)
