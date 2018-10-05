"""Tree module.

These class are used to represent the filters to apply to a query.
"""
from sqlalchemy.orm.query import Query

from sqla_filters.nodes.base import TreeNode


class SqlaFilterTree(object):
    """Class SqlaFilterTree.
    
    When you acces the parser.tree an instance of the class is returned.
    From the class you can access the root element and filter a sqlalchemy
    query.
    """

    def __init__(self, root: TreeNode) -> None:
        self._root = root

    @property
    def root(self) -> TreeNode:
        return self._root

    def filter(self, query: Query):
        entity = query.column_descriptions[0]['type']
        new_query, filters = self._root.filter(query, entity)
        return new_query.filter(filters)

    def __str__(self) -> str:
        """Return a representation of the tree."""
        def str_tree(element: TreeNode, depth: int, f_str: str):
            alg = '    '
            f_str += '{}- {}\n'.format(alg * depth if depth else '', element)
            for child in element.childs:
                f_str += str_tree(child, depth + 1, '')
            return f_str
        if self.root:
            final_str = 'SqlaFilterTree with following nodes:\n'
            final_str += str_tree(self.root, 0, '')
        else:
            final_str = 'Tree is empty.'
        return final_str
