from uuid import uuid4

from sqlalchemy import Column, Boolean, BigInteger, Text, ForeignKey, Enum, String, DECIMAL, Float
from sqlalchemy_utils import UUIDType

from app import db
from app.utils import get_epochtime_ms
from app.utils.crypto import Crypto
from app.utils.transaction_type import TransactionType


class Payment(db.Model):
    __tablename__ = "casino_payments"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    user_id = Column(UUIDType(binary=False), ForeignKey('casino_users.id'))
    type = Column(Enum(TransactionType), default=TransactionType.DEPOSIT)
    address = Column(String)
    payment_id = Column(String)
    amount = Column(Float)
    crypto = Column(String, default=Crypto.ETH.value)
    status = Column(String, default=TransactionType.DEPOSIT.value)
    note = Column(Text)
    created_at = Column(BigInteger, default=get_epochtime_ms())
    updated_at = Column(BigInteger, default=get_epochtime_ms(), onupdate=get_epochtime_ms())
    active = Column(Boolean, default=True)

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
