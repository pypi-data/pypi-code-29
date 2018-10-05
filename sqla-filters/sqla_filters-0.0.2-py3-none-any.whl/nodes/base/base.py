"""base module of filter package.

These class are used to represent the filters to apply to a query.
"""
import abc
import datetime
from typing import (
    Any,
    List,
    Dict,
    Tuple,
    Optional,
    Iterator,
    Callable
)
from sqlalchemy import (
    Date,
    Time,
    DateTime
)
from sqlalchemy import or_
from sqlalchemy.orm.query import Query



class TreeNode(metaclass=abc.ABCMeta):
    """Abstract base class for every nodes.

    This class
    """
    def __init__(self) -> None:
        """Constructor.

        Define the _childs attribute as an empty list.
        :return: None
        :rtype: None
        """
        self._childs: List['TreeNode'] = []

    @property
    def childs(self) -> List['TreeNode']:
        """Property that return the node childs list.

        :return: The node childs list.
        :rtype: List[TreeNode]
        """
        return self._childs

    @abc.abstractmethod
    def filter(self, query: Query, entity: type) -> Tuple[Query, Any]:
        """Define the filter function that every node must to implement.

        :param query: The sqlalchemy query.
        :type query: Query

        :param entity: The entity model.
        :type entity: type

        :return: The filtered query.
        :rtype: Tuple[Query, Any]
        """
        raise NotImplementedError('You must implement this.')


class BaseOperationalNode(TreeNode):
    def __init__(self, attribute: str, value: Any, attr_sep: str='.') -> None:
        """Constructor.

        :param attribute: The model attribute as a string.
        :type attribute: str

        :param value: The value of the attribute.
        :type value: Any

        :param attr_sep: The separator if the attribute concerns relations.
        :type attr_set: str

        :return: None
        :rtype: None
        """
        super(BaseOperationalNode, self).__init__()
        self._attribute = attribute
        self._value = value
        self._attr_sep = attr_sep

    @property
    def attribute(self) -> str:
        """Property that return the model attribute.

        :return: The model attribute.
        :rtype: str
        """
        return self._attribute

    @property
    def value(self) -> Any:
        """Property that return the value of the model attribute.

        :return: The value of the model attribute.
        :rtype: Any
        """
        return self._value

    def _extract_relations(self, attribute: str) -> Tuple[List[str], str]:
        """Split and return the list of relation(s) and the attribute.

        :param attribute:
        :type attribute: str

        :return: A tuple where the first element is the list of related
            entities and the second is the attribute.
        :rtype: Tuple[List[str], str]
        """
        splitted = attribute.split(self._attr_sep)
        return (splitted[:-1], splitted[-1])

    def _get_relation(self, related_model: type, relations: List[str]) -> Tuple[Optional[List[type]], Optional[type]]:
        """Transform the list of relation to list of class.

        :param related_mode: The model of the query.
        :type related_mode: type

        :param relations: The relation list get from the `_extract_relations`.
        :type relations: List[str]

        :return: Tuple with the list of relations (class) and the second
            element is the last relation class.
        :rtype: Tuple[Optional[List[type]], Optional[type]]
        """
        relations_list, last_relation = [], related_model
        for relation in relations:
            relationship = getattr(last_relation, relation, None)
            if relationship is None:
                return (None, None)
            last_relation = relationship.mapper.class_
            relations_list.append(last_relation)
        return (relations_list, last_relation)

    def _join_tables(self, query: Query, join_models: Optional[List[type]]) -> Query:
        """Method to make the join when relation is found.

        :param query: The sqlalchemy query.
        :type query: Query

        :param join_models: The list of joined models get from the method
            `_get_relation`.
        :type join_models: Optional[List[type]]

        :return: The new Query with the joined tables.
        :rtype: Query
        """
        joined_query = query
        # Create the list of already joined entities
        joined_tables = [mapper.class_ for mapper in query._join_entities]
        if join_models:
            for j_model in join_models:
                if not j_model in joined_tables:
                    # /!\ join return a new query /!\
                    joined_query = joined_query.join(j_model)
        return joined_query

    def filter(self, query: Query, entity: type) -> Tuple[Query, Any]:
        """Add a filters to the list of filters to apply.

        .. warning:: 
        
            This method must be override in childs nodes.
        
        :param query: The sqlachemy query.
        :type query: Query

        :param entity: The entity model of the query.
        :type entity: type

        :return: A tuple with in first place the updated query and in second
            place the list of filters to apply to the query.
        :rtype: Tuple[Query, Any]
        """
        raise NotImplementedError('You must implement this.')


def default_method(*args, **kwargs):
    raise NotImplementedError(
        'You must set the _method attribute in your BaseLogicalNode subclass'
    )


class BaseLogicalNode(TreeNode):
    def __init__(self, *args, method=default_method, **kwargs) -> None:
        """Constructor.

        :param *args: The model attribute as a string.
        :type *args: list

        :param method: The method to apply the the childs node.
        :type method: Callable

        :param **kwargs: The separator if the attribute concerns relations.
        :type **kwargs: dict

        :return: None
        :rtype: None
        """
        super(BaseLogicalNode, self).__init__()
        self._method = method

    def filter(self, query: Query, entity: type) -> Tuple[Query, Any]:
        """Apply the `_method` to all childs of the node.
        
        :param query: The sqlachemy query.
        :type query: Query

        :param entity: The entity model of the query.
        :type entity: type

        :return: A tuple with in first place the updated query and in second
            place the list of filters to apply to the query.
        :rtype: Tuple[Query, Any]
        """
        new_query = query
        c_filter_list = []
        for child in self._childs:
            new_query, f_list = child.filter(new_query, entity)
            c_filter_list.append(f_list)
        return (
            new_query,
            self._method(*c_filter_list)
        )
