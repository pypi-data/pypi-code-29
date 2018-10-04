"""Base class for Integration objects
"""


class Integration(object):
    TYPE_AWS = 'AWS'

    @classmethod
    def list(cls, **kwargs):
        if 'client' not in kwargs or 'model' not in kwargs:
            raise ValueError(
                'incorrect API usage. '
                'use rockset.Client().Integration.list() instead.'
            )
        client = kwargs.pop('client')
        model = kwargs.pop('model')

        kwargs = {}
        kwargs['method'] = model.All.listIntegrations
        integratons = client.apicall(**kwargs)['data']

        list = []
        for i in integratons:
            type = cls.TYPE_AWS
            list.append(cls(client=client, model=model, type=type, **i))
        return list

    @classmethod
    def retrieve(cls, **kwargs):
        """Retrieves a single integration

        Args:
            name (str): Name of the integration to be retrieved

        Returns:
            Integration: Integration object
        """

        if 'client' not in kwargs or 'model' not in kwargs:
            raise ValueError(
                'incorrect API usage. '
                'use rockset.Client().Integration.retrieve() instead.'
            )

        client = kwargs.pop('client')
        model = kwargs.pop('model')
        name = kwargs.pop('name')

        kwargs = {}
        kwargs['method'] = model.Integrations.describeIntegration
        kwargs['integration'] = name

        integration = client.apicall(**kwargs)['data']
        return cls(client=client, model=model, type=cls.TYPE_AWS, **integration)

    # instance_methods
    def __init__(self, client, model, name, type, **kwargs):
        """Represents a single Integration"""
        self.client = client
        self.model = model
        self.name = name
        self.type = type
        for key in kwargs:
            setattr(self, key, kwargs[key])
        return

    def __str__(self):
        """Converts the collection into a user friendly printable string"""
        return str(vars(self))

    def asdict(self):
        d = vars(self)
        d.pop('client')
        d.pop('model')

    def drop(self):
        kwargs = {}
        kwargs['method'] = self.model.Integrations.deleteIntegration
        kwargs['integration'] = self.name
        self.client.apicall(**kwargs)
        return
