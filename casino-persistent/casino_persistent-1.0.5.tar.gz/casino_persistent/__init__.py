from flask_sqlalchemy import SQLAlchemy
from casino_persistent.room import Room
from casino_persistent.consecutive_panel import ConsecutivePanel
from casino_persistent.game import Game
from casino_persistent.payment import Payment
from casino_persistent.panel import Panel
from casino_persistent.zone import Zone
from casino_persistent.user import User
from casino_persistent.wallet import Wallet

db = SQLAlchemy()


class CasinoPersistent(object):
    def __init__(self, app):
        self.db = db.init_app(app)

    def get_db(self) -> SQLAlchemy:
        return self.db


__all__ = [
    'base_entity',
    'consecutive_panel',
    'game',
    'payment',
    'panel',
    'room',
    'zone',
    'user',
    'wallet',
    'CasinoPersistent',
    'db'
]
