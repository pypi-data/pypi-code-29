from .backends import RedisBackend
import fakeredis
conn = fakeredis.FakeStrictRedis()

class FakeSerializer:
    data = {"foo": "bar"}
    def __init__(self, instance):
        self.instance = instance


def test_set_value():
    pass
