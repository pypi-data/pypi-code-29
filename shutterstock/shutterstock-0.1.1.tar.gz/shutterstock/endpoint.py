

class EndPointParam:
    NO_VALUE = (None, )  # Simple tuple for testing with `is`

    def __init__(self, vtype=str, default=NO_VALUE, help_text=None, required=False):
        self.name = 'param'
        self.data_type = vtype
        self.default = default
        self.help_text = help_text
        self.required = required

    def clean(self, value):
        if value is EndPointParam.NO_VALUE or (value is None and self.required):
            value = self.default

        return value


class ChoicesParam(EndPointParam):
    def __init__(self, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = choices

    def clean(self, value):
        value = super().clean(value)

        if value is not None and value not in self.choices:
            raise ValueError("Invalid Choice. Choices are {}".format(
                ', '.join(self.choices))
            )

        return value


class EndpointMeta(type):
    def __new__(mcs, clsname, bases, clsdict):
        params = []
        for name, val in clsdict.items():
            if isinstance(val, EndPointParam):
                clsdict[name].name = name
                params.append(val)

        clsdict['params'] = tuple(params)
        clsobj = super().__new__(mcs, clsname, bases, clsdict)
        return clsobj


class EndPoint(metaclass=EndpointMeta):
    params = ()

    def __init__(self, uri, params=None):
        self.uri = uri
        self.simple_params = params

    def prepare(self, **kwargs):
        uri = self.uri.format(**kwargs)
        params = {}

        for param in self.params:
            value = param.clean(kwargs.get(param.name, EndPointParam.NO_VALUE))
            if value is not EndPointParam.NO_VALUE:
                params[param.name] = value

        if isinstance(self.simple_params, list):
            for param in self.simple_params:
                value = kwargs.get(param, None)
                if value is not None:
                    params[param] = value

        return uri, params

    def explain(self):
        return "URI: {uri}\n\nDescription: {doc}\n\nParams:\n{params}".format(
            uri=self.uri,
            doc=self.__doc__,
            params="\n".join(
                [
                    '{name}: {help_text}'.format(
                        name=param.name,
                        help_text=param.help_text
                    )
                    for param in self.params
                ]
            )
        )
