from .labelrangesindex import LabelRangesIndexEncoder
class LabelRangesSequenceEncoder:
    def __init__(self, labels, use_other_q=True, start=0, stop=0):
        self.start = start
        self.stop = stop
        enc = LabelRangesIndexEncoder(labels, use_other_q)
        self.enc = enc
        self.labels = enc.labels

    def encode(self, sequence, ranges):
        if self.start == self.stop:
            self.stop = self.start + len(sequence)
        return [ self.enc.encode(c+self.start, ranges) for c in range(len(sequence)) ]
