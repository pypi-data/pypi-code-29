from collections import namedtuple
from urllib import parse
import urllib


class UriBuilder:

    def schema(self, value):
        self._scheme = value
        return self

    def netloc(self, value):
        self._netloc = value
        return self

    def path(self, value):
        self._path = value
        return self

    def fragment(self, value):
        self._fragment = value
        return self

    def params(self, value):
        self._params = value
        return self

    def add_parameter(self, key, value):
        self.parameters.append((key, value))
        return self

    def __init__(self):
        self._scheme = ""
        self._netloc = ""
        self._path = ""
        self._params = ""
        self._query = ""
        self._fragment = ""

        self.parameters = []

    def build(self):
        Uri = namedtuple("Uri", ['scheme', 'netloc', 'path', 'params', 'query', 'fragment'])
        q = parse.urlencode(self.parameters)
        u = Uri(scheme=self._scheme, netloc=self._netloc, path=self._path, params=self._params, query=q, fragment=self._fragment)
        return urllib.parse.urlunparse(u)
