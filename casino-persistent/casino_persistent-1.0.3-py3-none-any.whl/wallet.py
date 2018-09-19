from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, Float
from sqlalchemy_utils import UUIDType

from casino_persistent import CasinoPersistent
from casino_persistent.base_entity import BaseEntity
from casino_persistent.utils.crypto import Crypto


class Wallet(BaseEntity, CasinoPersistent.get_db().Model):
    __tablename__ = "casino_wallet"

    user_id = Column(UUIDType(binary=False), ForeignKey('casino_users.id'))
    address = Column(String, unique=True)
    amount = Column(Float, default=0.0)
    crypto = Column(String, default=Crypto.ETH.value)
    __table_args__ = (UniqueConstraint('user_id', 'crypto', name='user_crypto'),)

    def __init__(self, user, address, crypto, amount=0.0):
        self.users = user,
        self.address = address,
        self.amount = amount,
        self.crypto = crypto

    def to_json(self):
        return {
            'id': str(self.id),
            'user_id': str(self.user_id),
            'address': self.address,
            'amount': self.amount,
            'crypto': self.crypto,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }
