from builtins import object
import atexit

from simplejson import dumps
from pykafka.common import OffsetType
from pyramid.httpexceptions import HTTPServerError

from assembl.lib.kafka import get_kafka_client

TIMEOUT = 6000

CONFLICT_GROUP = 'conflict'


def compose_status(signal, value):
    return signal + value


def status_of_message(value):
    return value[0]


def payload_of_message(value):
    return value[1:]


class KafkaConflictResolverTweenFactory(object):
    # does this need to be a tween? Or a transaction manager?
    def __init__(self, handler, registry):
        self.handler = handler
        self.registry = registry
        self.kafka_client = kafka_client = get_kafka_client(registry.settings)
        hostname = registry.settings['public_hostname']
        conflict_topic = 'conflict_' + hostname

        conflict_topic = kafka_client.topics[conflict_topic]
        self.consumer = conflict_topic.get_simple_consumer(
            CONFLICT_GROUP, True,
            auto_commit_enable=False,
            auto_offset_reset=OffsetType.LATEST,
            fetch_wait_max_ms=0,
            fetch_error_backoff_ms=1,
            # queued_max_messages=1,
            # offsets_channel_backoff_ms=10,
            consumer_timeout_ms=TIMEOUT)
        self.producer = conflict_topic.get_producer(
            True,
            sync=True,
            retry_backoff_ms=10,
            linger_ms=1)
        atexit.register(lambda: self.producer.stop())

    def wait_for_conflict(self, request, key, value):
        if not isinstance(value, bytes):
            value = dumps(value, encoding="utf-8")
        request.asked_for_conflict = (key, value)
        self.producer.produce(compose_status("R", value), key)
        seen_my_msg = False
        seen_other_msg = False
        other_msgs = []
        msg = None
        while True:
            msg = self.consumer.consume()
            if msg is None:
                break
            if msg.partition_key != key:
                # Do I want to be consuming this with a grouped consumer?
                continue
            if payload_of_message(msg.value) == value:
                seen_my_msg = True
                if not other_msgs:
                    break
            else:
                status = status_of_message(msg.value)
                if status == 'R':
                    other_msgs.append(msg)
                    seen_other_msg = True
                else:
                    # TODO: Find exact message
                    other_msgs = []
                    if seen_my_msg and not other_msgs:
                        break
        if not seen_my_msg:
            raise HTTPServerError("Could not resolve conflict")
        if other_msgs:
            # timeout on other messages
            for omsg in other_msgs:
                # only timeout if specific message is too old
                # should timeout depend on nature of request?
                # if msg.timestamp() - now() > timeout:
                self.producer.produce(
                    compose_status("T", payload_of_message(omsg.value)), key)
        return seen_other_msg

    def __call__(self, request):
        request.conflict_resolver = self
        conflict_key = None

        try:
            response = self.handler(request)
            conflict_key, conflict_value = getattr(
                request, 'asked_for_conflict', (None, None))
            if conflict_key:
                self.producer.produce(
                    compose_status("S", conflict_value), conflict_key)
            return response
        except BaseException as e:
            if conflict_key:
                self.producer.produce(
                    compose_status("E", conflict_value), conflict_key)
            raise e
        finally:
            self.consumer.commit_offsets()
