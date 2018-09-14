#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Abstract entity
---------------

"""

from dataf import classproperty


class ABCEntity:
    """
    Abstract entity to represent table schema.
    Contains base method to handle table.
    """
    def __str__(self):
        """
        return all class attr when printing object.
        """
        return ", ".join(
            "{}: {}".format(key, value) for key, value in self.__dict__.items()
        )

    @classmethod
    def create(cls, db):
        """
        Create table in database.

        :param obj db: DatabaseManager.
        :return: cls object.
        """
        cls.__table__.create(db.engine)
        return cls

    @classmethod
    def drop(cls, db):
        """
        Drop table in database.

        :param obj db: DatabaseManager.
        :return: cls object.
        """
        cls.__table__.drop(db.engine)
        return cls

    @classmethod
    def exists(cls, db):
        """
        Check if tables exists in database.

        :param obj db: DatabaseManager.
        :return: True if exists otherwise False.
        """
        return cls.__table__.exists(db.engine)

    @classproperty
    def pk(cls):
        """
        Get the first primary key column object.

        :return: primary key column object.
        """
        return cls.__table__.primary_key.columns.values()[0]

    @classproperty
    def keys(cls):
        """
        Get all column names except the primary key.

        :return: list of column names as string.
        """
        return list(filter(cls.pk.name.__ne__, cls.c.keys()))

    @classproperty
    def relationships(cls):
        """
        Get all relationship columns.

        :return: list of column names as string.
        """
        return [elem.key for elem in cls.__mapper__.relationships]

    @classproperty
    def c(cls):
        """
        Get all column objects.

        :return: collection of column as sqlalchemy.sql.base.ImmutableColumnCollection
            use it like a dict, key: column name, value: column object.
        """
        return cls.__table__.c
