import json

from sqlalchemy import String, Column, BigInteger, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from flask_sqlalchemy import model
from casino_persistent.base_entity import BaseEntity
from casino_persistent.utils import get_epochtime_ms
from casino_persistent.utils.status import Status


class Game(BaseEntity, model):
    __tablename__ = "casino_games"

    room_id = Column(UUIDType(binary=False), ForeignKey('casino_rooms.id'))
    game_result = Column(JSONB)
    result = Column(String)
    time_seed = Column(String, nullable=False)
    fairness_seed = Column(String, nullable=False)
    total_panels_amount = Column(JSONB, nullable=True)
    total_panels_prize = Column(JSONB, nullable=True)
    winner_jackpot = Column(Integer, default=0)
    # 14-09-18 Linh dao added for game flow change
    start_at = Column(BigInteger)
    end_bet_at = Column(BigInteger)
    get_result_at = Column(BigInteger)
    show_at = Column(BigInteger)
    end_show_at = Column(BigInteger)
    end_at = Column(BigInteger)
    # 14-09-18 Added end
    status = Column(String(20))
    panels = relationship("Panel", backref='game', lazy=True, cascade_backrefs=True)

    def __init__(self,
                 room,
                 result=None,
                 start_at=None,
                 game_result=None,
                 time_seed=time_seed,
                 total_panels_amount=None,
                 winner_jackpot=0,
                 fairness_seed=fairness_seed,
                 total_panels_prize=None,
                 status=Status.RUNNING.value):

        if total_panels_prize is None:
            total_panels_prize = {}
        if total_panels_amount is None:
            total_panels_amount = {}
        if result is None:
            game_result = {}
        if start_at is None:
            self.start_at = get_epochtime_ms() + 5
        else:
            self.start_at = start_at
        self.room = room
        self.result = result
        self.game_result = game_result
        self.time_seed = time_seed
        self.total_panels_amount = total_panels_amount
        self.total_panels_prize = total_panels_prize
        self.winner_jackpot = winner_jackpot
        self.fairness_seed = fairness_seed
        self.status = status

        self.get_result_at = self.start_at + room.betting_period
        self.end_bet_at = self.get_result_at - room.end_bet_period
        self.show_at = self.get_result_at + room.get_result_period
        self.end_show_at = self.show_at + room.show_period
        self.end_at = self.end_show_at + room.end_bet_period

    @classmethod
    def from_json(cls, data, room):
        if data:
            result = data.get('result', None)
            game_result = data.get('game_result', None)
            time_seed = data.get('time_seed', None)
            fairness_seed = data.get('fairness_seed', None)
            total_panels_amount = [json.dumps(amount) for amount in data.get('total_panels_amount', [])]
            total_panels_prize = [json.dumps(price) for price in data.get('total_panels_prize', [])]
            winner_jackpot = data.get('winner_jackpot', 0)
            status = Status.from_name(data.get('status')).value

            return cls(
                room=room,
                result=result,
                game_result=game_result,
                time_seed=time_seed,
                fairness_seed=fairness_seed,
                total_panels_amount=total_panels_amount,
                total_panels_prize=total_panels_prize,
                winner_jackpot=winner_jackpot,
                status=status,
            )

    def to_json(self):
        return {
            "id": str(self.id),
            "room_id": str(self.room),
            "start_game": self.start_game,
            "end_game": self.end_game,
            "betting_time": self.betting_time,
            "result": self.result,
            "game_result": self.game_result,
            "time_seed": self.time_seed,
            "total_panels_amount": self.convert_to_array(),
            "winner_jackpot": self.winner_jackpot,
            "total_panels_prize": self.convert_prize_array(),
            "status": self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def to_game(self):
        return {
            "id": str(self.id),
            "room_id": str(self.room_id),
            "start_game": self.start_game,
            "end_game": self.end_game,
            "end_betting": self.betting_time,
            "result": self.result if self.status == Status.ENDED else '',
            "game_result": self.game_result,
            "time_seed": self.time_seed,
            "fairness_seed": self.fairness_seed,
            "status": self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def to_history(self):
        return {
            "id": str(self.id),
            "result": self.result
        }

    def to_bet_history(self):
        return {
            "id": str(self.id),
            "room_id": str(self.room.id),
            "game_result": self.game_result.to_json(),
            "time_seed": self.time_seed,
            "result": self.result if self.status == Status.ENDED.value or self.status == Status.ENDING.value else '',
            "fairness_seed": self.fairness_seed
        }

    def convert_to_array(self):
        return [json.loads(amount) for amount in self.total_panels_amount]

    def convert_prize_array(self):
        return [json.loads(prize) for prize in self.total_panels_prize]

    def is_keno(self):
        return self.room.zone.name == 'Keno'

    def is_bacarat(self):
        return self.room.zone.name == 'Bacarat'

    def is_power_ball(self):
        return self.room.zone.name == 'Power Ball'

    def is_rolet(self):
        return self.room.zone.name == 'Rolet'
