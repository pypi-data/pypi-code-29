import importlib

def get_class(class_path):
        bits = class_path.split('.')
        class_name = bits.pop()
        module_string = (".").join(bits)
        mod = importlib.import_module(module_string)
        return getattr(mod, class_name)

def get_client(path, **extra_data):
    '''
    client = get_client()
    '''
    return get_class(path)(**extra_data)
