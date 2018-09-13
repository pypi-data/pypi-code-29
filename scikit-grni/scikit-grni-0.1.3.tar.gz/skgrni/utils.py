import numpy as _np
import collections as _collections
import functools as _functools
import pickle as _pickle
import inspect as _inspect
import os.path as _ospath
import re as _re
import unicodedata as _unicodedata

# Some of the functionality is fetched from here:
# https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize

tol = _np.finfo(_np.float32).eps
# tol = np.spacing(1e6)
confidence_alpha = 0.01


def memoize(obj):
    '''A memoizing function that works on functions, methods,
    or classes, and exposes the cache publicly.'''

    cache = obj.cache = {}

    @_functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer


class memoized():
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, _collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return _functools.partial(self.__call__, obj)


class Memorize(object):
    '''
    A function decorated with @Memorize caches its return
    value every time it is called. If the function is called
    later with the same arguments, the cached value is
    returned (the function is not reevaluated). The cache is
    stored as a .cache file in the current directory for reuse
    in future executions. If the Python file containing the
    decorated function has been updated since the last run,
    the current cache is deleted and a new cache is created
    (in case the behavior of the function has changed).
    '''
    def __init__(self, func):
        self.func = func
        self.set_parent_file()  # Sets self.parent_filepath and self.parent_filename
        self.__name__ = self.func.__name__
        self.set_cache_filename()
        if self.cache_exists():
            self.read_cache()  # Sets self.timestamp and self.cache
            if not self.is_safe_cache():
                self.cache = {}
        else:
            self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, _collections.Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            self.save_cache()
            return value

    def set_parent_file(self):
        """
        Sets self.parent_file to the absolute path of the
        file containing the memoized function.
        """
        rel_parent_file = _inspect.stack()[-1].filename
        self.parent_filepath = _ospath.abspath(rel_parent_file)
        self.parent_filename = _filename_from_path(rel_parent_file)

    def set_cache_filename(self):
        """
        Sets self.cache_filename to an os-compliant
        version of "file_function.cache"
        """
        filename = _slugify(self.parent_filename.replace('.py', ''))
        funcname = _slugify(self.__name__)
        self.cache_filename = filename + '_' + funcname + '.cache'

    def get_last_update(self):
        """
        Returns the time that the parent file was last
        updated.
        """
        last_update = _ospath.getmtime(self.parent_filepath)
        return last_update

    def is_safe_cache(self):
        """
        Returns True if the file containing the memoized
        function has not been updated since the cache was
        last saved.
        """
        if self.get_last_update() > self.timestamp:
            return False
        return True

    def read_cache(self):
        """
        Read a pickled dictionary into self.timestamp and
        self.cache. See self.save_cache.
        """
        with open(self.cache_filename, 'rb') as f:
            data = _pickle.loads(f.read())
            self.timestamp = data['timestamp']
            self.cache = data['cache']

    def save_cache(self):
        """
        Pickle the file's timestamp and the function's cache
        in a dictionary object.
        """
        with open(self.cache_filename, 'wb+') as f:
            out = dict()
            out['timestamp'] = self.get_last_update()
            out['cache'] = self.cache
            f.write(_pickle.dumps(out))

    def cache_exists(self):
        '''
        Returns True if a matching cache exists in the current directory.
        '''
        if _ospath.isfile(self.cache_filename):
            return True
        return False

    def __repr__(self):
        """ Return the function's docstring. """
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """ Support instance methods. """
        return _functools.partial(self.__call__, obj)


def _slugify(value):
    """
    Normalizes string, converts to lowercase, removes
    non-alpha characters, and converts spaces to
    hyphens. From http://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename-in-python
    """
    value = _unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = _re.sub(r'[^\w\s-]', '', value.decode('utf-8', 'ignore'))
    value = value.strip().lower()
    value = _re.sub(r'[-\s]+', '-', value)
    return value


def _filename_from_path(filepath):
    return filepath.split('/')[-1]


svd = memoize(_np.linalg.svd)
