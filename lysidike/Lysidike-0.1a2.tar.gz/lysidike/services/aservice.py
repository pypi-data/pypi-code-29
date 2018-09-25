from pelops import mylogger


class AService:
    _mqtt_client = None
    _logger = None
    _config = None
    last_message = None

    def __init__(self, config, mqtt_client, logger_name, logger):
        self._logger = mylogger.get_child(logger, logger_name)
        self._mqtt_client = mqtt_client
        self._config = config

        self._logger.info("{}.__init__".format(self.__class__.__name__))
        self._logger.debug("{}.__init__ config: {}".format(self.__class__.__name__, self._config))

    def start(self):
        self._logger.info("{}.start - starting".format(self.__class__.__name__))
        self._start()
        if not self._test_connection():
            self._logger.error("{}.start - connection test failed".format(self.__class__.__name__))
            raise RuntimeError("{}.start - connection test failed".format(self.__class__.__name__))
        self._logger.info("{}.start - started".format(self.__class__.__name__))

    def stop(self):
        self._logger.info("{}.stop - stopping".format(self.__class__.__name__))
        self._stop()
        self._logger.info("{}.stop - stopped".format(self.__class__.__name__))

    def publish(self, subject, messages):
        """
        Publish the topics to this service

        :param subject: string - subject for message
        :param messages: list of topics to be published. each entry is a tuple (datetime, topic, message)
        """
        self._logger.info("{}.publish - starting".format(self.__class__.__name__))
        self._logger.debug("{}.publish - subject: '{}', len messages: {}, messages: {}"
                           .format(self.__class__.__name__, subject, len(messages), messages))

        self.last_message = self._render_message(messages)
        self._logger.debug("{}.publish - message: ".format(self.__class__.__name__, self.last_message))

        self._send_message(subject, self.last_message)

        self._logger.info("{}.publish - finished".format(self.__class__.__name__))

    def _start(self):
        raise NotImplementedError

    def _stop(self):
        raise NotImplementedError

    def _test_connection(self):
        """
        Test if the connection to the publishing service works - used during startup.
        :return: boolean. True if success
        """
        raise NotImplementedError

    def _render_message(self, messages):
        raise NotImplementedError

    def _send_message(self, subject, message):
        raise NotImplementedError
