from uuid import uuid4

from sqlalchemy import Column, JSON, Boolean, BigInteger, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from app import db
from app.utils import get_epochtime_ms


class Zone(db.Model):
    __tablename__ = "casino_zones"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    created_at = Column(BigInteger, default=get_epochtime_ms())
    updated_at = Column(BigInteger, default=get_epochtime_ms(), onupdate=get_epochtime_ms())
    active = Column(Boolean, default=True)
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
