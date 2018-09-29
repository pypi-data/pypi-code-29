"""This is the generic function package."""


from .base import (
    generic, method, variadic_method, 
    Dispatch, isgeneric, merge, get_implementation,
    gf_hash as __hash__,
)
from .go import *


__all__ = go.__all__[:]
__all__.extend((
    "generic", "method", "variadic_method", "Dispatch",
    "isgeneric", "get_implementation", "self_installing_generic",
    "__hash__",
))
