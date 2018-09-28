from flask_sqlalchemy import SQLAlchemy

from casino_persistent.consecutive_panel import ConsecutivePanel
from casino_persistent.game import Game
from casino_persistent.panel import Panel
from casino_persistent.payment import Payment
from casino_persistent.room import Room
from casino_persistent.user import User
from casino_persistent.wallet import Wallet
from casino_persistent.zone import Zone

db = SQLAlchemy()


class CasinoPersistent:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if CasinoPersistent.__instance is None:
            CasinoPersistent(db)
        return CasinoPersistent.__instance

    def __init__(self, db):
        """ Virtually private constructor. """
        if CasinoPersistent.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CasinoPersistent.__instance = db


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
]
