from flask_sqlalchemy import model
from sqlalchemy import Column, BigInteger, ForeignKey, String
from sqlalchemy_utils import UUIDType

from casino_persistent.base_entity import BaseEntity
from casino_persistent.utils import ShatoshiParser


class Payment(BaseEntity, model):
    __tablename__ = "casino_payments"

    user_id = Column(UUIDType(binary=False), ForeignKey('casino_users.id'))
    type = Column(String)
    address = Column(String)
    payment_id = Column(String)
    note = Column(String)
    amount = Column(BigInteger)
    crypto = Column(String(20))
    status = Column(String(20))

    def __init__(self, user, payment_id, type, address=address, amount=amount, crypto=crypto, status=status,
                 note=note):
        self.user = user
        self.type = type
        self.address = address
        self.amount = ShatoshiParser.convert_coin_to_shatoshi(amount)
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
