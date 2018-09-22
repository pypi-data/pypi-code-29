"""ComposedFunction class and its standalone helper functions."""


def resolve_composed_functions(data, recursive=True):
    """
    Calls `ComposedFunction`s and returns its return value. By default, this
    function will recursively iterate dicts, lists, tuples, and sets and
    replace all `ComposedFunction`s with their return value.
    """

    if isinstance(data, ComposedFunction):
        data = data()

    if recursive:
        if isinstance(data, dict):
            for key, value in data.items():
                data[key] = resolve_composed_functions(
                    value,
                    recursive=recursive,
                )
        elif isinstance(data, (list, tuple, set)):
            for index, value in enumerate(data):
                data[index] = resolve_composed_functions(
                    value,
                    recursive=recursive,
                )

    return data


class ComposedFunction:
    """
    Fully-composed callable object initialized with the elements of a typical
    function call. This is useful for passing parameter-filled function calls
    as arguments to be executed at a later time.

    Initialize
    ==========
    Saves the variables necessary for a fully-composed function call.

    Positional Arguments:
    ---------------------
    - function: Callable object.
    - args: List, tuple, or set of positional arguments for the function call.
    - kwargs: Dictionary of keyword arguments for the function call.

    Call Initialized Instance
    =========================
    Calling an initialized `ComposedFunction` instance will call the
    fully-composed function, using the `function`, `args, and `kwargs` saved
    from initialization, and returns its value.
    """

    __function = None
    __args = None
    __kwargs = None

    def __init__(self, function, args=None, kwargs=None):
        if not callable(function):
            msg = ('Cannot create ComposedFunction with the non-callable '
                   f'object `{function}` as its function.')
            raise TypeError(msg)

        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}

        self.__function = function
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self):
        return self.function(*self.args, **self.kwargs)

    def __str__(self):
        function = self.function.__name__
        arguments = ', '.join([
            *[f"'{a}'" if isinstance(a, str) else str(a) for a in self.args],
            *[f"{k}='{v}'" if isinstance(v, str) else f'{k}={v}'
              for k, v in self.kwargs.items()]
        ])
        return f'<{self.__class__.__name__}: {function}({arguments})>'

    @property
    def function(self):
        return self.__function

    @property
    def args(self):
        return self.__args

    @property
    def kwargs(self):
        return self.__kwargs
