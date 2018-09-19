from uuid import uuid4

from sqlalchemy import Column, JSON, Boolean, BigInteger, ForeignKey, Integer, ARRAY, Enum, Text
from sqlalchemy_utils import UUIDType

from app import db
from app.utils import get_epochtime_ms
from app.utils.status import Status


class ConsecutivePanel(db.Model):
    __tablename__ = "casino_consecutive_panels"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    room_id = Column(UUIDType(binary=False), ForeignKey('casino_rooms.id'))
    user_id = Column(UUIDType(binary=False), ForeignKey('casino_users.id'))

    start_game = Column(BigInteger, default=get_epochtime_ms())
    number_of_consecutive = Column(Integer)
    list_panel = Column(ARRAY(Text))
    bet_number = Column(JSON)
    bet_amount = Column(JSON)
    total_amount = Column(JSON)
    remaining = Column(Integer)

    created_at = Column(BigInteger, default=get_epochtime_ms())
    updated_at = Column(BigInteger, default=get_epochtime_ms(), onupdate=get_epochtime_ms())
    active = Column(Boolean, default=True)
    status = Column(Enum(Status), default=Status.RUNNING.value)

    def __init__(self,
                 room,
                 user,
                 start_game=start_game,
                 status=status,
                 number_of_consecutive=number_of_consecutive,
                 list_panel=list_panel,
                 bet_number=bet_number,
                 bet_amount=bet_amount,
                 total_amount=total_amount,
                 remaining=remaining
                 ):
        self.rooms = room
        self.users = user
        self.start_game = start_game,
        self.number_of_consecutive = number_of_consecutive
        self.list_panel = list_panel
        self.bet_number = bet_number
        self.bet_amount = bet_amount
        self.total_amount = total_amount
        self.remaining = remaining
        self.status = status

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
