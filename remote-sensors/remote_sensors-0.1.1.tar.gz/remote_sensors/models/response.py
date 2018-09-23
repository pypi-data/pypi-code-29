from dataclasses import dataclass, asdict

from typing import Any

from remote_sensors import datatypes
from remote_sensors.exc import (
    InvalidResponse,
    ResponseMarshalerError,
)
from remote_sensors.log import logger


# same as ResponseType
STATUSES = {
    'ACK': 0x05,
    'NOT_FOUND': 0x06,
    'SEND': 0x07,
    'RESOURCE_DELETED': 0x08,
    'ERROR_FOUND': 0x09,
}

CONTENT_TYPE = {
    'UNSIGNED': 0x00,
    'SIGNED': 0x01,
    'CHAR': 0x02,
    'FLOAT': 0x03,
}


@dataclass(order=True)
class Response:
    """Response instance.

    Frame order:
        |STATUS|TRANS|WORD_SIZE|CNT_TYPE|CNT_LENGTH|DATA...|

    :WORD_SIZE: unit is 1 byte

    """
    status: str
    transaction: int
    content_type: str = 'UNSIGNED'
    content_length: int = 0
    data: Any = None
    raw_data: Any = None
    word_size: int = 1  # byte

    @classmethod  # noqa: C901
    def from_bytearray(cls, data: bytearray):
        """Returns a Response instance from the given bytearray."""
        if not data:
            raise InvalidResponse('The frame is not a valid response')

        status = data[0]  # first byte is the responseType/Status
        if status not in STATUSES.values():
            raise ResponseMarshalerError(f'The response bytearray does not contain'
                                         f'a valid Status/Type ({status})')

        # get the canonical name
        for key, value in STATUSES.items():
            if value == status:
                status = key
                break

        transaction = data[1]  # second byte is the transaction

        word_size = data[2]  # third byte is the word size

        content_type = data[3]  # fourth byte is the content type
        if content_type not in CONTENT_TYPE.values():
            raise ResponseMarshalerError(f'The response bytearray does not contain'
                                         f'a valid Content Type ({content_type})')

        # get the cannonical name
        for key, value in CONTENT_TYPE.items():
            if value == content_type:
                content_type = key
                break

        data_length = data[4]  # fifth byte is the length of the data

        raw_data = None  # sometimes the response is empty
        logger.debug(f'Data length: {data_length}')
        if data_length > 0:
            raw_data = data[5:5 + data_length]  # data is from the 5th element until the end

        response = cls(content_type=content_type, status=status,
                       transaction=transaction, word_size=word_size,
                       content_length=data_length, raw_data=raw_data)

        try:
            _cnt = datatypes.get(content_type, raw_data, word_size)
        except NotImplemented:
            response.data = None
        else:
            response.data = _cnt

        return response

    def as_bytearray(self):
        """Dump the response as bytearray."""
        headers = list()

        status = STATUSES[self.status]
        headers.append(status)

        headers.append(self.transaction)
        headers.append(self.word_size)

        content_type = CONTENT_TYPE[self.content_type]
        headers.append(content_type)

        content_length = self.content_length
        if self.raw_data is not None:
            content_length = len(self.raw_data)
        headers.append(content_length)

        header = bytearray(headers)
        data = self.raw_data if self.raw_data is not None else bytearray()
        return header + data

    def as_dict(self, with_bytearrays: bool = True, encoding: str = 'utf8'):
        dictionary = asdict(self)
        # we have our own data types
        if self.data and isinstance(self.data, datatypes.RemoteSensorsType):
            dictionary['data'] = self.data.value
            del dictionary['raw_data']  # we dont need it :D
            return dictionary

        # custom datatypes: convert the bytearrays to utf-8 (ascii) supported
        if not with_bytearrays and isinstance(self.data, bytearray):
            dictionary['data'] = self.data.decode(encoding)
        if not with_bytearrays and isinstance(self.raw_data, bytearray):
            dictionary['raw_data'] = self.data.decode(encoding)
        return dictionary


def is_response(message) -> bool:
    if isinstance(message, Response):
        return True

    if not hasattr(message, 'data'):
        return False

    try:
        data = message.data
        if not isinstance(data, bytearray):
            logger.debug(f'Checked to see if its bytearray failed, {data}')
            return False
    except Exception as e:
        logger.error(f'Failed to check if it is a response, {e}, returning False')
        return False

    if len(data) == 0:
        logger.debug(f'Getting data length 0!')
        return False

    first_byte = data[0]
    logger.debug(f'Evaluating {first_byte}, {first_byte in STATUSES.values()}')
    return first_byte in STATUSES.values()
