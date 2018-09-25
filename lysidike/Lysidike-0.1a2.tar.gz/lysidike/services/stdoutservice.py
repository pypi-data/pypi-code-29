from lysidike.services.aservice import AService
import datetime


class StdOutService(AService):
    _prefix = None
    _suffix = None

    def __init__(self, config, mqtt_client, logger):
        AService.__init__(self, config, mqtt_client, __name__, logger)
        self._prefix = self._config["prefix"]
        self._suffix = self._config["suffix"]

    def _start(self):
        pass

    def _stop(self):
        pass

    def _test_connection(self):
        return True

    def _render_message(self, messages):
        body = "received {} messages since last update.\n".format(len(messages))
        body += "\nMessages:\n"
        for entry in messages:
            timestamp, topic, message = entry
            timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            body += "  {}; {}; '{}'\n".format(timestamp, topic, message)
        body += "EOF\n"
        return body

    def _send_message(self, subject, message):
        self._logger.info("Writing to stdout")
        print(self._prefix)
        print("@{}".format(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")))
        print(subject)
        print()
        print(message)
        print(self._suffix)
