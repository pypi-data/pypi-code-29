import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from socketio_server import app, socketio

socketio.run(app, port=5050) #app.config['SOCKETIO_PORT'])
