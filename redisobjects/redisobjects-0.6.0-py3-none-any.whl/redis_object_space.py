from .serializer import IdentitySerializer, StringSerializer, TupleSerializer
from .redis_atom import RedisAtom

import importlib
import uuid

class RedisObjectSpace:
    def __init__(self, db, keyspace, cls, *, key_serializer=IdentitySerializer(), key_factory=lambda: str(uuid.uuid4())):
        self.db = db
        self.keyspace = keyspace
        self.cls = cls
        self.key_serializer = key_serializer
        self.key_factory = key_factory
        self.cls_serializer = TupleSerializer.create_homogeneous(2, separator=':')

    async def create(self, cls, key=None):
        if key is None:
            key = self.key_factory()
        obj = cls()
        self.hydrate(cls, obj, key)
        cls_atom = RedisAtom(self.db, self.get_attribute_key(key, '__class__'), self.cls_serializer)
        await cls_atom.set((cls.__module__, cls.__name__))
        return obj

    async def remove(self, key):
        if isinstance(key, object):
            cls = key.__class__
            key = key._id
        else:
            cls = await self.get_class(key)
        if cls is not None:
            await self.db.execute('del', self.get_attribute_key(key, '__class__'))
            for attribute, _ in cls.model.items():
                await self.db.execute('del', self.get_attribute_key(key, attribute))

    def get_attribute_key(self, key, attribute):
        complete_key = '%s:%s:%s' % (self.keyspace, self.key_serializer.serialize(key), attribute)
        return complete_key

    def hydrate(self, cls, obj, key):
        obj._id = key
        for attribute, prop in cls.model.items():
            complete_key = self.get_attribute_key(key, attribute)
            setattr(obj, attribute, prop.map(self.db, complete_key))

    async def get_class(self, key):
        cls_atom =  RedisAtom(self.db, self.get_attribute_key(key, '__class__'), self.cls_serializer)
        if not await cls_atom.exists():
            return None
        module_name, cls_name = await cls_atom.get()
        cls = getattr(importlib.import_module(module_name), cls_name)
        if cls is None or not issubclass(cls, self.cls):
            return None
        return cls

    async def object(self, key):
        cls = await self.get_class(key)
        obj = None
        if cls is not None:
            obj = cls()
            self.hydrate(cls, obj, key)
        return obj
