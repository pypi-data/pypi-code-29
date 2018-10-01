# coding=utf-8
"""
Path utilities
"""

import typing
from pathlib import Path


def ensure_path(*path: typing.Union[str, Path], must_exist: bool = True) -> Path:
    """
    Ensure path is a Path instance

    Args:
        path: path
        must_exist: if True, raises FileNotFoundError when path does not exist

    Returns: Path instance
    """
    _path = Path(*path).absolute()
    if must_exist and not _path.exists():
        raise FileNotFoundError(str(_path))
    return _path.absolute()


def ensure_file(*file_path: typing.Union[str, Path], must_exist: bool = True) -> Path:
    """
    Ensure path is a Path instance

    Args:
        file_path: path
        must_exist: if True, raises FileNotFoundError when path does not exist

    Returns: Path instance

    """
    _file_path = ensure_path(*file_path, must_exist=must_exist)
    if _file_path.exists():
        if not _file_path.is_file():
            raise TypeError(f'not a file: {str(_file_path.absolute())}')
    return _file_path


def ensure_dir(*dir_path: typing.Union[str, Path], must_exist: bool = True, create=False) -> Path:
    """
    Ensure path is a Path instance

    Args:
        dir_path: path
        must_exist: if True, raises FileNotFoundError when path does not exist
        create: create the directory if it doesn't exist (implies "must_exist == False")

    Returns: Path instance

    """
    must_exist = not create if create else must_exist
    _dir_path = ensure_path(*dir_path, must_exist=must_exist)
    if _dir_path.exists():
        if not _dir_path.is_dir():
            raise TypeError(f'not a directory: {str(_dir_path.absolute())}')
    else:
        if create:
            _dir_path.mkdir(parents=True)
    return _dir_path
