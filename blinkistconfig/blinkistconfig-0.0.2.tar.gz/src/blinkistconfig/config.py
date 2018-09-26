from blinkistconfig import adapters
from blinkistconfig import errors

class Config:
    """
    Config represents a single configuration store. The interface is kept minimal
    with a single method to get a specific key from the store.

    ## Example
        config = Config(env="production", app_name="my_app", adapter="SSM")
        config.get("a/key")
    """

    def __init__(self, env, adapter_type, app_name):
        self.app_name = app_name
        self.env = env
        self.adapter_type = adapter_type

    # The *args is passed that way to handle None default values properly
    def get(self, key, *args, scope=None):
        """
        Returns the value of the key from the store or the default value if store
        fails
        """
        self._validate_params(*args)
        from_adapter = self._adapter().get(key, scope=scope, app_name=self.app_name)

        if from_adapter is None:
            return self._value_missing(key, *args, scope=scope)
        else:
            return from_adapter

    def _has_default(self, *args):
        return len(args) == 1

    def _default_value(self, *args):
        return args[0]

    def _validate_params(self, *args):
        args_length = len(args)
        error_message = f"wrong number of arguments"

        if args_length not in [0, 1]:
            raise ValueError(error_message)

    def _adapter(self):
        self.adapter = getattr(self, "adapter", adapters.Factory.by(self.adapter_type))
        return self.adapter

    def _handle_error(self, key, scope):
        raise errors.ValueMissingError(f"key: {key} has no value in {scope}")

    def _value_missing(self, key, *args, scope):
        if self._has_default(*args):
            return self._default_value(*args)
        self._handle_error(key, scope)
