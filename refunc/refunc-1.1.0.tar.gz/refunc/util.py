# -*- coding: utf-8 -*-

import asyncio
import functools
import json
import logging
import mimetypes
import os
import signal
import sys
import threading
import weakref
from asyncio import Task, TimeoutError
from os.path import expanduser
from threading import Thread

homedir = expanduser("~")

sys_logger = logging.getLogger("refunc")

# forwarding remote logs
remote_logger = logging.getLogger("refunc-logs-receiver")

__configured = False


def jsonline_dumps(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def enable_logging(level=logging.DEBUG):
    if not __configured:
        _config_loggers()  # ensure loggers are configured

    sys_logger.setLevel(level)
    remote_logger.setLevel(level)

    sys_logger.propagate = True
    remote_logger.propagate = True


def _config_loggers():
    """
    setup refunc's logger with given level and streaming to stderr
    """
    global __configured

    if __configured:
        return

    sch = logging.StreamHandler(sys.stderr)
    sch.setFormatter(logging.Formatter('[fn %(levelname).1s] %(message)s'))
    sys_logger.handlers = []
    sys_logger.addHandler(sch)
    sys_logger.propagate = False

    rch = logging.StreamHandler(sys.stderr)
    rch.setFormatter(logging.Formatter('[  >>] %(message)s'))
    remote_logger.handlers = []
    remote_logger.addHandler(rch)
    remote_logger.propagate = False

    __configured = True


_config_loggers()

if os.getenv('REFUNC_DEBUG', "false").lower() in ["1", "true"]:
    enable_logging()


def content_type_by_name(name):
    """根据文件名，返回Content-Type。"""
    ext = os.path.splitext(name)[1].lower()
    if ext in _EXTRA_TYPES_MAP:
        return _EXTRA_TYPES_MAP[ext]

    return mimetypes.guess_type(name)[0]


_EXTRA_TYPES_MAP = {
    ".js": "application/javascript",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".xltx": "application/vnd.openxmlformats-officedocument.spreadsheetml.template",
    ".potx": "application/vnd.openxmlformats-officedocument.presentationml.template",
    ".ppsx": "application/vnd.openxmlformats-officedocument.presentationml.slideshow",
    ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    ".sldx": "application/vnd.openxmlformats-officedocument.presentationml.slide",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".dotx": "application/vnd.openxmlformats-officedocument.wordprocessingml.template",
    ".xlam": "application/vnd.ms-excel.addin.macroEnabled.12",
    ".xlsb": "application/vnd.ms-excel.sheet.binary.macroEnabled.12",
    ".apk": "application/vnd.android.package-archive",
}


def _get_data_size(data):
    if hasattr(data, '__len__'):
        return len(data)

    if hasattr(data, 'len'):
        return data.len

    if hasattr(data, 'seek') and hasattr(data, 'tell'):

        def file_object_remaining_bytes(fileobj):
            current = fileobj.tell()

            fileobj.seek(0, os.SEEK_END)
            end = fileobj.tell()
            fileobj.seek(current, os.SEEK_SET)

            return end - current

        return file_object_remaining_bytes(data)

    return None


def to_bytes(data):
    """
    only valid for python3
    """
    if isinstance(data, str):
        return data.encode(encoding='utf-8')
    else:
        return data


__threadpool = None


def get_default_threadpool():
    global __threadpool
    if __threadpool is None:
        # shared executing pool with #workers = cpu count
        import multiprocessing
        from concurrent.futures import ThreadPoolExecutor

        max_workers = multiprocessing.cpu_count()
        __threadpool = ThreadPoolExecutor(max_workers=max(max_workers, 4))
    return __threadpool


_loop_lock = threading.Lock()
_running_loop: asyncio.BaseEventLoop = None
_pending_futures = weakref.WeakSet()


def add_future_to_cancel_list(fs):
    global _pending_futures
    with _loop_lock:
        _pending_futures.add(fs)
    return fs


def start_or_get_running_loop(
    fn=None, loop: asyncio.BaseEventLoop = None, run_in_backgroud=False
):
    global _running_loop

    with _loop_lock:
        if _running_loop and _running_loop.is_running():
            return _running_loop

    if loop is None:
        if run_in_backgroud:
            # ensure we got a valid event loop for background
            loop = asyncio.new_event_loop()
        else:
            # try to get loop in current thread,
            # may raise RuntimeError
            loop = asyncio.get_event_loop()

    if loop.is_running() and run_in_backgroud:
        # if given loop is running,
        # but we need a background loop,
        # override the running loop
        loop = asyncio.new_event_loop()

    def __cleanup_pendings():
        with _loop_lock:
            global _pending_futures
            while len(_pending_futures) > 0:
                f = _pending_futures.pop()
                f.cancel()
        if not run_in_backgroud:
            raise KeyboardInterrupt()

    # install signal handlers
    if not sys.platform.lower().startswith('win'):
        for sig in ('SIGINT', 'SIGTERM'):
            loop.add_signal_handler(getattr(signal, sig), __cleanup_pendings)

    def handle_exception(loop, context):
        exc = context.get('exception')
        if isinstance(exc, (TimeoutError, OSError)):
            sys_logger.error('{}: {}'.format(context['message'], exc))
            return
        loop.default_exception_handler(context)

    loop.set_exception_handler(handle_exception)

    if loop.is_running():
        with _loop_lock:
            _running_loop = loop
            return _running_loop

    f = loop.run_forever
    if fn:
        if not asyncio.iscoroutinefunction(fn):
            raise ValueError('fn must be a coroutine')
        f = functools.partial(loop.run_until_complete, fn())

    if not run_in_backgroud:
        with _loop_lock:
            _running_loop = loop
        f()
        if loop.is_running():
            return loop

        with _loop_lock:
            _running_loop = None

    # start in background thread
    with _loop_lock:
        t = Thread(target=f, name='background_main_loop')
        t.daemon = True
        _running_loop = loop
        t.start()

    return loop
