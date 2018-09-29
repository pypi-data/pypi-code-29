import six
import base64
import msgpack


class MsgPackNamedTuple:
    def dumpb(self):
        return msgpack.packb(self._asdict())

    @classmethod
    def loadb(cls, bdata):
        obj_ = {k.decode('utf-8'): v for k, v in msgpack.unpackb(bdata).items()}
        return cls(**obj_)


class Cipher(object):
    @classmethod
    def create_from(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    @classmethod
    def ensure_bytes(cls, data):
        if six.PY3 and isinstance(data, six.string_types):
            data = data.encode('utf-8')

        return data

    @classmethod
    def bytes_to_b64str(cls, data):
        data = cls.ensure_bytes(data)
        return base64.b64encode(data).decode('utf-8')

    @classmethod
    def b64str_to_bytes(cls, data):
        bdata = cls.ensure_bytes(data)
        return base64.b64decode(bdata)

    def encrypt(self, data):
        return self.cipher.encrypt(data)

    def decrypt(self, data):
        return self.cipher.decrypt(data)

    def encrypt_string(self, data):
        bdata = self.ensure_bytes(data)
        encrypted = self.encrypt(bdata)
        return self.bytes_to_b64str(encrypted)

    def decrypt_string(self, data):
        return self._decrypt_from_string(data).decode('utf-8')

    def encrypt_file_to_str(self, path):
        with open(path, 'rb')as f:
            content = f.read()
            encrypted = base64.b64encode(self.encrypt(content))
            return encrypted.decode('utf-8')

    def _decrypt_from_string(self, data):
        return self.decrypt(self.b64str_to_bytes(data))

    def decrypt_string_to_file(self, data, path):
        bdata = self._decrypt_from_string(data)
        with open(path, 'wb')as f:
            f.write(bdata)

        return


def missing_requirement_cipher(requirement):
    class NotImplementedCipher:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError(requirement)

    return NotImplementedCipher
