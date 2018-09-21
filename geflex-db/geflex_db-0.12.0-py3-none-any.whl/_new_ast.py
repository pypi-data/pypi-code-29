import builtins
from _ast import *
from ast import parse
from typing import Union

from .acnt import SafeDatatypesContainer

__all__ = 'literal_eval', 'SAFE_DATATYPES'


_SAFE_DATATYPES_DEFAULT = [builtins.bool,
                           builtins.int,
                           builtins.float,
                           builtins.str,
                           builtins.bytes,
                           builtins.list,
                           builtins.tuple,
                           builtins.set,
                           builtins.frozenset,
                           builtins.dict]
SAFE_DATATYPES = SafeDatatypesContainer(_SAFE_DATATYPES_DEFAULT)


def literal_eval(node_or_string: Union[str, Expression]):
    """
    Safely evaluate an expression node or a string containing a Python
    expression.  The string or node provided may only consist of the following
    Python literal structures: strings, bytes, numbers, tuples, lists, dicts,
    sets, booleans, and None.

    * Обновлена, т.к. оригинальная функция не читает 'set()', 'dict()' и подобные вызовы встроенных типов
    """
    if isinstance(node_or_string, str):
        node_or_string = parse(node_or_string, mode='eval')
    if isinstance(node_or_string, Expression):
        node_or_string = node_or_string.body

    def _convert_num(node):
        if isinstance(node, Constant):
            if isinstance(node.value, (int, float, complex)):
                return node.value
        elif isinstance(node, Num):
            return node.n

        # ============================================
        elif isinstance(node, Call):
            if node.func.id in SAFE_DATATYPES:
                # noinspection PyShadowingNames
                return SAFE_DATATYPES[node.func.id](
                    *[_convert(arg) for arg in node.args],
                    **{kwarg.arg: _convert(kwarg.value) for kwarg in node.keywords}
                )
        # ============================================

        raise ValueError('malformed node or string: ' + repr(node))

    def _convert_signed_num(node):
        if isinstance(node, UnaryOp) and isinstance(node.op, (UAdd, USub)):
            operand = _convert_num(node.operand)
            if isinstance(node.op, UAdd):
                return + operand
            else:
                return - operand
        return _convert_num(node)

    def _convert(node):
        if isinstance(node, Constant):
            return node.value
        elif isinstance(node, (Str, Bytes)):
            return node.s
        elif isinstance(node, Num):
            return node.n
        elif isinstance(node, Tuple):
            return tuple(map(_convert, node.elts))
        elif isinstance(node, List):
            return list(map(_convert, node.elts))
        elif isinstance(node, Set):
            return set(map(_convert, node.elts))
        elif isinstance(node, Dict):
            return dict(zip(map(_convert, node.keys),
                            map(_convert, node.values)))
        elif isinstance(node, NameConstant):
            return node.value
        elif isinstance(node, BinOp) and isinstance(node.op, (Add, Sub)):
            left = _convert_signed_num(node.left)
            right = _convert_num(node.right)
            if isinstance(left, (int, float)) and isinstance(right, complex):
                if isinstance(node.op, Add):
                    return left + right
                else:
                    return left - right
        return _convert_signed_num(node)
    return _convert(node_or_string)
