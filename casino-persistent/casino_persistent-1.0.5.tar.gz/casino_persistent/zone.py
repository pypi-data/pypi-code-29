from sqlalchemy import Column, JSON, String, Integer
from sqlalchemy.orm import relationship

from casino_persistent import db
from casino_persistent.base_entity import BaseEntity


class Zone(BaseEntity, db.Model):
    __tablename__ = "casino_zones"

    name = Column(String, nullable=False, unique=True)
    jackpot = Column(JSON)
    init_jackpot = Column(JSON)
    jackpot_rate = Column(Integer)
    rooms = relationship("Room", backref='zone')

    def __init__(self, name, jackpot=None, init_jackpot=None, jackpot_rate=None):
        self.name = name
        self.jackpot = jackpot
        self.init_jackpot = init_jackpot
        self.jackpot_rate = jackpot_rate

    def to_json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'jackpot': self.jackpot,
            'init_jackpot': self.init_jackpot,
            'active': self.active,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
