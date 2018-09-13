from functools import partial

__all__ = [
    'infix',
    'is_a',  # infix(isinstance)
    'to',
    'step',
    'has',  # infix(hasattr)
    'take',
    'drop',
]


class infix(partial):
    """A decorator that allows functions to be used as infix functions.
    Usage example:
    >>> @infix
    ... def plus(a, b):
    ...     return a + b
    ...
    >>> 40 /plus/ 2
    42
    >>> 5 /plus/ 6
    11
    >>> list(1 /to/ 4 /step/ -1)
    [3, 2, 1]
    >>> def pow(a, b):
    ...     return a ** b
    ...
    >>> pow = infix(pow)
    >>> 3 /pow/ 2
    9
    >>> 3 /is_a/ int
    True
    """

    def __truediv__(self, right):
        return self(right)

    def __rtruediv__(self, left):
        return infix(self.func, left)


is_a = infix(isinstance)
has = infix(hasattr)


@infix
def to(start, end):
    return range(start, end)


@infix
def step(obj, step):
    return obj[::step]


@infix
def take(obj, n):
    return obj[:n]


@infix
def drop(obj, n):
    return obj[n:]
