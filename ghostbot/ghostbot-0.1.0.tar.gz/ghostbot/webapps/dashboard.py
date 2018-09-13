from flask import Flask
from ghostbot import GhostbotProfile
from ghostbot.core import Basis, Service
from ghostbot.utils.logger import Logger
from ghostbot.utils.os import FileSystem as fs
from ghostbot.utils.json import Json
from ghostbot.webapps.views import CalendarView, DashboardView, DiagnoseView, EvidenceView, JobView, LogbookView
from ghostbot.webapps.views import SupportView, TaskView
from ghostbot.webapps.filters import filter_numeric


class Dashboard(Basis, Service):
    CONFIG_JSON = "config.json"
    STATIC_PATH = "static"
    TEMPLATE_PATH = "templates"
    DASHBOARD_HOST = "0.0.0.0"
    DASHBOARD_PORT = 1989
    DATABASE = "dashboard.db"
    DDL = "ddl/dashboard.sql"

    def __init__(self):
        super().__init__()
        self.logger = Logger(__name__)
        self._flask = Flask(__name__, static_folder=self.STATIC_PATH, template_folder=self.TEMPLATE_PATH)
        self._flask.jinja_env.filters["numeric"] = filter_numeric

    def flask(self):
        return self._flask

    def _register(self):
        self.logger.info("Dashboard registered all views")
        CalendarView.register(self._flask)
        DashboardView.register(self._flask)
        DiagnoseView.register(self._flask)
        EvidenceView.register(self._flask)
        JobView.register(self._flask)
        LogbookView.register(self._flask)
        SupportView.register(self._flask)
        TaskView.register(self._flask)

    def startup(self):
        self.logger.info("Dashboard started")
        config = Json.load(fs.join(GhostbotProfile.settings, self.CONFIG_JSON))
        if config:
            port = config["services"]["dashboard"]["port"]  # + Ghostbot.job_id()
        else:
            port = self.DASHBOARD_PORT                      # + Ghostbot.job_id()
        self.logger.info("host={} port={}".format(self.DASHBOARD_HOST, port))
        self._register()
        self._flask.run(host=self.DASHBOARD_HOST, port=port)

    def shutdown(self):
        self.logger.info("Dashboard stopped")


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.startup()
