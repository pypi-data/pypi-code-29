from abc import ABC, abstractmethod


class AbstractPlugin(ABC):
    """Abstract interface for all persistence layer plugins.
    Expects the following to be defined by the subclass:
        - :attr:`type` (as a read-only property)
        - :func:`write`
        - :func:`read`
        - :func:`update`
        - :func:`delete`
        - :func:`list`
        - :func:`query`
    """

    @abstractmethod
    def type(self):
        """A string denoting the type of plugin (e.g. BigchainDB)."""

    @abstractmethod
    def write(self, obj):
        """Write an object in OceanDB
         Args:
             obj : The registry that we want to write in OceanDB
         Returns:
             str: Id of the created registry on the persistence layer
         Raises:
             :exc:`~..OceanDbError`: If the registry failed to be
                 created
         """

    @abstractmethod
    def read(self, id):
        """Read the registry for a provided id
         Args:
             id: Id of the created registry on the persistence layer
         Returns:
             str: Value of the registry read.
        """

    @abstractmethod
    def update(self, obj, id):
        """Update an object in OceanDB
         Args:
             id: Id of the created registry on the persistence layer
             obj : The data that we want to write in OceanDB
         Returns:
             str: Value of the registry updated.
         Raises:
             :exc:`~..OceanDbError`: If the registry failed to be
                 created
        """

    @abstractmethod
    def delete(self, id):
        """Delete the registry for a provided id
         Args:
             id: Id of the created registry on the persistence layer
         Returns:
             str: Value of the id deleted.
        """

    @abstractmethod
    def list(self, search_from=None, search_to=None, limit=None):
        """List the elements saved in OceanDB
         Args:
             search_from : From which registry you want to start to show
             search_to : To which registry you want to start to show
             limit : Number of registries that will be show
         Returns:
             dict: List of registries
        """

    @abstractmethod
    def query(self, query_string):
        """Query the elements saved in OceanDB
        Args:
            query_string: Query to OceanDB in a string format.
        Returns:
             dict: List of registries
        """
