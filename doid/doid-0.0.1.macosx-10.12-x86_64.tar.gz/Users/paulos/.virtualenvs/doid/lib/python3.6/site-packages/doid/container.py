from .filter import Q, ga


class K(object):
    """Key getter object

    Receives an arbitrary list of strings or callables. Callables
    will be called with the object to be sorted and should return
    a sort key. Strings are resolved to attributes following the
    Django ORM protocol. Returns a list of keys in the same order
    as the arguments.
    """

    def __init__(self, *args):
        self._args = args

    @staticmethod
    def _ga(obj, attr_path):
        return ga(obj, *attr_path.split('__'))

    def _apply(self, obj, arg):
        if callable(arg):
            return arg(obj)
        return self._ga(obj, arg)

    def __call__(self, obj):
        return [self._apply(obj, arg) for arg in self._args]


class ListContainer(list):
    """The list container object is an ordered collection of objects that can
    be sorted and/or filtered
    """
    def __getitem__(self, k):
        if isinstance(k, slice):
            return ListContainer(super().__getitem__(k))
        return super().__getitem__(k)

    def filter(self, *args, **kwargs):
        f = Q(*args, **kwargs)
        return ListContainer(item for item in self if f(item))

    def order_by(self, *args, **kwargs):
        copy = self[:]
        copy.sort(key=K(*args), **kwargs)
        return ListContainer(copy)
