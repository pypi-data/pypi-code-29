from importlib import import_module


def f2m(cls, src: str = 'helper'):

    class F2M(cls):
        pass

    mod = import_module(src)
    internals = mod.__dict__.items()
    method_names = [name for name, val in internals if callable(val)]

    for name in method_names:
        met = getattr(mod, name)
        setattr(F2M, name, met)

    return F2M
