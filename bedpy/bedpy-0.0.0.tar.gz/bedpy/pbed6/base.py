from ..bed6.base import BASE as BEDBASE
from ..utils.misc import str_int_q

class BASE(BEDBASE):
    _header = [
        'chromosome', 'padded_start', 'padded_stop',
        'name', 'score', 'strand',
        'original_start', 'original_stop'
    ]

    def __init__(
        self,
        chromosome:str, padded_start:int, padded_stop:int,
        name:str, score:int, strand:str,
        original_start:int, original_stop:int
    ):
        self.chromosome = chromosome
        self.padded_start = padded_start
        self.padded_stop = padded_stop
        self.name = name
        self.score = score
        self.strand = strand
        self.original_start = original_start
        self.original_stop = original_stop


    def as_list(self):
        return super(BASE, self).as_list() + \
        [self.original_start, self.original_stop]

    def original_sequence_length(self):
        return self.original_stop - self.original_start

    def padded_sequence_length(self):
        return self.len('sequence')

    def len(self, which='sequence'):
        if which == 'original_sequence':
            return self.original_sequence_length()
        if which == 'padded_sequence':
            return self.padded_sequence_length()
        return super(BASE, self).len(which)



    # original_start PROPERTY
    @property
    def original_start(self):
        return self._original_start
    @original_start.setter
    def original_start(self, original_start):
        self.validate_position(original_start, 'original_start')
        self._original_start = int(original_start)
    @original_start.deleter
    def original_start(self):
        del self._original_start

    # original_stop PROPERTY
    @property
    def original_stop(self):
        return self._original_stop
    @original_stop.setter
    def original_stop(self, original_stop):
        self.validate_position(original_stop, 'original_stop')
        self._original_stop = int(original_stop)
    @original_stop.deleter
    def original_stop(self):
        del self._original_stop




    # padded_start PROPERTY
    @property
    def padded_start(self):
        return self._padded_start
    @padded_start.setter
    def padded_start(self, padded_start):
        self.validate_position(padded_start, 'padded_start')
        self._padded_start = int(padded_start)
    @padded_start.deleter
    def padded_start(self):
        del self._padded_start

    # padded_stop PROPERTY
    @property
    def padded_stop(self):
        return self._padded_stop
    @padded_stop.setter
    def padded_stop(self, padded_stop):
        self.validate_position(padded_stop, 'padded_stop')
        self._padded_stop = int(padded_stop)
    @padded_stop.deleter
    def padded_stop(self):
        del self._padded_stop


    """

    START and STOP refer to PADDED_START and PADDED_STOP

    """
    # padded_start PROPERTY
    @property
    def start(self):
        return self.padded_start
    @start.setter
    def start(self, padded_start):
        self.validate_position(padded_start, 'padded_start')
        self.padded_start = int(padded_start)
    @start.deleter
    def start(self):
        del self.padded_start

    # padded_stop PROPERTY
    @property
    def stop(self):
        return self.padded_stop
    @stop.setter
    def stop(self, padded_stop):
        self.validate_position(padded_stop, 'padded_stop')
        self.padded_stop = int(padded_stop)
    @stop.deleter
    def stop(self):
        del self.padded_stop
