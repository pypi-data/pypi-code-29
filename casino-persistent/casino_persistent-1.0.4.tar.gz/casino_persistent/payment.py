from sqlalchemy import Column, Text, ForeignKey, Enum, String, Float
from sqlalchemy_utils import UUIDType

from casino_persistent import db
from casino_persistent.base_entity import BaseEntity
from casino_persistent.utils.crypto import Crypto
from casino_persistent.utils.transaction_type import TransactionType


class Payment(BaseEntity, db.Model):
    __tablename__ = "casino_payments"

    user_id = Column(UUIDType(binary=False), ForeignKey('casino_users.id'))
    type = Column(Enum(TransactionType), default=TransactionType.DEPOSIT)
    address = Column(String)
    payment_id = Column(String)
    amount = Column(Float)
    crypto = Column(String, default=Crypto.ETH.value)
    status = Column(String, default=TransactionType.DEPOSIT.value)
    note = Column(Text)

    def __init__(self, user, payment_id, type=type, address=address, amount=amount, crypto=crypto, status=status,
                 note=note):
        self.users = user
        self.type = type
        self.address = address
        self.amount = amount
        self.crypto = crypto
        self.status = status
        self.note = note
        self.payment_id = payment_id

    def to_json(self):
        return {
            'id': str(self.id),
            'user_id': str(self.user_id),
            'type': self.type,
            'address': self.address,
            'amount': self.amount,
            'crypto': self.crypto,
            'status': self.status,
            'note': self.note
        }
