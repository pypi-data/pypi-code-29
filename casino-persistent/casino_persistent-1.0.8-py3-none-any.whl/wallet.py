from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, BigInteger
from sqlalchemy_utils import UUIDType

from flask_sqlalchemy import model
from casino_persistent.base_entity import BaseEntity
from casino_persistent.utils import ShatoshiParser
from casino_persistent.utils.crypto import Crypto


class Wallet(BaseEntity, model):
    __tablename__ = "casino_wallets"

    user_id = Column(UUIDType(binary=False), ForeignKey('casino_users.id'))
    address = Column(String)
    amount = Column(BigInteger)
    crypto = Column(String, default=Crypto.ETH.value)
    __table_args__ = (UniqueConstraint('user_id', 'crypto', name='user_crypto'),)

    def __init__(self, user, address, crypto, amount=0):
        self.user = user
        self.address = address
        self.crypto = crypto
        self.amount = ShatoshiParser.convert_coin_to_shatoshi(amount)

    def to_json(self):
        return {
            'id': str(self.id),
            'user_id': str(self.user_id),
            'address': self.address,
            'amount': ShatoshiParser.convert_shatoshi_to_coin(self.amount),
            'crypto': self.crypto,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }
