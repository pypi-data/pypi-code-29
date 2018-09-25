from . import _bpqcryptodll
import ctypes


_bpqcryptodll.aes_cipher_create.restype = ctypes.c_void_p
_bpqcryptodll.aes_cipher_free.argtypes = [ctypes.c_void_p]
_bpqcryptodll.aes_encrypt.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_long,
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_long)
]
_bpqcryptodll.aes_decrypt.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_long,
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_long)
]


class _BaseCryptor(object):

    def __init__(self, key, encrypt: bool, iv=None):

        if not isinstance(key, bytes):
            raise ValueError("aes key must be bytearray")

        if iv is None:
            iv = bytes(16)
        elif not isinstance(iv, bytes) or len(iv) != 16:
            raise ValueError('initialization vector must be 16 bytes')

        _key = ctypes.create_string_buffer(key)

        _iv = ctypes.create_string_buffer(iv)

        self._cipher = _bpqcryptodll.aes_cipher_create(_key, _iv, encrypt)

        if self._cipher is None:
            raise RuntimeError("Can't create AES cipher")

        pass

    def __del__(self):

        if self._cipher is not None:
            _bpqcryptodll.aes_cipher_free(self._cipher)
            self._cipher = None


class Encryptor(_BaseCryptor):

    def __init__(self, key, iv=None):
        super().__init__(key, True, iv)

    @classmethod
    def newCBC(self, key, iv=None):
        aes = Encryptor(key, iv)
        return aes

    def encrypt(self, m):

        if not isinstance(m, bytes):
            raise TypeError()

        _m_size = ctypes.c_long(len(m))
        _m = ctypes.create_string_buffer(m)

        _e_size = ctypes.c_long(len(m)+16)
        _e = ctypes.create_string_buffer(_e_size.value)

        if not _bpqcryptodll.aes_encrypt(self._cipher, _m, _m_size, _e, ctypes.byref(_e_size)):
            raise RuntimeError()

        return _e.raw[:_e_size.value]


class Decryptor(_BaseCryptor):

    def __init__(self, key, iv=None):
        super().__init__(key, False, iv)

    @classmethod
    def newCBC(self, key, iv=None):
        aes = Decryptor(key, iv)
        return aes

    def decrypt(self, m):

        if not isinstance(m, bytes):
            raise TypeError()

        _m_size = ctypes.c_long(len(m))
        _m = ctypes.create_string_buffer(m)

        _e_size = ctypes.c_long(len(m)+16)
        _e = ctypes.create_string_buffer(len(m)+16)

        if not _bpqcryptodll.aes_decrypt(self._cipher, _m, _m_size, _e, ctypes.byref(_e_size)):
            raise RuntimeError()

        return _e.raw[:_e_size.value]
