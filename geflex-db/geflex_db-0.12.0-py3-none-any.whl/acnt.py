"""Abstract classes and tools"""
from abc import abstractmethod
from copy import deepcopy as dcopy
from types import FunctionType
from typing import Union


__all__ = 'FileMeta', 'MagicMethodsMeta', 'File', 'Combiner', 'Dotdict', 'SafeDatatypesContainer'


class FileMeta(type):
    wrapper_names = ('change_plus', 'saving_off', 'save_copies')

    def __init__(cls, name, parents, attrs):
        super().__init__(name, parents, attrs)
        for wrapper_name in FileMeta.wrapper_names:
            if f'{wrapper_name}_methods' in cls.__dict__:
                for method in getattr(cls, f'{wrapper_name}_methods'):
                    setattr(cls, method, getattr(cls, f'_{wrapper_name}')(getattr(cls, method)))


class MagicMethodsMeta(type):
    magic_methods = (
        'repr', 'str', 'bytes', 'format'
        'iter', 'next', 'reversed',
        'call', 'hash'
        'len', 'contains',
        'getitem', 'setitem', 'delitem', 'missing'
        'add', 'sub', 'mul', 'truediv', 'floordiv',
        'mod', 'divmod', 'pow', 'lshift', 'rshift',
        'and', 'xor', 'or',
        'radd', 'rsub', 'rmul', 'rtruediv', 'rfloordiv',
        'rmod', 'rdivmod', 'rpow', 'rlshift', 'rrshift', 'rand', 'rxor', 'ror',
        'neq', 'pos', 'abs', 'invert', 'complex', 'int',
        'float', 'round', 'ceil', 'floor', 'trunc', 'a_list',
        'eq', 'ne', 'lt', 'le', 'gt', 'ge', 'bool',
        'copy', 'deepcopy', 'getstate', 'reduce',
        'reduce_ex', 'getnewargs', 'setstate',
        'enter', 'exit',
    )

    @staticmethod
    def new_method(method_name):
        def _new_method(self, *args, **kwargs):
            return self.__key__().__getattribute__(method_name)(*args, **kwargs)
        return _new_method

    def __new__(mcs, name, parents, attrs):
        for method_name in MagicMethodsMeta.magic_methods:
            method_name = f'__{method_name}__'
            attrs[method_name] = mcs.new_method(method_name)
        attrs['__getattr__'] = mcs.new_method('__getattribute__')
        return super().__new__(mcs, name, parents, attrs)


class File(metaclass=FileMeta):
    def __init__(self):
        pass

    @abstractmethod
    def __del__(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass

    @abstractmethod
    def read(self, path=None):
        pass

    @abstractmethod
    def loads(self, data: str):
        pass

    @abstractmethod
    def save(self, path=None):
        pass

    @abstractmethod
    def dumps(self, obj=None):
        pass


class Combiner:
    def __call__(self, obj, **kwargs):
        new = dcopy(self)
        for attr, value in obj.__dict__.items():
            if not isinstance(value, FunctionType):
                setattr(new, attr, value)
        for attr, value in kwargs:
            setattr(new, attr, value)
        return new


class Dotdict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, value in self.items():
            if type(value) is dict:
                self[name] = Dotdict(value)
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class SafeDatatypesContainer(dict):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
        except:
            super().__init__({c.__name__: c for c in args[0]}, **kwargs)

    def append(self, obj: Union[type, FunctionType]):
        self[obj.__name__] = obj

    def remove(self, obj: Union[type, FunctionType]):
        del self[obj.__name__]
