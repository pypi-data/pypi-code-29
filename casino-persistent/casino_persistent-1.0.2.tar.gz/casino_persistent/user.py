from uuid import uuid4

from sqlalchemy import String, Column, Boolean, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType, EmailType

from app import db
from app.utils import get_epochtime_ms


class User(db.Model):
    __tablename__ = "casino_users"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    created_at = Column(BigInteger, default=get_epochtime_ms())
    updated_at = Column(BigInteger, default=get_epochtime_ms(), onupdate=get_epochtime_ms())
    active = Column(Boolean, default=True)
    user_name = Column(String(128), nullable=False)
    email = Column(EmailType, nullable=False)
    uuid = Column(String(36), unique=True)
    wallets = relationship("Wallet", backref='users', lazy=True)
    panels = relationship("Panel", backref=db.backref('users', lazy=True))
    consecutive_panels = relationship("ConsecutivePanel", backref='users', lazy=True)
    payments = relationship("Payment", backref=db.backref('users', lazy=True))

    def __init__(self, user_name, email, uuid, wallets=None):
        self.user_name = user_name
        self.email = email
        self.uuid = uuid
        self.wallets = wallets

    def to_json(self):
        return {
            'id': str(self.id),
            'user_name': self.user_name,
            'email': self.email,
            'uuid': self.uuid,
            'active': self.active,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
