import requests
import logging
import json

from .parameters import Parameters
from .headers import Headers

class Request:
    def __init__(self, env):
        '''
        Constructor for class Request.
        Initialize requester used by Lambda script.
        '''
        logging.debug('# Configure requester')
        self.environment = env
        self.parameters = Parameters(self.environment)
        self._oauth_token()


    def __del__(self):
        '''
        Destroy automatically token in backend.
        '''
        self._oauth_revoke()


    def send(self, verb, path, body={}):
        '''
        Build request and send.
        If you use environment development write request in logger.
        '''
        try:
            header = Headers().oauth(self.access_token)
            url = '{}{}'.format(self.environment.get_api_endpoint(), path)
            verb = verb.lower()

            logging.debug('Send request : {} {}'.format(verb, url))
            logging.debug('With header : {}'.format(header))
            logging.debug('With body : {}'.format(body))

            getattr(requests, verb)(url, json=body, headers=header, verify=False)

        except requests.exceptions.MissingSchema as e:
            logging.critical('URL to API is not correctly configured !')
            logging.critical('Request [{}] not sending !'.format(path))
            logging.critical(e)


    def _path_oauth(self, action):
        '''
        Path for create or revoke token to Dazzl service.
        '''
        return '{}/oauth/{}'.format(self.environment.get_api_endpoint(), action)


    def _oauth_token(self):
        '''
        Send request to backend for ask valid token.
        '''
        try:
            logging.debug('Send request for create token')
            response = self._post(self._path_oauth('token'), self.parameters.token())
            data = json.loads(response.text)
            self.access_token = data['access_token']
            self.refresh_token = data['refresh_token']
            self.type_token = data['token_type']
        except requests.exceptions.MissingSchema as e:
            logging.critical('URL to API is not correctly configured !')
            logging.critical('Token creation failed !')
            logging.critical(e)


    def _oauth_revoke(self):
        '''
        Send request to backend for ask to revoke token.
        '''
        try:
            logging.debug('Send request for revoke token')
            self._post(self._path_oauth('revoke'),
                       self.parameters.revoke(self.access_token))
        except requests.exceptions.MissingSchema as e:
            logging.critical('URL to API is not correctly configured !')
            logging.critical('Token revokation failed !')
            logging.critical(e)


    def _post(self, path, body):
        '''
        Send request post for token create/revoke
        '''
        return requests.post(path, json=body, headers={}, verify=False)
