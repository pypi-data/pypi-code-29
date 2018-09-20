#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Test abc entity
---------------

Test suite for abc_entity.

"""

from unittest import TestCase, mock

from sqlalchemy import Column, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.base import ImmutableColumnCollection

from dataf import BaseEntity, DatabaseManager
from dataf.tests import settings


class Entity(BaseEntity): pass


class EntityWithField(BaseEntity):
    text = Column(Text)


class EntityWithRelationship(BaseEntity):
    rel = relationship('EntityWithFk')


class EntityWithFk(BaseEntity):
    fk = Column(Integer, ForeignKey(EntityWithRelationship.id))


class TestABCEntity(TestCase):
    """
    Test for ABCEntity class.
    """
    @classmethod
    def setUpClass(cls):
        cls.db = DatabaseManager(settings.DATABASE['test'])

    def test_str(self):
        """
        Test repr method.
        """
        entity = Entity()
        entity_str = ", ".join(
            "{}: {}".format(key, value) for key, value in entity.__dict__.items()
        )
        self.assertEqual(entity.__str__(), entity_str)

    @mock.patch('sqlalchemy.schema.Table.create')
    def test_create(self, mock):
        """
        Test create method.
        """
        ret = Entity.create(self.db)
        mock.assert_called_with(self.db.engine)
        self.assertEqual(ret, Entity)

    @mock.patch('sqlalchemy.schema.Table.drop')
    def test_drop(self, mock):
        """
        Test drop method.
        """
        ret = Entity.drop(self.db)
        mock.assert_called_with(self.db.engine)
        self.assertEqual(ret, Entity)

    @mock.patch('sqlalchemy.schema.Table.exists', return_value=True)
    def test_exists(self, mock):
        """
        Test exists method.
        """
        ret = Entity.exists(self.db)
        mock.assert_called_with(self.db.engine)
        self.assertTrue(ret)

    def test_pk(self):
        """
        Test pk method.
        """
        self.assertEqual(
            Entity.pk, Entity.__table__.primary_key.columns.values()[0]
        )

    def test_keys(self):
        """
        Test keys method.
        """
        self.assertEqual(Entity.keys, [])
        self.assertEqual(EntityWithField.keys, ['text'])
        self.assertEqual(EntityWithRelationship.keys, [])
        self.assertEqual(EntityWithFk.keys, ['fk'])

    def test_relationships(self):
        """
        Test relationships method.
        """
        self.assertEqual(Entity.relationships, [])
        self.assertEqual(EntityWithRelationship.relationships, ['rel'])
        self.assertEqual(EntityWithFk.relationships, [])

    def test_c(self):
        """
        Test c method.
        """
        self.assertIsInstance(Entity.c, ImmutableColumnCollection)
        self.assertEqual(Entity.c.keys(), ['id'])
        self.assertEqual(EntityWithField.c.keys(), ['id', 'text'])
        self.assertEqual(EntityWithRelationship.c.keys(), ['id'])
        self.assertEqual(EntityWithFk.c.keys(), ['id', 'fk'])
