#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Database singleton
------------------

Singleton who store a database manager.

"""

from dataf import DatabaseManager


class DatabaseSingleton:
    """
    Singleton for database manager.
    Use this class like a DatabaseManager.

    :attr instance: _DatabaseSingleton instance.
    """
    class _DatabaseSingleton:
        def __init__(self, db):
            self.db = db

    _instance = None

    def __init__(self, configuration, *, url=None, prefix='', **kwargs):
        """
        Init DatabaseManager if not exists.

        :param dict configuration: engine configuration.
        :param str prefix: prefix to match and then strip from keys in
            ‘configuration’, default to ''.
        :param dict kwargs: each keyword argument overrides the corresponding
            item taken from the ‘configuration’ dictionary.
            Keyword arguments should not be prefixed
        """
        if not DatabaseSingleton._instance:
            DatabaseSingleton._instance = DatabaseSingleton._DatabaseSingleton(
                DatabaseManager(configuration, url=url, prefix=prefix, **kwargs)
            )

    def __getattr__(self, name):
        """
        Access DatabaseManager attr.

        :param str name: attr name.
        """
        return getattr(self._instance.db, name)
