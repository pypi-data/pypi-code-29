from importlib import import_module


def pydy(cls, src: str = 'helper'):

    class Pydy(cls):
        pass

    mod = import_module(src)
    internals = mod.__dict__.items()
    method_names = [name for name, val in internals if callable(val)]

    for name in method_names:
        met = getattr(mod, name)
        setattr(Pydy, name, met)

    return Pydy
