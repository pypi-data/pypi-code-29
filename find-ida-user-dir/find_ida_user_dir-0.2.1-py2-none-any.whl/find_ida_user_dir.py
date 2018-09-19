'''
Created on 14 Sep 2018

@author: Mike Thomas
'''
import os


def _find_windows():
    path = os.getenv("APPDATA")
    if path:
        return os.path.join(path, 'Hex-Rays', 'IDA Pro')
    return ""


def _find_starnix():
    path = os.path.expanduser("~")
    if path:
        return os.path.join(path, '.idapro')


def _add_subdir(path, subdir):
    return os.path.join(path, subdir)


def find_path(subdir=None):
    """Find the IDA user directory for the current user on the current platform.

    Returns the path to the IDA user directory. No guarantee is made of the
    existence of the directory, but is is the correct path as defined by the
    IDA documentation.

    If subdir is given then the path to that subdirectory of the IDA user
    directory is returned.
    """
    path = os.getenv("IDAUSR")
    if path:
        pass
    elif os.name == "nt":
        path = _find_windows()
    else:
        path = _find_starnix()
    if subdir is not None:
        path = os.pathsep.join(_add_subdir(single_path, subdir)
                               for single_path in path.split(os.pathsep))
    return path


def main():
    path = find_path()
    print path


if __name__ == '__main__':
    main()
