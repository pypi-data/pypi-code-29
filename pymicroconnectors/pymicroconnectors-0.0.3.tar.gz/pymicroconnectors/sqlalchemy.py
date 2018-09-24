from sqlalchemy import create_engine
import pymicroconnectors.config as config

api = None

def init():
    global api
    api = create_engine(*config.get_value('sqlalchemy.base'), **config.get_value('sqlalchemy.config'))