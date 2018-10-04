from contextlib import contextmanager

import os


@contextmanager
def location(target_path: str):
    """
    Context manager that facilitates switching to a directory.
    """
    old_path = os.getcwd()
    os.chdir(target_path)
    yield
    os.chdir(old_path)