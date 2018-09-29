from collections import namedtuple
from .cipher import MsgPackNamedTuple, Cipher
from .symmertric import Symmetric
from .symmertric import SymmetricEncryptedData


class EnvelopeData(namedtuple('EnvelopeData', ['data', 'key']), MsgPackNamedTuple):
    pass


class Envelope(Cipher):
    def __init__(self, key_cipher, content_cipher_class=None):
        self.key_cipher = key_cipher
        self.content_cipher_class = content_cipher_class or Symmetric

    def encrypt_key(self, key):
        return self.key_cipher.encrypt(key)

    def decrypt_key(self, key):
        return self.key_cipher.decrypt(key)

    def encrypt(self, data):
        content_cipher = self.content_cipher_class(self.content_cipher_class.get_key())
        data = content_cipher.encrypt(data)
        key = self.encrypt_key(content_cipher.key)
        return EnvelopeData(data=data, key=key).dumpb()

    def decrypt(self, data):
        data = EnvelopeData.loadb(data)
        plain_key = self.decrypt_key(data.key)
        content_cipher = self.content_cipher_class(plain_key)
        return content_cipher.decrypt(data.data)

    @classmethod
    def convert_encrypted_envelope_data_to_triple(cls, envelope_data):
        envelope = EnvelopeData.loadb(envelope_data)
        data = SymmetricEncryptedData.loadb(envelope.data)
        return dict(iv=cls.bytes_to_b64str(data.iv), key=cls.bytes_to_b64str(envelope.key), data=cls.bytes_to_b64str(data.data))

    @classmethod
    def convert_triple_to_encrypted_envelope_data(cls, triple_dict):
        bdict = {k: cls.b64str_to_bytes(triple_dict[k]) for k in ['iv', 'data', 'key']}
        data = SymmetricEncryptedData(iv=bdict['iv'], data=bdict['data'])
        envelope = EnvelopeData(data=data.dumpb(), key=bdict['key'])
        return envelope.dumpb()
