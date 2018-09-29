from .cipher import Cipher

from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA512
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Util import number


class Asymmetric(Cipher):
    KEY = 'PKCS1_OAEP-SHA512'

    @classmethod
    def get_key_pair(cls, size=4096):
        key = RSA.generate(size)
        private = key.exportKey('PEM')
        public = key.publickey().exportKey('PEM')
        return private.decode('utf-8'), public.decode('utf-8')

    @classmethod
    def get_cipher_from_bytes(cls, key_bytes, passphrase=None):
        kwargs = {}
        if passphrase is not None:
            kwargs['passphrase'] = passphrase
        key = RSA.importKey(key_bytes, **kwargs)
        return key, PKCS1_OAEP.new(key, hashAlgo=SHA512)

    def __init__(self, key, passphrase=None):
        self.key, self.cipher = self.get_cipher_from_bytes(self.ensure_bytes(key), passphrase=passphrase)

    def export_public_key_bytes(self, mode='OpenSSH'):
        return self.key.publickey().exportKey(mode)

    def export_private_key_bytes(self, mode='PEM', passphrase=None):
        return self.key.exportKey(mode, passphrase=passphrase)
