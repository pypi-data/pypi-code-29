from .redis_atom import RedisAtom
from .serializer import IdentitySerializer

class RedisInteger(RedisAtom):
    def __init__(self, connection, key, value_serializer=IdentitySerializer()):
        RedisAtom.__init__(self, connection, key, value_serializer)

    async def increment(self, n=1, *, tx=None):
        tx = tx or self.connection
        if n == 1:
            return await tx.execute('incr', self.key)
        else:
            return await tx.execute('incrby', self.key, n)

    async def decrement(self, n=1, *, tx=None):
        tx = tx or self.connection
        if n == 1:
            return await tx.execute('decr', self.key)
        else:
            return await tx.execute('decrby', self.key, n)
