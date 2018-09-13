from ghostbot import StatusCode, GhostbotProfile
from ghostbot.core import Appearances, WebDrivers, WebAgent
from ghostbot.utils.logger import Logger
from ghostbot.utils.os import FileSystem
from ..containers import ChromeContainer
from ..reactors import ChromeReactor


class ChromeAgent(WebAgent):

    def __init__(self, scenario):
        super().__init__(scenario)
        self.logger = Logger(__name__)
        self.container(ChromeContainer(self))
        self.reactor(ChromeReactor(self))

    def execute(self, options=None):
        options = options if options else {}
        options.update({"driver": WebDrivers.FIREFOX, "appearance": Appearances.HEADLESS})
        # options.update({"driver": WebDrivers.FIREFOX, "appearance": Appearances.STANDARD})
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
        container.scrap("driver", target)
        self.open(data["url"])
        element = container.select(data["latest_release"])
        container.scrap("latest_release", element.string)
        self.close()
        self.reactor().execute()

    def _update(self, target):
        data = self.scenario().data()
        container = self.container()
        container.scrap("driver", target)
        self.open(data["url"])
        container.scrap("supports", container.select(data["description"]["supports"]))
        container.scrap("changes", container.select(data["description"]["changes"]))
        if "download" in data:
            url = container.select(data["download"]["link"])
            container.scrap("version", url.string.split()[1])
            self.open(url["href"], data["download"]["loading_marker"])
        self.logger.info(StatusCode[122], target)
        element = container.find("a", text=target)
        container.scrap("url", self.fqdn(element["href"]))
        element = element.find_parent("td").next_sibling
        container.scrap("datetime", element.string)
        element = element.next_sibling
        container.scrap("size", element.string)
        element = element.next_sibling
        container.scrap("etag", element.pre.string)
        download_file = FileSystem.join(GhostbotProfile.downloads, target)
        container.scrap("download_file", download_file)
        self.download_link(download_file, target)
        self.close()
        if self.is_exports():
            self.reactor().execute()
