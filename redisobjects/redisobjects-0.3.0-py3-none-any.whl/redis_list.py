from .serializer import IdentitySerializer

class RedisList:
    def __init__(self, connection, key, serializer=IdentitySerializer()):
        self.connection = connection
        self.key = key
        self.serializer = serializer

    def _serialize_values(self, values):
        return [self.serializer.serialize(value) for value in values]

    async def add(self, *values):
        return await self.push_right(*values)

    async def push_right(self, *values):
        return await self.connection.execute('rpush', self.key, *self._serialize_values(values))

    async def push_left(self, *values):
        return await self.connection.execute('lpush', self.key, *self._serialize_values(values))

    async def items(self, limit=1000):
        results = await self.connection.execute('lrange', self.key, 0, limit)
        return (self.serializer.deserialize(value) for value in results)

    async def pop_left(self):
        result = await self.connection.execute('lpop', self.key)
        return self.serializer.deserialize(result)

    async def pop_right(self):
        result = await self.connection.execute('rpop', self.key)
        return self.serializer.deserialize(result)

    async def size(self):
        return await self.connection.execute('llen', self.key)
