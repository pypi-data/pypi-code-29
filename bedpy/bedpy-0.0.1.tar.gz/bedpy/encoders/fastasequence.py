from .fastacharacter import FastaCharacterEncoder
class FastaSequenceEncoder:
    def __init__(self, tandem_repeats=False, u=False):
        self.enc = FastaCharacterEncoder(tandem_repeats, u)
    def encode(self, seq):
        return [ self.enc.encode(c) for c in seq ]
    def decode(self, seq):
        return [ self.enc.decode(c) for c in seq ]
