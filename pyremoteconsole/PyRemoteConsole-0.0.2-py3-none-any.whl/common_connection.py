try:
    from prawframe.obfuscation import Scrambler
except ImportError:
    from .obfuscation import Encryptor


def bytes_packet(_bytes, termination_string=']'):
    """
    Create a packet containing the amount of bytes for the proceeding data.

    :param _bytes:
    :param termination_string:
    :return:
    """

    return '{}{}'.format(len(_bytes), termination_string)


def scrambles_input_unscrambles_output(func):
    scrambler = Encryptor().load_key_file()

    def decorator(*args, **kwargs):
        args = list(args)
        args[0] = scrambler.encrypt(args[0])
        result = func(*args, **kwargs)
        descrabled = scrambler.decrypt(result)
        return descrabled
    return decorator


def unscrambles_output(func):
    scrambler = Encryptor().load_key_file()

    def decorator(*args, **kwargs):
        args = list(args)
        scrambled_result = func(*args, **kwargs)
        result = scrambler.decrypt(scrambled_result)
        return result
    return decorator


def scrambles_input(func):
    scrambler = Encryptor().load_key_file()

    def decorator(*args, **kwargs):
        args = list(args)
        args[0] = scrambler.encrypt(args[0])
        result = func(*args, **kwargs)
        return result
    return decorator
