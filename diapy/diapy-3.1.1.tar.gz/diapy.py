import base64
import getpass
import hashlib
import os
import pickle
import pickletools
import random
import re
from datetime import datetime
from cryptography.fernet import Fernet
import zlib

__version__ = '3.1.1'


def opened(func):
    def wrapper(*arg, **kw):
        if not arg[0].closed:
            return func(*arg, **kw)
        else:
            raise ValueError('File closed.')
    return wrapper


class Diary:
    # Class the instance which will be returned in get function.
    class Entry:
        def __init__(self, timestamp: int, content: str):
            self.timestamp = timestamp
            self.content = content

        def __str__(self):
            datetimeobj = datetime.fromtimestamp(self.timestamp)

            # Calculate date and weekday.
            date = datetimeobj.date()
            weekdays = ['Monday', 'Tuesday', 'Wednesday',
                        'Thursday', 'Friday', 'Saturday', 'Sunday']

            return str(datetimeobj) + ' ' + \
                weekdays[datetime.weekday(date)] + '\n' + self.content

        __repr__ = __str__

    def __init__(self, path: str):
        self.path = path
        self.closed = False

        self._input_pwd('Please input the main password: ')

        # If path doesn't exist, create a new file.
        if not os.path.exists(self.path):
            print('Creating a new file...')
            with open(self.path, 'wb'):
                pass

        with open(self.path, 'rb') as f:
            text = f.read()

        # Check if this is a new file.
        if text == b'':
            self._content = {}
        else:
            f = Fernet(self._key)
            self._content = pickle.loads(zlib.decompress(
                f.decrypt(base64.urlsafe_b64encode(text))))

    @opened
    def __getitem__(self, item: int):
        timestamp = self.key(item)
        if self._content.get(timestamp) is None:
            return None
        else:
            content = self._content[timestamp]
            return self.Entry(timestamp, content)

    def _input_pwd(self, text: str):
        pwd = getpass.getpass(text)

        self._key = base64.urlsafe_b64encode(
            hashlib.sha256(pwd.encode('utf-8')).digest())

    @opened
    def change_pwd(self):
        self._input_pwd('Please input the new password: ')

    @opened
    def close(self):
        f = Fernet(self._key)
        with open(self.path, 'wb') as file:
            # Dump, optimize, compress, encrypt, decode.
            file.write(base64.urlsafe_b64decode(f.encrypt(zlib.compress(
                pickletools.optimize(pickle.dumps(self._content, 4))))))
        self._key = None
        self._content = None
        self.closed = True

    @opened
    def key(self, date: int=None):
        table = {}
        for k in self._content.keys():
            # Convert to an 8 digit int
            d = int(datetime.fromtimestamp(
                k).date().strftime('%Y%m%d'))
            table[d] = k

        if date:
            return table[date]
        else:
            return list(table.keys())

    @opened
    def new(self, content: str, datetimeobj: datetime=None):
        if not datetimeobj:
            datetimeobj = datetime.now()

        time = int(datetimeobj.timestamp())
        date = int(datetime.fromtimestamp(
            time).date().strftime('%Y%m%d'))
        if date in self.key():
            print('You have written a diary today:')
            print(self[date])
            print('''
Do you want to overwrite, discard changes or merge them together?
(overwrite/discard/merge) Default: discard''')
            c = input()
            if c == 'overwrite':
                self._content.pop(self.key(date))
            elif c == 'merge':
                content = self[date].content + '\n' + content
                self._content.pop(self.key(date))
            else:
                return
        self._content[time] = content

        print(self[date])

    @opened
    def random(self):
        return self[random.choice(list(self.key()))]

    @opened
    def search(self, kw: str):
        for key in self._content.keys():
            if kw in self._content[key]:
                print(self[int(datetime.fromtimestamp(
                    key).date().strftime('%Y%m%d'))], end='\n\n')
