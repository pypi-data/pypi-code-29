import asyncio
from abc import ABC, abstractmethod

from actappliance.connections import CALL_TIMEOUT
from actappliance.models import ActCmd


class AIOConnection(ABC):
    def __init__(self, system, connect_kwargs: dict=None, *, call_kwargs: dict=None, loop=None,
                 call_timeout=CALL_TIMEOUT):
        self.system = system
        self.connect_kwargs = connect_kwargs if connect_kwargs is not None else {}
        self.call_kwargs = call_kwargs if call_kwargs is not None else {}
        self._loop = loop or asyncio.get_event_loop()
        self.timeout = call_timeout
        self._conn = None

    def connect(self, *args, **kwargs):
        self._loop.run_until_complete(self._connect(*args, **kwargs))

    @abstractmethod
    async def _connect(self, *args, **kwargs):
        pass

    def disconnect(self):
        self._loop.run_until_complete(self._disconnect())

    @abstractmethod
    async def _disconnect(self):
        pass

    async def _call(self, act_cmd_obj: ActCmd):
        await self._request(act_cmd_obj)

    async def _request(self, act_cmd_obj: ActCmd, *, check: bool=True):
        """Make the request with the same conn from connect or an ephemeral connection if the user hasn't connected"""
        if not self._conn:
            return await self._single_conn_request(act_cmd_obj, check=check)
        return await self._conn_request(act_cmd_obj, conn=self._conn, check=check)

    @abstractmethod
    async def _single_conn_request(self, act_cmd_obj, *, check: bool=True):
        """Create an ephemeral connection and then make a request with it"""
        pass

    @abstractmethod
    async def _conn_request(self, act_cmd_obj, *, conn, check: bool=True):
        """Make a request with a provided connection"""
        pass

    async def _timeout_call(self, *args, **kwargs):
        fut = self._call(*args, **kwargs)
        # Consider the speed benefits of asyncio_timeout.timeout vs added dep
        # Warning: this behaves differently <3.7 because wait_for wouldn't wait for future to cancel before Error
        result = await asyncio.wait_for(fut, self.timeout, loop=self._loop)
        return result

    def cmd(self, *args, **update_cmds):
        return self._loop.run_until_complete(self._cmd(*args, **update_cmds))

    async def _cmd(self, operation, **update_cmds):
        ac = ActCmd(conn_object=self)
        ac.cmd_input(operation, **update_cmds)
        await self._timeout_call(ac)
        return ac.response
