# Copyright (c) Microsoft Corporation. All rights reserved.
"""Owner of core objects for the Python API"""
import sys
from asyncio import AbstractEventLoop
from .api import EngineAPI
from .messagehandler import AsyncMessageHandler
from .asynchelper import create_event_loop


class AppServices:
    """AppServices"""
    def __init__(self):
        self._event_loop = create_event_loop()
        message_co = AsyncMessageHandler.start_engine_process(self._event_loop)
        self._message_handler = self._event_loop.run_until_complete(message_co)
        self._engine_api = EngineAPI(self._message_handler, self._event_loop)
        self._telemetry_client = None

    @property
    def engine_api(self) -> EngineAPI:
        """Helper for sending and receiving messages from the engine process."""
        return self._engine_api

    @property
    def telemetry_client(self):
        """The current AppInsights telemetry client; may be None if AppInsights is not available."""
        if not hasattr(self, '_telemetry_client'):
            from .telemetry import create_telemetry_client
            self._telemetry_client = create_telemetry_client()
        return self._telemetry_client


_app_services = None

def _register_shutdown():
    def shutdown():
        event_loop = _app_services._event_loop
        message_handler = _app_services._message_handler
        if not event_loop.is_closed():
            event_loop.run_until_complete(message_handler.close())
            event_loop.close()
    import atexit
    atexit.register(shutdown)

    # This is to workaround the event loop closing issue for python==3.6.x.
    # Setting exception handler to default again is not suppose to do anything.
    # But only be doing so Python will not print out the ignored exception message on exit.
    def exception_handler(event_loop, context):
        event_loop.default_exception_handler(context)
    _app_services._event_loop.set_exception_handler(exception_handler)

def get_app_services():
    global _app_services
    if not _app_services:
        _app_services = AppServices()
        _register_shutdown()
    return _app_services
