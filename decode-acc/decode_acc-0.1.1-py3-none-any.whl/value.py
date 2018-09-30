"""
A trivial base class for immutable value objects.
"""


class ValueObject(object):
    """
    A trivial base class for immutable value objects that keep
    their data in a _data dictionary member and should only
    provide access to it through getter properties.
    """

    def __init__(self, _data=None):
        """
        Initialize the base ValueObject with the specified _data
        dictionary.
        """
        self._data = _data if _data is not None else {}

    def _as_dict(self):
        """
        An internal-use method that returns a shallow copy of the data
        dictionary so that other objects may be created from it.
        """
        return {k: v for (k, v) in self._data.items()}

    def __eq__(self, other):
        """
        Compare two value objects for equality: compare the object types,
        keys, and values.
        """
        return type(self) == type(other) and \
            set(self._data.keys()) == set(other._data.keys()) and \
            all([self._data[k] == other._data[k] for k in self._data.keys()])

    def __lt__(self, other):
        """
        Not implemented: check if a value object is less than another one.
        """
        raise NotImplementedError()

    def __le__(self, other):
        """
        Not implemented: check if a value object is less than or equal to
        another one.
        """
        raise NotImplementedError()

    def __gt__(self, other):
        """
        Not implemented: check if a value object is greater than another one.
        """
        raise NotImplementedError()

    def __ge__(self, other):
        """
        Not implemented: check if a value object is greater than or equal to
        another one.
        """
        raise NotImplementedError()
