from typing import List, Tuple, Union, Iterator

from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql.elements import UnaryExpression
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm.query import Query
from sqlalchemy.orm import mapper

from clustaar.sqlalchemy.sql_alchemy_conditions_translator import SQLAlchemyConditionsTranslator
from clustaar.sqlalchemy.constants import SQLALCHEMY_SORT_SYNTAX_RE
from clustaar.sqlalchemy.database import Database
from clustaar.sqlalchemy.schema import Schema


class Table:
    """ Class that manage table logic """

    def __init__(self, database: Database, schema: Schema = None, model: object = None):
        """
        Args:
            database (Database): the database
            schema (Schema): the shema logic of the table
            model (object): the object represented by the table
        """

        self._database = database
        self._model = model or self._model
        self._schema = schema or self._schema
        self._table = self._schema(database._metadata)
        self._conditions_translator = SQLAlchemyConditionsTranslator(self._model)

        mapper(self._model, self._table)

    def insert(self, **kwargs) -> object:
        """ Method used to insert an entry """

        obj = self._model(**kwargs)
        self._persist(obj)
        return obj

    def count(self, conditions: dict = None) -> int:
        """ Returns the actual entry count in function of conditions (sql_alchemy_condition_translator)

        Args:
            condition (dict): a condition

        Returns:
            int: the number of entry thats matches with conditions
        """

        session = self._get_session()

        conditions = self._conditions_translator.map_conditions(conditions or {})

        return session.query(self._model).filter(*conditions).count()

    def get(self, conditions: dict = None, page: int = None, limit: int = None, sort: str = None, safe: bool = False, batch_size: int = 10_000) -> Union[Iterator[object], List[object]]:
        """
        Used to get entries in function of conditions.

        Args:
            conditions (dict): some conditions -> {"user_id": {">=": 44}}
            page (int): the page offset
            limit (int): limit the number of returned results
            sort (str): choose a particular order for the returned results
            batch_size (int): represent the numbers of entry fetched by the yield_per method
            safe (bool): returns lightweight iterator instead of a potential big list

        If safe parameter is set to True this method use the yield_per.
        The purpose of this method is when fetching very large result sets (> 10K rows), to batch results in sub-collections and yield them out partially, so that the Python interpreter doesn’t need to declare very large areas of memory which is both time consuming and leads to excessive memory use


        Infos:
            The sort string permit to order asc/desc with this syntax:

            +user_id
            -user_id

            You can also easly set:
                - a limit
                - an order
                - the batch size

        Returns:
            Union[Iterator[object], List[object]]
        """

        session = self._get_session()
        conditions = self._conditions_translator.map_conditions(conditions or {})
        query = session.query(self._model).filter(*conditions)

        if safe:
          query = query.yield_per(batch_size)

        if sort is not None:
            sort_clause = self._get_sort_clause(sort)
            if sort_clause is not None:
                query = query.order_by(sort_clause)

        if page is not None and limit is not None:
            offset = (page - 1) * limit
            query = query.offset(offset)
        if limit is not None:
            query = query.limit(limit)

        return query if safe else query.all()

    def bulk_insert(self, mappings: Tuple[dict]):
        """ Used for insert a list of new entry

        Args:
            mappings (Tuple[dict]): a list of entry
        """

        query = insert(self._table).values(mappings).on_conflict_do_nothing()

        session = self._get_session()
        session.execute(query)
        session.flush()

    def delete(self, obj: object):
        """ Used for delete an entry

        Args:
            obj (object): the object to remove
        """

        session = self._get_session()
        session.delete(obj)
        session.flush()

    def delete_where(self, conditions: dict):
        """ Like the delete function a condition

        Args:
            condition (dict): a condition
        """

        session = self._get_session()
        conditions = self._conditions_translator.map_conditions(conditions)
        session.query(self._model).\
            filter(*conditions).\
            delete(synchronize_session=False)

    def truncate(self):
        """ Permit to clear a table.
        Commit the session before and after the truncate
        """

        session = self._get_session()

        #  The session is committed to prevent potential query still here/alive (in a db transaction).
        session.commit()

        session.execute(f"TRUNCATE TABLE {self._table}")
        session.commit()

    def _get_session(self):
        """ Get the table session """

        return self._database.get_session()

    def _persist(self, obj) -> object:
        """ Save an object

        Args:
            obj (object): the object to save

        Returns:
            object
        """

        session = self._get_session()
        session.add(obj)
        session.flush()
        return obj

    def _get_sort_clause(self, sort: str):
        """ Convrerte string to UnaryExpression

        Args:
            sort (str): the original string
        """

        sort_matches = SQLALCHEMY_SORT_SYNTAX_RE.match(sort)
        if sort_matches:
            sign   = sort_matches.group(1)
            column = self._get_sort_column(sort_matches.group(2))
            if sign == '-':
                return column.desc()
            else:
                return column.asc()

    def _get_sort_column(self, column_name: str) -> UnaryExpression:
        """
        Get column even on associated relationships

        Args:
            column_name (str): the column name

        Returns:
            UnaryExpression
        """

        column_parts = column_name.split(".")
        model = self._model
        for column_part in column_parts:
            column = getattr(model, column_part)
            if hasattr(column, "property") and hasattr(column.property, "mapper"):
                model = column.property.mapper.class_

        return column
