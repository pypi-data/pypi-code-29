from .operational import (
    EqNode,
    NotEqNode,
    GtNode,
    GteNode,
    LtNode,
    LteNode,
    ContainsNode,
    LikeNode,
    InNode,
    NotInNode,
    NullNode,
    NotNullNode,
)

OPERATIONAL_NODES = {
    'like': LikeNode,
    'eq': EqNode,
    'not_eq': NotEqNode,
    'null': NullNode,
    'not_null': NotNullNode,
    'gt': GtNode,
    'gte': GteNode,
    'lt': LtNode,
    'lte': LteNode,
    'in': InNode,
    'not_in': NotInNode,
    'contains': ContainsNode
}

__all__ = (
    'EqNode',
    'NotEqNode',
    'GtNode',
    'GteNode',
    'LtNode',
    'LteNode',
    'ContainsNode',
    'LikeNode',
    'InNode',
    'NotInNode',
    'NullNode',
    'NotNullNode',

    'OPERATIONAL_NODES',
)
