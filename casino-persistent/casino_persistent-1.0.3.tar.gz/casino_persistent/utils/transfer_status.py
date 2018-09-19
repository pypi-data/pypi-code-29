from enum import Enum

from casino_persistent.exceptions.api_errors import ApiError


class TransferStatus(Enum):
    PENDING = 1
    APPROVED = 2
    REJECT = 3

    @classmethod
    def from_name(cls, name) -> Enum:
        for status in TransferStatus:
            if status.value == name.upper():
                return status
            raise ApiError(
                f'{name} is not a valid transfer status. Transfer status in ({[e.value for e in TransferStatus]})')
