#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Test database singleton
-----------------------

Test suite for database_singleton.

"""

import unittest

from sqlalchemy.engine.base import Engine

from dataf import DatabaseSingleton
from dataf.tests import settings


class TestDatabaseSingleton(unittest.TestCase):
    """
    Test for DatabaseSingleton class.
    """
    # __INIT__
    def test_init(self):
        """
        Test class constructor create instance only one time.
        """
        instance1 = DatabaseSingleton(settings.DATABASE['test'])
        instance2 = DatabaseSingleton(settings.DATABASE['test'])

        self.assertIsInstance(instance1._instance, DatabaseSingleton._DatabaseSingleton)
        self.assertIs(instance1._instance, instance2._instance)

    # __GETATTR__
    def test_getattr(self):
        """
        Test getattr.
        """
        instance = DatabaseSingleton(settings.DATABASE['test'])
        self.assertIsInstance(instance.engine, Engine)
        self.assertTrue(callable(instance.session))
