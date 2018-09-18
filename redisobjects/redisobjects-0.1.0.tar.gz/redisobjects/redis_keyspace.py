from .serializer import IdentitySerializer
from .redis_state import RedisState
from .redis_list import RedisList

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

    def state(self, *keys, value_serializer=IdentitySerializer()):
        key = self._make_key(*keys)
        return RedisState(self.connection, key, value_serializer)

    def list(self, *keys, value_serializer=IdentitySerializer()):
        key = self._make_key(*keys)
        return RedisList(self.connection, key, value_serializer)
