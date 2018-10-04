from .serializer import IdentitySerializer, StringSerializer
from .redis_atom import RedisAtom

class RedisIndexAtom:
    def __init__(self, connection, key, index_space, index_type, key_serializer=IdentitySerializer(), index_serializer=StringSerializer()):
        self.connection = connection
        self.key = key
        self.index_space = index_space
        self.index_type = index_type
        self.primary_atom = RedisAtom(connection, self._make_primary_key(), index_serializer)
        self.secondary_atom = None
        self.key_serializer = key_serializer
        self.index_serializer = index_serializer

    def _make_primary_key(self):
        key = '%s:%s:%s' % (self.index_space, self.key, self.index_type)
        return key

    def _make_secondary_key(self, value):
        index = '%s:__index__:%s:%s' % (self.index_space, self.index_type, value)
        return index

    async def set(self, value, *, tx=None):
        tx = tx or self.connection
        await self.primary_atom.set(value, tx=tx)
        if self.secondary_atom is None:
            self.secondary_atom = RedisAtom(self.connection, self._make_secondary_key(value), self.key_serializer)
        await self.secondary_atom.set(self.key, tx=tx)

    async def get(self):
        return await self.primary_atom.get()

    async def exists(self):
        return await self.primary_atom.exists()

    async def remove(self, *, tx=None):
        tx = tx or self.connection
        await self.primary_atom.remove(tx=tx)
        if self.secondary_atom is not None:
            await self.secondary_atom.remove(tx=tx)
            self.secondary_atom = None
