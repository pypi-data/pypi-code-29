# Copyright (c) Microsoft Corporation. All rights reserved.
"""Send and receive messages from the engine"""
import os
import sys
import asyncio.subprocess
import asyncio
import copy
from uuid import UUID, uuid1
import json
from enum import Enum
from dotnetcore2 import runtime


# pylint: disable=line-too-long
class CustomEncoder(json.JSONEncoder):
    """Custom Encoding"""
    # pylint: disable=E0202
    def default(self, o):
        if isinstance(o, UUID):
            return str(o)
        if isinstance(o, Enum):
            return o.value
        if hasattr(o, 'to_pod'):
            return o.to_pod()
        if hasattr(o, '__dict__'):
            return {CustomEncoder._to_camel_case(k): v for k, v in vars(o).items()}
        return json.JSONEncoder.default(self, o)

    @staticmethod
    def _to_camel_case(value: str):
        first, *others = value.lstrip('_').split('_')
        return ''.join([first.lower(), *map(str.title, others)])


class AsyncMessageHandler:
    """asyncio connection to local engine process."""
    def __init__(self, stream_reader, stream_writer, process, event_loop):
        self._stream_reader = stream_reader
        self._stream_writer = stream_writer
        self._process = process
        self._last_message_id = 0
        self._event_loop = event_loop

    @staticmethod
    async def start_engine_process(event_loop: asyncio.AbstractEventLoop):
        """start the engine process and connect to stdio"""
        engine_args = json.dumps({
            'debug': 'false',
            'firstLaunch': 'false',
            'sessionId': str(uuid1()),
            'invokingPythonPath': sys.executable
        }).replace("\"", "'")

        engine_path = AsyncMessageHandler._get_engine_path()
        dependencies_path = runtime.ensure_dependencies()
        dotnet_path = runtime.get_runtime_path()
        env = copy.copy(os.environ)
        if dependencies_path is not None:
            env['LD_LIBRARY_PATH'] = dependencies_path
        base_command = '"{command}" "{path}" "{args}"' if sys.platform == 'win32' \
            else '\'{command}\' \'{path}\' "{args}"'
        process = await asyncio.create_subprocess_shell(
            base_command.format(command=dotnet_path,
                                path=engine_path,
                                args=engine_args),
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.DEVNULL,  # Hide spurious dotnet errors (Vienna:45714) TODO: collect Errors
            loop=event_loop,
            limit=5 * 1024 * 1024,
            env=env)

        stream_writer = process.stdin
        stream_reader = process.stdout
        return AsyncMessageHandler(stream_reader, stream_writer, process, event_loop)

    @staticmethod
    def _get_engine_path():
        engine_dll = "Microsoft.DPrep.Execution.EngineHost.dll"
        current_folder = os.path.dirname(os.path.realpath(__file__))
        engine_path = os.path.join(current_folder, 'bin', engine_dll)
        return engine_path

    async def send_message(self, op_code: str, message: object) -> int:
        """Send message to the engine"""
        self._last_message_id += 1
        message_id = self._last_message_id
        await self.write_line(json.dumps({
            "messageId": message_id,
            "opCode": op_code,
            "data": message
        }, cls=CustomEncoder))
        return message_id

    async def write_line(self, line: str):
        """write line the the engine stdio"""
        self._stream_writer.write(line.encode())
        self._stream_writer.write("\n".encode())
        await self._stream_writer.drain()

    async def read_line(self):
        """read line from the engine stdio"""
        string = None
        while string is None:
            line = await self._stream_reader.readline()
            string = line.decode()
            if len(string) == 0 or string[0] != '{':
                string = None

        parsed = None
        try:
            parsed = json.loads(string)
        finally:
            if parsed is None:  # Exception is being thrown
                print("Line read from engine could not be parsed as JSON. Line:")
                try:
                    print(string)
                except UnicodeEncodeError:
                    print(bytes(string, 'utf-8'))
        return parsed

    async def close(self):
        """Close the underlying process"""
        self._process.terminate()
        await self._process.wait()
