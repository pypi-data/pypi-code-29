"""
Functions available inside the configuration files
"""
import inspect
import os
import urllib.parse

from .loaders import load

# TODO get from internet?

__all__ = ['include_config', 'read']

def __relative_to_cwd(file_path: os.PathLike) -> str:
    """
    Gets the path to ``file_path`` relative to the current working dir so it can be read
    """
    frame = inspect.currentframe()
    try:
        # We have to go back to levels, the function that called this function and the configuration
        # file that called that function
        calling_frame = frame.f_back.f_back
        parent_filename = calling_frame.f_code.co_filename
    finally:
        del frame
    path = urllib.parse.urljoin(parent_filename, file_path)
    return path


def include_config(relative_path: os.PathLike):
    """
    Imports configuration from ``relative_path`` and appends it to the caller locals
    """
    # TODO: detect circles?
    path = __relative_to_cwd(relative_path)

    frame = inspect.currentframe()
    try:
        importer_locals = frame.f_back.f_locals
    finally:
        del frame
    
    imported_configuration = load(path)
    importer_locals.update(imported_configuration)


def read(file_path: os.PathLike) -> str:
    """
    Read the content of ``file_path`` and return it as a string.
    """
    path = __relative_to_cwd(file_path)
    with open(path, 'r') as file_object:
        content = file_object.read()
    return content