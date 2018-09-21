import warnings
from typing import Callable, Union

from .versioned import Versioned


class supproperty(property, Versioned):
    """ A `property` subclass with bells and whistles.

    This is a rather specific (yet common) implementation of the property mechanism. The getter returns the
    _<property name> or the default if that is None. The setter sets _<property name> to the value after
    validating it. If the value is set to None, then the getter *will* return the default. **In summary** you
    do not have to do any of the implementation! It **is** enough to ```def property_name(self): pass```.


    Examples
    --------


    """
    def __init__(self, *args, **kwargs):
        """

        Parameters
        ----------
        default: Union[lambda container_object, value -> value, type]
            The default value for the property. Can be a lambda function too. Self is passed at the only
            parameter of the lambda function to evaluate more complex default values.
        type: Union[Callable, type]
            This is a type or any function that takes anything supported and converts in into the desired
            correct type, or fails if the type or the value is not supported or correct.
        validator: lambda container_object, value -> bool
            This is a function that return a Bool representing whether the value is valid. Note that the object
            is passed to the function too, so one can make more complicated validation based on the state of the
            object.
        warn : bool
            If the validation fails, should it cause a warning or raise an Exception.
            Default: False
        available: StrictVersion
            The minimum version number that this property is supported on.

        Examples
        --------

        >>> @supproperty(type=np.float, default=0.01, validator=lambda x, _: x >= 0, warn=True, available='5.0')
        >>> def velocity(self):
        >>>     pass


        The property called `velocity` can be set as an numpy float. Because np.float is the type
        even if `self.velocity=2` is set `self.velocity` will return 2.0. Validator just checks non-negativeness. The
        system will only warn the user about a negative values, but will still set the property.

        """

        self._default = kwargs.get('default')
        self.type: Union[Callable, type] = kwargs.get('type')
        self.validator: Callable = kwargs.get('validator')
        self.warning_only = kwargs.get('warn', False)
        self.warning_message = kwargs.get('warning_message')
        self.version = kwargs.get('available')
        self.strict = kwargs.get('strict_type_check', False)
        self._did_set = None
        self._will_set = None

        self.f = args[0] if args else None

        if self.strict:
            if not isinstance(self.type, type):
                raise TypeError(f'The type of this property has to be a type! Currently it is a {type(self.type)}')

        super(supproperty, self).__init__(fget=self._fget, fset=self._fset)

    def __call__(self, f):
        self.f = f
        return self

    def _fget(self, obj):

        self.version_check(obj)

        try:
            v = obj.__getattribute__(self.private_name)
        except AttributeError:
            v = None

        try:
            return v if v is not None else self.default(obj)
        except (AttributeError, TypeError) as e:
            # warnings.warn(f'{e}; {self.f.__name__}', Warning)
            return None

    def _fset(self, obj, value):

        if self._will_set:
            self._will_set(obj, value)

        self.version_check(obj)

        old_value = self._fget(obj)

        if value is None:
            obj.__setattr__(self.private_name, None)
        else:
            if self.strict:
                if not isinstance(value, self.type):
                    raise TypeError(f'Expected type ({self.type}) received {type(value)}')
            else:
                value = value if isinstance(self.type, type) and isinstance(value, self.type) else self.type(value)
            try:
                self.validate(obj, value)
            except AttributeError as e:
                warnings.warn(f'{e}')
            obj.__setattr__(self.private_name, value)

        if self._did_set:
            self._did_set(obj, old_value)

    @property
    def private_name(self):
        return "_{}".format(self.f.__name__)

    @property
    def public_name(self):
        return self.f.__name__

    def default(self, obj):
        if self._default is None:
            return None

        default_to_return = self._default(obj) if callable(self._default) else self._default

        if default_to_return is None:
            return None
        elif isinstance(self.type, type) and isinstance(default_to_return, self.type):
            return default_to_return
        else:
            return self.type(default_to_return)

    def validate(self, obj, value):
        if self.validator is not None and self.validator(obj, value) is False:
            message = self.warning_message or "Setting {} to {} does not fulfill restrictions.".format(self.public_name, value)
            if self.warning_only:
                warnings.warn(message, Warning)
            else:
                raise ValueError(message)

    def version_check(self, obj):
        if isinstance(obj, Versioned) and self.version is not None and obj.version is not None:
            if self.version > obj.version:
                warnings.warn('This is not supported on current version!', Warning)

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, f):
        self.__doc__ = f.__doc__
        self._f = f

    def did_set(self, f):
        self._did_set = f
        return self

    def will_set(self, f):
        self._will_set = f
        return self
