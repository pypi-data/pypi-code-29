import os
import time
import logging
import asyncio
from functools import partial
from aioapp.app import Application
from aioapp import config
from aioapp.tracer import Span
from aioapp_redis import Redis


class Config(config.Config):
    db_url: str
    _vars = {
        'db_url': {
            'type': str,
            'name': 'DB_URL',
            'descr': 'Database connection string in following format '
                     'redis://host:port/dbname?encoding=utf-8'
        }
    }


async def do_something(app: Application, ctx: Span) -> None:
    """
    do not run this task infinitely!!!
    there is no graceful shutdown!
    """
    await app.db.execute(ctx, 'test_set', 'SET', 'key', time.time())
    res = await app.db.execute(ctx, 'test_set', 'GET', 'key')
    print('query result', res)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()

    cfg = Config(os.environ)

    app = Application(loop=loop)
    app.add(
        'db',
        Redis(url=cfg.db_url),
        stop_after=[]
    )
    app.on_start = partial(do_something, app)
    app.run()
