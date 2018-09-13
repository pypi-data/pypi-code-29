from functools import wraps


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


def action(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if hasattr(self, "actions"):
            self.actions([func, args, kwargs])
        func(self, *args, **kwargs)
    return wrapper
