from abc import ABCMeta, abstractmethod


class AbstractFilter:
    """Abstract class for creating filters"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, content):  # pragma: no cover
        """
        Execute filter

        :param string content: binary content of the photo
        """
        raise NotImplementedError()
