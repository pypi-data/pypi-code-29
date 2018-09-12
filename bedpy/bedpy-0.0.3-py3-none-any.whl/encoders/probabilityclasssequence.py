from .probabilityclassindex import ProbabilityClassIndexEncoder
class ProbabilityClassSequenceEncoder:
    def __init__(
        self, classes, other_class_q=True,
        seq_rng_start=0, seq_rng_stop=0
    ):
        self.start = seq_rng_start
        self.stop = seq_rng_stop
        enc = ProbabilityClassIndexEncoder(classes, other_class_q)
        self.enc = enc
        self.classes = enc.classes


    def encode(self, sequence, ranges):
        if self.start == self.stop:
            self.stop = self.start + len(sequence)
        return [ self.enc.encode(c+self.start, ranges) for c in range(len(sequence)) ]
