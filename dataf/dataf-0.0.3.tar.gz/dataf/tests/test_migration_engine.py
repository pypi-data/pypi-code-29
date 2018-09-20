#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Test migration engine
---------------------

Test suite for migration_engine.

"""

import os
from unittest import TestCase, mock
from datetime import datetime

from alembic.config import Config
from alembic.script import ScriptDirectory

from dataf import MigrationEngine, DatabaseManager, BaseEntity
from dataf.tests import settings


class TestMigrationEngine(TestCase):
    """
    Tests for MigrationEngine.
    """
    @classmethod
    def setUpClass(cls):
        cls.migration_dir = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'migration'
        )
        cls.db = DatabaseManager(settings.DATABASE['test'])
        cls.me = MigrationEngine(cls.db, cls.migration_dir)

    def test_init_(self):
        """
        Test class __init__ method.
        """
        self.assertEqual(self.me.db, self.db)
        self.assertEqual(self.me.migration_dir, self.migration_dir)
        self.assertEqual(
            self.me.config_path, os.path.join(self.migration_dir, 'alembic.ini')
        )
        self.assertIsInstance(self.me.config, Config)
        self.assertIsInstance(self.me.script, ScriptDirectory)
        self.assertEqual(
            self.me.config.get_main_option('script_location'),
            self.migration_dir
        )

    def test_tables(self):
        """
        Test tables attributes.
        """
        self.assertEqual(self.me.tables, BaseEntity.__subclasses__())

    @mock.patch('dataf.migration_engine.MigrationEngine.init')
    def test_run(self, init_mock):
        """
        Test run method correctly call class method with name passed in params.
        """
        self.me.run('init')
        init_mock.assert_called_with(None)

    @mock.patch('dataf.migration_engine.MigrationEngine.upgrade')
    def test_init(self, up_mock):
        """
        Test init method
        """
        self.me.init(None)
        up_mock.assert_called_with(None)

    @mock.patch('dataf.migration_engine.command.revision', return_value='ret')
    def test_revision(self, cmd_mock):
        """
        Test revision method.
        """
        ret = self.me.revision()
        cmd_mock.assert_called_with(
            self.me.config,
            message=datetime.now().strftime("%Y-%m-%d_%H:%M"),
            autogenerate=True
        )
        self.assertEqual(ret, 'ret')

    @mock.patch('dataf.migration_engine.command.upgrade')
    def test_upgrade_with_revision(self, cmd_mock):
        """
        Test upgrade method with a given revision.
        """
        revision = 'revision123'
        self.me.upgrade(revision)
        cmd_mock.assert_called_with(self.me.config, revision)

    @mock.patch('dataf.migration_engine.command.upgrade')
    def test_upgrade_without_revision(self, cmd_mock):
        """
        Test upgrade method without revision.
        """
        self.me.upgrade(None)
        cmd_mock.assert_called_with(
            self.me.config, self.me.script.get_current_head()
        )

    @mock.patch('dataf.migration_engine.command.downgrade')
    def test_downgrade_with_revision(self, cmd_mock):
        """
        Test downgrade method with a given revision.
        """
        revision = 'revision123'
        self.me.downgrade(revision)
        cmd_mock.assert_called_with(self.me.config, revision)

    @mock.patch('dataf.migration_engine.command.downgrade')
    def test_downgrade_without_revision(self, cmd_mock):
        """
        Test downgrade method without revision.
        """
        self.me.downgrade(None)
        cmd_mock.assert_called_with(
            self.me.config, self.me.script.get_base()
        )

    @mock.patch('dataf.migration_engine.command.heads')
    def test_heads(self, heads_mock):
        """
        Test heads method.
        """
        self.me.heads()
        heads_mock.assert_called_with(self.me.config, verbose=True)

    @mock.patch('dataf.migration_engine.BaseEntity.exists', return_value=True)
    @mock.patch('dataf.migration_engine.BaseEntity.drop')
    @mock.patch('sqlalchemy.engine.Engine.execute')
    @mock.patch('dataf.migration_engine.MigrationEngine.downgrade')
    def test_drop(self, down_mock, exec_mock, drop_mock, exists_mock):
        """
        Test drop method.
        """
        with self.assertLogs(self.me.logger, level='INFO') as logs:
            self.me.drop()
        self.assertEqual(
            logs.output,
            ['INFO:dataf.migration_engine:Drop all tables and schemas done.']
        )
        down_mock.assert_called_with(None)
        exec_mock.assert_called_with('DROP TABLE IF EXISTS public.alembic_version')
        self.assertEqual(drop_mock.call_count, len(self.me.tables))
        self.assertEqual(exists_mock.call_count, len(self.me.tables))

    @mock.patch('dataf.migration_engine.BaseEntity.drop')
    def test_drop_table(self, drop_mock):
        """
        Test drop table.
        """
        table_name = self.me.tables[0].__table__.name
        with self.assertLogs(self.me.logger, level='INFO') as logs:
            self.me.drop_table(table_name)
        self.assertEqual(
            logs.output,
            ['INFO:dataf.migration_engine:Table {} dropped.'.format(table_name)]
        )
        drop_mock.assert_called_once_with(self.me.db)

    @mock.patch('dataf.migration_engine.BaseEntity.create')
    def test_create_table(self, create_mock):
        """
        Test create table.
        """
        table_name = self.me.tables[0].__table__.name
        with self.assertLogs(self.me.logger, level='INFO') as logs:
            self.me.create_table(table_name)
        self.assertEqual(
            logs.output,
            ['INFO:dataf.migration_engine:Table {} created.'.format(table_name)]
        )
        create_mock.assert_called_once_with(self.me.db)
