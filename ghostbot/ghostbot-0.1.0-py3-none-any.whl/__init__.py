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
    _project = {
        "signature": None,
        "name": None,
        "home": None
    }
    _cache = {}

    @classmethod
    def signature(cls, signature=None):
        if signature:
            cls._project["signature"] = signature
        return cls._project["signature"]

    @classmethod
    def project_name(cls, name=None):
        if name:
            cls._project["name"] = name
        return cls._project["name"]

    @classmethod
    def project_home(cls, home=None):
        if home:
            cls._project["home"] = home
        return cls._project["home"]

    @classmethod
    def cache(cls, key, value=None):
        result = None
        if key and value:
            cls._cache[key] = value
        elif key:
            if key in cls._cache:
                result = cls._cache[key]
        return result


class GhostbotApplications(Enum):
    GHOSTBOT = "ghostbot"
    DASHBOARD = "dashboard"
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
        return join(self._home, "assets/queries/dashboard")

    @classproperty
    def assets_queries_repository(self):
        return join(self._home, "assets/queries/repository")

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
        200: "Resource Error: {}",
        201: "Loading process failed: {}",
        202: "Key not found: key={} dictionary={}",
        203: "Unexpected value: key={} value={}",
        210: "Json file not found: path={}",
        211: "Json file schema incorrect: schema={} path={}",
        212: "Json file version incorrect: version={} path={}",
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
        340: "Recset one exception: args={}",
        341: "Recset all exception: args={}",
        342: "Recset next exception: args={}",
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
        510: "Unsupported WebDevice: device={}",
        511: "WebDriver initialization failed: device={}",
        512: "WebDriver instance not found: method={}",
        513: "WebDriver exception occurred: args={}",
        514: "WebDriver deployment failed: args={}",
        515: "Unsupported element: element={}",
        520: "Container parser failed: args={}",
        521: "Container data not found: method={}",
        522: "Container exception occurred: args={}",
        530: "Repository is not ready: method={}",
        531: "Repository signature already exists: signature={}",
        532: "Repository can't insert data: project_name={} signature={}",
        533: "Repository can't read sql: file={}",
        534: "Repository project loading failed",
        600: "External Error: {}",
        610: "Jinja2 exception occurred: args={}"
    }
