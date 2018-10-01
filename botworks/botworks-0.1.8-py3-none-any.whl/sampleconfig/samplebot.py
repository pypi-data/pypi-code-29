import _thread
import configparser
import logging
import os

from botworks.botworks import Botworks
from botworks.channel.Channel import Channel
from botworks.config_constants import ERROR_SLEEP_TIME, SLEEP_TIME, LOG_LEVEL
from sampleconfig import gameofthrones

config = configparser.ConfigParser().read("config.ini")

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)


def listen_thread():
    got_channel = Channel(name="gameofthrones", mod_names=["Syrio Forel", "threeeyedraven"],
                          responses=gameofthrones.messages)
    Botworks(
        str(os.environ.get('SLACK_BOT_TOKEN')),
        str(os.environ.get('SLACK_BOT_NAME')),
        [got_channel],
        config={
            LOG_LEVEL: logging.WARNING,
            SLEEP_TIME: 3,
            ERROR_SLEEP_TIME: 8
        }
    ).listen()


if __name__ == "__main__":
    log.error("Starting")
    _thread.start_new_thread(listen_thread, ())
    log.error("Listener thread started")
