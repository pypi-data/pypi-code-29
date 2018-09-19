from enum import Enum

from casino_persistent.exceptions.api_errors import ApiError


class TransactionType(Enum):
    WITHDRAW = 'withdraw'
    DEPOSIT = 'deposit'

    @classmethod
    def from_name(cls, name) -> Enum:
        for transaction in TransactionType:
            if transaction.value == name.upper():
                return transaction
            raise ApiError(
                f'{name} is not a valid transaction name. Transaction Type in ({[e.value for e in TransactionType]})')
