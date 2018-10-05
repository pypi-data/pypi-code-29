"""Logical nodes.

The nodes in this file are logical nodes. Logical node are used to apply a
logical operation to 2 or more child nodes.

Currently two logical operation are supported:

1. And
2. Or
"""
from sqlalchemy import and_, or_
from sqlalchemy.orm.query import Query

from sqla_filters.nodes.base import BaseLogicalNode

class AndNode(BaseLogicalNode):
    """Represent the ``and`` operation from sqlalchemy.

    When the filter method is called on this node it run on all of it's childs
    to create the filters list and apply the ``and_`` function to this list.
    """

    def __init__(self) -> None:
        super(AndNode, self).__init__(method=and_)

    def __str__(self) -> str:
        return '<AND node : {}>'.format(id(self))


class OrNode(BaseLogicalNode):
    """Represent the ``or`` operation from sqlalchemy.

    When the filter method is called on this node it run on all of it's childs
    to create the filters list and apply the ``or_`` function to this list."""

    def __init__(self) -> None:
        super(OrNode, self).__init__(method=or_)

    def __str__(self) -> str:
        return '<OR node : {}>'.format(id(self))
