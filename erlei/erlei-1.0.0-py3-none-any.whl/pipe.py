from functools import partial

__all__ = ['pipe']


class Pipe(object):
    """Provide simple syntax for function composition, such as
    f[g(x)], f(g(h(x))) etc.(through << and >> operators)
    Usage example:
    >>> func = Pipe() << (lambda x: x + 1) << (lambda x: x**2)
    >>> print(func(5))
    26
    >>> func = Pipe() >> (lambda x: x + 1) >> (lambda x: x**2)
    >>> print(func(5))
    36
    >>> func = Pipe() >> (lambda x: filter(lambda y: y < 6, x)) >> sum
    >>> print(func(range(10)))
    15
    >>> func = Pipe(lambda l: map(lambda x: x*x, l)) >> sum >> (lambda x: x**(1/2))
    >>> print(func(range(3, 5)))
    5.0
    """
    __slots__ = 'f'

    def __init__(self, f=lambda x: x, *args, **kwargs):
        self.f = partial(f, *args, **kwargs) if any([args, kwargs]) else f

    def __str__(self):
        return "<class 'Pipe'>"

    @classmethod
    def __compound(cls, f, g):
        return cls(lambda *args, **kwargs: f(g(*args, **kwargs)))

    def __rshift__(self, g):
        return self.__class__.__compound(g, self.f)

    def __lshift__(self, g):
        return self.__class__.__compound(self.f, g)

    def __rrshift__(self, g):
        return self.__class__() >> g >> self.f

    def __rlshift__(self, g):
        return self.__class__() >> self.f >> g

    def __le__(self, other):
        return self.__call__(other)

    def __ror__(self, other):
        return self.__call__(other)

    def __or__(self, other):
        return self.__call__(other)

    def __call__(self, *args, **kwargs):
        if not args:
            return self.__class__() >> (lambda x: x)
        if callable(args[0]):
            return self.__class__() >> args[0]
        return self.f(*args, **kwargs)


pipe = Pipe()

if __name__ == '__main__':
    pass
