import binascii
from collections import namedtuple
from .cipher import MsgPackNamedTuple
import six
from .cipher import Cipher

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter

ltype = int if six.PY3 else long


class SymmetricEncryptedData(namedtuple('SymmetricEncryptedData', ['data', 'iv']), MsgPackNamedTuple):
    pass


class Symmetric(Cipher):
    KEY = 'AES-CTR-32'
    KEY_SIZE = 32

    @classmethod
    def get_key(cls):
        return Random.new().read(cls.KEY_SIZE)

    def get_cipher(self, iv):
        iv_int = int(binascii.hexlify(iv), 16)
        ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)
        return AES.new(self.key, AES.MODE_CTR, counter=ctr)

    def __init__(self, key):
        self.key = self.ensure_bytes(key)

    def _get_iv(self):
        return Random.new().read(AES.block_size)

    def encrypt(self, data):
        iv = self._get_iv()
        cipher = self.get_cipher(iv)
        enc_data = cipher.encrypt(data)
        return SymmetricEncryptedData(data=enc_data, iv=iv).dumpb()

    def decrypt(self, data):
        data = SymmetricEncryptedData.loadb(data)
        return self.get_cipher(data.iv).decrypt(data.data)
