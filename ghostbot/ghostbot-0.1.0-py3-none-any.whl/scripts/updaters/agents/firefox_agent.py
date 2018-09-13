import re
from ghostbot import StatusCode, GhostbotProfile
from ghostbot.core import Appearances, WebDrivers, WebAgent
from ghostbot.utils.logger import Logger
from ghostbot.utils.os import FileSystem
from ..containers import FirefoxContainer
from ..reactors import FirefoxReactor


class FirefoxAgent(WebAgent):

    def __init__(self, scenario):
        super().__init__(scenario)
        self.logger = Logger(__name__)
        self.container(FirefoxContainer(self))
        self.reactor(FirefoxReactor(self))

    def execute(self, options=None):
        options = options if options else {}
        options.update({"driver": WebDrivers.GHOST, "appearance": Appearances.HEADLESS})
        self.options(options)
        self.startup(options)
        if "action" in options:
            if options["action"] == "check":
                self._check(options["target"])
            elif options["action"] == "update":
                self._update(options["target"])
            else:
                self.error(StatusCode[203], options["action"], "action")
        else:
            self.error(StatusCode[202], "action", "options")
        self.shutdown()

    def _check(self, target):
        data = self.scenario().data()
        container = self.container()
        self.open(data["url"])
        element = container.select(data["latest_release"])
        target = target.format(element.string[1:])
        container.scrap("driver", target)
        container.scrap("latest_release", element.string)
        self.close()
        self.reactor().execute()

    def _update(self, target):
        data = self.scenario().data()
        container = self.container()
        self.open(data["url"])
        element = container.select(data["latest_release"])
        version = element.string[1:]
        target = target.format(version)
        container.scrap("version", version)
        container.scrap("driver", target)
        container.scrap("description", container.select(data["description"]))
        self.logger.info(StatusCode[122], target)
        element = container.find("a", href=re.compile(target))
        url = self.fqdn(element["href"])
        container.scrap("url", url)
        container.scrap("size", element.find_next("small").text)
        download_file = FileSystem.join(GhostbotProfile.downloads, target)
        container.scrap("download_file", download_file)
        self.download(download_file, url)
        self.close()
        if self.is_exports():
            self.reactor().execute()
