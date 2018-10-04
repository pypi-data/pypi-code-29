import json

from sqlalchemy import String, Column, ForeignKey, Integer, ARRAY
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from flask_sqlalchemy import model
from casino_persistent.base_entity import BaseEntity
from casino_persistent.utils import update_balance, update_balance_to_float


class Room(BaseEntity, model):
    __tablename__ = "casino_rooms"

    zone_id = Column(UUIDType(binary=False), ForeignKey('casino_zones.id'))
    games = relationship("Game", backref='room', lazy=True)
    name = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False, unique=True)
    jackpot = Column(JSONB)
    init_jackpot = Column(JSONB)
    # 18-09-18 Linh dao added for game flow change
    jackpot_rate = Column(Integer)
    betting_period = Column(Integer)
    end_bet_period = Column(Integer)
    get_result_period = Column(Integer)
    show_period = Column(Integer)
    end_show_period = Column(Integer)
    # 18-09-18 Added end
    minimum_amount = Column(ARRAY(JSONB), nullable=True)
    maximum_amount = Column(ARRAY(JSONB), nullable=True)
    consecutive_panels = relationship("ConsecutivePanel", backref='room', lazy=True)

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
                jackpot = update_balance(data.get('jackpot'))
                init_jackpot = update_balance(data.get('init_jackpot'))
                title = data.get('title')
                betting_period = data.get('betting_period', 10)
                minimum_amount = Room.convert_maximum_amount_to_text(data.get('minimum_amount', []))
                maximum_amount = Room.convert_maximum_amount_to_text(data.get('maximum_amount', []))
                end_bet_period = data.get('end_bet_period')
                jackpot_rate = data.get('jackpot_rate')
                get_result_period = data.get('get_result_period')
                show_period = data.get('show_period')
                end_show_period = data.get('end_show_period')
                return cls(name=name,
                           jackpot=jackpot,
                           init_jackpot=init_jackpot,
                           title=title,
                           zone=zone,
                           betting_period=betting_period,
                           minimum_amount=minimum_amount,
                           maximum_amount=maximum_amount,
                           end_bet_period=end_bet_period,
                           get_result_period=get_result_period,
                           jackpot_rate=jackpot_rate,
                           show_period=show_period,
                           end_show_period=end_show_period
                           )
        except ValueError:
            raise Exception('Invalid content')

    def to_json(self):
        return {
            'id': str(self.id),
            'zone_id': str(self.zone_id),
            'title': self.title,
            'name': self.name,
            'jackpot': update_balance_to_float(self.jackpot),
            'init_jackpot': update_balance_to_float(self.init_jackpot),
            'betting_period': self.betting_period,
            'minimum_amount': self.convert_minimum_amount_to_array_float(),
            'maximum_amount': self.convert_maximum_amount_to_array_float(),
            'active': self.active,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def simple_room(self):
        return {
            'id': str(self.id),
            'minimum_amount': self.convert_minimum_amount_to_array_float(),
            'maximum_amount': self.convert_maximum_amount_to_array_float(),
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }

    @staticmethod
    def convert_minimum_amount_to_text(minimum_amount):
        return [json.dumps(update_balance(amount)) for amount in minimum_amount]

    @staticmethod
    def convert_maximum_amount_to_text(maximum_amount):
        return [json.dumps(update_balance(amount)) for amount in maximum_amount]

    def convert_minimum_amount_to_array(self):
        return [json.loads(amount) for amount in self.minimum_amount]

    def convert_maximum_amount_to_array(self):
        return [json.loads(amount) for amount in self.maximum_amount]

    def convert_minimum_amount_to_array_float(self):
        return [update_balance_to_float(json.loads(amount)) for amount in self.minimum_amount]

    def convert_maximum_amount_to_array_float(self):
        return [update_balance_to_float(json.loads(amount)) for amount in self.maximum_amount]
