from flask_sqlalchemy import SQLAlchemy


class CasinoPersistent(object):
    def __init__(self, app):
        self.db = SQLAlchemy(app)

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
    'CasinoPersistent'
]
