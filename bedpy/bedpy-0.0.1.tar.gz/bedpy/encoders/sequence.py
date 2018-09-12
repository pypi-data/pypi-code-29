from .onehotsequence import OneHotSequenceEncoder
from .labelrangessequence import LabelRangesSequenceEncoder
from .probabilityclasssequence import ProbabilityClassSequenceEncoder
from .fastasequence import FastaSequenceEncoder
class SequenceEncoder:

    def __init__(self,
        characters,
        classes,
        use_other_q=True,
        start=0, stop=0,
        tandem_repeats=False,
        u=False
    ):
        self.img = OneHotSequenceEncoder(characters)
        self.img = FastaSequenceEncoder(tandem_repeats, u)
        lbl_enc = LabelRangesSequenceEncoder(classes, use_other_q, start, stop)
        self.lbl = lbl_enc
        self.labels = lbl_enc.labels
        cls_enc = ProbabilityClassSequenceEncoder(classes, use_other_q, start, stop)
        self.cls = cls_enc
        self.classes = cls_enc.classes

    def encode(self, sequence, ranges=None, which='img'):
        if which == 'img':
            return self.img.encode(sequence)
        if which == 'cls':
            return self.cls.encode(sequence, ranges)
        if which == 'lbl':
            return self.lbl.encode(sequence, ranges)
