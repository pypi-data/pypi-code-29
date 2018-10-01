from __future__ import print_function
from __future__ import division
from builtins import range
from past.utils import old_div
from time import sleep, time
from random import random
from os import getpid
import pdb

import confluent_kafka.cimpl as kafka


TOPIC = 'test'
TIMEOUT = 6000

conf = {
    'bootstrap.servers': 'localhost',
    'group.id': 'local', 'session.timeout.ms': TIMEOUT,
    'default.topic.config': {'auto.offset.reset': 'smallest'}}

producer = kafka.Producer(**conf)
consumer = kafka.Consumer(**conf)
consumer.subscribe([TOPIC])


def status_of_message(msg):
    return msg[0]


def payload_of_message(msg):
    return msg[1:]


def compose_status(status, value):
    return status + value


def wait_for_conflict(key, value, test_sleep=0):
    start = time()
    print("writing", value)
    producer.produce(TOPIC, compose_status("R", value), key)
    producer.flush()
    seen_my_msg = False
    seen_other_msg = False
    other_msgs = []
    while True:
        msg = consumer.poll()
        error = msg.error()
        if error:
            if error.code() == kafka.KafkaError._PARTITION_EOF:
                break
            print("error", msg.error())
            raise RuntimeError(error)
        if msg is None:
            print("None")
            break
        print("read", msg.value())
        if msg.key() != key:
            continue
        if payload_of_message(msg.value()) == value:
            seen_my_msg = True
            if not other_msgs:
                break
        else:
            status = status_of_message(msg.value())
            if status == 'R':
                other_msgs.append(msg)
                seen_other_msg = True
            else:
                # TODO: Find exact message
                other_msgs = []
                if seen_my_msg and not other_msgs:
                    break
    print("over", seen_my_msg, other_msgs)
    assert seen_my_msg
    if other_msgs:
        # timeout on other messages
        for msg in other_msgs:
            # only timeout if specific message is too old
            # if msg.timestamp() - now() > timeout:
            producer.produce(TOPIC, compose_status(
                "T", payload_of_message(msg.value())), key)
            producer.flush()
    duration = time() - start
    # for testing purposes. Normally this would be after return
    if test_sleep:
        sleep(test_sleep)
    producer.produce(TOPIC, compose_status("S", value), key)
    producer.flush()
    # we expect to do stuff here
    return seen_other_msg, duration


if __name__ == '__main__':
    num_seen = 0
    intervals = []
    pid = getpid()
    pdb.set_trace()
    for i in range(100):
        try:
            seen, interval = wait_for_conflict('key', "%d_%d" % (pid, i), old_div(random(),4))
        except:
            pdb.post_mortem()
            break
        if seen:
            num_seen += 1
        intervals.append(interval)
    print("at %d, numseen: %d, avg interval: %f" % (i, num_seen, old_div(sum(intervals),len(intervals))))

