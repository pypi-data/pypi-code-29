import json

from sqlalchemy import Column, Boolean, ForeignKey, ARRAY, String, Integer, Text, BigInteger
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy_utils import UUIDType

from casino_persistent import CasinoPersistent
from casino_persistent.base_entity import BaseEntity
from casino_persistent.utils import ShatoshiParser
from casino_persistent.utils.status import Status
from flask_sqlalchemy import model

class Panel(BaseEntity, model):
    __tablename__ = "casino_panels"

    game_id = Column(UUIDType(binary=False), ForeignKey('casino_games.id'))
    user_id = Column(UUIDType(binary=False), ForeignKey('casino_users.id'))
    bet_number = Column(ARRAY(Integer), nullable=True)
    bet_tie = Column(String, nullable=True)
    bet_amount = Column(BigInteger)
    bet_crypto = Column(String)
    power_play = Column(Boolean)
    result_amount = Column(JSONB)
    win_jackpot = Column(Boolean)
    status = Column(String(20))
    blackball = Column(Integer)
    description = Column(Text, nullable=True)

    def __init__(self, game, user, bet_number, bet_crypto, bet_amount, power_play=False,
                 status=Status.RUNNING.value, result_amount=None, win_jackpot=None, blackball=-1, bet_tie=None):
        self.game = game
        self.user = user
        self.bet_amount = ShatoshiParser.convert_coin_to_shatoshi(bet_amount)
        self.bet_number = bet_number
        self.power_play = power_play
        self.result_amount = result_amount
        self.win_jackpot = win_jackpot
        self.status = status
        self.blackball = blackball
        self.bet_tie = bet_tie
        self.bet_crypto = bet_crypto

    @classmethod
    def form_json(cls, data, game, user):
        try:
            if data:
                bet_number = data.get('bet_number', [])
                bet_amount = data.get('bet_amount')
                bet_crypto = data.get('bet_crypto')
                power_play = data.get('power_play')
                status = data.get('status')
                result_amount = data.get('result_amount')
                win_jackpot = data.get('win_jackpot')
                bet_tie = data.get('bet_tie')
                return cls(game=game,
                           user=user,
                           bet_number=bet_number,
                           bet_amount=bet_amount,
                           power_play=power_play,
                           status=status,
                           result_amount=result_amount,
                           win_jackpot=win_jackpot,
                           bet_tie=bet_tie,
                           bet_crypto=bet_crypto
                           )
        except ValueError:
            raise Exception('Invalid content')

    def to_json(self):
        return {
            'id': str(self.id),
            'game_id': str(self.game_id),
            'user_id': str(self.user_id),
            'bet_tie': self.bet_tie,
            'bet_amount': ShatoshiParser.convert_shatoshi_to_coin(self.bet_amount),
            'bet_number': self.bet_number,
            'bet_crypto': self.bet_crypto,
            'power_play': self.power_play,
            'result_amount': self.result_amount,
            'win_jackpot': self.win_jackpot,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }

    def to_panel(self):
        return {
            'bet_tie': self.bet_tie,
            'bet_number': self.bet_number(),
            "bet_amount": ShatoshiParser.convert_shatoshi_to_coin(self.bet_amount),
            "bet_crypto": self.bet_crypto,
            "power_play": self.power_play,
            "status": self.status
        }

    def convert_bet_number_to_array(self):
        return [json.loads(amount) for amount in self.bet_number]
