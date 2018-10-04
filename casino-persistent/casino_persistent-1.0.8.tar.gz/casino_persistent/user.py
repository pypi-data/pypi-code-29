from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType

from flask_sqlalchemy import model
from casino_persistent.base_entity import BaseEntity


class User(BaseEntity, model):
    __tablename__ = "casino_users"

    user_name = Column(String(128), nullable=False)
    email = Column(EmailType, nullable=False)
    uuid = Column(String(36), unique=True)
    wallets = relationship("Wallet", backref='user', lazy=True)
    panels = relationship("Panel", backref=db.backref('user', lazy=True))
    consecutive_panels = relationship("ConsecutivePanel", backref='user', lazy=True)
    payments = relationship("Payment", backref='user', lazy=True)

    def __init__(self, user_name, email, uuid):
        self.user_name = user_name
        self.email = email
        self.uuid = uuid

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
