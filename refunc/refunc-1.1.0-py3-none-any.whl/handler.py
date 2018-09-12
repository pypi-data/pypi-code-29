# -*- coding: utf-8 -*-

import logging
import os
from collections import defaultdict

from .codec import get_codec
from .ctx import BaseContext
from .env import current_env, new_env, use_ctx
from .interface import Context, Handler, Message, Request
from .loader import compile_func

__all__ = ["SourceHandler"]

logger = logging.getLogger("loader")


class SourceHandler(Handler):
    def __init__(
        self, src: str, filename: str = None, endpoint: str = "", scope: dict = {}
    ):
        if not src:
            if not filename:
                raise ValueError("source code or filename must be set")
            with open(filename) as f:
                scope["__file__"] = os.path.abspath(filename)
                src = f.read()
            filename = os.path.basename(filename)
            logger.debug("loading from {}".format(filename))
        else:
            logger.debug("loading from source code")

        listeners = defaultdict(lambda: [])

        class ListenerGetter(BaseContext):
            def subscribe(self, topic: str, callback):
                logger.debug('got listener for "{}"'.format(topic))
                listeners[topic.lower()].append(callback)

        with use_ctx(ListenerGetter()):
            assert scope is not None

            import refunc
            from .interface import Context, Message

            scope.update({"refunc": refunc, "Context": Context, "Message": Message})
            scope = compile_func(src, scope, filename)

        # set endpoint, maybe override by context
        if endpoint:
            self._endpoint = endpoint
        elif hasattr(current_env().context, "endpoint"):
            self._endpoint = getattr(current_env().context, "endpoint")
        elif current_env().get("endpoint", ""):
            self._endpoint = current_env().get("endpoint")
        else:
            self._endpoint = current_env().name

        if "on_request" in scope and hasattr(scope["on_request"], "__call__"):
            self._req_func = scope["on_request"]
        else:

            def empty_req_handler(ctx: Context, req: Request):
                logger.error("empty handler got payload: {}".format(req))
                raise NotImplementedError("missing request handler")

            self._req_func = empty_req_handler
            logger.debug("missing request handler")

        # any message not captured by specific callback will use this
        if "on_messages" in scope and hasattr(scope["on_messages"], "__call__"):
            self._msg_func = scope["on_messages"]
        else:

            def empty_listener(ctx: Context, msg: Message):
                logger.debug("recv: {}".format(msg))

            self._msg_func = empty_listener

        self._listeners = listeners
        logger.info("got #{} listeners".format(len(listeners)))

    @property
    def endpoint(self) -> str:
        return self._endpoint

    def dispatch(self, ctx: Context, msg: Message):
        """
        dispatch event on `topic` with `msg`
        """
        callbacks = self._listeners[msg.topic.lower()]
        if not callbacks:
            self._msg_func(ctx, msg)
            return

        for cb in callbacks:
            cb(ctx, msg)

    def on_request(self, ctx: Context, req: Request):
        """
        handle request with payload
        """
        env = current_env()
        log_endpoint = req.options.get("logEndpoint")
        overides = {
            "context": ctx,
            "callers": req.callers,
            "pull_logs": bool(req.options.get("logging", env.pull_logs))
            or log_endpoint,
            # extras
            "log_endpoint": log_endpoint,
            "user": req.user,
            "raw_request": req,
        }

        with new_env(env, **overides):
            return get_codec(self.endpoint).to_bytes(self._req_func(ctx, req.args))


assert issubclass(SourceHandler, Handler)
