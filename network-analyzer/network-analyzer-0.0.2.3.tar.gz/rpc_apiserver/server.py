import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from flask import request, Response
# from rpc_apiserver import socketio
from rpc_apiserver import app, methods

@methods.add
def ping():
    logger.info("Inside Ping Pong")
    return 'pong'

@methods.add
def hello(name):
    return "Hello " + name

@app.route('/v1' + 
    # app.config["API_VERSION"] + 
    '/jsonrpc', methods=['POST'])
def rpc():
    req = request.get_data().decode()
    response = methods.dispatch(req)
    return Response(str(response), response.http_status,
        mimetype='application/json')