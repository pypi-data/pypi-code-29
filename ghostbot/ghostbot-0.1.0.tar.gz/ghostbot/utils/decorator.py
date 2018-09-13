from functools import wraps
# FIXME resolve problem of package, error occurred when "from ghostbot import Ghostbot"
import ghostbot


# def timeout(duration=None):
#     def outer(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#            # TODO
#            return func(*args, **kwargs)
#        return inner
#    return outer

def classproperty(func):
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)
    return ClassPropertyDecorator(func)


class ClassPropertyDecorator(object):

    def __init__(self, callback):
        self.callback = callback

    def __get__(self, obj, class_=None):
        if class_ is None:
            class_ = type(obj)
        return self.callback.__get__(obj, class_)()


def api(func):
    @wraps(func)
    def decorator(self, *args, **kwargs):
        if hasattr(self, "api_calls"):
            self.api_calls([func, args, kwargs])
        func(self, *args, **kwargs)
    return decorator


def action(uri, is_generator=False):
    def decorator(func):
        class_name, method_name = func.__qualname__.split(".")
        ghostbot.Ghostbot.actions(uri, class_name, method_name, is_generator)
        return func
    return decorator
