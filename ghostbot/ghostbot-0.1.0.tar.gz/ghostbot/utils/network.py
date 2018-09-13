import requests
from enum import Enum
from ghostbot.utils.json import Json


class Methods(Enum):
    GET = "get"
    POST = "post"


class Cookie(object):
    pass


class Session(object):
    pass


class Request(object):
    pass


class Response(object):
    pass


class UdpRequest(Request):
    pass


class UdpResponse(Response):
    pass


class HttpRequest(Request):

    def __init__(self):
        self.method = None
        self.url = None
        self.params = None

    def clear(self):
        for key in self.__dict__.keys():
            setattr(self, key, None)

    def setup(self, method, url, params):
        self.method = method
        self.url = url
        self.params = params


class HttpResponse(Response):

    def __init__(self):
        self.url = None
        self.status_code = None
        self.headers = None
        self.content = None

    def clear(self):
        for key in self.__dict__.keys():
            setattr(self, key, None)

    def setup(self, url, status_code, headers, content):
        self.url = url
        self.status_code = status_code
        self.headers = headers
        self.content = content

    def json(self):
        return Json.decode(self.content)


class HttpSession(Session):

    def __init__(self):
        self.session = requests.session()

    def header(self, headers):
        self.session.headers.update(headers)


class HttpClient(object):

    def __init__(self):
        self._session = None
        self._request = HttpRequest()
        self._response = HttpResponse()

    def session(self):
        self._session = HttpSession()

    def request(self):
        return self._request

    def response(self):
        return self._response

    def get(self, url, params=None, headers=None):
        self._request.setup(Methods.GET, url, params)
        if self._session:
            if headers:
                self._session.header(headers)
            res = self._session.session.get(url, params=params)
        else:
            res = requests.get(url, params=params)
        self._response.setup(res.url, res.status_code, res.headers, res.text)
        return self._response

    def post(self, url, params=None, headers=None):
        self._request.setup(Methods.POST, url, params)
        if self._session:
            if headers:
                self._session.header(headers)
            res = self._session.post(url, data=params)
        else:
            res = requests.post(url, data=params)
        self._response.setup(res.url, res.status_code, res.headers, res.text)
        return self._response

    def download(self, file, url):
        if self._session:
            reply = self._session.session.get(url, stream=True)
        else:
            reply = requests.get(url, stream=True)
        with open(file, "wb") as fd:
            for chunk in reply.iter_content(chunk_size=1024):
                if chunk:
                    fd.write(chunk)

    def close(self):
        self._session = None
        self._request = HttpRequest()
        self._response = HttpResponse()
