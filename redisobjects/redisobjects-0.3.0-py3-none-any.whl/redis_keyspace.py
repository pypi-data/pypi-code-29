from .serializer import IdentitySerializer
from .redis_atom import RedisAtom
from .redis_list import RedisList
from .redis_dict import RedisDict
from .redis_set import RedisSet

class RedisKeyspace:
    def __init__(self, connection, keyspace='?', *key_serializers):
        self.connection = connection
        self.placeholder = '?'
        self.keyspace = keyspace
        self.key_serializers = key_serializers if len(key_serializers) > 0 else [IdentitySerializer()] * (keyspace.count(self.placeholder))

    def _make_key(self, *keys):
        key = self.keyspace
        for i in range(len(keys)):
            key = key.replace(self.placeholder, self.key_serializers[i].serialize(keys[i]))
        if self.placeholder in key:
            raise RuntimeError('Not all placeholders have been replaced for `%s`' % (key,))
        return key

    def atom(self, *keys, value_serializer=IdentitySerializer()):
        key = self._make_key(*keys)
        return RedisAtom(self.connection, key, value_serializer)

    def list(self, *keys, value_serializer=IdentitySerializer()):
        key = self._make_key(*keys)
        return RedisList(self.connection, key, value_serializer)

    def dict(self, *keys, value_serializer=IdentitySerializer(), field_serializer=IdentitySerializer()):
        key = self._make_key(*keys)
        return RedisDict(self.connection, key, value_serializer, field_serializer)

    def set(self, *keys, value_serializer=IdentitySerializer()):
        key = self._make_key(*keys)
        return RedisSet(self.connection, key, value_serializer)
