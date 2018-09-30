from importlib import import_module


def scattr(cls, src: str = 'helper'):

    class SubClassAttributes(cls):
        pass

    mod = import_module(src)
    internals = mod.__dict__.items()
    method_names = [name for name, val in internals if callable(val)]

    for name in method_names:
        met = getattr(mod, name)
        setattr(SubClassAttributes, name, met)

    return SubClassAttributes
