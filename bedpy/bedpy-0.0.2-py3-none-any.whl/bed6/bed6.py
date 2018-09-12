from .base import BASE
from random import randint




class BED6(BASE):
    """
    Class for the BED6 file format.
    Only the first three optional parameters are accepted.

    See: https://genome.ucsc.edu/FAQ/FAQformat.html for more information.
    """


    def __init__(self,
        chromosome:str,
        start:int,
        stop:int,
        name:str='my_bed_seq',
        score:int=0,
        strand:str='.'
    ):
        self.chromosome  = chromosome
        self.start       = start
        self.stop        = stop
        self.name        = name
        self.score       = score
        self.strand      = strand


    def pad(self, length, position=None):
        from ..pbed6 import PBED6
        needed = length - self.len('sequence')
        pad_start = position if position is not None else randint(0, abs(needed))

        max = self.len('chromosome')

        if needed < 0:
            pad_start *= -1

        if self.start - pad_start <= 0:
            pad_start = 0

        pad_stop = needed - pad_start
        if self.stop + pad_stop >= max:
            pad_stop = max - pad_stop
            pad_start = needed - pad_stop

        new_start = self.start - pad_start
        new_stop = self.stop + pad_stop
        new_length = new_stop - new_start

        if new_length != length:
            msg = f'Incorrect padding: {new_length} is not equal to {length}'
            raise ValueError(msg)


        return PBED6(*[
            self.chromosome, new_start, new_stop,
            self.name, self.score, self.strand,
            self.start, self.stop
        ])
