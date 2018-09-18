import aiohttp

from actappliance.connections.aioconnection import AIOConnection

AIO_TIMEOUT = aiohttp.ClientTimeout(total=None, connect=121, sock_connect=121, sock_read=241)


class AIORest(AIOConnection):
    """
    self._conn holds an aiohttp session in this class
    """
    async def _connect(self, *args, **kwargs):
        # These kwargs are kwo so no arg handling required
        kwargs.setdefault('timeout', AIO_TIMEOUT)
        kwargs.setdefault('loop', self._loop)
        kwargs.setdefault('headers', {'Content-Type': 'application/json'})
        self._conn = aiohttp.ClientSession(*args, **{**self.connect_kwargs, **kwargs})
        result = await self._conn.post(f"https://{self.system}/actifio/api/login", params=self.call_kwargs,
                                       verify_ssl=False)
        result.raise_for_status()
        sid_r = await result.json()
        self.sid = sid_r['sessionid']

    async def _disconnect(self):
        await self._conn.close()

    async def _single_conn_request(self, act_cmd_obj, *, check: bool=True):
        async with aiohttp.ClientSession() as session:
            session._raise_for_status = check
            return await self._conn_request(act_cmd_obj, conn=session)

    async def _conn_request(self, act_cmd_obj, *, conn, check: bool=True):
        print(act_cmd_obj.call_kwargs)
        r = await conn.request(**act_cmd_obj.call_kwargs, verify_ssl=False)
        if check:
            r.raise_for_status()
        act_cmd_obj.output.result = await r.json()
