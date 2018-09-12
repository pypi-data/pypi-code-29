import os
from ..utils.constants import (CHROMOSOME_LENGTHS, TMP_BED_FILE, TMP_FASTA_FILE)
from ..utils.misc import pretty_print_header_list


class BASE:
    _header = [ 'chromosome', 'start', 'stop', 'name', 'score', 'strand']
    _genome='hg38'
    _valid_genomes = ['hg38']

    _tmp_bed_file = TMP_BED_FILE
    _tmp_seq_file = TMP_FASTA_FILE

    @property
    def genome(self):
        return self._genome
    @genome.setter
    def genome(self, genome):
        if type(genome) is not str:
            raise ValueError(f'Genome {genome} is not a string')
        if genome not in _valid_genomes:
            raise ValueError(f'Genome {genome} is not a supported genome ({self._valid_genomes})')
    @genome.deleter
    def genome(self):
        del self._genome


    # CHROMOSOME PROPERTY
    @property
    def chromosome(self):
        return self._chromosome
    @chromosome.setter
    def chromosome(self, chromosome):
        if type(chromosome) is not str:
            msg = f'Chromosome {chromosome} is not a string.'
            raise ValueError(msg)
        if chromosome not in CHROMOSOME_LENGTHS[self.genome].keys():
            msg = f'Chromosome {chromosome} is not in genome {self.genome} chromosome names.'
            raise ValueError(msg)
        self._chromosome = chromosome
    @chromosome.deleter
    def chromosome(self):
        del self._chromosome

    # START PROPERTY
    @property
    def start(self):
        return self._start
    @start.setter
    def start(self, start):
        self.validate_position(start, 'start')
        self._start = int(start)
    @start.deleter
    def start(self):
        del self._start

    #STOP PROPERTY
    @property
    def stop(self):
        return self._stop
    @stop.setter
    def stop(self, stop):
        self.validate_position(stop, 'stop')
        self._stop = int(stop)
    @stop.deleter
    def stop(self):
        del self._stop

    # NAME PROPERTY
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if type(name) is not str:
            raise ValueError(f'name {name} is not a string.')
        self._name = name
    @name.deleter
    def name(self):
        del self._name

    # SCORE PROPERTY
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        try:
            score = int(score)
        except ValueError:
            raise ValueError(f'score {score} is not an integer.')
        if 0 > score or score > 1000:
            raise ValueError(f'score {score} is out of bounds [0, 1000].')
        self._score = score
    @score.deleter
    def score(self):
        del self._score

    # STRAND PROPERTY
    _valid_strands = ['.', '+', '-']
    @property
    def strand(self):
        return self._strand
    @strand.setter
    def strand(self, strand):
        if strand not in self._valid_strands:
            raise ValueError(f'strand {strand} is not a valid specifier {self._valid_strands}.')
        self._strand = strand
    @strand.deleter
    def strand(self):
        del self._strand



    def chromomsome_length(self):
        return CHROMOSOME_LENGTHS[self.genome][self.chromosome]

    def sequence_length(self):
        return self.stop - self.start

    def len(self, which='sequence'):
        if which == 'sequence':
            return self.sequence_length()
        if which == 'chromosome':
            return self.chromomsome_length()


    def validate_position(self, position, which=''):
        """
        validate_position takes position and ensures that it follows the bed
        file format standards i.e. position is bounded by [0, length_of_chromosome-1]

        """
        try:
            position = int(position)
        except ValueError:
            msg = f'{which} position {position} is not an integer.'
            raise ValueError(msg)

        if position < 0:
            msg = f'{which} position {position} should be non-negative.'
            raise ValueError(msg)

        if position > CHROMOSOME_LENGTHS[self.genome][self.chromosome]:
            msg = f'{which} position {position} is greater than the length of the specified chromosome {self.chromosome}.'
            raise ValueError(msg)

        return True

    def header(self):
        return self._header

    def as_list(self):
        return [self.chromosome, self.start, self.stop, self.name, self.score, self.strand]

    def as_str_list(self):
        return [str(e) for e in self.as_list()]

    def as_tuple(self):
        return tuple(self.as_list())

    def __hash__(self):
        return hash(self.as_tuple())

    def as_txt(self, delim='\t', newline='\n', newline_q=True):
        return delim.join(self.as_str_list()) + (newline if newline_q else '')

    def as_dict(self):
        return dict(zip(self.header(), self.as_list()))

    def as_csv(self, newline='\n', newline_q=True):
        return self.as_txt(',', newline, newline_q)

    def as_tsv(self, newline='\n', newline_q=True):
        return self.as_txt('\t', newline, newline_q)



    def __str__(self):
        return pretty_print_header_list(self.header(), self.as_list(), 10)


    def __repr__(self):
        return (f'{self.__class__.__name__}{self.as_tuple()}')

    def extract(self, genome_file):
        bed_file = self._tmp_bed_file
        seq_file = self._tmp_seq_file

        # write out bed file
        with open(bed_file, 'w+') as f:
            f.write(self.as_txt('\t'))

        # use BEDTools to extract sequence
        try:
            command = 'fastaFromBed -fi {} -bed {} -fo {} -s -name -tab'.format(genome_file, bed_file, seq_file)
            os.system(command)
        except Exception:
            print('Error in trying to extract sequence. Is bedtools installed?')

        # Read in extracted sequences
        seq = None
        with open(seq_file, 'r') as f:
            seq = f.readlines()[0].rstrip('\n').split('\t')[1]


        try: # Goodby bed file
            os.remove(bed_file)
        except OSError:
            msg = f'Error trying to remove temp bed file {bed_file}.'
            raise OSError(msg)

        try: # Goodby sequence file
            os.remove(seq_file)
        except OSError:
            msg = f'Error trying to remove temp seq file {seq_file}.'
            raise OSError(msg)


        return seq
