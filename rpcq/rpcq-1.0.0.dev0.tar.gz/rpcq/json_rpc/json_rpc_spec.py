# ###########################################################################
# Copyright (C) Rigetti & Co. Inc. - All Rights Reserved                    #
# September, 2017                                                           #
# ###########################################################################
"""
Class with json_rpc_call decorator for asynchronous JSON RPC calls
"""
import asyncio
import logging
import traceback
from typing import Union

from rpcq.core_messages import RPCRequest, RPCReply, RPCError
from rpcq.json_rpc.utils import rpc_reply, rpc_error, RPCMethodError, get_input

_log = logging.getLogger(__name__)


class RPCSpec(object):
    """
    Class for keeping track of class methods that are exposed to the JSON RPC interface
    """
    def __init__(self, *, provide_tracebacks: bool = True):
        """
        Create a JsonRpcSpec object.

        Usage:
            jr = JsonRpcSpec()

            class MyClass(object):
                def __init__(self):
                    self.num = 5

            @jr.add_method
            def add(obj, *args):
                return sum(args) + obj.num

            obj = MyClass()

            request = {
                "jsonrpc": "2.0",
                "id": "0",
                "method": "add",
                "params": [1, 2]
            }

            reply = jr.call(request, obj)

        :param provide_tracebacks: If set to True, unhandled exceptions which occur during RPC call
            implementations will have their tracebacks forwarded to the calling client as part of
            the generated RPCError reply objject. If set to False, the generated RPCError reply will
            omit this information (but the traceback will still get written to the logfile).
        """
        self._json_rpc_methods = {}
        self.provide_tracebacks = provide_tracebacks

    def add_handler(self, f):
        """
        Adds the function f to a dictionary of JSON RPC methods.

        :param callable f: Method to be exposed
        :return:
        """
        self._json_rpc_methods[f.__name__] = f
        return f

    def get_handler(self, request):
        """
        Get callable from JSON RPC request

        :param RPCRequest request: JSON RPC request
        :return: Method
        :rtype: callable
        """
        try:
            f = self._json_rpc_methods[request.method]

        except (AttributeError, KeyError):  # pragma no coverage
            raise RPCMethodError("Received invalid method '{}'".format(request.method))

        return f

    async def run_handler(self, request: RPCRequest) -> Union[RPCReply, RPCError]:
        """
        Process a JSON RPC request

        :param RPCRequest request: JSON RPC request
        :return: JSON RPC reply
        """
        try:
            rpc_handler = self.get_handler(request)
        except RPCMethodError as e:
            return rpc_error(request.id, str(e))

        try:
            # Run RPC and get result
            args, kwargs = get_input(request.params)
            result = rpc_handler(*args, **kwargs)

            if asyncio.iscoroutine(result):
                result = await result

        except Exception as e:
            _traceback = traceback.format_exc()
            _log.error(_traceback)
            if self.provide_tracebacks:
                return rpc_error(request.id, "{}\n{}".format(str(e), _traceback))
            else:
                return rpc_error(request.id, str(e))

        return rpc_reply(request.id, result)
