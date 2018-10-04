## pylint: disable=R0903, C0103, W0401, C0111, C0326
# provide decorators for functions that reads a folder/file name/list as the only argument
import sys
from typing import Optional, TypeVar, Union, List, Callable

try:
    from .qtopen import *
    multi_folder = True
except ImportError:
    try:
        from .wxopen import *
        multi_folder = True
    except ImportError:
        from .tkopen import *
        multi_folder = False


T = TypeVar('T')


def filter_args(argv) -> Union[str, List[str]]:
    if len(argv) == 1:
        return list()
    flag = None
    flags = list()  # flags
    args = list()  # locational args
    for arg in argv[1:]:
        if flag is not None:
            if arg.startswith('-'):
                flags.append((flag, ''))
                flag = arg[1:]
            else:
                flags.append((flag, arg))
                flag = None
        elif arg.startswith('-'):
            flag = arg[1:]
        else:
            args.append(arg)
    return args if args else list()


class FolderSelector(object):
    # Folder(s)Selector doesn't take arguments, so the init argument is the callable
    __func__ = folder_to_open

    def __init__(self, func: Callable[[str], T]):
        self.func = func

    def __call__(self)-> T:
        args = filter_args(sys.argv)
        if not args:
            args = type(self).__func__()
        else:
            args = args[0]
        return self.func(args)


class SaveFolderSelector(FolderSelector):
    __func__ = folder_to_save


class FoldersSelector(object):
    def __init__(self, func: Callable[[List[str]], T]):
        self.func = func

    def __call__(self) -> T:
        args = filter_args(sys.argv)
        if not args:
            if multi_folder:
                args = folders_to_open()
            else:
                print("Error! MultiFolder selection requires wxpython. Falling back to single folder selection.")
                args = [folder_to_open()]
        return self.func(args)


class FilesSelector(object):
    __func__ = files_to_open

    def __init__(self, filters: Optional[List[str]]=list()):
        self.filters = filters

    def __call__(self, func: Callable[[List[str]], T]) -> Callable[[], T]:
        def temp():
            filters = list(self.filters)
            args = filter_args(sys.argv)
            if not args and filters is None:
                raise ValueError("supply a list of files or file filters in argument or command line arguments")
            filters += args
            files = [x for x in filters if x.startswith('.') and 3 < len(x) < 4]
            filters = list(set(filters) - set(files))
            # noinspection PyCallByClass
            return func(files + type(self).__func__(filters))
        return temp


class FileSelector(object):
    __func__ = file_to_open

    def __init__(self, filters: Optional[List[str]]=list()):
        self.filters = filters

    def __call__(self, func: Callable[[str], T]) -> Callable[[], T]:
        def temp():
            filters = list(self.filters)
            args = filter_args(sys.argv)
            if not args and filters is None:
                raise ValueError("supply a list of files or file filters in argument or command line arguments")
            filters += args
            files = [x for x in filters if x.startswith('.') and 3 < len(x) < 4]
            if len(files) > 1:
                raise ValueError("Only one file can be opened at a time")
            elif len(files) == 1:
                return func(files[0])
            else:  # len(files) == 0
                filters = list(set(filters) - set(files))
                # noinspection PyCallByClass
                return func(type(self).__func__(filters))
        return temp


class SaveSelector(FileSelector):
    __func__ = file_to_save
