# -*- coding: utf-8 -*-

import logging
import multiprocessing

from wspr.containers.address import Address
from wspr.containers.credentials import Credentials


class Mumble(multiprocessing.Process):
    """Mumble client library."""

    def __init__(self, address: Address, credentials: Credentials, tasks: multiprocessing.Queue,
                 results: multiprocessing.Queue, logger: logging.Logger):
        """Create a new whisper Mumble thread, ready to connect to the server."""
        # Basic logging
        self._logger: logging.Logger = logger
        self._tasks: multiprocessing.Queue = tasks
        self._results: multiprocessing.Queue = results
        self._killed: multiprocessing.Event() = multiprocessing.Event()

        self._address: Address = address
        self._credentials: Credentials = credentials

        super().__init__(name=f"whisper-{credentials.name}")

    def run(self) -> None:
        """Start the execution of the process. Will connect to the server and start the main loop."""
        try:
            self.__loop()
        except Exception as ex:
            self._logger.critical("Error:")
            self._logger.exception(ex)
        finally:
            self._logger.debug("Shutting down")

    def __loop(self) -> None:
        """"""
        raise NotImplemented
