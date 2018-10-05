from sqla_filters.tree import SqlaFilterTree


class BaseSqlaParser(object):
    """Base class for the parsers use to generate filters tree."""

    def __init__(self, data: str, attr_sep: str= '.') -> None:
        self._raw_data = data
        self._attr_sep = attr_sep
        self._filters_tree = self._generate_filters_tree()

    @property
    def raw_data(self) -> str:
        """Return the raw data string."""
        return self._raw_data

    @property
    def attr_sep(self) -> str:
        """Return the current attriute separator."""
        return self._attr_sep

    @attr_sep.setter
    def attr_sep(self, new_sep: str) -> None:
        """Set the new value for the attribute separator.
        
        When the new value is assigned a new tree is generated.
        """
        self._attr_sep = new_sep
        self._filters_tree = self._generate_filters_tree()

    @property
    def tree(self) -> SqlaFilterTree:
        return self._filters_tree

    def _generate_filters_tree(self) -> SqlaFilterTree:
        raise NotImplementedError('You must implement this method.')
