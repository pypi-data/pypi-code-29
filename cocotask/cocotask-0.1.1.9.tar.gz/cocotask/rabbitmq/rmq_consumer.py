# -*- coding: utf-8 -*-
import pika.exceptions as exceptions
from ..base_consumer import CocoBaseConsumer
from .common import createBlockingConnection


class CocoRMQConsumer(CocoBaseConsumer):

    def __init__(self, conf, worker, logger = None):
        self._exchange_name = conf['EXCHANGE_NAME']
        self._queue_name = conf['QUEUE_NAME']
        self._connection = None
        super().__init__(conf, worker, logger)

    def connect(self):
        self._connection, channel = createBlockingConnection(self._config)
        channel.queue_bind(exchange = self._exchange_name,
                           queue = self._queue_name)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(self.on_message,
                              queue=self._queue_name)
        channel.start_consuming()

    def on_message(self, ch, method, properties, body):
        self._worker.process(body)
        try:
            ch.basic_ack(delivery_tag = method.delivery_tag)
        except exceptions.ChannelClosed as e:
            self._logger.error("channel closed. exp: %s" % repr(e))
