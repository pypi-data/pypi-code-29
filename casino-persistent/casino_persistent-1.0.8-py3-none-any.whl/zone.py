from sqlalchemy import Column, JSON, String, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from flask_sqlalchemy import model
from casino_persistent.base_entity import BaseEntity
from casino_persistent.utils import update_balance, update_balance_to_float


class Zone(BaseEntity, model):
    __tablename__ = "casino_zones"

    name = Column(String, nullable=False, unique=True)
    jackpot = Column(JSON)
    init_jackpot = Column(JSONB)
    jackpot_rate = Column(Integer)
    rooms = relationship("Room", backref='zone')

    def __init__(self, name, jackpot=None, init_jackpot=None, jackpot_rate=None):
        self.name = name
        self.jackpot = update_balance(jackpot)
        self.init_jackpot = update_balance(init_jackpot)
        self.jackpot_rate = jackpot_rate

    def to_json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'jackpot': update_balance_to_float(self.jackpot),
            'init_jackpot': update_balance_to_float(self.init_jackpot),
            'active': self.active,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
