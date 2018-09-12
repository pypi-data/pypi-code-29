# -*- coding: utf-8 -*-

import asyncio
import importlib
import logging
import os
import sys
import time
import traceback

from .ctx import LocalExecContext, LocalHandlerContext
from .dotenv import dotenv_values
from .env import current_env, pop_env, push_env, use_ctx
from .errors import ResultError
from .handler import SourceHandler
from .interface import Handler
from .io import new_ioloop
from .redstdout import stdout_redirector
from .util import jsonline_dumps, start_or_get_running_loop

logger = logging.getLogger('refunc')


def load(mp: str) -> Handler:
    def which(mp):
        def is_ok(fpath):
            return os.path.isfile(fpath)

        fpath = os.path.split(mp)[0]
        if fpath:
            if is_ok(mp):
                return mp
        else:
            for path in [os.getcwd()] + os.environ["PATH"].split(os.pathsep):
                fpath = os.path.join(path.strip('"'), mp)
                if is_ok(fpath):
                    return fpath

        raise ValueError('cannot find module {}'.format(mp))

    t0 = time.time()  # nopep8

    filename = os.path.abspath(which(mp))
    targetdir = os.path.dirname(filename)
    sys.path.insert(0, targetdir)
    os.chdir(targetdir)

    handler = SourceHandler(
        src="", endpoint=current_env().name, filename=filename  # load from file
    )

    logger.info(f'loaded: {mp}, using {1000 * (time.time() - t0):.4f}ms')

    return handler


def run_from_handler(handler_factory):
    """
    run from a handler factory
    """

    def write_error(sys_stdout, et, e: Exception, tb):
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
        sys_stdout.write(jsonline_dumps({'a': 'err', 'p': msg}) + "\r\n")
        sys_stdout.flush()

    with stdout_redirector(sys.stderr) as sys_stdout:
        try:
            # get event loop in main thread
            loop = asyncio.get_event_loop()
            ioloop = new_ioloop(
                current_env().context,
                handler_factory(),
                ins=sys.stdin,
                outs=sys_stdout,
                loop=loop,
            )
            start_or_get_running_loop(ioloop, run_in_backgroud=False)
        except KeyboardInterrupt as e:
            logger.debug("caught keyboard interrupt, exiting")
            write_error(sys_stdout, None, e, None)
            loop.stop()
        except RuntimeError as e:
            if f'{e}'.find('Event loop stopped before Future completed') != -1:
                write_error(sys_stdout, *sys.exc_info())
        except Exception:
            write_error(sys_stdout, *sys.exc_info())
        finally:
            logger.debug("loader exited")
            sys_stdout.flush()
            sys.stderr.flush()
            os._exit(0)


def run_from_file():

    if len(sys.argv) == 2:
        run_from_handler(lambda: load(sys.argv[1]))
    else:
        print(
            '''
usage:
$ {} /func/path
        '''.format(
                os.path.basename(sys.argv[0])
            )
        )
        os._exit(1)


def run_from_file_dev():
    if len(sys.argv) == 3:
        endpoint, filename = sys.argv[1], sys.argv[2]
    elif len(sys.argv) == 2:
        endpoint, filename = '', sys.argv[1]
    else:
        print(
            '''
usage:
$ {} [ns/name] /func/path
        '''.format(
                os.path.basename(sys.argv[0])
            )
        )
        os._exit(1)

    # insert dir context
    filename = os.path.abspath(filename)
    targetdir = os.path.dirname(filename)
    dotenvfile = os.path.join(targetdir, '.env')
    if os.path.exists(dotenvfile):
        logger.info('loading envrions from .env')
        environs = dotenv_values(dotenvfile)
        for k, v in environs.items():
            os.environ[k] = v
    sys.path.insert(0, targetdir)
    os.chdir(targetdir)
    run_src_dev(endpoint, filename=filename)


def run_src_dev(endpoint: str = "", src: str = "", filename: str = ""):
    scope = {'__name__': '__refunc_dev__'}
    ctx = LocalExecContext(endpoint, scope, current_env().context)
    with use_ctx(ctx):
        return SourceHandler(src, filename, endpoint=endpoint, scope=scope)


def load_ipython_extension(ipython):
    """call by ipython"""
    ipython.register_magic_function(run_ipython_cell, 'line_cell', 'refunc')


def run_ipython_cell(line, cell=None):
    args = line.split()
    if len(args) == 0:
        raise ValueError("'%%%%load_ext ns/func' is needed")
    endpoint = args[0]
    env = current_env()
    if isinstance(env.context, LocalHandlerContext) and getattr(
        env.context, '__refunc_magic', False
    ):
        pop_env()

    # generate handler from cell
    h = run_src_dev(endpoint, cell, 'cell')
    # mark this a magic
    setattr(h, '__refunc_magic', True)
    env = env.new(context=LocalHandlerContext(h))
    push_env(env)


__all__ = ['load', 'run_from_file', 'run_from_file_dev', 'load_ipython_extension']
