from sqlalchemy import Column, BigInteger, ForeignKey, Integer, ARRAY, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy_utils import UUIDType, ChoiceType

from flask_sqlalchemy import model
from casino_persistent.base_entity import BaseEntity
from casino_persistent.utils import get_epochtime_ms, ShatoshiParser
from casino_persistent.utils.status import Status


class ConsecutivePanel(BaseEntity, model):
    __tablename__ = "casino_consecutive_panels"

    room_id = Column(UUIDType(binary=False), ForeignKey('casino_rooms.id'))
    user_id = Column(UUIDType(binary=False), ForeignKey('casino_users.id'))

    start_game = Column(BigInteger, default=get_epochtime_ms())
    number_of_consecutive = Column(Integer)
    list_panel = Column(ARRAY(JSONB))
    bet_number = Column(JSONB)
    bet_amount = Column(BigInteger)
    bet_crypto = Column(String)
    total_amount = Column(JSONB)
    remaining = Column(Integer)

    status = Column(ChoiceType(Status))

    def __init__(self,
                 room,
                 user,
                 bet_crypto,
                 start_game=start_game,
                 status=status,
                 number_of_consecutive=number_of_consecutive,
                 list_panel=list_panel,
                 bet_number=bet_number,
                 bet_amount=bet_amount,
                 total_amount=total_amount,
                 remaining=remaining
                 ):
        self.room = room
        self.user = user
        self.start_game = start_game,
        self.number_of_consecutive = number_of_consecutive
        self.list_panel = list_panel
        self.bet_number = bet_number
        self.bet_amount = ShatoshiParser.convert_coin_to_shatoshi(bet_amount)
        self.total_amount = total_amount
        self.remaining = remaining
        self.status = status
        self.bet_crypto = bet_crypto

    def to_json(self):
        return {
            "id": str(self.id),
            "room_id": str(self.user_id),
            "user_id": str(self.user_id),
            "number_of_consecutive": self.number_of_consecutive,
            "list_panel": self.list_panel,
            "bet_number": self.bet_number,
            "bet_amount": self.bet_amount,
            "total_amount": self.total_amount,
            "remaining": self.remaining,
            "status": self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
