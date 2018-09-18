import asyncssh

from actappliance.connections.aioconnection import AIOConnection
from actappliance.connections.ssh import ssh_out


class AIOSsh(AIOConnection):
    """
    self._conn holds an ssh connection in this class
    """
    def __init__(self, *args, **kwargs):
        super(AIOSsh, self).__init__(*args, **kwargs)

    def connect(self, *args, **kwargs):
        self._loop.run_until_complete(self._connect(*args, **kwargs))

    async def _connect(self, *args, **kwargs):
        kwargs.setdefault('port', 26)
        kwargs.setdefault('client_factory', None)
        self._conn, _ = await asyncssh.create_connection(*args, host=self.system, loop=self._loop,
                                                         **{**self.connect_kwargs, **kwargs})

    async def _disconnect(self):
        await self._conn.__aexit__()

    async def _single_conn_request(self, *args, **kwargs):
        async with asyncssh.connect(self.system, **self.connect_kwargs) as conn:
            await self._conn_request(*args, conn=conn, **kwargs)

    async def _conn_request(self, act_cmd_obj, *, conn, check: bool=True):
        # Can't use ssh_kwargs because run's input is 'cmd' not 'command'
        result = await conn.run(act_cmd_obj.input.ssh_command, check=True)

        ssh_o = ssh_out(
            result.stdout.rstrip('\n').split('\n'),
            result.stderr.rstrip('\n').split('\n'),
            result.exit_status
        )
        act_cmd_obj.output.sshout = ssh_o

    def scp(self, srcpaths, path=b'.', **kwargs):
        """Copy file(s) to a destination path using scp

        :param srcpaths: See asyncssh.scp
        :param path: A str only input will be used as a path instead of a connection with a default path of b'.'
            Note: This is not the same as asyncssh.scp as it's dstpath assumes a str input is
        :param kwargs: See asyncssh.scp
        """
        # Comparison from asyncssh.scp's _parse_path
        if not isinstance(path, (str, bytes)):
            # The connection will be added by the class's connection and shouldn't be passed through this method
            raise ValueError(f"Path input should be destination path only.")
        dstpath = (self._conn, path)
        self._loop.run_until_complete(asyncssh.scp(srcpaths, dstpath, **kwargs))
