import json
import time
import logging
import requests
from .exceptions import (
    RPCError,
    NumRetriesReached
)
log = logging.getLogger(__name__)


class Rpc:
    """ This class allows to call API methods synchronously, without
        callbacks.

        :param str url: A single REST endpoint URL
        :param int num_retries: Try x times to num_retries to a node on
               disconnect, -1 for indefinitely

        Usage:

        .. code-block:: python

            ws = GrapheneHTTPRPC("https://cread.creas.io")
            print(ws.get_account_count())

    """
    def __init__(self, url, **kwargs):
        self._request_id = 0

        self.num_retries = kwargs.get("num_retries", 1)
        self.user = kwargs.get("user")
        self.password = kwargs.get("password")
        self.url = url

    def get_request_id(self):
        self._request_id += 1
        return self._request_id

    def connect(self):
        pass

    def disconnect(self):
        pass

    def post_process_exception(self, exception):
        raise exception

    def parse_response(self, query):
        ret = {}
        try:
            ret = json.loads(query, strict=False)
        except ValueError:
            raise ValueError("Client returned invalid format. Expected JSON!")

        log.debug(json.dumps(query))

        if 'error' in ret:
            if 'detail' in ret['error']:
                raise RPCError(ret['error']['detail'])
            else:
                raise RPCError(ret['error']['message'])
        else:
            return ret["result"]

    def __getattr__(self, name):
        """ Map all methods to RPC calls and pass through the arguments
        """
        def method(*args, **kwargs):

            api_method = name
            if "api" in kwargs:
                api_method = kwargs["api"] + "." + name

            # let's be able to define the num_retries per query
            self.num_retries = kwargs.get("num_retries", self.num_retries)

            params = kwargs
            if 'params' in kwargs:
                params = kwargs["params"]

            query = {"method": api_method,
                     "jsonrpc": "2.0",
                     "params": params,
                     "id": self.get_request_id()}

            r = self.rpcexec(query)
            message = self.parse_response(r)
            return message
        return method
