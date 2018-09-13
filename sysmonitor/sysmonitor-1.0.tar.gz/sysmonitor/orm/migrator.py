"""SysMonitor Database migration tool"""

import logging
import os
import importlib
import re
import ast

from playhouse.db_url import connect

from sysmonitor.configuration import Configuration
from sysmonitor import release

from sysmonitor.models.database import DatabaseVariable
from sysmonitor.models.host import Host, Disk, Resource, Service, ServiceHistory

LOGGER = logging.getLogger(__name__)

class Migrator():
    """
    Migration Tool

    It executes migration scriptsw when needed.

    This scripts must be located inside a file named migrate.py, under a
    folder with the target version as name and inside the migrations folder.
    Example for a migration targeting version 1.0.0:
        migrations/1.0.1/migrate.py

    Inside the file, the migration code mut be inside a function called migrate
    and it receives one argument, the database object
    """
    def __init__(self):
        self.config = Configuration()
        self.database = connect(self.config.get("database", "url"))

    def do_migration(self):
        """
        Execute the migration.

        If no tables exists, it runs peewee create_table method.
        If tables exists, it runs the necessar migration scripts
        """
        self.database.connect()
        if self.database.get_tables():
            self.upgrade()
        else:
            self.create()
        self.update_version()

    def create(self):
        """Create tables using peewee create_tables method"""
        self.database.create_tables([DatabaseVariable, Host, Disk, Resource,
                                     Service, ServiceHistory])
        LOGGER.info("Created tables")
        uname = os.uname()
        Host.create(name=uname.nodename, address="http://127.0.0.1:8068",
                    requires_authentication=False, active=False,
                    nodename=uname.nodename, os=" ".join(uname))
        LOGGER.info("Created a host for this machine")

    def upgrade(self):
        """Executes migration scripts"""
        # Check if upgrade is required
        db_version = ast.literal_eval(DatabaseVariable.get_variable("version"))
        if db_version >= release.version_db:
            LOGGER.debug("Database in version %s. Nothing to do.",
                         ".".join([str(x) for x in release.version_db]))
            return

        # Load all available migrations
        migrations_path = os.path.dirname(os.path.abspath(__file__))
        migrations_path = os.path.join(migrations_path, "migrations")
        migrations = set()
        for migration in os.listdir(migrations_path):
            # Migration folder must be in format x.x.x
            if not re.match(r"^\d.\d.\d$", migration):
                LOGGER.error("Invalid migration %s", migration)
                continue
            migration = [int(x) for x in migration.split(".")]
            migrations.add(tuple(migration))

        # Discard previous migrations and do a sort
        migrations = sorted([x for x in migrations if x > db_version])

        # Executes the required migrations
        for migration in migrations:
            migration_str = ".".join([str(x) for x in migration])
            migration_file = os.path.join(migrations_path, migration_str,
                                          "migrate.py")
            spec = importlib.util.spec_from_file_location(migration_str,
                                                          migration_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            LOGGER.info("Upgrading database to version %s", migration_str)
            module.migrate(self.database)
            self.update_version(migration)
            LOGGER.info("Database migrated to version %s", migration_str)

    @staticmethod
    def update_version(version=False):
        """
        Update database migration

        :param tuple version: New version. If false uses release.version_db
        """
        version = release.version_db if not version else version
        DatabaseVariable.set_variable("version", version)
