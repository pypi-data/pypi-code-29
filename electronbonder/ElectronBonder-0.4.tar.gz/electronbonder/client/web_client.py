from requests import Session
from six import add_metaclass
import json
from requests.adapters import HTTPAdapter
from urllib.parse import urlparse
from urllib3.util.retry import Retry


class ElectronBondAuthError(Exception): pass


class ElectronBondReturnError(Exception): pass


def http_meth_factory(meth):
    '''Utility method for producing HTTP proxy methods for ElectronBondProxyMethods mixin class.

    Urls are prefixed with the baseurl defined
    '''
    def http_method(self, url, *args, **kwargs):
        url = urlparse(url)
        full_url = "/".join([self.config['baseurl'].rstrip("/"), url.path.lstrip("/")])
        result = getattr(self.session, meth)(full_url, *args, **kwargs)
        return result
    return http_method


def retry_session(retries, session=None, backoff_factor=0.3, status_forcelist=(500, 502, 503, 504)):
    session = session or Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


class ElectronBondProxyMethods(type):
    '''Metaclass to set up proxy methods for all requests-supported HTTP methods'''
    def __init__(cls, name, parents, dct):

        for meth in ('get', 'post', 'head', 'put', 'delete', 'options',):
            fn = http_meth_factory(meth)
            fn.__name__ = meth
            fn.__doc__ = '''Proxied :meth:`requests.Session.{}` method from :class:`requests.Session`'''.format(meth)

            setattr(cls, meth, fn)


@add_metaclass(ElectronBondProxyMethods)
class ElectronBond(object):
    '''ElectronBonder Web Client'''

    def __init__(self, **config):
        self.config = {}
        self.config.update(config)

        if not hasattr(self, 'session'): self.session = retry_session(retries=5)
        self.session.headers.update({'Accept': 'application/json',
                                     'User-Agent': 'ElectronBond/0.1'})

    def get_paged(self, url, *args, **kwargs):
        '''get list of json objects from urls of paged items'''
        params = {"page": 1}
        if "params" in kwargs:
            params.update(**kwargs['params'])
            del kwargs['params']

        current_page = self.get(url, params=params, **kwargs)
        current_json = current_page.json()
        # Regular paged object
        try:
            while len(current_json['results']) > 0:
                for obj in current_json['results']:
                    yield obj
                if not current_json.get('next'): break
                params['page'] += 1
                current_page = self.get(url, params=params)
                current_json = current_page.json()
        except:
            raise ElectronBondReturnError("get_paged doesn't know how to handle {}".format(current_json))
