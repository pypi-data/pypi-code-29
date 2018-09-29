from .envelope import Envelope


class MultiKeyEnvelope(Envelope):
    def __init__(self, *args):
        self.key_ciphers = args
        super(MultiKeyEnvelope, self).__init__(None, None)

    def encrypt_key(self, key):
        res = key
        for cipher in self.key_ciphers:
            res = Envelope(cipher).encrypt(res)

        return res

    def decrypt_key(self, key):
        res = key
        for cipher in self.key_ciphers[::-1]:  # decrypt in reverse order
            res = Envelope(cipher).decrypt(res)

        return res
