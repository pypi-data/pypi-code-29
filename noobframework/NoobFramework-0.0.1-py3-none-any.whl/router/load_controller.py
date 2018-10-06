import sys


def load_controller(string):
    module_name, func = string.split(':', 1)
    __import__(module_name)
    module = sys.modules[module_name]
    func = getattr(module, func)

    return func
