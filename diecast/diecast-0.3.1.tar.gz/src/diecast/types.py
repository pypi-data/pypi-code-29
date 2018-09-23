# -*- coding: utf-8 -*-

import inspect
from typing import (
    Any,
    Callable,
    Dict,
    NewType,
)

from diecast.component import Component

ComponentState = NewType('ComponentState', Dict[str, Any])
Injector = NewType(
    'Injector',
    Callable[[Callable], Callable],
)
