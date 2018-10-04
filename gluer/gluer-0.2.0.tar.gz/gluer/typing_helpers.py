import sys
NEW_TYPING = sys.version_info[:3] >= (3, 7, 0) # why the hell did they change that

from typing import Sequence, Type

def is_list_type(t: Type) -> bool:
    if NEW_TYPING:
        return hasattr(t, "__origin__") and t.__origin__ is list
    else:
        return Sequence in t.mro()


def get_inner_type(t: Type) -> Type:
    return t.__args__[0]
