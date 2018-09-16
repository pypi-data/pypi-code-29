from __future__ import unicode_literals


def _check_base_classes(_class, _method_name, current, depth):
    if current == depth:
        return _method_name in _class.__dict__

    for base in _class.__bases__:
        if _method_name in base.__dict__:
            return True
        if current < depth and _check_base_classes(base, _method_name, current + 1, depth):
            return True
    return False


def method_filter(item, _class, depth=0):
    return _check_base_classes(_class, item, 0, depth)


def dir_filter(item):
    """
    Accept each item which doesn't start with _
    :type item: str
    :param item: a string item to filter
    :return: true if item doesn't start with _
    """
    return not item.startswith("_")
