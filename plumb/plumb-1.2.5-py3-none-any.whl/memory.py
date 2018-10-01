"""
In-memory source and sink implementation.

Designed as a test artifact for external systems.
"""
from plumb.base import BaseSource, BaseSink


class Source(BaseSource):
    """Test artifact, initialized with packages.

    It provides "replay" functionality by returning pre-loaded packages.
    """

    def __init__(self, packages):
        """Get a reference to the package repository.

        Positional parameter:
        * packages list.
        """
        self.depth = len(packages)
        self.packages = packages
        # Will use list.pop() to get the packages.
        self.packages.reverse()

    def get(self, timeout=None):
        """Pop first package from the repository.

        Raises RuntimeError if there are no more packages."""
        try:
            # TODO: Make this a blocking get by using a common blocking object.
            # This should never rise an exception. It should just block.
            return self.packages.pop()
        except IndexError:
            raise RuntimeError('no more packages in MemorySource')

    def close(self):
        pass


class Sink(BaseSink):
    """Wrap a list to simulate a Package Sink object."""

    def __init__(self):
        self.packages = []

    def put(self, message):
        self.packages.append(message)

    def close(self):
        pass
