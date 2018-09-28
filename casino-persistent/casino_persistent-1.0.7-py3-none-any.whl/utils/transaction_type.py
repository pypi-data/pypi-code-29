from enum import Enum


class TransactionType(Enum):
    WITHDRAW = 'withdraw'
    DEPOSIT = 'deposit'

    @classmethod
    def from_name(cls, name) -> Enum:
        for transaction in TransactionType:
            if transaction.value == name.upper():
                return transaction
            print(f'{name} is not a valid transaction name. Transaction Type in ({[e.value for e in TransactionType]})')
