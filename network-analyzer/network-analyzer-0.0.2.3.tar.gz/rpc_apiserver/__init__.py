import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
LOGGER_CONFIG = os.path.join(os.path.dirname(BASE_DIR), 'logger.conf')

import logging
import logging.config
print "Logger config location", LOGGER_CONFIG
logging.config.fileConfig(LOGGER_CONFIG)
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

# from core_rest_apiserver import app
from flask import Flask
app = Flask(__name__)
from jsonrpcserver import methods
from jsonrpcserver.exceptions import *

import rpc_apiserver.core
import rpc_apiserver.controllers
import rpc_apiserver.server