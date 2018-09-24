import mongoengine
import pymicroconnectors.config as config

def init():
    mongoengine.connect(**config.get_value('mongo.connection'))