import json

try:
    PY3 = True
    from urllib.parse import urlencode
    from urllib.request import urlopen, Request as Req
    from urllib.error import HTTPError
except ImportError:
    PY3 = False
    from urllib import urlencode
    from urllib2 import urlopen, Request as Req, HTTPError

from .exceptions import PositionalArgumentsNotSupported, SmappiServerError, SmappiAPIError, DeclarationError


class Request(object):

    def __init__(self, path='', fmt='json'):
        self._fmt = fmt
        self._path = path
        if not path:
            raise DeclarationError()

    def __getattribute__(self, name):
        if name.startswith('_'):
            return super(Request, self).__getattribute__(name)
        if ':' in self._path:  # host:port
            url = 'http://{host}/{func}'.format(host=self._path, func=name)
        else:
            url = 'https://{s._fmt}.smappi.org/{s._path}/{func}'.format(s=self, func=name)
        def wrap(*args, **kwargs):
            if args:
                raise PositionalArgumentsNotSupported()
            data = urlencode(kwargs)
            if PY3:
                data = bytes(data, 'utf-8')
            req = Req(url, data=data)
            try:
                res = urlopen(req).read().decode()
            except HTTPError as e:
                raise SmappiServerError(e)
            if self._fmt == 'json':
                res = json.loads(res)
                if isinstance(res, dict) and 'error' in res:
                    error = res['error']
                    if 'message' in error:
                        error = '{0} (code: {1})'.format(error.get('message'), error.get('code'))
                    raise SmappiAPIError(error)
            return res
        return wrap
