# -*- coding: utf-8 -*-
from . import env
from .codec import register_codec
from .ctx import BaseContext
from .entry import load_ipython_extension
from .env import current_env, pop_env, pull_log, push_env, new_env
from .interface import Context, Message
from .version import git_commit, version


def invoke(endpoint: str, request=None, **kwargs):
    return current_env().context.invoke(endpoint, request, **kwargs)


def put_object(key: str, bytes_or_filelike, content_type='', expires=60, shared=False):
    return current_env().context.put_object(
        key, bytes_or_filelike, content_type, expires, shared
    )


def get_object(key: str):
    return current_env().context.get_object(key)


def remove_object(key: str):
    return current_env().context.remove_object(key)


def publish(topic: str, payload: dict):
    return current_env().context.publish(topic, payload)


def subscribe(topic: str, callback):
    return current_env().context.subscribe(topic, callback)


def ainvoke(endpoint: str, request=None, **kwargs):
    return current_env().context.ainvoke(endpoint, request, **kwargs)


def wait(*fs):
    return current_env().context.wait(*fs)


def log(s: str, *args, **kwargs):
    return current_env().context.log(s, *args, **kwargs)


def on(topic: str):
    def decorator(fn):
        subscribe(topic, fn)
        return fn

    return decorator


# context init
if env.__base_env.context is None:
    env.__base_env = env.__base_env.new(context=BaseContext(parent=object()))

del env

__all__ = [
    'ainvoke',
    'Context',
    'get_object',
    'invoke',
    'load_ipython_extension',
    'log',
    'Message',
    'new_env',
    'pop_env',
    'pull_log',
    'push_env',
    'put_object',
    'register_codec',
    'remove_object',
    'subscribe',
    'wait',
]
