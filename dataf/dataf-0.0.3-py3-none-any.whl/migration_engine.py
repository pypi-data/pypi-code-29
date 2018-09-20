#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Migration engine
----------------

Engine for database migration.

"""

import os
import logging
from datetime import datetime

from alembic import command
from alembic.config import Config
from alembic.script import ScriptDirectory

from dataf import simple_logger, lambda_logger, BaseEntity


class MigrationEngine:
    """
    Handle database migration.

    :param obj db: DatabaseManager to the database to manipulate.
    :param str migration_dir: absolute path of alembic migration directory.
    :param str config_path: absolute path of alembic.ini file,
        default: migration_dir/alembic.ini
    """
    def __init__(self, db, migration_dir, config_path=None):
        self.db = db
        self.migration_dir = migration_dir
        self.config_path = config_path or os.path.join(migration_dir, 'alembic.ini')
        self.logger = logging.getLogger(__name__)
        self.config = Config(self.config_path)
        self.config.set_main_option('script_location', self.migration_dir)
        self.script = ScriptDirectory.from_config(self.config)

    @property
    def tables(self):
        return BaseEntity.__subclasses__()

    _command_annotation = [
        'init', 'drop', 'revision', 'upgrade', 'downgrade',
        'heads', 'create_table', 'drop_table'
    ]
    def run(self, command: _command_annotation, revision=None):
        """
        Powerpot database migration.

        :param str command: command to execute.
        :param str revision: migration revision code.
        """
        getattr(self, command)(revision)

    def init(self, revision):
        """
        Init a clean database.

        :param str revision: migration revision name to happend.
        """
        self.upgrade(revision)

    def revision(self, *_):
        """
        Create a revision, happen current date to revision name.

        :return: revision result.
        """
        message = datetime.now().strftime("%Y-%m-%d_%H:%M")
        result = command.revision(
            self.config, message=message, autogenerate=True
        )
        return result

    def upgrade(self, revision):
        """
        Update database with given revision.

        :param str revision: migration revision code to update, default to head.
        """
        revision = revision or self.script.get_current_head()
        command.upgrade(self.config, revision)

    def downgrade(self, revision):
        """
        Rollback database to given revision.

        :param str revision: migration revision code to rollback, default to base.
        """
        revision = revision or self.script.get_base()
        command.downgrade(self.config, revision)

    def heads(self, *_):
        """
        Show current available revision heads.
        """
        command.heads(self.config, verbose=True)

    @simple_logger('info', end='Drop all tables and schemas done.')
    def drop(self, *_):
        """
        Drop all tables and schemas in powerpot.
        """
        self.downgrade(None)
        [table.drop(self.db) for table in self.tables if table.exists(self.db)]
        self.db.engine.execute('DROP TABLE IF EXISTS public.alembic_version')

    @lambda_logger('info', end=lambda table, cls: 'Table {} dropped.'.format(table))
    def drop_table(self, table):
        """
        Drop a table.

        :param str table: table name.
        """
        next(filter(lambda x: x.__table__.name == table, self.tables)).drop(self.db)

    @lambda_logger('info', end=lambda table, cls: 'Table {} created.'.format(table))
    def create_table(self, table):
        """
        Create a table.

        :param str table: table name.
        """
        next(filter(lambda x: x.__table__.name == table, self.tables)).create(self.db)

