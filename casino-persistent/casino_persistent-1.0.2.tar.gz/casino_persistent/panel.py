import json
from uuid import uuid4

from flask_restplus import abort
from sqlalchemy import Column, JSON, Boolean, BigInteger, ForeignKey, ARRAY, String, Integer
from sqlalchemy_utils import UUIDType

from app import db
from app.utils import get_epochtime_ms
from app.utils.status import Status


class Panel(db.Model):
    __tablename__ = "casino_panels"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    game_id = Column(UUIDType(binary=False), ForeignKey('casino_games.id'))
    user_id = Column(UUIDType(binary=False), ForeignKey('casino_users.id'))
    bet_number = Column(ARRAY(Integer), nullable=True)
    bet_tie = Column(String, nullable=True)
    bet_amount = Column(JSON)
    power_play = Column(Boolean)
    result_amount = Column(JSON)
    win_jackpot = Column(Boolean)
    status = Column(String(10))
    blackball = Column(Integer)
    created_at = Column(BigInteger, default=get_epochtime_ms())
    updated_at = Column(BigInteger, default=get_epochtime_ms(), onupdate=get_epochtime_ms())
    active = Column(Boolean, default=True)

    def __init__(self, game, user, bet_number, bet_amount=bet_amount, power_play=False,
                 status=Status.RUNNING.value, result_amount=None, win_jackpot=None, blackball=-1, bet_tie=None):
        self.games = game
        self.users = user
        self.bet_amount = bet_amount
        self.bet_number = bet_number
        self.power_play = power_play
        self.result_amount = result_amount
        self.win_jackpot = win_jackpot
        self.status = status
        self.blackball = blackball
        self.bet_tie = bet_tie

    @classmethod
    def form_json(cls, data, game, user):
        try:
            if data:
                bet_number = [json.dumps(amount) for amount in data.get('bet_number', [])]
                bet_amount = data.get('bet_amount')
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
                           bet_tie=bet_tie)
        except ValueError:
            abort(code=406, message="Invalid content")

    def to_json(self):
        return {
            'id': str(self.id),
            'game_id': str(self.game_id),
            'user_id': str(self.user_id),
            'bet_tie': self.bet_tie,
            'bet_amount': self.bet_amount,
            'bet_number': self.convert_bet_number_to_array(),
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
            'bet_number': self.convert_bet_number_to_array(),
            "bet_amount": self.bet_amount,
            "power_play": self.power_play,
            "status": self.status
        }

    def convert_bet_number_to_array(self):
        return [json.loads(amount) for amount in self.bet_number]
