from apacheconfig import make_loader

from .base import ConfigParserBase


class ApacheConfigParser(ConfigParserBase):
    __slots__ = ["content"]

    def parse(self, content: str) -> dict:
        """Return a dict with the parsed config

        :return: Parsed configuration
        :rtype: dict
        """

        content = super().parse(content)

        if content == "":
            raise ValueError("Cannot parse empty configuration")

        config = None
        with make_loader() as loader:
            config = loader.loads(content)

        return config
