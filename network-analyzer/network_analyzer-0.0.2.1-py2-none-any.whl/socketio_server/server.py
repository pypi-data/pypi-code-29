import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from socketio_server import app, socketio, methods
from flask_socketio import SocketIO, send, emit

@socketio.on('jsonrpc')
def handle_jsonrpc(request):
    logger.info("Inside JSONRPC handler" + str(request))
    response = methods.dispatch(request)
    if not response.is_notification:
        emit('jsonrpc.response', response)
        send(response, json=True)
