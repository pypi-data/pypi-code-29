import pymicroconnectors.flask as flask
import pymicroconnectors.config as config
from flask_ask import Ask


api = None

def init():
    if flask.app is None:
        flask.init()

    global api
    api = Ask(flask.app, f"/{config.get_value('flask.ask.context')}")