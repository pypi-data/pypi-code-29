from ghostbot.core import Basis, Service, Scenario
from ghostbot.utils.os import FileSystem, Computer
from ghostbot.utils.json import Json
from ghostbot.utils.logger import Logger
from ghostbot.scripts.updaters import ChromeAgent, FirefoxAgent
from . import GhostbotProfile, StatusCode


class Diagnose(Basis, Service):
    BROWSERS_JSON = "browsers.json"
    BROWSERS_SCHEMA = "browsers"
    BROWSERS_VERSION = "0.1.0"
    DRIVERS_JSON = "drivers.json"
    DRIVERS_SCHEMA = "drivers"
    DRIVERS_VERSION = "0.1.0"

    def __init__(self):
        super().__init__()
        self.logger = Logger(__name__)
        self._browsers = None
        self._drivers = None

    def startup(self):
        pass

    def shutdown(self):
        self._browsers = None
        self._drivers = None

    def _load_browsers(self):
        if not self._browsers:
            path = FileSystem.join(GhostbotProfile.assets_resources, self.BROWSERS_JSON)
            self.logger.info(StatusCode[110].format(path))
            if FileSystem.exists(path):
                browsers = Json.load(path)
                if browsers["schema"] == self.BROWSERS_SCHEMA:
                    if browsers["version"] == self.BROWSERS_VERSION:
                        self._browsers = browsers
                    else:
                        self.error(StatusCode[212], browsers["version"], path)
                else:
                    self.error(StatusCode[211], browsers["schema"], path)
            else:
                self.error(StatusCode[210], path)
        return self._browsers is not None

    def _load_drivers(self):
        if not self._drivers:
            path = FileSystem.join(GhostbotProfile.assets_resources, self.DRIVERS_JSON)
            self.logger.info(StatusCode[110].format(path))
            if FileSystem.exists(path):
                drivers = Json.load(path)
                if drivers["schema"] == self.DRIVERS_SCHEMA:
                    if drivers["version"] == self.DRIVERS_VERSION:
                        self._drivers = drivers
                    else:
                        self.error(StatusCode[212], drivers["version"], path)
                else:
                    self.error(StatusCode[211], drivers["schema"], path)
            else:
                self.error(StatusCode[210], path)
        return self._drivers is not None

    def execute(self, action):
        if self._load_browsers() and self._load_drivers():
            system = Computer.system()
            if system in self._browsers["browsers"]:
                browsers = self._browsers["browsers"][system]
                for driver, data in self._drivers["drivers"].items():
                    if driver not in browsers:
                        continue
                    if system in data["os"]:
                        self.logger.info(StatusCode[121].format(driver, system))
                        scenario = Scenario(data)
                        if driver == "chrome":
                            agent = ChromeAgent(scenario)
                            agent.execute({"action": action, "target": data["os"][system]})
                        elif driver == "firefox":
                            agent = FirefoxAgent(scenario)
                            agent.execute({"action": action, "target": data["os"][system]})
                        else:
                            self.error(StatusCode[510], driver)
                    else:
                        self.error(StatusCode[202], system, "os")
            else:
                self.error(StatusCode[202], system, "browsers")
        else:
            self.error(StatusCode[201], "Update#execute")
