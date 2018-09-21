from .serializer import IdentitySerializer

import aioredis

class RedisAtom:
    def __init__(self, connection, key, serializer=IdentitySerializer()):
        self.connection = connection
        self.key = key
        self.serializer = serializer

    async def get(self):
        value = await self.connection.execute('get', self.key)
        return self.serializer.deserialize(value)

    async def exists(self):
        return await self.connection.execute('exists', self.key) > 0

    async def set(self, value):
        serialized_value = self.serializer.serialize(value)
        return await self.connection.execute('set', self.key, serialized_value)

    async def remove(self):
        return await self.connection.execute('del', self.key) > 0

    async def increment(self, n=1):
        if n == 1:
            return await self.connection.execute('incr', self.key)
        else:
            return await self.connection.execute('incrby', self.key, n)

    async def decrement(self, n=1):
        if n == 1:
            return await self.connection.execute('decr', self.key)
        else:
            return await self.connection.execute('decrby', self.key, n)

    async def get_set(self, value):
        return await self.connection.execute('getset', self.key, self.serializer.serialize(value))
