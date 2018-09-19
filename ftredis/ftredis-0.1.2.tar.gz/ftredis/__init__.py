from itertools import chain
from redis import StrictRedis
from redis.client import BasePipeline
from redis.client import bool_ok
from redis.exceptions import ResponseError


class Client(StrictRedis):
    def __init__(self, namespace, *args, **kwargs):
        self.namespace = namespace
        StrictRedis.__init__(self, *args, **kwargs)
        self.set_response_callback('ft.create', bool_ok)
        self.set_response_callback('ft.add', bool_ok)
        self.set_response_callback('ft.drop', bool_ok)

    def ftcreate(self, *args):
        return self.execute_command('ft.create', self.namespace, 'schema', *args)

    def ftadd(self, id, **fields):
        args = ['ft.add', self.namespace, id, 1.0, 'nosave', 'fields']
        args += chain(*fields.items())
        return self.execute_command(*args)

    def ftdel(self, id):
        return self.execute_command('ft.del', self.namespace, id)

    def ftsearch(self, *args):
        return self.execute_command('ft.search', self.namespace, *args)

    def ftdrop(self):
        return self.execute_command('ft.drop', self.namespace)

    def pipeline(self, transaction=True, shard_hint=None):
        pipeline = Pipeline(self.connection_pool, self.response_callbacks.copy(), transaction, shard_hint)
        pipeline.namespace = self.namespace
        return pipeline

class Pipeline(BasePipeline, Client):
    pass

