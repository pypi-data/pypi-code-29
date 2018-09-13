from flask import Flask
from ghostbot import GhostbotProfile
from ghostbot.core import Basis, Service
from ghostbot.utils.logger import Logger
from ghostbot.utils.os import FileSystem as fs
from ghostbot.utils.json import Json
from ghostbot.webapps.filters import filter_numeric
from ghostbot.webapps.views import ConsoleView, WizardView


class Console(Basis, Service):
    CONFIG_JSON = "config.json"
    STATIC_PATH = "static"
    TEMPLATE_PATH = "templates"
    CONSOLE_HOST = "0.0.0.0"
    CONSOLE_PORT = 1984
    DATABASE = "repository.db"
    DDL = "ddl/repository.sql"

    def __init__(self):
        super().__init__()
        self.logger = Logger(__name__)
        self._flask = Flask(__name__, static_folder=self.STATIC_PATH, template_folder=self.TEMPLATE_PATH)
        self._flask.jinja_env.filters["numeric"] = filter_numeric

    def flask(self):
        return self._flask

    def _register(self):
        ConsoleView.register(self._flask)
        WizardView.register(self._flask)

    def startup(self):
        self.logger.info("Console started")
        config = Json.load(fs.join(GhostbotProfile.settings, self.CONFIG_JSON))
        if config:
            port = config["services"]["console"]["port"]
        else:
            port = self.CONSOLE_PORT
        self.logger.info("host={} port={}".format(self.CONSOLE_HOST, port))
        self._register()
        self._flask.run(host=self.CONSOLE_HOST, port=port)

    def shutdown(self):
        self.logger.info("Console stopped")


if __name__ == "__main__":
    console = Console()
    console.startup()
