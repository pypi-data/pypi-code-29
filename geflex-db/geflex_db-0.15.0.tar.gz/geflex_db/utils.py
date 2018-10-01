"""Abstract classes and tools"""
from abc import abstractmethod
from copy import deepcopy as dcopy
from types import FunctionType
from typing import Union

__all__ = ('DecoratedMeta', 'ObjectWrapperMeta', 'ObjectWrapperDecorated',
           'File', 'Unfier', 'DotDict', 'ContainerOfCallables')


class MetaWith__new__(type):
    @classmethod
    @abstractmethod
    def prepare_attrs(mcs, attrs):
        pass


class MethodsDecorator:
    def __init__(self, decorator, method_names):
        self.decorator = decorator
        self.method_names = method_names

    def __call__(self, func):
        return self.wrap(func)

    def __getattr__(self, item):
        return getattr(self.decorator, item)

    def __repr__(self):
        return f'{self.__class__}({self.decorator}, {self.method_names})'

    def wrap(self, func):
        return self.decorator(func)

    def wrap_all(self, cls):
        for method_name in self.method_names:
            method = getattr(cls, method_name)
            wrapped_method = self.wrap(method)
            setattr(cls, method_name, wrapped_method)


class DecoratedMeta(type):
    def __init__(cls, name, parents, attrs):
        super().__init__(name, parents, attrs)
        for func in attrs.values():
            if isinstance(func, staticmethod):
                func = func.__func__
            if isinstance(func, MethodsDecorator):
                func.wrap_all(cls)

    @staticmethod
    def decorate(*methods):
        if not isinstance(methods[0], str):
            methods = list(methods[0]) + list(methods[1:])

        def wrap(func):
            return MethodsDecorator(func, methods)
        return wrap


class ObjectWrapperMeta(MetaWith__new__):
    magic_methods = ['__repr__', '__str__', '__bytes__', '__format__',
                     '__iter__', '__next__', '__reversed__', '__call__',
                     '__hash__', '__len__', '__contains__', '__getitem__',
                     '__setitem__', '__delitem__', '__missing__', '__add__',
                     '__sub__', '__mul__', '__truediv__', '__floordiv__',
                     '__mod__', '__divmod__', '__pow__', '__lshift__',
                     '__rshift__', '__and__', '__xor__', '__or__', '__radd__',
                     '__rsub__', '__rmul__', '__rtruediv__', '__rfloordiv__',
                     '__rmod__', '__rdivmod__', '__rpow__', '__rlshift__',
                     '__rrshift__', '__rand__', '__rxor__', '__ror__',
                     '__neq__', '__pos__', '__abs__', '__invert__',
                     '__complex__', '__int__', '__float__', '__round__',
                     '__ceil__', '__floor__', '__trunc__', '__a_list__',
                     '__eq__', '__ne__', '__lt__', '__le__', '__gt__',
                     '__ge__', '__bool__',
                     '__getstate__', '__reduce__', '__reduce_ex__',
                     '__getnewargs__', '__setstate__', '__enter__', '__exit__']

    @classmethod
    def prepare_attrs(mcs, attrs):
        for method_name in ObjectWrapperMeta.magic_methods:
            if method_name not in attrs:
                func = attrs[method_name] = mcs.new_method(method_name)
                func.__name__ = method_name
        if '__getattr__' not in attrs:
            attrs['__getattr__'] = mcs.new_method('__getattribute__')
        return attrs

    @staticmethod
    def new_method(method_name):
        def _new_method(self, *args, **kwargs):
            obj = self.__key__()
            method = getattr(obj.__class__, method_name)
            return method(obj, *args, **kwargs)
        return _new_method

    def __new__(mcs, name, parents, attrs):
        attrs = mcs.prepare_attrs(attrs)
        return super().__new__(mcs, name, parents, attrs)


class ObjectWrapperDecorated(DecoratedMeta, ObjectWrapperMeta):
    def __init__(cls, name, parents, attrs):
        super().__init__(name, parents, attrs)


class File(metaclass=DecoratedMeta):
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


class Unfier:
    def __call__(self, obj=None, **kwargs):
        new = dcopy(self)
        if obj is not None:
            for attr, value in obj.__dict__.items():
                if not isinstance(value, FunctionType):
                    setattr(new, attr, dcopy(value))
        for attr, value in kwargs:
            setattr(new, attr, value)
        return new


class DotDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, value in self.items():
            if type(value) is dict:
                self[name] = DotDict(value)
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class ContainerOfCallables(dict):
    def __init__(self, *args, **kwargs):
        # noinspection PyBroadException
        try:
            super().__init__(*args, **kwargs)
        except:
            super().__init__({c.__name__: c for c in args[0]}, **kwargs)

    def append(self, obj: Union[type, FunctionType]):
        self[obj.__name__] = obj

    def remove(self, obj: Union[type, FunctionType]):
        del self[obj.__name__]
