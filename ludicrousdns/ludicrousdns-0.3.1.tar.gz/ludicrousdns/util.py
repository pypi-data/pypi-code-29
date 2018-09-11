import asyncio
import re


def read_nameservers_from_file(filename):
    with open(filename) as f:
        return read_nameservers_from_string(f.read())


def read_nameservers_from_string(s):
    nameservers = [re.sub(r'#.*$', '', line).strip() for line in s.splitlines()]
    return [ns for ns in nameservers if ns != '']


class QueueClosed(Exception):
    pass


class ClosableQueue(asyncio.Queue):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._closed = False

    def close(self):
        self._closed = True

    async def put(self, item):
        if self._closed:
            raise QueueClosed

        await super().put(item)

    async def get(self):
        if self.empty() and self._closed:
            raise QueueClosed

        return await super().get()
