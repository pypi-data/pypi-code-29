from functools import partial, wraps
from inspect import getfullargspec


def currying(func):
    """A decorator that makes the function curried
    Usage example:
    >>> @currying
    ... def sum5(a, b, c, d, e):
    ...     return a + b + c + d + e
    ...
    >>> sum5(1)(2)(3)(4)(5)
    15
    >>> sum5(1, 2, 3)(4, 5)
    15
    """

    @wraps(func)
    def _currying(*args, **kwargs):
        f = func
        count = 0
        while isinstance(f, partial):
            if f.args:
                count += len(f.args)
            f = f.func

        spec = getfullargspec(f)

        if count == len(spec.args) - len(args):
            return func(*args, **kwargs)

        return currying(partial(func, *args, **kwargs))

    return _currying
