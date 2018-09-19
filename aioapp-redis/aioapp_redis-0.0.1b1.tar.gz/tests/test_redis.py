import asyncio
import pytest
from aioapp.app import Application
from aioapp.error import PrepareError
from aioapp.misc import async_call
from aioapp.tracer import Span
from async_timeout import timeout
from aioapp_redis import Redis


async def _start_redis(app: Application, url: str,
                       connect_max_attempts=10,
                       connect_retry_delay=1.0) -> Redis:
    db = Redis(url, connect_max_attempts=connect_max_attempts,
               connect_retry_delay=connect_retry_delay)
    app.add('redis', db)
    await app.run_prepare()
    await db.start()
    return db


def _create_span(app) -> Span:
    if app.tracer:
        return app.tracer.new_trace(sampled=False, debug=False)


async def test_redis(app, redis):
    db = await _start_redis(app, redis)
    span = _create_span(app)

    res = await db.execute(span, 'redis:set', 'SET', 'key1', 1)
    assert res == 'OK'

    res = await db.execute(span, 'redis:get', 'GET', 'key1')
    assert res == '1'

    async with db.connection(span) as conn1:
        async with db.connection(span) as conn2:
            res = await conn1.execute(span, 'redis:get', 'GET', 'key1')
            assert res == '1'

            res = await conn2.execute_pubsub(span, 'redis:sub',
                                             'SUBSCRIBE', 'test_channel')
            assert [[b'subscribe', b'test_channel', 1]] == res

            channel = conn2.pubsub_channels['test_channel']

            res = await conn1.execute(span, 'redis:pub', 'PUBLISH',
                                      'test_channel', 'val')
            assert res == 1

            async with timeout(5):
                if await channel.wait_message():
                    msg = await channel.get(encoding="UTF-8")
                    assert msg == 'val'

            res = await conn2.execute_pubsub(span, 'redis:unsub',
                                             'UNSUBSCRIBE', 'test_channel')
            assert [[b'unsubscribe', b'test_channel', 0]] == res


async def test_redis_prepare_failure(app, unused_tcp_port):
    with pytest.raises(PrepareError):
        await _start_redis(app,
                           'redis://%s:%s/1' % ('127.0.0.1', unused_tcp_port),
                           connect_max_attempts=2, connect_retry_delay=0.001)


async def test_redis_health_bad(app: Application, unused_tcp_port: int,
                                loop: asyncio.AbstractEventLoop) -> None:
    url = 'redis://%s:%s/1' % ('127.0.0.1', unused_tcp_port)

    db = Redis(url)
    app.add('redis', db)

    async def start():
        await app.run_prepare()
        await db.start()

    res = async_call(loop, start)
    await asyncio.sleep(1)

    result = await app.health()
    assert 'redis' in result
    assert result['redis'] is not None
    assert isinstance(result['redis'], BaseException)

    if res['fut'] is not None:
        res['fut'].cancel()


async def test_redis_health_ok(app: Application, redis: str,
                               loop: asyncio.AbstractEventLoop) -> None:
    db = Redis(redis)
    app.add('redis', db)

    async def start():
        await app.run_prepare()
        await db.start()

    res = async_call(loop, start)
    await asyncio.sleep(1)

    result = await app.health()
    assert 'redis' in result
    assert result['redis'] is None

    if res['fut'] is not None:
        res['fut'].cancel()
