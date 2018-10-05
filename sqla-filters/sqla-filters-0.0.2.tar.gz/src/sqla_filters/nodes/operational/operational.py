from typing import (
    Any,
    List,
    Dict,
    Tuple,
    Optional,
    Iterator,
    Callable
)

from sqlalchemy.orm.query import Query
from sqlalchemy.sql import operators

from sqla_filters.nodes.base import BaseOperationalNode

# #############################################################################
# ############################## COMPARISON ###################################
# #############################################################################
class EqNode(BaseOperationalNode):
    """EqNode class.
    
    This node test the equality between two values.
    Internally it use the `operators.eq` function available in
    `sqlalchemy.sql.operators`.
    """

    def __init__(self, attribute: str, value: Any, attr_sep: str = '.') -> None:
        super(EqNode, self).__init__(attribute, value, attr_sep)

    def filter(self, query: Query, entity: type):
        relations, attr = self._extract_relations(self._attribute)
        join_models, related_model = self._get_relation(entity, relations)
        if related_model and hasattr(related_model, attr):
            return (
                self._join_tables(query, join_models),
                getattr(related_model, attr) == self._value
            )

    def __str__(self) -> str:
        return '<Eq node | attr : {} | value : {}'.format(
            self._attribute,
            self._value
        )


class NotEqNode(BaseOperationalNode):
    """NotEqNode class.
    
    This node test the non equality between two values.
    Internally it use the `operators.ne` function available in
    `sqlalchemy.sql.operators`.
    """

    def __init__(self, attribute: str, value: Any, attr_sep: str = '.') -> None:
        super(NotEqNode, self).__init__(attribute, value, attr_sep)

    def filter(self, query: Query, entity: type):
        relations, attr = self._extract_relations(self._attribute)
        join_models, related_model = self._get_relation(entity, relations)
        if related_model and hasattr(related_model, attr):
            return (
                self._join_tables(query, join_models),
                getattr(related_model, attr) != self._value
            )

    def __str__(self) -> str:
        return '<Not Eq node | attr : {} | value : {}'.format(
            self._attribute,
            self._value
        )


class GtNode(BaseOperationalNode):
    """GtNode class.
    
    This node test if a value is greater than another one.
    Internally it use the `operators.gt` function available in
    `sqlalchemy.sql.operators`.
    """

    def __init__(self, attribute: str, value: Any, attr_sep: str = '.') -> None:
        super(GtNode, self).__init__(attribute, value, attr_sep)

    def filter(self, query: Query, entity: type):
        relations, attr = self._extract_relations(self._attribute)
        join_models, related_model = self._get_relation(entity, relations)
        if related_model and hasattr(related_model, attr):
            return (
                self._join_tables(query, join_models),
                getattr(related_model, attr) > self._value
            )

    def __str__(self) -> str:
        return '<Gt node | attr : {} | value : {}'.format(
            self._attribute,
            self._value
        )


class GteNode(BaseOperationalNode):
    """GteNode class.
    
    This node test if a value is greater or equal to another one.
    Internally it use the `operators.ge` function available in
    `sqlalchemy.sql.operators`.
    """

    def __init__(self, attribute: str, value: Any, attr_sep: str = '.') -> None:
        super(GteNode, self).__init__(attribute, value, attr_sep)
        self._method = operators.ge

    def filter(self, query: Query, entity: type):
        relations, attr = self._extract_relations(self._attribute)
        join_models, related_model = self._get_relation(entity, relations)
        if related_model and hasattr(related_model, attr):
            return (
                self._join_tables(query, join_models),
                getattr(related_model, attr) >= self._value
            )

    def __str__(self) -> str:
        return '<Gte node | attr : {} | value : {}'.format(
            self._attribute,
            self._value
        )


class LtNode(BaseOperationalNode):
    """LtNode class.
    
    This node test if a value is lower than another one.
    Internally it use the `operators.lt` function available in
    `sqlalchemy.sql.operators`.
    """

    def __init__(self, attribute: str, value: Any, attr_sep: str = '.') -> None:
        super(LtNode, self).__init__(attribute, value, attr_sep)

    def filter(self, query: Query, entity: type):
        relations, attr = self._extract_relations(self._attribute)
        join_models, related_model = self._get_relation(entity, relations)
        if related_model and hasattr(related_model, attr):
            return (
                self._join_tables(query, join_models),
                getattr(related_model, attr) < self._value
            )

    def __str__(self) -> str:
        return '<Lt node | attr : {} | value : {}'.format(
            self._attribute,
            self._value
        )


class LteNode(BaseOperationalNode):
    """LteNode class.
    
    This node test if a value is lower or equal to another one.
    Internally it use the `operators.le` function available in
    `sqlalchemy.sql.operators`.
    """

    def __init__(self, attribute: str, value: Any, attr_sep: str = '.') -> None:
        super(LteNode, self).__init__(attribute, value, attr_sep)

    def filter(self, query: Query, entity: type):
        relations, attr = self._extract_relations(self._attribute)
        join_models, related_model = self._get_relation(entity, relations)
        if related_model and hasattr(related_model, attr):
            return (
                self._join_tables(query, join_models),
                getattr(related_model, attr) <= self._value
            )

    def __str__(self) -> str:
        return '<Lte node | attr : {} | value : {}'.format(
            self._attribute,
            self._value
        )


# #############################################################################
# ############################### SEQUENCE ####################################
# #############################################################################
class ContainsNode(BaseOperationalNode):
    """ContainsNode class.
    
    This node test if an attribut contains the value.
    Internally it use the `operators.contains` function available in
    `sqlalchemy.sql.operators`."""

    def __init__(self, attribute: str, value: Any, attr_sep: str = '.') -> None:
        super(ContainsNode, self).__init__(attribute, value, attr_sep)

    def filter(self, query: Query, entity: type):
        relations, attr = self._extract_relations(self._attribute)
        join_models, related_model = self._get_relation(entity, relations)
        if related_model and hasattr(related_model, attr):
            return (
                self._join_tables(query, join_models),
                getattr(related_model, attr).contains(self._value)
            )

    def __str__(self) -> str:
        return '<Contains node | attr : {} | value : {}'.format(
            self._attribute,
            self._value
        )


# #############################################################################
# #############################################################################
# #############################################################################
class LikeNode(BaseOperationalNode):
    """ContainsNode class.
    
    This node test if an attribut is like the value.
    This function have the behavior of the `LIKE` in the sql language.
    This node use the attr.like function of a model attribute.
    """

    def __init__(self, attribute: str, value: Any, attr_sep: str = '.') -> None:
        super(LikeNode, self).__init__(attribute, value, attr_sep)

    def filter(self, query: Query, entity: type):
        relations, attr = self._extract_relations(self._attribute)
        join_models, related_model = self._get_relation(entity, relations)
        if related_model and hasattr(related_model, attr):
            return (
                self._join_tables(query, join_models),
                getattr(related_model, attr).like(self._value)
            )

    def __str__(self) -> str:
        return '<Like node | attr : {} | value : {}'.format(
            self._attribute,
            self._value
        )


class InNode(BaseOperationalNode):
    """InNode class.
    
    This node test if an attribut is in a list of values.
    This function have the behavior of the `in` in the sql language.
    This node use the attr.in function of a model attribute.
    """

    def __init__(self, attribute: str, value: Any, attr_sep: str = '.') -> None:
        super(InNode, self).__init__(attribute, value, attr_sep)

    def filter(self, query: Query, entity: type):
        relations, attr = self._extract_relations(self._attribute)
        join_models, related_model = self._get_relation(entity, relations)
        if related_model and hasattr(related_model, attr):
            return (
                self._join_tables(query, join_models),
                getattr(related_model, attr).in_(self._value)
            )

    def __str__(self) -> str:
        return '<In node | attr : {} | value : {}'.format(
            self._attribute,
            self._value
        )


class NotInNode(BaseOperationalNode):
    """NotInNode class.
    
    This node test if an attribut is not in a list of values.
    This function have the behavior of the `not in` in the sql language.
    This node use the ~attr.in_ function of a model attribute.
    """

    def __init__(self, attribute: str, value: Any, attr_sep: str = '.') -> None:
        super(NotInNode, self).__init__(attribute, value, attr_sep)

    def filter(self, query: Query, entity: type):
        relations, attr = self._extract_relations(self._attribute)
        join_models, related_model = self._get_relation(entity, relations)
        if related_model and hasattr(related_model, attr):
            return (
                self._join_tables(query, join_models),
                ~getattr(related_model, attr).in_(self._value)
            )

    def __str__(self) -> str:
        return '<Not In node | attr : {} | value : {}'.format(
            self._attribute,
            self._value
        )


class NullNode(BaseOperationalNode):
    """NullNode class.
    
    This node test if an attribut is null.
    This node use lambda function that test if the attr == None.
    """

    def __init__(self, attribute: str, value: Any = None, attr_sep: str = '.') -> None:
        super(NullNode, self).__init__(attribute, value, attr_sep)

    def filter(self, query: Query, entity: type):
        relations, attr = self._extract_relations(self._attribute)
        join_models, related_model = self._get_relation(entity, relations)
        if related_model and hasattr(related_model, attr):
            return (
                self._join_tables(query, join_models),
                getattr(related_model, attr) == None
            )

    def __str__(self) -> str:
        return '<Null node | attr : {} | value : {}'.format(
            self._attribute,
            self._value
        )


class NotNullNode(BaseOperationalNode):
    """NotNullNode class.
    
    This node test if an attribut is not null.
    This node use lambda function that test if the attr != None.
    """

    def __init__(self, attribute: str, value: Any = None, attr_sep: str = '.') -> None:
        super(NotNullNode, self).__init__(attribute, value, attr_sep)

    def filter(self, query: Query, entity: type):
        relations, attr = self._extract_relations(self._attribute)
        join_models, related_model = self._get_relation(entity, relations)
        if related_model and hasattr(related_model, attr):
            return (
                self._join_tables(query, join_models),
                getattr(related_model, attr) != None
            )

    def __str__(self) -> str:
        return '<Not Null node | attr : {} | value : {}'.format(
            self._attribute,
            self._value
        )
