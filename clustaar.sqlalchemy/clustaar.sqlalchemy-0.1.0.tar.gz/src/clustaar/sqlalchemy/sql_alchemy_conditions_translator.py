from typing import List

from sqlalchemy.sql.elements import BinaryExpression
from sqlalchemy.orm.attributes import InstrumentedAttribute

from clustaar.sqlalchemy.database import Database

class SQLAlchemyConditionsTranslator:
    """ Use to transform text or dict in sqlalchemy conditions """

    def __init__(self, model: object):
        """
        Args:
            model (object): an object linked to the table
        """

        self._model = model

    def map_conditions(self, conditions: dict) ->List[BinaryExpression]:
        """ Tansform the dict conditions to a sqlalchemy condition

        Ex: {"user_id": "5555"}, {"user_id": ["5555", "66666"]}
            {"user_id": {">": "50"}}

        Args:
            conditions (dict): a 'human' condition

        Returns:
            List[BinaryExpression]
        """

        sql_alch_conditions = []
        for column, value in conditions.items():
            if isinstance(column, str):
                column = getattr(self._model, column)
            if isinstance(value, dict):
                condition = self._get_condition(column, *value.popitem())
            elif isinstance(value, list) or isinstance(value, set) or isinstance(value, tuple):
                condition = column.in_(value)
            else:
                condition = column == value
            sql_alch_conditions.append(condition)

        return sql_alch_conditions

    def _get_condition(self, column: InstrumentedAttribute, operation: str, value: any) -> BinaryExpression:
        """ Transform an user condition to a BinaryExpression comprehensible by sqlalchemy

        Args:
            column (InstrumentedAttribute): represent the target column
            operation (str): the user operation/condition
            value (any): the value to match with the condition

        Return:
            BinaryExpression
        """

        if operation == "contains":
            return column.ilike("%{0}%".format(value))
        elif operation == "<=":
            return column <= value
        elif operation == "<":
            return column < value
        elif operation == ">=":
            return column >= value
        elif operation == ">":
            return column > value
        elif operation == "!=":
            return column != value
