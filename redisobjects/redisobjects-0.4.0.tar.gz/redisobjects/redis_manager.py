from .redis_keyspace import RedisKeyspace
from .redis_object_factory import RedisObjectFactory
from .serializer import IdentitySerializer

from aioredis import create_connection

class RedisManager(RedisObjectFactory):
    def __init__(self, connection):
        RedisObjectFactory.__init__(self, connection)

    def keyspace(self, keyspace, key_serializer=IdentitySerializer()):
        return RedisKeyspace(self.connection, keyspace, key_serializer)

    def close(self):
        self.connection.close()
