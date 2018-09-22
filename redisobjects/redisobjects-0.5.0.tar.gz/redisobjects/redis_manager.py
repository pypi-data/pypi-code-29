from .redis_keyspace import RedisKeyspace
from .redis_object_factory import RedisObjectFactory
from .redis_transaction import RedisTransaction
from .serializer import IdentitySerializer

from aioredis import create_connection

class RedisManager(RedisObjectFactory):
    def __init__(self, connection):
        RedisObjectFactory.__init__(self, connection)

    def keyspace(self, keyspace, key_serializer=IdentitySerializer()):
        return RedisKeyspace(self.connection, keyspace, key_serializer)

    def create_transaction(self):
        return RedisTransaction(self.connection)

    def close(self):
        self.connection.close()
