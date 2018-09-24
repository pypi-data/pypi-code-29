import inspect

from shutterstock import resources, resource


class Client:
    def __init__(self):
        self.resources = []

    def __setattr__(self, key, value):
        if callable(value) and issubclass(value, resource.Resource):
            self.resources.append(value)
        super().__setattr__(key, value)

    def configure(self):
        for res in self.resources:
            for cls in res.__mro__:
                if issubclass(cls, resources.Resource):
                    for key, var in cls.__dict__.items():
                        if isinstance(var, resource.ResourceMethodAccessor):
                            setattr(res, key, var.configure_for_client(self))


def configure_api(api):
    client = Client()

    for name, val in resources.__dict__.items():
        if inspect.isclass(val) and issubclass(val, resources.Resource):
            setattr(client, name, type(name, (val,), {'API': api}))

    client.configure()
    return client


def configure(token):
    from shutterstock.api import ShutterstockAPI
    return configure_api(ShutterstockAPI(token))
