import pymicroconnectors.flask as flask
import pymicroconnectors.config as config
from flask_assistant import Assistant


api = None

def init():
    if flask.app is None:
        flask.init()

    global api
    api = Assistant(flask.app, f"/{config.get_value('flask.assistant.context')}")