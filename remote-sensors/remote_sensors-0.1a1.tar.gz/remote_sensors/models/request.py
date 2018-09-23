import urllib.parse

from dataclasses import (
    dataclass,
    asdict,
    field,
)

from remote_sensors.exc import (
    InvalidRequest,
    RequestMarshalerError,
)
from remote_sensors.log import logger


REQUEST_HEADER_SIZE = 0x04

METHODS = {
    'GET': 0x01,
    'POST': 0x02,
    'DELETE': 0x03,
    'REGISTRATION': 0x04,
    'END_REGISTRATION': 0x00,
}

CONNECTIONS = {
    'ONE_TIME': 0x01,
    'STREAM': 0x02,
    'CLOSE': 0x03,
}


@dataclass
class URI:

    base: str = '/'
    params: dict = field(default_factory=dict)

    def __post_init__(self):
        if not self.base.startswith('/'):
            self.base = f'/{self.base}'

        if '?' in self.base:
            self.base, self.params = self.base.split('?')
            self.params = urllib.parse.parse_qs(self.params)

    def __truediv__(self, path: str):
        """Append the path to the base url."""
        if path.startswith('/'):
            path = path[1:]
        self.base = f'{self.base}/{path}'
        return self

    def __str__(self):
        """Returns the string representation of the URI"""
        uri = self.base

        if self.params:
            params_dump = urllib.parse.urlencode(self.params)
            uri = f'{uri}?{params_dump}'

        return uri

    def __eq__(self, other) -> bool:
        if isinstance(other, URI):
            return self.path == other.path or self.path == other.path[:-1]

        trimming_slash = other
        if other.endswith('/'):
            trimming_slash = other[:-1]
        return self.path == other or str(self) == other or \
            self.path == trimming_slash or str(self) == trimming_slash

    @property
    def path(self) -> str:
        return self.base

    def add_params(self, params: dict):
        """Adds the parameters to the current parameters."""
        _params = {**self.params, **params}
        self.params = _params


@dataclass
class Request:
    """Request instance.

        Frame order:
            |METHOD|TRANS|CONNECTION|URI_LENGTH|URI...|

    """

    method: str
    transaction: int
    connection: str
    uri: URI

    def __post_init__(self):
        """Validate the input."""
        if self.method not in METHODS:
            raise InvalidRequest('Request Method is not valid.')

        if self.connection not in CONNECTIONS:
            raise InvalidRequest('Request Connection Type is not valid.')

    @classmethod
    def from_bytearray(cls, data: bytearray):
        """Returns a parsed request instance."""
        if not data or len(data) < REQUEST_HEADER_SIZE:
            raise RequestMarshalerError('Frame is invalid')

        method = data[0]  # first byte is the request method
        if method not in METHODS.values():
            raise RequestMarshalerError(f'Method {method} is not valid')

        # set the canonical name
        for key, value in METHODS.items():
            if value == method:
                method = key
                break

        transaction = data[1]  # first byte is the transaction

        connection = data[2]  # third byte is the connection type
        if connection not in CONNECTIONS.values():
            raise RequestMarshalerError(f'Connection {connection} is not valid')

        # set the canonical name
        for key, value in CONNECTIONS.items():
            if value == connection:
                connection = key

        uri_length = data[3]  # fourth byte is the URI length
        raw_uri = data[4:4 + uri_length]
        raw_uri = raw_uri.decode('ascii')
        uri = URI(raw_uri)

        req = cls(method=method, connection=connection,
                  transaction=transaction, uri=uri)

        return req

    def as_bytearray(self):
        """Dump the Request to a bytearray."""
        data = list()

        method = METHODS[self.method]
        data.append(method)

        trans = self.transaction
        data.append(trans)

        connection = CONNECTIONS[self.connection]
        data.append(connection)

        uri = str(self.uri)
        uri = uri.encode('ascii')
        uri_length = len(uri)
        data.append(uri_length)  # add uri length to header

        headers = bytearray(data)
        return headers + uri

    def as_dict(self):
        return asdict(self)


def is_request(message) -> bool:
    if isinstance(message, Request):
        return True

    if not hasattr(message, 'data'):
        return False

    data = message.data
    if not isinstance(data, bytearray):
        return False

    if len(data) == 0:
        logger.debug(f'Data from message was empty')
        return False

    first_byte = data[0]
    return first_byte in METHODS.values()
