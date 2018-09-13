from datetime import datetime, time
from ghostbot import StatusCode, GhostbotProfile
from ghostbot.core import Basis, Service
from ghostbot.constants import Appearances, Architectures, CPU, OperatingSystems, WebDrivers
from ghostbot.utils.logger import Logger
from ghostbot.utils.os import FileSystem as fs
from ghostbot.utils.database import Database, RDBMS
from ghostbot.utils.datetime import Datetime, Timer


class Computer(object):
    DEFAULT_SCREEN_SIZE = (800, 600)

    def __init__(self):
        self._maker = None
        self._model = None
        self._cpu = CPU.UNKNOWN
        self._os_type = OperatingSystems.UNKNOWN
        self._os_arch = Architectures.UNKNOWN
        self._os_version = None
        self._screen_sensor = False
        self._screen_size = self.DEFAULT_SCREEN_SIZE

    def maker(self, maker=None):
        if maker:
            self._maker = maker
        return self._maker

    def model(self, model=None):
        if model:
            self._model = model
        return self._maker

    def cpu(self, cpu=None):
        if cpu:
            self._cpu = cpu
        return self._cpu

    def os_type(self, os_type=None):
        if os_type:
            self._os_type = os_type
        return self._os_type

    def os_arch(self, os_arch=None):
        if os_arch:
            self._os_arch = os_arch
        return self._os_arch

    def os_version(self, os_version=None):
        if os_version:
            self._os_version = os_version
        return self._os_version

    def screen_sensor(self, screen_sensor=None):
        if screen_sensor:
            self._screen_sensor = screen_sensor
        return self._screen_sensor

    def screen_size(self, screen_size=None):
        if screen_size:
            self._screen_size = screen_size
        return self._screen_size


class Runtime(object):
    DEFAULT_VERSION = "current"

    def __init__(self):
        self._computer = Computer()
        self._browser_driver = WebDrivers.DEFAULT
        self._browser_version = self.DEFAULT_VERSION
        self._browser_user_agent = None
        self._browser_plugins = []
        self._browser_cookies = []
        self._appearance = Appearances.STANDARD

    def computer(self, computer=None):
        if computer:
            self._computer = computer
        return self._computer

    def browser_driver(self, browser_driver=None):
        if browser_driver:
            self._browser_driver = browser_driver
        return self._browser_driver

    def browser_version(self, browser_version=None):
        if browser_version:
            self._browser_version = browser_version
        return self._browser_version

    def browser_user_agent(self, browser_user_agent=None):
        if browser_user_agent:
            self._browser_user_agent = browser_user_agent
        return self._browser_user_agent

    def browser_plugins(self, browser_plugins=None):
        if browser_plugins:
            self._browser_plugins.extend(browser_plugins)
        return self._browser_plugins

    def browser_cookies(self, browser_cookies=None):
        if browser_cookies:
            self._browser_cookies.extend(browser_cookies)
        return self._browser_cookies

    def appearance(self, appearance=None):
        if appearance:
            self._appearance = appearance
        return self._appearance


class Launch(object):
    UNKNOWN = "unknown"
    ONCE = "once"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    END_OF_MONTH = -1

    def __init__(self):
        self._type = self.UNKNOWN
        self._year = None
        self._month = None
        self._day = None
        self._hour = None
        self._minute = None
        self._weekday = None

    def once(self, year, month, day, hour, minute):
        self._type = self.ONCE
        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minute = minute

    def daily(self, hour, minute):
        self._type = self.DAILY
        self._hour = hour
        self._minute = minute

    def weekly(self, weekday, hour, minute):
        self._type = self.WEEKLY
        self._weekday = weekday
        self._hour = hour
        self._minute = minute

    def monthly(self, day, hour, minute):
        self._type = self.MONTHLY
        self._day = day
        self._hour = hour
        self._minute = minute

    def fetch(self):
        if self._type == self.ONCE:
            content = datetime(self._year, self._month, self._day, self._hour, self._minute)
            result = self._type, content
        elif self._type == self.DAILY:
            content = time(self._hour, self._minute)
            result = self._type, content
        elif self._type == self.WEEKLY:
            content = time(self._hour, self._minute)
            result = self._type, self._weekday, content
        elif self._type == self.MONTHLY:
            content = time(self._hour, self._minute)
            result = self._type, self._day, content
        else:
            result = None
        return result


class Workflow(object):
    UNKNOWN = "unknown"
    SINGLE = "single"
    SERIAL = "serial"
    PARALLEL = "parallel"
    REPEAT = "repeat"
    SWITCH = "switch"

    def __init__(self):
        self._type = self.UNKNOWN
        self._name = None
        self._code = None
        self._interval = None
        self._context = []
        self.variables = {}

    def single(self, name, agent):
        self._type = self.SINGLE
        self._name = name
        self._context.append(agent)

    def serial(self, name, *agents):
        self._type = self.SERIAL
        self._name = name
        self._context.extend(*agents)

    def parallel(self, name, *agents):
        self._type = self.PARALLEL
        self._name = name
        self._context.extend(*agents)

    def repeat(self, name, code, interval, *agents):
        if code and isinstance(code, function):
            self._type = self.REPEAT
            self._name = name
            self._code = code
            self._interval = interval
            self._context.extend(*agents)

    def switch(self, name, code):
        if code and isinstance(code, function):
            self._type = self.SWITCH
            self._name = name
            self._code = code

    def fetch(self):
        if self._type == self.SINGLE:
            result = self._type, self._name, self._context[0]
        elif self._type in [self.SERIAL, self.PARALLEL]:
            result = self._type, self._name, self._context
        elif self._type == self.REPEAT:
            result = self._type, self._name, self._code, self._interval, self._context
        elif self._type == self.SWITCH:
            result = self._type, self._name, self._code
        else:
            result = None
        return result


class Task(object):
    UNKNOWN = "unknown"
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __init__(self):
        self._id = None
        self._status = self.UNKNOWN
        self._name = None
        self._description = None
        self._scenario = None
        self._runtime = None
        self._launch = None
        self._workflow = []

    def id(self, id=None):
        if id:
            self._id = id
        return self._id

    def status(self, status=None):
        if status:
            self._status = status
        return self._status

    def name(self, name=None):
        if name:
            self._name = name
        return self._name

    def description(self, description=None):
        if description:
            self._description = description
        return self._description

    def scenario(self, scenario=None):
        if scenario:
            self._scenario = scenario
        return self._scenario

    def runtime(self, runtime=None):
        if runtime:
            self._runtime = runtime
        return self._runtime

    def launch(self, launch=None):
        if launch:
            self._launch = launch
        return self._launch

    def workflow(self, workflow=None):
        if workflow:
            self._workflow.extend(workflow)
        return self._workflow

    def register(self):
        pass

    def activate(self):
        self._status = self.ACTIVE
        pass

    def inactivate(self):
        self._status = self.INACTIVE
        pass

    def unregister(self):
        pass


class Job(object):
    UNKNOWN = "unknown"
    QUEUEING = "queueing"
    RUNNING = "running"
    WAITING = "waiting"
    STOPPED = "stopped"
    API_CALL = "api_call"
    COMPLETED_ACTIONS = "completed_actions"
    FINISHED_ACTIONS = "finished_actions"
    FAILED_ACTIONS = "finished_actions"
    ABORTED_ACTIONS = "aborted_actions"

    def __init__(self):
        self._id = None
        self._task_id = None
        self._status = self.UNKNOWN
        self._execution = None
        self._departure = None
        self._arrival = None
        self._reason = None
        self._counter = {
            self.API_CALL: 0,
            self.COMPLETED_ACTIONS: 0,
            self.FINISHED_ACTIONS: 0,
            self.FAILED_ACTIONS: 0,
            self.ABORTED_ACTIONS: 0
        }

    def id(self, id=None):
        if id:
            self._id = id
        return self._id

    def task_id(self, task_id=None):
        if task_id:
            self._task_id = task_id
        return self._task_id

    def status(self, status=None):
        if status:
            self._status = status
        return self._status

    def execution(self, execution=None):
        if execution:
            self._execution = execution
        return self._execution

    def queueing(self):
        self._status = self.QUEUEING

    def run(self):
        self._status = self.RUNNING
        self._departure = datetime.now()

    def pause(self):
        self._status = self.WAITING

    def resume(self):
        self._status = self.RUNNING

    def stop(self):
        self._status = self.STOPPED
        self._arrival = datetime.now()

    def increment(self, item):
        if item in self._counter.keys():
            self._counter[item] += 1

    def register(self):
        pass

    def unregister(self):
        pass


# TODO fork new process when the job executed
class Scheduler(Basis, Service):
    DATABASE = "scheduler.db"
    DDL = "ddl/scheduler.sql"
    LOGBOOKS_INSERT = "dml/logbooks_insert.sql"
    LOGBOOKS_UPDATE = "dml/logbooks_update.sql"
    LOGBOOKS_SELECT = "dql/logbooks_select.sql"

    def __init__(self):
        super().__init__()
        self.logger = Logger(__name__)
        self._dsn = fs.join(GhostbotProfile.assets_database, self.DATABASE)

    def startup(self):
        pass

    def shutdown(self):
        pass

    def is_ready(self):
        if not (fs.exists(self._dsn)):
            ddl = fs.join(GhostbotProfile.assets_queries_scheduler, self.DDL)
            if fs.exists(ddl):
                fs.touch(self._dsn)
                db = Database(RDBMS.SQLITE)
                conn = db.open(self._dsn)
                with conn.cursor() as cursor:
                    cursor.execute(db.load(ddl))
                conn.close()
            else:
                self.critical(StatusCode[504], ddl)
        return True

    def select_logbook(self):
        if self.is_ready():
            logbooks_select = fs.join(GhostbotProfile.assets_queries_scheduler, self.LOGBOOKS_SELECT)
            if fs.exists(logbooks_select):
                db = Database(RDBMS.SQLITE)
                conn = db.open(self._dsn)
                with conn.cursor() as cursor:
                    row = cursor.query(db.load(logbooks_select)).fetchone()
                    if row:
                        # TODO fix parameter and effect this method
                        # Ghostbot.signature(row["signature"])
                        # Ghostbot.project_name(row["project_name"])
                        # Ghostbot.project_home(row["project_home"])
                        pass
                    else:
                        # TODO fix parameter and effect this method
                        self.error(StatusCode[554])
                conn.close()
            else:
                self.error(StatusCode[551], self.LOGBOOKS_SELECT)
        else:
            self.error(StatusCode[550], __name__)

    def append_logbook(self, schedule_id, signature, location):
        result = None
        if self.is_ready():
            logbooks_insert = fs.join(GhostbotProfile.assets_queries_scheduler, self.LOGBOOKS_INSERT)
            if fs.exists(logbooks_insert):
                db = Database(RDBMS.SQLITE)
                conn = db.open(self._dsn)
                with conn.cursor() as cursor:
                    now = Datetime.now(to_string=True)
                    params = {
                        "schedule_id": schedule_id,
                        "signature": signature,
                        "departure_at": now,
                        "status": Job.RUNNING,
                        "location": location,
                        "created_by": fs.file(__file__),
                        "created_at": now
                    }
                    if cursor.execute(db.load(logbooks_insert), params) == 1:
                        result = cursor.last_insert_id()
                        self.logger.info(StatusCode[160], signature, result)
                    else:
                        self.error(StatusCode[552], signature, "logbooks")
                conn.close()
            else:
                self.error(StatusCode[551], self.LOGBOOKS_INSERT)
        else:
            self.error(StatusCode[550], __name__)
        return result

    def update_logbook(self, logbook_id, signature, status, warnings, errors, criticals, remarks):
        if self.is_ready():
            logbooks_update = fs.join(GhostbotProfile.assets_queries_scheduler, self.LOGBOOKS_UPDATE)
            if fs.exists(logbooks_update):
                db = Database(RDBMS.SQLITE)
                conn = db.open(self._dsn)
                with conn.cursor() as cursor:
                    now = Datetime.now(to_string=True)
                    params = {
                        "id": logbook_id,
                        "arrival_at": now,
                        "status": status,
                        "warnings": warnings,
                        "errors": errors,
                        "criticals": criticals,
                        "remarks": remarks,
                        "updated_by": fs.file(__file__),
                        "updated_at": now
                    }
                    if cursor.execute(db.load(logbooks_update), params) == 1:
                        self.logger.info(StatusCode[161], signature, logbook_id)
                    else:
                        self.error(StatusCode[553], signature, "logbooks")
                conn.close()
            else:
                self.error(StatusCode[551], self.LOGBOOKS_UPDATE)
        else:
            self.error(StatusCode[530], __name__)
