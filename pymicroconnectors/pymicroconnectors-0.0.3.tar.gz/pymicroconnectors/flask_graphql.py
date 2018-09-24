from flask_graphql import GraphQLView
import pymicroconnectors.flask as flask
import pymicroconnectors.config as config

def init():
    if flask.app is None:
        flask.init()


def install(schema):
    flask.app.add_url_rule(config.get_value('flask.graphQL.contex'),
                           view_func=GraphQLView.as_view(
                               config.get_value('flask.graphQL.contex'),
                               schema=schema,
                               graphiql=config.get_value('flask.graphQL.graphiql')
                           ))
