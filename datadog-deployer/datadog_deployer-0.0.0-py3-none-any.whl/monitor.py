from collections import OrderedDict

from datadog import api


class Monitor(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def create(self):
        kwargs = self()
        api.Monitor.create(**kwargs)

    def upsert(self):
        if 'id' in self:
            self.update()
        else:
            self.insert()

    def update(self):
        kwargs = self.copy()
        del kwargs['type']
        api.Monitor.update(self.id, **kwargs)

    @staticmethod
    def read_all() -> list('Monitor'):
        result = []
        for monitor in api.Monitor.get_all():
            if 'deleted' not in monitor or not monitor['deleted']:
                result.append(Monitor(monitor))
        return result

    def normalized(self) -> OrderedDict:
        property_order = [
            'name', 'type', 'query', 'message', 'options', 'tags', 'deleted'
        ]
        meta = {
            'id', 'matching_downtimes', 'created', 'created_at', 'creator',
            'org_id', 'modified', 'overall_state_modified', 'overall_state'
        }
        result = OrderedDict()

        for p in property_order:
            if p in self and self[p]:
                result[p] = self[p]

        for p in self.keys():
            if p not in property_order and p not in meta:
                result[p] = self[p]

        return result
