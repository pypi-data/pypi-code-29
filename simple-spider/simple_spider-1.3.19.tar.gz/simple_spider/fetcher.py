import requests

from .proxy import Proxy


class Fetcher:
    default_headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    def __init__(self,options):

        self.enable_session = options.get('enable_session',False)
        self.debug_proxy = options.get('debug_proxy',None)

        proxy_list = options.get('proxy_list',None)
        self.proxy = Proxy(proxy_list)

        if self.enable_session:
            self.http = requests.session()
        else:
            self.http = requests

    def fetch(self,url, method ='GET', data = None, headers=None, cookies = None,encoding=None):
        fetch_headers = {}
        fetch_headers.update(Fetcher.default_headers)
        if headers:
            fetch_headers.update(headers)

        proxy = {}
        if self.debug_proxy:
            proxy = {
                'http': self.debug_proxy,
                'https': self.debug_proxy
            }
        elif self.proxy.http_proxy():
            proxy = {
                'http': self.proxy.http_proxy(),
                'https': self.proxy.http_proxy()
            }
        else:
            pass

        if method.upper() == 'GET':
            resp = self.http.get(url,headers = fetch_headers, proxies = proxy, cookies = cookies,verify=False)
        else:
            resp = self.http.post(url, data=data, headers = fetch_headers, proxy = proxy, cookies = cookies)

        if encoding:
            resp.encoding = encoding

        return {
            'status_code': resp.status_code,
            'reason': resp.reason,
            'content': resp.content,
            'text': resp.text,
            'url': resp.url
        }

    def current_proxy(self):
        return self.proxy.http_proxy()

    def desc_proxy_score(self,proxy):
        return self.proxy.desc_score(proxy)

    def inc_proxy_score(self,proxy):
        return self.proxy.inc_score(proxy)

    def pick_new_proxy(self):
        return self.proxy.switch_proxy()
