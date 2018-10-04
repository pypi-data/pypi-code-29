from .serializer import IdentitySerializer
from .redis_atom import RedisAtom
from .redis_list import RedisList
from .redis_dict import RedisDict
from .redis_set import RedisSet

class RedisObjectFactory:
    def __init__(self, connection):
        self.connection = connection

    def _make_key(self, key):
        return key

    def atom(self, key, value_serializer=IdentitySerializer()):
        return RedisAtom(self.connection, self._make_key(key), value_serializer)

    def integer(self, key, value_serializer=IdentitySerializer()):
        return RedisInteger(self.connection, self._make_key(key), value_serializer)

    def list(self, key, value_serializer=IdentitySerializer()):
        return RedisList(self.connection, self._make_key(key), value_serializer)

    def dict(self, key, value_serializer=IdentitySerializer(), field_serializer=IdentitySerializer()):
        return RedisDict(self.connection, self._make_key(key), value_serializer, field_serializer)

    def set(self, key, value_serializer=IdentitySerializer()):
        return RedisSet(self.connection, self._make_key(key), value_serializer)
