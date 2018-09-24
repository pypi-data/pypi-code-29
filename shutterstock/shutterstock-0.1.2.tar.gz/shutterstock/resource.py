from functools import partial


class ResourceObjectInitializer:
    def __init__(self, cls, func, instance):
        self.func = func
        self.instance = instance or cls()

    def __call__(self, *args, **kwargs):
        self.instance.reset()
        self.instance.set_data(**self.func(*args, **kwargs))
        return self.instance


class ResourceCollectionInitializer:
    def __init__(self, cls, func, instance):
        self.cls = cls
        self.func = func

    def __call__(self, *args, **kwargs):
        collection = []
        data = self.func(*args, **kwargs)
        if 'errors' in data:
            raise Exception(data['errors'][0]['message'])

        for item in data['data']:
            collection.append(self.cls(**item))
        return collection


class ResourceMethodAccessor:
    def __init__(self, func, initializer, resource=None, **params):
        self.func = func
        self.initializer = initializer
        self.resource = resource
        self.params = params

    def configure_for_client(self, client):
        if self.resource is None:
            return self
        resource = getattr(client, self.resource.__name__)
        return ResourceMethodAccessor(self.func, self.initializer, resource, **self.params)

    def __get__(self, instance, cls):
        params = {}
        if instance:
            for key, val in self.params.items():
                print(key, val)
                params[key] = getattr(instance, val)

        return self.initializer(self.resource or cls, partial(self.func, cls=cls, **params), instance)


class ResourceMethod:
    def __init__(self, initializer, resource=None, **params):
        self.initializer = initializer
        self.resource = resource
        self.params = params

    def __call__(self, func):
        return ResourceMethodAccessor(func, self.initializer, resource=self.resource, **self.params)


class ResourceObjectMethod(ResourceMethod):
    def __init__(self, **params):
        super().__init__(ResourceObjectInitializer, **params)


class ResourceCollectionMethod(ResourceMethod):
    def __init__(self, **params):
        super().__init__(ResourceCollectionInitializer, **params)


class Resource:
    API = None
    LIST = None
    GET = None
    CREATE = None
    UPDATE = None
    DELETE = None

    def __init__(self, **kwargs):
        self.set_data(**kwargs)

    def reset(self):
        pass

    def set_data(self, **params):
        for key, val in params.items():
            setattr(self, key, val)

    @ResourceCollectionMethod()
    def all(cls, **params):
        return cls.API.get(cls.LIST, **params)

    @ResourceCollectionMethod()
    def list(cls, **params):
        return cls.API.get(cls.LIST, **params)

    @ResourceObjectMethod(id='id')
    def get(cls, **params):
        return cls.API.get(cls.GET, **params)