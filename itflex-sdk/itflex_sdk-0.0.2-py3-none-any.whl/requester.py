from abc import ABCMeta, abstractmethod
from enum import Enum
from http import HTTPStatus

from dataclasses import dataclass
from requests import Request, Session

from .consts import ResponseStatus
from .errors import AuthenticationError

GET_STATUS = {
    HTTPStatus.OK: ResponseStatus.SUCCESS,
    HTTPStatus.UNAUTHORIZED: ResponseStatus.PERMISSION_ERROR,
    HTTPStatus.FORBIDDEN: ResponseStatus.PERMISSION_ERROR,
    HTTPStatus.NOT_FOUND: ResponseStatus.NOT_FOUND_ERROR,
    HTTPStatus.BAD_REQUEST: ResponseStatus.CLIENT_ERROR,
    HTTPStatus.CONFLICT: ResponseStatus.VALIDATION_ERROR,
}


class HttpMethods(Enum):
    POST = "POST"
    PUT = "PUT"
    GET = "GET"
    DELETE = "DELETE"


@dataclass
class HttpRequest:
    method: HttpMethods
    uri: str
    headers: dict = None
    query: dict = None
    json: dict = None
    text: str = None
    data: bytes = None


@dataclass
class HttpResponse:
    status: ResponseStatus
    headers: dict = None
    json: dict = None
    text: str = None
    data: bytes = None

    @property
    def success(self):
        return self.status == ResponseStatus.SUCCESS


def make_response(resp):
    status = GET_STATUS[resp.status_code]
    headers = resp.headers
    json = None

    if (
        "content-type" in resp.headers
        and resp.headers["content-type"] == "application/json"
        and resp.text
    ):
        json = resp.json()

    return HttpResponse(
        status=status, headers=headers, json=json, text=resp.text
    )


class RequesterBase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, request: HttpRequest):
        raise NotImplementedError


class Requester(RequesterBase):
    def __init__(
        self,
        host,
        username=None,
        password=None,
        apikey=None,
        verify_ssl=True,
        session=None,
    ):
        self.authenticated = False
        self.host = host
        self.username = username
        self.password = password
        self.apikey = apikey

        self.session = session
        if not self.session:
            self.session = Session()
            self.session.verify = verify_ssl

    def auth(self):
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
        }

        if self.apikey:
            data = {
                "grant_type": "refresh_token",
                "refresh_token": self.apikey,
            }

        resp = self._execute(
            HttpRequest(
                method=HttpMethods.POST, uri="/api/oauth2/token", json=data
            )
        )
        if not resp.success:
            raise AuthenticationError()

        self.authenticated = True
        return self

    def execute(self, request: HttpRequest):
        if not self.authenticated:
            self.auth()

        return self._execute(request)

    def _execute(self, request: HttpRequest):
        data = request.data

        if not data:
            data = request.text

        req = Request(
            method=request.method.value,
            url=self.host + request.uri,
            params=request.query,
            headers=request.headers,
            data=data,
            json=request.json,
        )
        prepped = self.session.prepare_request(req)
        resp = self.session.send(prepped)
        return make_response(resp)
