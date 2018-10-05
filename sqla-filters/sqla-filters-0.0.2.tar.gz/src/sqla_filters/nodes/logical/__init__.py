from .logical import (
    AndNode,
    OrNode,
)

LOGICAL_NODES = {
    'and': AndNode,
    'or': OrNode
}

__all__ = (
    'AndNode',
    'OrNode',
    'LOGICAL_NODES',
)
