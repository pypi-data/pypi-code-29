# -*- coding: utf-8 -*-

import ctypes
import os
import sys
from contextlib import contextmanager
from io import TextIOWrapper

if sys.platform.lower().startswith('win'):

    @contextmanager
    def stdout_redirector(fileobj):
        yield sys.stdout


else:

    libc = ctypes.CDLL(None)
    try:
        c_stdout = ctypes.c_void_p.in_dll(libc, 'stdout')
    except ValueError:
        c_stdout = ctypes.c_void_p.in_dll(libc, '__stdoutp')

    @contextmanager
    def stdout_redirector(fileobj):
        # The original fd stdout points to. Usually 1 on POSIX systems.
        original_stdout_fd = sys.stdout.fileno()

        def _redirect_stdout(to_fd):
            """Redirect stdout to the given file descriptor."""
            # Flush the C-level buffer stdout
            libc.fflush(c_stdout)
            # Flush and close sys.stdout - also closes the file descriptor (fd)
            sys.stdout.close()
            # Make original_stdout_fd point to the same file as to_fd
            os.dup2(to_fd, original_stdout_fd)
            # Create a new sys.stdout that points to the redirected fd
            sys.stdout = TextIOWrapper(
                buffer=os.fdopen(original_stdout_fd, mode='wb', buffering=0),
                line_buffering=True,
                write_through=True,
            )

        # Save a copy of the original stdout fd in saved_stdout_fd
        saved_stdout_fd = os.dup(original_stdout_fd)
        try:
            _redirect_stdout(fileobj.fileno())
            yield TextIOWrapper(
                buffer=os.fdopen(saved_stdout_fd, mode='wb', buffering=0),
                line_buffering=True,
                write_through=True,
            )
            _redirect_stdout(saved_stdout_fd)
            fileobj.flush()
        finally:
            os.close(saved_stdout_fd)


if __name__ == '__main__':
    with stdout_redirector(sys.stderr):
        print('hello word to stderr')

    print('again to stdout')

    '''
    $ python redstdout.py
    hello word to stderr
    again to stdout

    $ python redstdout.py 2>/dev/null
    again to stdout
    '''
