# -*- coding: utf-8 -*-

"""Bio2BEL miRBase converts miRBase resources to BEL."""

from .manager import Manager  # noqa: F401
from .utils import get_version  # noqa: F401

__all__ = [
    'Manager',
    'get_version',
]
