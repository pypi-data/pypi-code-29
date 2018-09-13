from enum import Enum
from datetime import datetime
from os.path import abspath, dirname, join
from ghostbot.utils.decorator import classproperty
from ghostbot.utils.os import FileSystem
from ghostbot.utils.datetime import Datetime


class Environments(Enum):
    LOCAL = "local",
    DEVELOPMENT = "development",
    STAGING = "staging",
    PRODUCTION = "production"


class Scaffolds(Enum):
    PROJECT = "project"
    AGENT = "agent"
    CONTAINER = "container"
    REACTOR = "reactor"

    @classmethod
    def parse(cls, text):
        result = None
        for name, member in cls.__members__.items():
            if member.value == text:
                result = member
                break
        return result


class Ghostbot(object):
    _instances = {
        "diagnose": None,
        "webapps": None,
        "inspector": None,
        "scheduler": None,
        "repository": None,
        "wizard": None
    }
    _project = {
        "signature": None,
        "project_name": None,
        "project_home": None,
        "settings_directory": None,
        "database_directory": None,
        "evidence_directory": None,
        "logs_directory": None,
        "job_id": None
    }
    _actions = {}
    _cache = {}

    @classmethod
    def diagnose(cls):
        if not cls._instances["diagnose"]:
            from .diagnose import Diagnose
            instance = Diagnose()
            instance.startup()
            cls._instances["diagnose"] = instance
        return cls._instances["diagnose"]

    @classmethod
    def webapps(cls):
        if not cls._instances["webapps"]:
            from .webapps import Dashboard
            instance = Dashboard()
            instance.startup()
            cls._instances["webapps"] = instance
        return cls._instances["webapps"]

    @classmethod
    def inspector(cls):
        if not cls._instances["inspector"]:
            from .inspector import Inspector
            instance = Inspector()
            instance.startup()
            cls._instances["inspector"] = instance
        return cls._instances["inspector"]

    @classmethod
    def repository(cls):
        if not cls._instances["repository"]:
            from .repository import Repository
            instance = Repository()
            instance.startup()
            cls._instances["repository"] = instance
        return cls._instances["repository"]

    @classmethod
    def scheduler(cls):
        if not cls._instances["scheduler"]:
            from .scheduler import Scheduler
            instance = Scheduler()
            instance.startup()
            cls._instances["scheduler"] = instance
        return cls._instances["scheduler"]

    @classmethod
    def wizard(cls):
        if not cls._instances["wizard"]:
            from .wizard import Wizard
            instance = Wizard()
            instance.startup()
            cls._instances["wizard"] = instance
        return cls._instances["wizard"]

    @classmethod
    def signature(cls, signature=None):
        if signature:
            cls._project["signature"] = signature
        return cls._project["signature"]

    @classmethod
    def project_name(cls, project_name=None):
        if project_name:
            cls._project["project_name"] = project_name
        return cls._project["project_name"]

    @classmethod
    def project_home(cls, project_home=None):
        if project_home:
            cls._project["project_home"] = project_home
        return cls._project["project_home"]

    @classmethod
    def settings_directory(cls, settings_directory=None):
        if settings_directory:
            cls._project["settings_directory"] = settings_directory
        return cls._project["settings_directory"]

    @classmethod
    def database_directory(cls, database_directory=None):
        if database_directory:
            cls._project["database_directory"] = database_directory
        return cls._project["database_directory"]

    @classmethod
    def evidence_directory(cls, evidence_directory=None):
        if evidence_directory:
            cls._project["evidence_directory"] = evidence_directory
        return cls._project["evidence_directory"]

    @classmethod
    def logs_directory(cls, logs_directory=None):
        if logs_directory:
            cls._project["logs_directory"] = logs_directory
        return cls._project["logs_directory"]

    @classmethod
    def job_id(cls, job_id=None):
        if job_id:
            cls._project["job_id"] = job_id
        return cls._project["job_id"]

    @classmethod
    def actions(cls, uri=None, class_name=None, method_name=None, is_generator=False):
        result = cls._actions
        if uri and class_name and method_name:
            if class_name not in cls._actions:
                cls._actions[class_name] = {}
            cls._actions[class_name].update({uri: (method_name, is_generator)})
        elif uri and class_name:
            if class_name in cls._actions:
                if uri in cls._actions[class_name]:
                    result = cls._actions[class_name][uri]
                else:
                    result = None
            else:
                result = None
        return result

    @classmethod
    def cache(cls, key, value=None):
        result = None
        if key and value:
            cls._cache[key] = value
        elif key:
            if key in cls._cache:
                result = cls._cache[key]
        return result

    @classproperty
    def fixtures_accounts(self):
        return FileSystem.join(Ghostbot.project_home(), "assets/fixtures/accounts")

    @classproperty
    def fixtures_cookies(self):
        return FileSystem.join(Ghostbot.project_home(), "assets/fixtures/cookies")

    @classproperty
    def fixtures_devices(self):
        return FileSystem.join(Ghostbot.project_home(), "assets/fixtures/devices")

    @classproperty
    def resources_bindings(self):
        return FileSystem.join(Ghostbot.project_home(), "assets/resources/binding")

    @classproperty
    def resources_forms(self):
        return FileSystem.join(Ghostbot.project_home(), "assets/resources/forms")

    @classproperty
    def resources_schemas(self):
        return FileSystem.join(Ghostbot.project_home(), "assets/resources/schemas")

    @classproperty
    def resources_validators(self):
        return FileSystem.join(Ghostbot.project_home(), "assets/resources/validators")


class GhostbotApplications(Enum):
    GHOSTBOT = "ghostbot"
    DASHBOARD = "webapps"
    INSPECTOR = "inspector"
    SCHEDULER = "scheduler"


class GhostbotProfile(object):
    RELEASE_DATETIME = datetime(2018, 3, 12, 14, 0, 0)
    VERSION_BASE = (0, 1)
    VERSIONS = {
        GhostbotApplications.GHOSTBOT:  (0,),
        GhostbotApplications.DASHBOARD: (0,),
        GhostbotApplications.INSPECTOR: (0,),
        GhostbotApplications.SCHEDULER: (0,)
    }
    _home = abspath(dirname(__file__))

    @classmethod
    def version(cls, app=GhostbotApplications.GHOSTBOT):
        numbers = [str(x) for x in cls.version_info(app)]
        return ".".join(numbers)

    @classmethod
    def version_info(cls, app=GhostbotApplications.GHOSTBOT):
        version_app = cls.VERSIONS[app]
        return tuple(cls.VERSION_BASE + tuple(version_app))

    @classmethod
    def release_datetime(cls):
        return cls.RELEASE_DATETIME.strftime(Datetime.DATETIME)

    @classproperty
    def downloads(self):
        return FileSystem.tempdir("downloads")

    @classproperty
    def home(self):
        return self._home

    @classproperty
    def assets(self):
        return join(self._home, "assets")

    @classproperty
    def assets_database(self):
        return join(self._home, "assets/database")

    @classproperty
    def assets_drivers(self):
        return join(self._home, "assets/drivers")

    @classproperty
    def assets_queries(self):
        return join(self._home, "assets/queries")

    @classproperty
    def assets_queries_dashboard(self):
        return join(self._home, "assets/queries/webapps")

    @classproperty
    def assets_queries_repository(self):
        return join(self._home, "assets/queries/repository")

    @classproperty
    def assets_queries_scheduler(self):
        return join(self._home, "assets/queries/scheduler")

    @classproperty
    def assets_resources(self):
        return join(self._home, "assets/resources")

    @classproperty
    def assets_templates(self):
        return join(self._home, "assets/templates")

    @classproperty
    def assets_webpages(self):
        return join(self._home, "assets/webpages")

    @classproperty
    def core(self):
        return join(self._home, "core")

    @classproperty
    def logs(self):
        return join(self._home, "logs")

    @classproperty
    def scripts_drivers(self):
        return join(self._home, "scripts/drivers")

    @classproperty
    def scripts_extensions(self):
        return join(self._home, "scripts/extensions")

    @classproperty
    def assets_updaters(self):
        return join(self._home, "scripts/updaters")

    @classproperty
    def settings(self):
        return join(self._home, "settings")

    @classproperty
    def utils(self):
        return join(self._home, "utils")


class Meta(type):
    VECTOR = None

    def __getitem__(cls, index):
        return "<{}> {}".format(index, cls.VECTOR[index])


class StatusCode(metaclass=Meta):
    VECTOR = {
        100: "Information: {}",
        110: "Loading json file: path={}",
        120: "Checking WebDriver: device={}",
        121: "Updating WebDriver: device={} system={}",
        122: "Download WebDriver: file={}",
        123: "Deployed WebDriver: file={}",
        124: "Latest WebDriver used: driver={} version={}",
        125: "Newer WebDriver detected: driver={} version={}",
        126: "Unsupported Archive format: extension={}",
        127: "Startup WebDriver: config={}",
        128: "Shutdown WebDriver: instance={}",
        130: "Wizard create project: path={}",
        131: "Wizard create agent: path={}",
        132: "Wizard create container: path={}",
        133: "Wizard create reactor: path={}",
        140: "Repository project successfully appended: project_name={} signature={}",
        141: "Repository project successfully removed: signature={}",
        142: "Repository project successfully activated: signature={}",
        143: "Repository {} successfully appended: name={} path={}",
        150: "Event loop dispatch handler: class={} uri='{}'",
        151: "Action executing: uri='{}'",
        160: "Scheduler logbook successfully appended: signature={} logbook_id={}",
        161: "Scheduler logbook successfully updated: signature={} logbook_id={}",
        200: "Resource Error: {}",
        201: "Loading process failed: {}",
        202: "Key not found: key={} dictionary={}",
        203: "Unexpected value: key={} value={}",
        210: "Json file not found: path={}",
        211: "Json file schema incorrect: schema={} path={}",
        212: "Json file version incorrect: version={} path={}",
        213: "Fixtures reference error: path prefix must start with '{}'",
        214: "Resources reference error: path prefix must start with '{}'",
        220: "WebDriver not found: driver={}",
        221: "WebDriver not supported: driver={} system={}",
        222: "WebDriver can not update: driver={} system={}",
        223: "WebDriver checksum error: driver={} hash={}",
        224: "WebDriver file not found: file={}",
        230: "Parent directory doesn't exists: path={}",
        231: "Project home directory already exists: path={}",
        232: "Unknown projects data format: value={}",
        233: "Unsupported projects data type: type={}",
        234: "Agent file already exists: path={}",
        235: "Container file already exists: path={}",
        236: "Reactor file already exists: path={}",
        300: "Database Error: {}",
        310: "Database open exception: args={}",
        311: "Database load failed: path={}",
        320: "Connection instance is None",
        321: "Connection begin exception: args={}",
        322: "Connection cursor exception: args={}",
        323: "Connection commit exception: args={}",
        324: "Connection rollback exception: args={}",
        325: "Connection end exception: args={}",
        326: "Connection close exception: args={}",
        330: "Cursor instance is None",
        331: "Cursor query exception: args={}",
        332: "Cursor execute exception: args={}",
        333: "Cursor executes exception: args={}",
        334: "Cursor close exception: args={}",
        340: "MongoDB db initialize exception: args={}",
        341: "MongoDB collection insert exception: args={}",
        342: "MongoDB collection update exception: args={}",
        343: "MongoDB collection delete exception: args={}",
        344: "MongoDB collection select exception: args={}",
        400: "Network Error: {}",
        410: "Unexpected status code: status_code={} url={}",
        500: "Internal Error: {}",
        501: "Index out of range: {}",
        502: "List length error: expected={} actual={}",
        503: "Dictionary key error: key='{}' dictionary={}",
        504: "File not found: path={}",
        505: "Directory not exists: path={}",
        506: "Wrong count of arguments: count={}",
        507: "Wrong type of arguments: type={}",
        508: "Wrong value of arguments: value={}",
        509: "Unsupported handler type: type={}",
        510: "Unsupported WebDevice: device={}",
        511: "WebDriver initialization failed: device={}",
        512: "WebDriver instance not found: method={}",
        513: "WebDriver exception occurred: args={}",
        514: "WebDriver deployment failed: args={}",
        515: "Unsupported element: element={}",
        520: "Container parser failed: args={}",
        521: "Container data not found: method={}",
        522: "Container expression is wrong: expression={}",
        523: "Container exception occurred: args={} file={}",
        530: "Repository is not ready: method={}",
        531: "Repository signature already exists: signature={}",
        532: "Repository can't insert data: project_name={} signature={}",
        533: "Repository can't read sql: file={}",
        534: "Repository project loading failed",
        540: "Action not found: class={} method={}",
        541: "Handler not found: class={} uri={}",
        550: "Scheduler is not ready: method={}",
        551: "Scheduler can't read sql: file={}",
        552: "Scheduler can't insert data: signature={} table={}",
        553: "Scheduler can't update data: signature={} table={}",
        554: "Scheduler can't select data: signature={} table={}",
        600: "External Error: {}",
        610: "Jinja2 exception occurred: args={}"
    }


__all__ = [Environments, Scaffolds, Ghostbot, GhostbotProfile, GhostbotApplications, StatusCode]
