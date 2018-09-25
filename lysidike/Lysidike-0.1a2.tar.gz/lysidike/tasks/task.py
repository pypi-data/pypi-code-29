from pelops import mylogger
import threading
import datetime


class Task:
    _config = None
    _mqtt_client = None
    _logger = None

    _topics_sub = None
    _message_handler = None

    _service = None
    _subject = None
    name = None

    _every_nth_message = None
    _use_every_message = None

    _every_nth_second = None
    _use_every_second = None
    _loop_thread = None
    _stop_loop = None

    _message_list = None
    _lock_list = None

    def __init__(self, config, services, mqtt_client, logger):
        self._config = config
        self.name = self._config["name"]
        self._mqtt_client = mqtt_client
        self._logger = mylogger.get_child(logger, __name__ + "." + self.name)

        self._logger.info("Task.__init__ - start")
        self._logger.debug("Task.__init__ - config: {}".format(self._config))

        self._subject = self._config["subject"]
        self._topics_sub = self._config["topics-sub"]
        self._service = services[self._config["service"].lower()]

        self._every_nth_message = self._config["every-nth-message"]
        if self._every_nth_message == 0:
            self._use_every_message = False
        else:
            self._use_every_message = True

        self._every_nth_second = self._config["every-nth-second"]
        if self._every_nth_second == 0:
            self._use_every_second = False
        else:
            self._use_every_second = True
        self._loop_thread = threading.Thread(target=self._loop)
        self._stop_loop = threading.Event()
        self._stop_loop.set()

        self._message_handler = {}
        for topic in self._topics_sub:
            self._message_handler[topic] = self._create_handler(topic)

        self._message_list = []
        self._lock_list = threading.Lock()

        self._logger.info("Task.__init__ - finished")

    def _create_handler(self, handler_topic):
        def _handler(message):
            timestamp = datetime.datetime.now()
            entry = (timestamp, handler_topic, message)
            self._logger.info("Task._handler.'{}' - received message".format(handler_topic))
            self._logger.debug("Task._handler.'{}' - {}".format(handler_topic, entry))
            with self._lock_list:
                self._logger.debug("Task._handler.'{}' - lock acquired".format(handler_topic))
                self._message_list.append(entry)
            self._logger.debug("Task._handler.'{}' - lock released".format(handler_topic))
            self._logger.debug("Task._handler.'{}' - added message to list".format(handler_topic))
            self._handler_post_processor()

        self._logger.debug("Task._create_handler - added handler {} for topic {}.".format(_handler, handler_topic))
        return _handler

    def _handler_post_processor(self):
        if self._use_every_message and len(self._message_list) >= self._every_nth_message:
            self._logger.info("Task._handler_post_processer - message_list size: {}.".format(len(self._message_list)))
            self._publish()

    def _loop(self):
        self._logger.info("Task._loop - start loop")
        while not self._stop_loop.is_set():
            self._logger.info("Task._loop - wait for {} seconds.".format(self._every_nth_second))
            self._stop_loop.wait(self._every_nth_second)
            if self._stop_loop.is_set():
                continue
            self._logger.info("Task._loop - sending messages")
            self._publish()

    def _publish(self):
        self._logger.info("Task._publish - start")
        with self._lock_list:
            self._logger.debug("Task._publish - lock acquired")
            messages = self._message_list.copy()
            self._logger.debug("Task._publish - copied {} messages.".format(len(messages)))
            self._message_list.clear()
        self._logger.debug("Task._publish - lock released")
        self._service.publish(self._subject, messages)
        self._logger.info("Task._publish - finished")

    def start(self):
        self._logger.info("Task.start - starting")
        if self._use_every_second:
            self._logger.info("Task.start - start loop")
            self._stop_loop.clear()
            self._loop_thread.start()
        self._logger.info("Task.start - register {} topics".format(len(self._message_handler.items())))
        for topic, handler in self._message_handler.items():
            self._logger.debug("Task.start - subscribing to topic {} the handler {}".format(topic, handler))
            self._mqtt_client.subscribe(topic, handler)
        self._logger.info("Task.start - finished")

    def stop(self):
        self._logger.info("Task.stop - stopping")
        self._logger.info("Task.start - unregister {} topics".format(len(self._message_handler.items())))
        for topic, handler in self._message_handler.items():
            self._logger.debug("Task.start - unsubscribing from topic {} the handler {}".format(topic, handler))
            self._mqtt_client.unsubscribe(topic, handler)
        if self._use_every_second:
            self._logger.info("Task.start - stop loop")
            self._stop_loop.set()
            self._loop_thread.join()
        self._logger.info("Task.stop - finished")