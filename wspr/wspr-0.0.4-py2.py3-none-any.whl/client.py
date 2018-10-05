# -*- coding: utf-8 -*-

import logging
import multiprocessing
import time
from collections import defaultdict
from pathlib import Path

from wspr.blob import Blob
from wspr.channel import Channel
from wspr.containers.address import Address
from wspr.containers.credentials import Credentials
from wspr.control.events import FullTreeEvent
from wspr.control.connection import Connection
from wspr.control.tasks import (
    Task,
    StartTask,
    ConnectTask,
    StopTask,
    FullTreeTask,
    MessageTask,
    PrivateMessageCommand
)
from wspr.protocol.packets import Packet
from wspr.user import User


class Mumble(multiprocessing.Process):
    """Mumble client library."""

    @classmethod
    def from_config(cls, configuration_file_path: Path):
        """"""
        raise NotImplemented

    def __init__(self, address: Address, credentials: Credentials, tasks: multiprocessing.Queue,
                 results: multiprocessing.Queue, logger: logging.Logger):
        """Create a new whisper Mumble thread, ready to connect to the server."""
        # Basic logging
        self._logger: logging.Logger = logger
        self._tasks: multiprocessing.Queue = tasks
        self._results: multiprocessing.Queue = results
        self._killed: multiprocessing.Event() = multiprocessing.Event()

        self._blobs: defaultdict = defaultdict(Blob)
        self._channels: defaultdict = defaultdict(Channel)
        self._users: defaultdict = defaultdict(User)

        self._address: Address = address
        self._credentials: Credentials = credentials

        super().__init__(name=f"whisper-{credentials.name}")

    def __handle_tasks(self, connection=None) -> None:
        """"""
        # Process incoming task commands
        while not self._tasks.empty():
            task: Task = self._tasks.get()
            if type(task) == StartTask:
                pass
            elif type(task) == ConnectTask:
                pass
            elif type(task) == StopTask:
                self._logger.debug("Stopping")
                self._killed.set()
            elif type(task) == FullTreeTask:
                self._results.put(FullTreeEvent(self._channels, self._users))
            elif type(task) == MessageTask:
                if connection:
                    p = task.get_packet()
                    connection.send(*p)
            elif type(task) == PrivateMessageCommand:
                if connection:
                    p = task.get_packet()
                    connection.send(*p)

    def __handle_packets(self, c):
        """"""
        packets: [Packet] = c.incoming_packets()
        for packet in packets:
            self._logger.debug(f"Incoming: {packet}")
            try:
                packet.update(c, self._results, self)
            except AttributeError:
                packet.handle(c, self._results)

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
        while not self._killed.is_set():
            # Handle tasks before we're connected
            self.__handle_tasks()
            # We have established a connection
            with Connection(self._address, self._credentials, self._logger) as c:
                self._logger.debug("Main loop")
                # Keep connection alive
                while not self._killed.is_set():
                    # Handle tasks while connected
                    self.__handle_tasks(c)
                    # Send ping and keep last time
                    c.send_ping()
                    # Process all incoming packets
                    self.__handle_packets(c)
                    time.sleep(0.1)
                self._logger.debug("Main loop ended")
            time.sleep(1)
