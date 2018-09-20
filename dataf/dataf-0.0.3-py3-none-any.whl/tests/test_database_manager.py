#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Test database manager
---------------------

Test suite for database_manager.

"""

from unittest import TestCase, mock

from sqlalchemy import Column, Text, Table, create_engine, engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import Session

from dataf import DatabaseManager, BaseEntity
from dataf.tests import settings


class EntityTest(BaseEntity):
    """
    Entity test class.
    """
    text = Column(Text)
    __table_args__ = {'schema': 'TestDatabaseManager'}


class NonExistingEntity(BaseEntity): pass


class TestDatabaseManager(TestCase):
    """
    Test for DatabaseManager class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Called before all tests in class.
        """
        cls.db = DatabaseManager(settings.DATABASE['test'])
        cls.db.create_schema(cls.__name__)

    @classmethod
    def tearDownClass(cls):
        """
        Called after all tests in class.
        """
        cls.db.drop_schema(cls.__name__)

    def setUp(self):
        """
        Method called before every tests to prepare test fixtures.
        """
        EntityTest.create(self.db)

    def tearDown(self):
        """
        Method called after every tests.
        """
        # Clean database in case of test crash
        if EntityTest.exists(self.db):
            EntityTest.drop(self.db)
        if self.db.schema_exists('test_schema') is True:
            self.db.drop_schema("test_schema")

    # __INIT__
    def test_init_attr(self):
        """
        Test if __init__ create engine link to our database.
        """
        self.assertIsInstance(self.db.engine, Engine)
        self.assertIsInstance(self.db.Session, scoped_session)

    def test_init_with_bad_database_info(self):
        """
        Test if __init__ raise exception with bad database info.
        """
        with self.assertRaises(Exception) as cm:
            DatabaseManager(settings.DATABASE['test'], database='bad_database')

        self.assertEqual(cm.exception.message, 'Failed to connect to database')
        self.assertEqual(cm.exception.logger.name, DatabaseManager.__module__)

        with self.assertRaises(Exception):
            DatabaseManager(None)

    def test_init_with_url_arg(self):
        """
        Test __init__ method with url argument.
        """
        url = {
            'drivername': 'postgresql',
            'username': 'admin',
            'password': 'password',
            'host': 'localhost',
            'port': 5432,
            'database': 'test'
        }
        db = DatabaseManager({'url': 'bad_url'}, url=url)
        self.assertEqual(db.engine.url, engine.url.URL(**url))

    # DATABASE_EXISTS
    def test_database_exists(self):
        """
        Test if database exists return True with good database.
        """
        self.assertTrue(self.db._database_exists())

    def test_database_exists_with_bad_database_info(self):
        """
        Test if database_exists raise exception with bad database.
        """
        db = DatabaseManager(settings.DATABASE['test'])
        db.engine = create_engine(
            'postgresql://username:password@localhost:5432/database'
        )
        with self.assertRaises(Exception):
            db._database_exists()

    # SESSION
    def test_session(self):
        """
        Test session yield a Session Object.
        """
        with self.db.session() as session:
            self.assertIsInstance(session, Session)

    def test_session_with_bad_query(self):
        """
        Test if session rollback with bad query.
        """
        with self.assertRaises(Exception):
            with self.db.session(raise_err=True) as session:
                session.query(None).all()

    @mock.patch('sqlalchemy.orm.session.Session.rollback')
    def test_session_without_raise_err(self, mock):
        """
        Test session with raise_err at False.
        """
        with self.db.session(raise_err=False) as session:
            session.delete(EntityTest(id=1))
        mock.assert_called_with()

    @mock.patch('sqlalchemy.orm.scoping.scoped_session.configure')
    def test_session_with_session_config(self, mock):
        """
        Test session with session_config.
        """
        self.db.Session.registry.clear()
        config = {
            'autocommit': True,
            'expire_on_commit': True
        }
        with self.db.session(session_config=config):
            pass
        mock.assert_called_with(**config)

    # CREATE_SCHEMA
    def test_create_schema(self):
        """
        Test create_schema.
        """
        self.db.create_schema("test_schema")
        result = self.db.schema_exists('test_schema')
        self.assertTrue(result)
        self.db.drop_schema("test_schema")

    def test_create_schema_already_exists(self):
        """
        Test create_schema with schema already exists.
        """
        self.db.create_schema("test_schema")

        with self.assertRaises(Exception):
            self.db.create_schema("test_schema")

        self.db.drop_schema("test_schema")

    # DROP_SCHEMA
    def test_drop_schema(self):
        """
        Test drop_schema.
        """
        self.db.create_schema("test_schema")
        self.db.drop_schema("test_schema")
        result = self.db.schema_exists('test_schema')
        self.assertFalse(result)

    def test_drop_schema_not_exists(self):
        """
        Test drop_schema with schema who doesnt exists.
        """
        with self.assertRaises(Exception):
            self.db.drop_schema("test_schema")

    # SCHEMA_EXISTS
    def test_schema_exists(self):
        """
        Test schema exists with existing schema.
        """
        self.db.create_schema('test_schema')
        result = self.db.schema_exists('test_schema')
        self.assertTrue(result)

    def test_schema_exists_with_bad_schema(self):
        """
        Test schema exists with non existing schema.
        """
        result = self.db.schema_exists('test_schema')
        self.assertFalse(result)

    # ADD
    def test_add(self):
        """
        Test add.
        """
        entity = EntityTest(id=1)
        self.db.add(entity)

        with self.db.session() as session:
            result = session.query(EntityTest).get(1)

        self.assertIsNotNone(result)
        self.assertEqual(result.id, 1)

    def test_add_with_bad_data(self):
        """
        Test add with bad data.
        """
        with self.assertRaises(Exception):
            self.db.add(None)

    # ADD_ALL
    def test_add_all(self):
        """
        Test add_all.
        """
        entity_list = [EntityTest(id=count) for count in range(100)]
        self.db.add_all(entity_list)

        with self.db.session() as session:
            result = session.query(EntityTest).all()

        self.assertEqual(len(result), len(entity_list))

    def test_add_all_with_bad_data(self):
        """
        Test add_all with bad data.
        """
        with self.assertRaises(Exception):
            self.db.add_all([None, None])

    # READ
    def test_read(self):
        """
        Test read.
        """
        entity = EntityTest(id=1)
        self.db.add(entity)
        result = self.db.read(EntityTest)

        self.assertIsInstance(result[0], EntityTest)
        self.assertEqual(result[0].id, 1)

    def test_read_with_bad_table(self):
        """
        Test read on table who doesnt exists.
        """
        with self.assertRaises(Exception):
            self.db.read(None)

    # DELETE
    def test_delete(self):
        """
        Test delete.
        """
        entity = EntityTest(id=1)
        self.db.add(entity)
        self.db.delete(entity)
        result = self.db.read(EntityTest)
        self.assertEqual(result, [])

    def test_delete_with_bad_data(self):
        """
        Test delete with data who doesnt exists.
        """
        entity = EntityTest(id=1)
        with self.assertRaises(Exception):
            self.db.delete(entity)

    @mock.patch('sqlalchemy.orm.session.Session.flush')
    @mock.patch('sqlalchemy.orm.session.Session.delete')
    @mock.patch('sqlalchemy.orm.session.Session.merge', return_value='merge_return')
    def test_delete_with_merge(self, mock_merge, mock_del, _):
        """
        Test delete method with merge True.
        """
        entity = EntityTest(id=1)
        self.db.delete(entity, merge=True)
        mock_merge.assert_called_with(entity)
        mock_del.assert_called_with('merge_return')

    # MAP_TABLE
    def test_map_tables(self):
        """
        Tes map_tables.
        """
        table = self.db.map_tables(
            [EntityTest.__tablename__], schema=EntityTest.__table_args__['schema']
        )[0]
        self.assertEqual(
            str(table.__table__),
            "{}.{}".format(
                EntityTest.__table_args__['schema'], EntityTest.__tablename__
            )
        )

    def test_map_tables_with_bad_table(self):
        """
        Test map_tables with table who doesnt exists.
        """
        with self.assertRaises(Exception):
            self.db.map_tables(['bad_table_name'])

    def test_create_table_obj_without_autoload(self):
        """
        Test create_table_obj without autoload.
        """
        table = self.db.create_table_obj(
            'table_test', autoload=False
        )
        self.assertIsInstance(table, Table)

    def test_create_table_obj_with_autoload(self):
        """
        Test create_table_obj without autoload.
        """
        table = self.db.create_table_obj('entitytest', schema=self.__class__.__name__)
        self.assertIn('text', table.c)

    def test_create_table_obj_on_bad_table(self):
        """
        Test create_table_obj on non existing table.
        """
        with self.assertRaises(Exception):
            self.db.create_table_obj('table_test')

    # ENTITY_EXISTS
    def test_entity_exists(self):
        """
        Test entity_exists with existing entity.
        """
        entity = EntityTest(id=1)
        self.db.add(entity)
        result = self.db.entity_exists([EntityTest.id == entity.id])
        self.assertTrue(result)

    def test_entity_exists_with_multiple_filter(self):
        """
        Test entity_exists with multiple filter.
        """
        entity = EntityTest(id=1, text='test')
        self.db.add(entity)
        result = self.db.entity_exists(
            [EntityTest.id == entity.id, EntityTest.text == entity.text]
        )
        self.assertTrue(result)

    def test_entity_exists_with_non_existing_data(self):
        """
        Test entity_exists with non existing entity.
        """
        result = self.db.entity_exists([EntityTest.id == 1])
        self.assertFalse(result)

    def test_entity_exists_error(self):
        """
        Test entity_exists on non existing table.
        """
        with self.assertRaises(Exception):
            self.db.entity_exists(None)

    # UPDATE
    def test_update(self):
        """
        Test update.
        """
        entity = EntityTest(id=1, text='test')
        self.db.add(entity)
        self.db.update(EntityTest(id=1, text='test_update'), ['text'])

        with self.db.session() as session:
            result = session.query(EntityTest).get(1)

        self.assertEqual(result.text, 'test_update')

    def test_update_with_bad_table(self):
        """
        Test update with bad table.
        """
        EntityTest.drop(self.db)
        with self.assertRaises(Exception):
            self.db.update(EntityTest(id=1, text='test'), ['text'])

    def test_update_with_bad_data(self):
        """
        Test update with bad data.
        """
        self.db.add(EntityTest(id=1, text='test'))
        with self.assertRaises(Exception):
            self.db.update(EntityTest(id=1, text='test_update'), ['error'])

    # BULK OP
    def test_bulk_insert_mappings(self):
        """
        Test bulk_insert_mappings.
        """
        data = [
            {'text': 'text1'},
            {'text': 'text2'},
        ]
        self.db.bulk_insert_mappings(EntityTest, data)
        with self.db.session() as session:
            result = session.query(EntityTest).all()

        self.assertEqual(len(result), len(data))

    def test_bulk_insert_mappings_with_bad_table(self):
        """
        Test bulk_insert_mappings with non existing table.
        """
        with self.assertRaises(Exception):
            self.db.bulk_insert_mappings(NonExistingEntity, [{'text': 'text1'}])

    def test_bulk_save_objects(self):
        """
        Test bulk_save_objects.
        """
        data = [
            EntityTest(text='text1'),
            EntityTest(text='text2'),
        ]
        self.db.bulk_save_objects(data)
        with self.db.session() as session:
            result = session.query(EntityTest).all()

        self.assertEqual(len(result), len(data))

    def test_bulk_save_objects_return_defaults(self):
        """
        Test bulk_save_objects with return defaults.
        """
        data = [
            EntityTest(text='text1'),
            EntityTest(text='text2'),
        ]
        self.db.bulk_save_objects(data, return_defaults=True)
        self.assertEqual(data[0].id, 1)

    def test_bulk_save_objects_with_bad_table(self):
        """
        Test bulk_save_objects with non existing table.
        """
        with self.assertRaises(Exception):
            self.db.bulk_save_objects([NonExistingEntity()])

    def test_bulk_insert_mappings_core(self):
        """
        Test bulk_insert_mappings_core.
        """
        data = [
            {'text': 'text1'},
            {'text': 'text2'},
        ]
        self.db.bulk_insert_mappings_core(EntityTest, data)
        with self.db.session() as session:
            result = session.query(EntityTest).all()

        self.assertEqual(len(result), len(data))

    @mock.patch('sqlalchemy.orm.session.Session.execute')
    def test_bulk_insert_mappings_core_chunk(self, mock):
        """
        Test bulk_insert_mappings_core chunk corectly.
        """
        data = [
            {'text': 'text1'},
            {'text': 'text2'},
            {'text': 'text3'},
            {'text': 'text4'},
        ]
        self.db.bulk_insert_mappings_core(EntityTest, data, 2)
        self.assertEqual(mock.call_count, len(data) / 2)
