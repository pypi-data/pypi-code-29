from time import sleep

import pika
import pika.channel
from pika import spec

from plumb.base import BaseSource, BaseSink
from plumb.mixins import CompressionMixin
from plumb.serializers import JSON


class RabbitMQResource(CompressionMixin, JSON):
    def __init__(self,
                 queue_name,
                 host='localhost',
                 port=5672,
                 virtual_host='/',
                 username='guest',
                 password='guest',
                 erase_on_connect=False,
                 channel_max=pika.channel.MAX_CHANNELS,
                 frame_max=spec.FRAME_MAX_SIZE,
                 heartbeat=None,
                 ssl=False,
                 ssl_options=None,
                 connection_attempts=1,
                 retry_delay=2.0,
                 socket_timeout=10.0,
                 locale='en_US',
                 backpressure_detection=False,
                 blocked_connection_timeout=None,
                 client_properties=None,
                 tcp_options=None,
                 url=None,
                 use_compression=True):
        if url is None:
            credentials = pika.PlainCredentials(username=username, password=password, erase_on_connect=erase_on_connect)
            parameters = pika.ConnectionParameters(
                host=host, port=port, virtual_host=virtual_host, credentials=credentials,
                channel_max=channel_max, frame_max=frame_max, heartbeat=heartbeat,
                ssl=ssl, ssl_options=ssl_options,
                connection_attempts=connection_attempts, retry_delay=retry_delay, socket_timeout=socket_timeout,
                locale=locale,
                backpressure_detection=backpressure_detection, blocked_connection_timeout=blocked_connection_timeout,
                client_properties=client_properties, tcp_options=tcp_options
            )
        else:
            parameters = pika.URLParameters(url)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.queue_name = queue_name
        self.use_compression = use_compression

    def close(self):
        self.connection.close()


class Source(RabbitMQResource, BaseSource):
    def __init__(self, queue_name, auto_ack=False, sleep_time=100, **kwargs):
        super().__init__(queue_name, **kwargs)
        self.auto_ack = auto_ack
        self.sleep_time = sleep_time
        self.to_ack_tags = list()

    def _ack_processed_messages(self):
        if not self.auto_ack:
            while len(self.to_ack_tags) > 0:
                delivery_tag = self.to_ack_tags.pop()
                self.channel.basic_ack(delivery_tag)

    def _recover_message(self, body):
        body = body.decode()
        if self.use_compression:
            message_body = self.decompress(body)
        else:
            message_body = body
        message = self.deserialize(message_body)
        return message

    def get(self, timeout=None):
        self._ack_processed_messages()
        message_received = False
        if timeout is None or timeout == 0:
            timeout_time = None
        else:
            timeout_time = timeout
        timeout = False
        while not message_received and not timeout:
            method_frame, properties, body = self.channel.basic_get(self.queue_name,
                                                                    no_ack=self.auto_ack)
            if method_frame is not None:
                message_received = True
            elif timeout_time is not None:
                sleep(self.sleep_time / 1000)
                timeout_time -= self.sleep_time
                if timeout_time <= 0:
                    timeout = True
        if message_received:
            message = self._recover_message(body)
            if not self.auto_ack:
                self.to_ack_tags.append(method_frame.delivery_tag)
        else:
            message = None
        return message


class Sink(RabbitMQResource, BaseSink):

    def __init__(self, queue_name, exchange='', **kwargs):
        super().__init__(queue_name=queue_name, **kwargs)
        self.exchange = exchange

    def put(self, message):
        message_body = self.serialize(message)
        if self.use_compression:
            body = self.compress(message_body)
        else:
            body = message_body
        self.channel.publish(exchange=self.exchange,
                             routing_key=self.queue_name,
                             body=body)
