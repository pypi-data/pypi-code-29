# -*- coding: utf-8 -*-

from .env import IS_NATS_RPC

if IS_NATS_RPC:
    from .func_nats import FuncNATS

    Func = FuncNATS
else:
    from .func_http import FuncHTTP

    Func = FuncHTTP

__all__ = ['Func']
