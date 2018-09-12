import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from rpc_apiserver import app

# from rpc_apiserver import socketio

# socketio.run(app, port=app.config['SOCKETIO_PORT'])
app.run(port=5000) #app.config['RPC_PORT'])