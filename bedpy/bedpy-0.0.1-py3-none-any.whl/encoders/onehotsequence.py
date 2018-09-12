from .onehotcharacter import OneHotCharacterEncoder
class OneHotSequenceEncoder:
    def __init__(self, chars):
        self.chars = chars
        self.enc = OneHotCharacterEncoder(chars)
    def encode(self, seq):
        return [ self.enc.encode(c) for c in seq ]
    def decode(self, seq):
        return [ self.enc.decode(c) for c in seq ]
