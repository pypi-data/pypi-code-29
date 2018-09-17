"""
Functions available inside the configuration files
"""
import inspect
import os
import urllib.parse

from .loaders import load

__all__ = ['include_config']

def include_config(parent_config_path:os.PathLike, relative_path: os.PathLike):
    """
    Imports configuration from ``filename`` and appends it to the caller locals
    """
    # TODO: detect circles?
    path = urllib.parse.urljoin(parent_config_path, relative_path)

    frame = inspect.currentframe()
    try:
        importer_locals = frame.f_back.f_locals
    finally:
        del frame
    
    imported_configuration = load(path)
    importer_locals.update(imported_configuration)