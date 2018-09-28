from sqlalchemy import String, Column, Integer
from clustaar.sqlalchemy.schema import Schema
from clustaar.sqlalchemy.table import Table


# User

class User(object):
    """The class use by the UserTable """

    def __init__(self, name: str):
        """
        Args:
            name (str): the user name
        """
        self.name = name


class UserTable(Table):
    """ A simple factory table used for tests """

    _model = User
    _schema = Schema("users",
                     Column("id", Integer, primary_key=True),
                     Column("name", String, nullable=False))


# Subscription

class Subscription(object):
    """The class use by the SubscriptionTable """

    def __init__(self, type: str, bot_id: str, user_id: str):
        """
        Args:
            type (str): the subscription type
            bot_id (str): the bot id
            user_id (str): the user id
        """
        self.type = type
        self.bot_id = bot_id
        self.user_id = user_id


class SubscriptionTable(Table):
    """ A simple factory table used for tests """

    _model = Subscription
    _schema = Schema("subscriptions",
                     Column("id", Integer, primary_key=True),
                     Column("type", String, nullable=False),
                     Column("bot_id", String, nullable=True),
                     Column("user_id", String, nullable=False))
