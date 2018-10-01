from .config.urls import BASE_URL
from .modules.engagements import Engagements


__all__ = ['Client']


class Client:

    def __init__(self, token, base_url=BASE_URL):
        '''Portal for all engagespark requests

        Usage:
        >>> from engagespark import Client
        >>> client = Client(token='your_token')

        Parameters:
        - token
          - Type: string
          - Required
        - base_url
          - Type: string
          - Optional
        '''
        self._token = token
        self._base_url = base_url

    @property
    def engagements(self):
        return Engagements(self._token, self._base_url)
