#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Test base entity
----------------

Test suite for base_entity.

"""

from unittest import TestCase

from sqlalchemy import inspect, Column, Integer

from dataf import EmptyEntity, BaseEntity


class EmptyEntityTest(EmptyEntity):
    test = Column(Integer, primary_key=True)


class BaseEntityTest(BaseEntity): pass


class TestEmptyEntity(TestCase):
    """
    Test EmptyEntity class.
    """
    def test_class_attr(self):
        """
        Test class does not have any fields.
        """
        # print(EmptyEntity.__dict__)
        i = inspect(EmptyEntityTest)
        self.assertEqual(len(i.attrs), 1)
        self.assertIn('test', i.attrs)

    def test_tablename_attr(self):
        """
        Test tablename attr.
        """
        self.assertEqual(
            EmptyEntityTest.__table__.name, EmptyEntityTest.__name__.lower()
        )


class TestBaseEntity(TestCase):
    """
    Test BaseEntity class.
    """
    def test_class_attr(self):
        """
        Test class have a primary key 'id'.
        """
        i = inspect(BaseEntityTest)
        self.assertEqual(len(i.attrs), 1)
        self.assertIn('id', i.attrs)

    def test_tablename_attr(self):
        """
        Test tablename attr.
        """
        self.assertEqual(
            BaseEntityTest.__table__.name, BaseEntityTest.__name__.lower()
        )
