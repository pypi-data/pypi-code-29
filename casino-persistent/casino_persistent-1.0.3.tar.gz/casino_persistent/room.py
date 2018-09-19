import json
from uuid import uuid4

from sqlalchemy import String, Column, JSON, Boolean, BigInteger, Text, ForeignKey, Integer, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from casino_persistent import CasinoPersistent
from casino_persistent.base_entity import BaseEntity
from casino_persistent.exceptions.api_errors import ApiError
from casino_persistent.utils import get_epochtime_ms


class Room(BaseEntity, CasinoPersistent.get_db().Model):
    __tablename__ = "casino_rooms"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    zone_id = Column(UUIDType(binary=False), ForeignKey('casino_zones.id'))
    games = relationship("Game", backref='room', lazy=True)
    name = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False, unique=True)
    jackpot = Column(JSON)
    init_jackpot = Column(JSON)
    # 18-09-18 Linh dao added for game flow change
    jackpot_rate = Column(Integer)
    betting_period = Column(Integer)
    end_bet_period = Column(Integer)
    get_result_period = Column(Integer)
    show_period = Column(Integer)
    end_show_period = Column(Integer)
    # 18-09-18 Added end
    minimum_amount = Column(ARRAY(Text), nullable=True)
    maximum_amount = Column(ARRAY(Text), nullable=True)
    created_at = Column(BigInteger, default=get_epochtime_ms())
    updated_at = Column(BigInteger, default=get_epochtime_ms(), onupdate=get_epochtime_ms())
    active = Column(Boolean, default=True)
    consecutive_panels = relationship("ConsecutivePanel", backref='rooms', lazy=True)

    def __init__(self, name, title, zone,
                 jackpot=None, init_jackpot=None, jackpot_rate=None,
                 minimum_amount=None, maximum_amount=None,
                 betting_period=None, end_bet_period=None,
                 get_result_period=None, show_period=None,
                 end_show_period=None):

        if minimum_amount is None:
            minimum_amount = []
        if maximum_amount is None:
            maximum_amount = []
        self.name = name
        self.zone = zone
        self.title = title
        self.minimum_amount = minimum_amount
        self.maximum_amount = maximum_amount
        self.jackpot = jackpot
        self.init_jackpot = init_jackpot
        self.jackpot_rate = jackpot_rate
        self.betting_period = betting_period
        self.end_bet_period = end_bet_period
        self.get_result_period = get_result_period
        self.show_period = show_period
        self.end_show_period = end_show_period

    @classmethod
    def form_json(cls, data, zone):
        try:
            if data:
                name = data.get('name')
                jackpot = data.get('jackpot')
                init_jackpot = data.get('init_jackpot')
                title = data.get('title')
                betting_period = data.get('betting_period', 10)
                minimum_amount = [json.dumps(amount) for amount in data.get('minimum_amount', [])]
                maximum_amount = [json.dumps(amount) for amount in data.get('maximum_amount', [])]

                return cls(name=name,
                           jackpot=jackpot,
                           init_jackpot=init_jackpot,
                           title=title,
                           zone=zone,
                           betting_period=betting_period,
                           minimum_amount=minimum_amount,
                           maximum_amount=maximum_amount
                           )
        except ValueError:
            raise ApiError('Invalid Value')

    def to_json(self):
        return {
            'id': str(self.id),
            'zone_id': str(self.zone_id),
            'title': self.title,
            'name': self.name,
            'jackpot': self.jackpot,
            'init_jackpot': self.init_jackpot,
            'betting_period': self.betting_period,
            'waiting_period': self.waiting_period,
            'minimum_amount': self.convert_minimum_amount_to_array(),
            'maximum_amount': self.convert_maximum_amount_to_array(),
            'active': self.active,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def simple_room(self):
        return {
            'id': str(self.id),
            "minimum_amount": self.convert_minimum_amount_to_array(),
            "maximum_amount": self.convert_maximum_amount_to_array(),
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }

    def convert_minimum_amount_to_array(self):
        return [json.loads(amount) for amount in self.minimum_amount]

    def convert_maximum_amount_to_array(self):
        return [json.loads(amount) for amount in self.maximum_amount]
