from cryptography.fernet import Fernet


def encrypt(s, key=None):
    """Takes UTF-8 string and optional key(bytes or UTF-8), and spits UTF-8 token"""

    if key is None:
        key = Fernet.generate_key()

    try:
        f = Fernet(_to_bytes(key))
    except binascii.Error:
        raise ValueError('The key was not valid')

    try:
        token = f.encrypt(_to_bytes(s))
    except TypeError:
        raise TypeError('Can only encode string or bytes')

    s_token, s_key = token.decode('utf8'), key.decode('utf8')
    return s_token, s_key


def decrypt(token, key):
    """Takes token and key in UTF-8 (or bytes) and spits UTF-8 string"""

    try:
        f = Fernet(_to_bytes(key))
    except TypeError:
        raise TypeError('Can only encode string or bytes')

    try:
        bytes = f.decrypt(_to_bytes(token))
    except TypeError:
        raise TypeError('Needs key as string or bytes')
    except binascii.Error:
        raise ValueError('The key was not valid')

    return bytes.decode('utf8')


def _to_bytes(str_bytes):
    """Takes UTF-8 string or bytes and safely spits out bytes"""
    try:
        bytes = str_bytes.encode('utf8')
    except AttributeError:
        return str_bytes
    return bytes
