from flask_restful import Api
import pymicroconnectors.flask as flask
import pymicroconnectors.config as config


api = None

def init():
    if flask.app is None:
        flask.init()

    global api
    api = Api(flask.app, prefix=f"/{config.get_value('flask.restful.context')}", **config.get_value('flask.restful.config'))


def install(resource_list):
    for resource in resource_list:
        api.add_resource(resource[0], resource[1], **resource[2])
