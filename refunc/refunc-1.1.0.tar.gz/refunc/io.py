# -*- coding: utf-8 -*-

import asyncio
import base64
import functools
import json
import logging
import os
import queue
import sys
import traceback
from asyncio import AbstractEventLoop, Task
from collections import namedtuple
from io import TextIOBase

import six

from .ctx import BaseContext
from .interface import Context, Handler, Message, Request
from .util import jsonline_dumps, get_default_threadpool
from .errors import ResultError

__all__ = ['new_ioloop']


def new_ioloop(
    ctx: Context,
    # events handler
    handler: Handler,
    # in stream
    ins: TextIOBase = sys.stdin,
    # out stream
    outs: TextIOBase = sys.stdout,
    # main loop
    loop: AbstractEventLoop = None,
):

    logger = logging.getLogger('loader')

    if loop is None:
        loop = asyncio.get_event_loop()

    task_ref = {}

    async def stop():
        if task_ref['reader']:
            reader = task_ref['reader']
            task_ref['reader'] = None
            reader.cancel()

            # wait for io task exiting
            tasks = Task.all_tasks()
            if tasks:
                await asyncio.wait(tasks, loop=loop)

    def read_line():
        return loop.run_in_executor(get_default_threadpool(), ins.readline)

    def write_line(line):
        line = line + "\r\n"

        def flush():
            try:
                outs.write(line)
                outs.flush()
            except Exception:
                logger.error(traceback.format_exc())
                stop()

        return loop.run_in_executor(get_default_threadpool(), flush)

    def write_err(et, e: Exception, tb):
        if tb:
            for entry in traceback.format_exception(et, e, tb):
                for line in entry.split('\n'):
                    if line:
                        logger.error(line)
        if isinstance(e, ResultError):
            msg = str(e)
        else:
            if len(e.args) > 0:
                msg = '{}: {}'.format(
                    type(e).__name__, ','.join(['{}'.format(a) for a in e.args])
                )
            else:
                msg = type(e).__name__
        return write_line(jsonline_dumps({'a': 'err', 'p': msg}))

    # dynamic cls override publish
    # ts_0 = datetime(1970, 1, 1)

    # def ts_now()->int:
    #     return int((datetime.utcnow() - ts_0).total_seconds() * 1000000)

    # if ctx_cls is None:
    #     ctx_cls = BaseContext

    # class PublishContext(ctx_cls):
    #     def publish(self, topic: str, payload: dict):
    #         actout = {
    #             'a': 'emit',
    #             'p': {
    #                 'topic': topic,
    #                 'ts': ts_now(),
    #                 'data': payload,
    #             },
    #         }
    #         loop.create_task(write_line(jsonline_dumps(actout)))

    # assert issubclass(PublishContext, Context)

    # ctx = PublishContext()

    ReqProps = tuple(Request.__abstractmethods__)
    ReqTuple = namedtuple("ReqTuple", ReqProps)

    assert issubclass(ReqTuple, Request)

    async def handle_request(payload):
        # unpack requests
        req = ReqTuple(
            args=payload.pop('args', {}),
            callers=payload.pop('callers', []),
            hash=payload.pop('hash', ''),
            options=payload.pop('options', {}),
            user=payload.pop('user', ''),
        )
        if asyncio.iscoroutinefunction(handler.on_request):
            task = handler.on_request(ctx, req)
        else:
            task = loop.run_in_executor(
                get_default_threadpool(), handler.on_request, ctx, req
            )

        try:
            rsp, = await asyncio.gather(task, loop=loop)
            if isinstance(rsp, bytes):
                # encode bytes to base64 string quoted with '"'
                p = '"{}"'.format(base64.b64encode(rsp).decode('utf-8'))
            elif rsp:
                p = jsonline_dumps(rsp)
            else:
                # empty string
                p = '""'
        except Exception:
            await write_err(*sys.exc_info())
            return

        # send response back
        await write_line('{{"a":"rsp","p":{}}}'.format(p))

    # new message type
    MsgProps = tuple(Message.__abstractmethods__)
    MsgTuple = namedtuple("MsgTuple", MsgProps)

    assert issubclass(MsgTuple, Message)

    imsgq = asyncio.Queue(maxsize=1024)

    async def dispatch_message():
        while True:
            payload = await imsgq.get()
            try:
                message = MsgTuple(**payload)
                if asyncio.iscoroutinefunction(handler.on_request):
                    task = handler.dispatch(ctx, message)
                else:
                    task = loop.run_in_executor(
                        get_default_threadpool(), handler.dispatch, ctx, message
                    )

                await asyncio.gather(task, loop=loop, return_exceptions=True)
            except Exception:
                await write_err(*sys.exc_info())
            finally:
                imsgq.task_done()

    async def readloop():
        try:
            while True:
                line = await read_line()
                if not line:
                    logger.debug("istream closed")
                    return
                line = line.strip()
                if not line or line.startswith('#') or line.startswith('//'):
                    # skip comments
                    continue
                actin = json.loads(line)

                # unpack payload
                if 'p' in actin:
                    payload = actin['p']
                else:
                    payload = {}

                if actin['a'] == "req":
                    # handle response
                    loop.create_task(handle_request(payload))

                elif actin['a'] == 'emit':
                    # dispatch message, do not block main loop
                    imsgq.put_nowait(payload)
        except asyncio.CancelledError:
            return
        except Exception:
            await write_err(*sys.exc_info())

    async def mainloop():
        dispatcher = loop.create_task(dispatch_message())
        task_ref['reader'] = loop.create_task(readloop())

        await asyncio.gather(task_ref['reader'], imsgq.join(), loop=loop)
        dispatcher.cancel()

    return mainloop
