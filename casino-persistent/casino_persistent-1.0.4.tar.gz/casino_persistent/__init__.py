from flask_sqlalchemy import SQLAlchemy

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
