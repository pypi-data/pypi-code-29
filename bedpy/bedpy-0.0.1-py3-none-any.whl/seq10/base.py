import os, sys, ast

from .visualizations import img_as_sns, cls_as_sns


from ..pbed6 import PBED6
from ..ranges import ClassRanges
from ..encoders import SequenceEncoder

from ..utils.misc import (percents as perc, pretty_print_percents, truncate_str)


class BASE(PBED6):
    _header = [
        'chromosome', 'padded_start', 'padded_stop',
        'name', 'score', 'strand',
        'original_start', 'original_stop',
        'sequence', 'class_ranges'
    ]




    def __init__(
        self,
        chromosome:str, p_start:int, p_stop:int,
        name:str,  score:int, strand:str,
        o_start:int, o_stop:int,
        sequence:str, rngs:list=[],

        valid_chars=['A', 'C', 'T', 'G'],
        other_class_q=True,
        classes=['Exon', 'Intron']
    ):
        self.chromosome     = chromosome
        self.padded_start   = p_start
        self.padded_stop    = p_stop
        self.name           = name
        self.score          = score
        self.strand         = strand
        self.original_start = o_start
        self.original_stop  = o_stop
        self.sequence       = sequence

        if type(rngs) is str: rngs = ast.literal_eval(rngs)

        self.class_ranges   = ClassRanges(rngs)
        self.valid_chars    = valid_chars


        se = SequenceEncoder(valid_chars, classes, other_class_q,
            self.padded_start, self.padded_stop)

        self.encoder = se
        self.classes = se.classes
        self.labels = se.labels


    def as_list(self):
        return super(BASE, self).as_list() + [self.sequence, self.class_ranges.as_list()]


    def __str__(self):
        t = 10
        return \
        f'''Sequence: {truncate_str(str(self.sequence), t)}''' + '\n' + \
        f'''on {self.chromosome}'s {self.strand} strand (shown as sense-strand)''' + '\n' + \
        f'''length: {self.len()}''' + '\n' + \
        f'''{pretty_print_percents(self.percents())}'''


    def __repr__(self):
        t = 10
        return (f'{self.__class__.__name__}('
                f'{truncate_str(str(self.chromosome), t)}, {truncate_str(str(self.padded_start), t)}, '
                f'{truncate_str(str(self.padded_stop), t)}, {truncate_str(str(self.name), t)}, '
                f'{truncate_str(str(self.score), t)}, {truncate_str(str(self.strand), t)}, '
                f'{truncate_str(str(self.original_start), t)}, {truncate_str(str(self.original_stop), t)}, '
                f'{truncate_str(str(self.sequence), t)})')

    def percents(self):
        return perc(self.sequence)

    @property
    def sequence(self):
        return self._seq

    @sequence.setter
    def sequence(self, sequence):
        # if not all([char in self.chars for char in sequence]):
        #     raise ValueError(f'''
        #         Sequence ({sequence}) contains characters outside the
        #         valid character set ({self.chars})
        #     ''')
        self._seq = sequence

    @sequence.deleter
    def sequence(self):
        del self._seq



    def as_sns(self, which='img'):
        return self._img_as_sns() if which == 'img' else \
               self._cls_as_sns() if which == 'cls' else \
               self._lbl_as_sns()

    def _img_as_sns(self):
        if not hasattr(self, 'encoded_img'):
            self.encode('img')
        return img_as_sns(self.encoded_img, self.valid_chars)

    def _cls_as_sns(self):
        if not hasattr(self, 'encoded_cls'):
            self.encode('cls')
        return cls_as_sns(self.encoded_cls, self.encoder.classes)

    def _lbl_as_sns(self):
        if not hasattr(self, 'encoded_lbl'):
            self.encode('lbl')
        return cls_as_sns(self.encoded_lbl, self.encoder.labels)






    def encode(self, which="img", force=False, verbose=False):
        if not hasattr(self, f'encoded_{which}') or force:
            encoded = self.encoder.encode(self.sequence, self.class_ranges, which)
            if which == 'img':
                self.encoded_img = encoded
            if which == 'cls':
                self.encoded_cls = encoded
            if which == 'lbl':
                self.encoded_lbl = encoded
        else:
            if verbose: print(f'{which} encoding already exists. Set force to "True" to overwrite.')
            if which == 'img':
                encoded = self.encoded_img
            if which == 'cls':
                encoded = self.encoded_cls
            if which == 'lbl':
                encoded = self.encoded_lbl
        return encoded

    def as_schema(self):
        h = [' '.join([c.capitalize() for c in s.split('_')]) for s in self.header()][:-2]
        v = [
            self.chromosome, self.padded_start, self.padded_stop, self.name,
            self.score, self.strand, self.original_start, self.original_stop,
            self.sequence
        ]
        h += ['Nucleotides', 'Sequence', 'Labels']
        v += [self.encode('img'), self.encode('lbl')]
        d = dict(zip(h, v))
        if 'np' not in sys.modules: import numpy as np

        d['Sequence'] = np.array(d['Sequence'], dtype='int64')
        d['Labels']   = np.array(d['Labels'],   dtype='int64')

        return d
