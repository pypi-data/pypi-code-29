from ghostbot import Ghostbot, GhostbotProfile, StatusCode
from ghostbot.core import Basis, Service
from ghostbot.utils.logger import Logger
from ghostbot.utils.os import Hash, FileSystem as fs
from ghostbot.utils.datetime import Datetime
from ghostbot.utils.database import RDBMS, Database


class Repository(Basis, Service):
    DATABASE = "repository.db"
    DDL = "ddl/repository.sql"
    ACTIVATES_INSERT = "dml/activates_insert.sql"
    ACTIVATES_UPDATE = "dml/activates_update.sql"
    PROJECTS_INSERT = "dml/projects_insert.sql"
    PROJECTS_DELETE = "dml/projects_delete.sql"
    PROJECTS_SELECT = "dql/projects_select.sql"
    SCAFFOLDS_INSERT = "dml/scaffolds_insert.sql"
    SIGNATURE = "{}@{}"

    def __init__(self):
        super().__init__()
        self.logger = Logger(__name__)
        self._dsn = fs.join(GhostbotProfile.assets_database, self.DATABASE)

    def startup(self):
        pass

    def shutdown(self):
        pass

    def is_ready(self):
        if not fs.exists(self._dsn):
            ddl = fs.join(GhostbotProfile.assets_queries_repository, self.DDL)
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

    def signature(self, name, home):
        hash_code = Hash.digest(home + Datetime.now(to_string=True), digit=6)
        return self.SIGNATURE.format(name, hash_code)

    def active_project(self):
        if self.is_ready():
            projects_select = fs.join(GhostbotProfile.assets_queries_repository, self.PROJECTS_SELECT)
            if fs.exists(projects_select):
                db = Database(RDBMS.SQLITE)
                conn = db.open(self._dsn)
                with conn.cursor() as cursor:
                    args = {"page_offset": 0, "page_limit": 1}
                    row = cursor.query(db.load(projects_select), args).fetchone()
                    if row:
                        Ghostbot.signature(row["signature"])
                        Ghostbot.project_name(row["project_name"])
                        Ghostbot.project_home(row["project_home"])
                    else:
                        self.error(StatusCode[534])
                conn.close()
            else:
                self.error(StatusCode[533], self.PROJECTS_SELECT)
        else:
            self.error(StatusCode[530], __name__)

    def fetch_project(self, page_offset=0, page_limit=-1):
        result = None
        if self.is_ready():
            projects_select = fs.join(GhostbotProfile.assets_queries_repository, self.PROJECTS_SELECT)
            if fs.exists(projects_select):
                db = Database(RDBMS.SQLITE)
                conn = db.open(self._dsn)
                with conn.cursor() as cursor:
                    args = {"page_limit": page_limit, "page_offset": page_offset}
                    result = cursor.query(db.load(projects_select), args).fetchall()
                conn.close()
            else:
                self.error(StatusCode[533], self.PROJECTS_SELECT)
        else:
            self.error(StatusCode[530], __name__)
        return result

    def append_project(self, project_name, project_home, schema_version, location):
        result = None
        if self.is_ready():
            projects_insert = fs.join(GhostbotProfile.assets_queries_repository, self.PROJECTS_INSERT)
            activates_insert = fs.join(GhostbotProfile.assets_queries_repository, self.ACTIVATES_INSERT)
            if fs.exists(projects_insert) and fs.exists(activates_insert):
                db = Database(RDBMS.SQLITE)
                conn = db.open(self._dsn)
                with conn.cursor() as cursor:
                    signature = self.signature(project_name, project_home)
                    now = Datetime.now(to_string=True)
                    params = {
                        "signature": signature,
                        "project_name": project_name,
                        "project_home": project_home,
                        "schema_version": schema_version,
                        "location": location,
                        "last_contact": now,
                        "created_by": fs.file(__file__),
                        "created_at": now
                    }
                    sql = [db.load(projects_insert), db.load(activates_insert)]
                    if cursor.execute(sql, params) == 1:
                        self.logger.info(StatusCode[140], project_name, signature)
                        result = signature
                    else:
                        self.error(StatusCode[532], project_name, signature, "projects")
                conn.close()
            else:
                self.error(StatusCode[533], ",".join([self.PROJECTS_INSERT, self.ACTIVATES_INSERT]))
        else:
            self.error(StatusCode[530], __name__)
        return result

    def remove_project(self, signature):
        if self.is_ready():
            projects_delete = fs.join(GhostbotProfile.assets_queries_repository, self.PROJECTS_DELETE)
            if fs.exists(projects_delete):
                db = Database(RDBMS.SQLITE)
                conn = db.open(self._dsn)
                with conn.cursor() as cursor:
                    params = {"signature": signature}
                    if cursor.execute(db.load(projects_delete), params) == 1:
                        self.logger.info(StatusCode[141], signature)
                    else:
                        self.error(StatusCode[532], signature)
                conn.close()
            else:
                self.error(StatusCode[533], self.PROJECTS_DELETE)
        else:
            self.error(StatusCode[530], __name__)

    def activate_project(self, signature):
        if self.is_ready():
            activates_update = fs.join(GhostbotProfile.assets_queries_repository, self.ACTIVATES_UPDATE)
            if fs.exists(activates_update):
                db = Database(RDBMS.SQLITE)
                conn = db.open(self._dsn)
                with conn.cursor() as cursor:
                    now = Datetime.now(to_string=True)
                    params = {
                        "signature": signature,
                        "last_contact": now,
                        "updated_by": fs.file(__file__),
                        "updated_at": now
                    }
                    if cursor.execute(db.load(activates_update), params) == 1:
                        self.logger.info(StatusCode[142], signature)
                    else:
                        self.error(StatusCode[532], signature)
                conn.close()
            else:
                self.error(StatusCode[533], self.ACTIVATES_UPDATE)
        else:
            self.error(StatusCode[530], __name__)

    def append_class(self, signature, scaffold, class_name, file_name):
        if self.is_ready():
            scaffolds_insert = fs.join(GhostbotProfile.assets_queries_repository, self.SCAFFOLDS_INSERT)
            if fs.exists(scaffolds_insert):
                db = Database(RDBMS.SQLITE)
                conn = db.open(self._dsn)
                with conn.cursor() as cursor:
                    now = Datetime.now(to_string=True)
                    params = {
                        "signature": signature,
                        "scaffold": scaffold,
                        "class_name": class_name,
                        "file_name": file_name,
                        "created_by": fs.file(__file__),
                        "created_at": now
                    }
                    if cursor.execute(db.load(scaffolds_insert), params) == 1:
                        self.logger.info(StatusCode[142], signature)
                    else:
                        self.error(StatusCode[532], signature)
                conn.close()
            else:
                self.error(StatusCode[533], self.ACTIVATES_UPDATE)
        else:
            self.error(StatusCode[530], __name__)
