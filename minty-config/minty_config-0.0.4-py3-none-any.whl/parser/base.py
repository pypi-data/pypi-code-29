from abc import ABC, abstractmethod


class ConfigParserBase(ABC):
    @abstractmethod
    def parse(self, content: str) -> str:
        """Parse configuration content

        :param content: contents of the configuration file to parse
        :type content: str
        :return: the "content" parameter, unchanged
        :rtype: str
        """

        return content
