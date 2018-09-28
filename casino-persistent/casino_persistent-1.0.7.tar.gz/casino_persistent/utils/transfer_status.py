from enum import Enum


class TransferStatus(Enum):
    PENDING = 1
    APPROVED = 2
    REJECT = 3

    @classmethod
    def from_name(cls, name) -> Enum:
        for status in TransferStatus:
            if status.value == name.upper():
                return status
            print(f'{name} is not a valid transfer status. Transfer status in ({[e.value for e in TransferStatus]})')
