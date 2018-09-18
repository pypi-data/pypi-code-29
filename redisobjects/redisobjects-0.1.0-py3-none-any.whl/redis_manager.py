from .redis_keyspace import RedisKeyspace
from .serializer import IdentitySerializer

from aioredis import create_connection

class RedisManager:
    def __init__(self, connection, placeholder='?'):
        self.connection = connection
        self.placeholder = placeholder

    def keyspace(self, keyspace, *key_serializers):
        if len(key_serializers) == 0:
            key_serializers = [IdentitySerializer()] * (keyspace.count(self.placeholder))
        return RedisKeyspace(self.connection, keyspace, *key_serializers)
