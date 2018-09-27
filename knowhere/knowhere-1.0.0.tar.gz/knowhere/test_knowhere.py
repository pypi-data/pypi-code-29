import time, uuid

from datetime import timedelta
from cache import Cache

c = Cache(shard_size=2, eviction_interval=timedelta(seconds=1))

testkey = "hello"
testvalue = "world"

def test_set_1s_exp():
    c.set(testkey, testvalue, ttl=timedelta(seconds=1))
    assert(c.get(testkey) == testvalue)
    time.sleep(1)
    assert(c.get(testkey) == None)

def test_set_5s_exp():
    c.set(testkey, testvalue, ttl=timedelta(seconds=5))
    assert(c.get(testkey) == testvalue)
    time.sleep(1)
    assert(c.get(testkey) == testvalue)
    time.sleep(1)
    assert(c.get(testkey) == testvalue)
    time.sleep(1)
    assert(c.get(testkey) == testvalue)

    time.sleep(2)
    assert(c.get(testkey) == None)

def test_delete():
    c.set(testkey, testvalue, ttl=timedelta(days=1))
    assert(c.get(testkey) == testvalue)
    c.delete(testkey)
    assert(c.get(testkey) == None)

def test_flush():
    for i in range(0, 100):
        c.set(str(uuid.uuid4()), testvalue, timedelta(days=1))

    assert(len(c.keys()) == 100)
    c.flush()
    assert(len(c.keys()) == 0)

def test_evition_service():
    c.set(testkey, testvalue, timedelta(seconds=5))
    assert(c.keys()[0] == testkey)
    time.sleep(1)
    assert(c.keys()[0] == testkey)
    time.sleep(1)
    assert(c.keys()[0] == testkey)
    time.sleep(1)

    time.sleep(4)
    assert(c.keys() == [])

def test_close():
    c.close()
