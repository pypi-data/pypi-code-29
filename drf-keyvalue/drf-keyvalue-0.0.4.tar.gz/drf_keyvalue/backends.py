import importlib, json

class NoSQLBackend:

    def __get_serializer_class(self, serializer_path):
        bits = serializer_path.split('.')
        class_name = bits.pop()
        module_string = (".").join(bits)
        mod = importlib.import_module(module_string)
        return getattr(mod, class_name)

    def get_serialized(self, instance, created = False):
        serializer = self.__get_serializer_class(instance.serializer_path)
        dta = serializer(instance).data
        id = str(instance.id)
        return (id, dta)

class RequestsBackend(NoSQLBackend):

    def __init__(self, base_url):
        self.base_url = base_url

    def collection(self, name):
        pass

    def set(self, serializer, instance):
        pass



class RedisBackend(NoSQLBackend):
    '''
    usage:
    ```
    collection = RedisBackend(connection).collection('todos')
    collection.set(TodoSerializer, todo)
    collection.get(todo)
    collection.delete(instance)
    ```
    '''

    def __init__(self, connection, **kwargs):
        super().__init__()
        self.redis = connection

    def __get_key(self, instance, instance_key=None):
        if instance_key:
            return "{}.{}".format(self.collection, getattr(instance, instance_key))
        return "{}.{}".format(self.collection, instance.pk)

    def collection(self, name):
        self.collection = name
        return self # this is so we can chain

    def set(self, serializer, instance, instance_key=None):
        key = self.__get_key(instance, instance_key)
        value = serializer(instance).data
        as_string = json.dumps(value)
        self.redis.set(key, as_string)
        return value

    def get(self, instance, instance_key=None):
        key = self.__get_key(instance, instance_key)
        value = self.redis.get(key)
        if value is None: return None
        return json.loads(value)

    def delete(self, instance, instance_key=None):
        key = self.__get_key(instance, instance_key)
        self.redis.delete(key)
