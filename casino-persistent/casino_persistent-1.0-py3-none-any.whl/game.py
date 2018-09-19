import json
from uuid import uuid4

from sqlalchemy import String, Column, JSON, Boolean, BigInteger, ForeignKey, Integer, ARRAY, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from app import db
from app.utils import get_epochtime_ms, calculate_time_bet
from app.utils.status import Status


class Game(db.Model):
    __tablename__ = "casino_games"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    room_id = Column(UUIDType(binary=False), ForeignKey('casino_rooms.id'))
    game_result = Column(JSON)
    result = Column(String)
    time_seed = Column(String, nullable=False)
    fairness_seed = Column(String, nullable=False)
    total_panels_amount = Column(ARRAY(Text), nullable=True)
    total_panels_prize = Column(ARRAY(Text), nullable=True)
    winner_jackpot = Column(Integer, default=0)
    created_at = Column(BigInteger, default=get_epochtime_ms())
    # 14-09-18 Linh dao added for game flow change
    start_at = Column(BigInteger)
    end_bet_at = Column(BigInteger)
    get_result_at = Column(BigInteger)
    show_at = Column(BigInteger)
    end_show_at = Column(BigInteger)
    end_at = Column(BigInteger)
    # 14-09-18 Added end
    updated_at = Column(BigInteger, default=get_epochtime_ms(), onupdate=get_epochtime_ms())
    active = Column(Boolean, default=True)
    status = Column(String(10))
    panels = relationship("Panel", backref=db.backref('games', lazy=True))

    def __init__(self,
                room,
                status,
                result=result,
                start_at=start_at,
                end_bet_at = end_bet_at,
                get_result_at = get_result_at,
                show_at = show_at,
                end_show_at = end_show_at,
                end_at = end_at,
                game_result=game_result,
                time_seed=time_seed,
                total_panels_amount=None,
                winner_jackpot=0,
                fairness_seed=fairness_seed,
                total_panels_prize=None):

        if total_panels_prize is None:
            total_panels_prize = []
        if total_panels_amount is None:
            total_panels_amount = []
        self.room = room
        self.start_game = start_game
        self.end_game = end_game
        self.betting_time = betting_time
        self.result = result
        self.game_result = game_result
        self.time_seed = time_seed
        self.total_panels_amount = total_panels_amount
        self.total_panels_prize = total_panels_prize
        self.winner_jackpot = winner_jackpot
        self.fairness_seed = fairness_seed
        self.status = status
        self.start_at = start_at,
        self.end_bet_at = end_bet_at,
        self.get_result_at = get_result_at,
        self.show_at = show_at,
        self.end_show_at = end_show_at,
        self.end_at = end_at,

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

            start_game = get_epochtime_ms()
            betting_time = calculate_time_bet()
            end_game = start_game + betting_time

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
                start_game=start_game,
                betting_time=betting_time,
                end_game=end_game
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
            "result": self.result if self.status == Status.ENDED else '',
            "fairness_seed": self.fairness_seed
        }

    def convert_to_array(self):
        return [json.loads(amount) for amount in self.total_panels_amount]

    def convert_prize_array(self):
        return [json.loads(prize) for prize in self.total_panels_prize]
