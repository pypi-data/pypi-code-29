import yaml
from typing import Any

from sqla_filters.nodes.base import TreeNode
from sqla_filters.nodes.logical import(
    OrNode,
    AndNode,
    LOGICAL_NODES
)
from sqla_filters.nodes.operational import OPERATIONAL_NODES
from sqla_filters.tree import SqlaFilterTree
from sqla_filters.parser.base import BaseSqlaParser
from .exceptions import YAMLFiltersParserTypeError


def validate_element(e_type, e_value) -> bool:
    if not e_type or not e_value:
        return False
    if (e_type == 'and' or e_type == 'or') and not isinstance(e_value, list):
        return False
    return True


class YAMLFiltersParser(BaseSqlaParser):
    def __init__(self, data: str, attr_sep: str = '.') -> None:
        super(YAMLFiltersParser, self).__init__(data, attr_sep)

    def _create_node(self, key: str, data: Any) -> TreeNode:
        if key == 'and' or key == 'or':
            return LOGICAL_NODES[key]()
        elif key == 'operator':
            operator = data.get('operator')
            attr_sep = data.get('attr_sep', None)
            return OPERATIONAL_NODES[operator](
                data.get('attribute', ''),
                data.get('value', None),
                attr_sep=attr_sep if attr_sep else self._attr_sep
            )
        else:
            raise YAMLFiltersParserTypeError('Unknown key.')

    def _generate_nodes(self, key: str, data: Any) -> TreeNode:
        node = self._create_node(key, data)
        if isinstance(node, AndNode) or isinstance(node, OrNode):
            for element in data:
                e_type = element.get('type', None)
                e_data = element.get('data', None)
                node.childs.append(self._generate_nodes(e_type, e_data))
        return node

    def _generate_filters_tree(self) -> SqlaFilterTree:
        yaml_dict = yaml.load(self._raw_data)
        r_type = yaml_dict.get('type', None)
        r_data = yaml_dict.get('data', None)
        if not validate_element(r_type, r_data):
            raise YAMLFiltersParserTypeError('Invalid yaml')
        return SqlaFilterTree(self._generate_nodes(r_type, r_data))
