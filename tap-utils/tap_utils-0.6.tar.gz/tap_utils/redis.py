import json
import logging
from json import JSONDecodeError


logger = logging.getLogger("utils")


def load_redis_message(raw_message):
    message = None

    if raw_message["type"] == "message":
        try:
            message = json.loads(raw_message["data"].decode("utf-8"))
        except UnicodeDecodeError:
            logger.exception("Can't decode redis message: %s" % raw_message)
        except (TypeError, JSONDecodeError):
            logger.exception("Can't load json from redis message: %s" % raw_message)

    return message
