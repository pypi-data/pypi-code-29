# coding: utf-8 or # -*- coding: utf-8 -*-
import requests
import traceback
from urllib.parse import urlparse

try:
    # 禁用安全请求警告
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except ImportError:
    print("WARN：禁用安全请求警告操作错误(InsecureRequestWarning import error)")


class RequestsUtils:

    """
     e.g. proxies={"http":"http://127.0.0.1:1087","https":"http://127.0.0.1:1087"}
    """
    def __init__(self, headers=None, referer="", timeout=(3.05, 5), proxies={}):
        if headers is None:
            headers = {
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36",
                "X-Requested-With": "xmlHttpRequest",
                "Referer": referer,
                "Accept": "*/*",
                'Cache-Control': 'no-cache',
                'If-Modified-Since': '0'
            }
        self.sess = requests.Session()
        self.sess.proxies = proxies
        self.headers = headers
        self.timeout = timeout
        self.sess.verify = False
        self.cookies_jar = requests.cookies.RequestsCookieJar()

    def get(self, url, params=None, retry_count=0, retry_count_max=0):
        try:
            if self.headers.get("Host") is None or len(self.headers.get("Host")) < 1:
                self.headers["Host"] = self.url_parse(url).hostname
            return self.sess.get(url, params=params, headers=self.headers, cookies=self.cookies_jar, timeout=self.timeout)
        except:
            traceback.print_exc()
            if retry_count < retry_count_max:
                retry_count += 1
                print("get url:" + url + ",retry times:" + str(retry_count) + " of " + str(retry_count_max))
                self.get(url, params, retry_count)

    def post(self, url, data=None, retry_count=0, retry_count_max=0):
        try:
            if self.headers.get("Host") is None or len(self.headers.get("Host")) < 1:
                self.headers["Host"] = self.url_parse(url).hostname
            return self.sess.post(url, data=data, headers=self.headers, cookies=self.cookies_jar, timeout=self.timeout)
        except:
            traceback.print_exc()
            if retry_count < retry_count_max:
                retry_count += 1
                print("post url:" + url + ",retry times:" + str(retry_count) + " of " + str(retry_count_max))
                self.post(url, data, retry_count)

    def close(self):
        self.sess.close()

    def set_cookie_by_name(self, name, value, domain="", path="/"):
        self.cookies_jar.set(name, value, domain=domain, path=path)

    def remove_cookie_by_name(self, name, domain=None, path=None):
        """Unsets a cookie by name, by default over all domains and paths.

        Wraps CookieJar.clear(), is O(n).
        """
        clearables = []
        for cookie in self.cookies_jar:
            if cookie.name != name:
                continue
            if domain is not None and domain != cookie.domain:
                continue
            if path is not None and path != cookie.path:
                continue
            clearables.append((cookie.domain, cookie.path, cookie.name))

        for domain, path, name in clearables:
            self.cookies_jar.clear(domain, path, name)

    @staticmethod
    def url_parse(url):
        return urlparse(url)

    @staticmethod
    def domain_parse(url, globle_domain=False):
        domain = RequestsUtils.url_parse(url).hostname
        if not globle_domain:
            return domain
        else:
            split_at = domain.split(".")
            i = (0, 1)[globle_domain and len(split_at)>2]
            return ".".join(split_at[i:]).lower()

    @staticmethod
    def decode_content(req_content, encoding="utf-8"):
        return req_content.decode(encoding=encoding)


if __name__ == '__main__':
    url = "http://www.stackoverflow.com?1=2"
    base_url = RequestsUtils.domain_parse(url, True)
    print(base_url)
    parse = RequestsUtils.url_parse("https://api.github.com/events")
    print(parse.hostname)
    req = RequestsUtils(proxies={"http":"http://127.0.0.1:1087","https":"http://127.0.0.1:1087"})
    r = req.get("https://api.github.com/events")
    print(r.json())



