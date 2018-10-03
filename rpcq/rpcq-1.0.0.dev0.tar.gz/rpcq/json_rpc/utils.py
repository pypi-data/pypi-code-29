# ###########################################################################
# Copyright (C) Rigetti & Co. Inc. - All Rights Reserved                    #
# September, 2017                                                           #
# ###########################################################################
"""Utils for message passing"""
import uuid

from rpcq.core_messages import RPCRequest, RPCReply, RPCError


def rpc_request(method_name, *args, **kwargs):
    """
    Create RPC request

    :param str method_name: Method name
    :param args: Positional arguments
    :param kwargs: Keyword arguments
    :return: JSON RPC formatted dict
    :rtype: RPCRequest
    """
    if args:
        kwargs['*args'] = args

    return RPCRequest(
        jsonrpc="2.0",
        id=str(uuid.uuid4()),
        method=method_name,
        params=kwargs
    )


def rpc_reply(id, result):
    """
    Create RPC reply

    :param str|int id: Request ID
    :param result: Result
    :return: JSON RPC formatted dict
    :rtype: RPCReply
    """
    return RPCReply(
        jsonrpc="2.0",
        id=id,
        result=result
    )


def rpc_error(id, error_msg):
    """
    Create RPC error

    :param str|int id: Request ID
    :param str error_msg: Error message
    :return: JSON RPC formatted dict
    :rtype: RPCError
    """
    return RPCError(
        jsonrpc="2.0",
        id=id,
        error=error_msg)


def get_input(params):
    """
    Get positional or keyword arguments from JSON RPC params

    :param dict|list params: Parameters passed through JSON RPC
    :return: args, kwargs
    :rtype: tuple
    """
    # Backwards compatibility for old clients that send params as a list
    if isinstance(params, list):
        args = params
        kwargs = {}
    elif isinstance(params, dict):
        args = params.pop('*args', [])
        kwargs = params
    else:  # pragma no coverage
        raise TypeError(
            "Unknown type {} of params, must be list or dict".format(type(params)))

    return args, kwargs


class RPCErrorError(IOError):
    """JSON RPC error that is raised by a Client when it receives an RPCError message"""


class RPCMethodError(AttributeError):
    """JSON RPC error that is raised by JSON RPC spec for nonexistent methods"""

