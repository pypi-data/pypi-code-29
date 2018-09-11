from numbers import Number
from copy import copy, deepcopy
class ClassRange:
    """
    Type conversions
    """
    def as_list(self):
        return [self.name, self.start, self.stop]
    def as_str_list(self):
        return [str(e) for e in self.as_list()]
    def as_tuple(self):
        return tuple(self.as_list())
    def as_dict(self):
        return dict(zip(['name', 'start', 'stop'], self.as_list()))
    def as_txt(self, delim='\t', newline='\n', newline_q=True):
        return delim.join(self.as_str_list()) + (newline if newline_q else '')
    def as_csv(self, newline='\n', newline_q=True):
        return self.as_txt(',', newline, newline_q)
    def as_tsv(self, newline='\n', newline_q=True):
        return self.as_txt('\t', newline, newline_q)

    def __hash__(self):
        return hash(self.as_tuple())

    def __init__(self, name, start, stop):
        self.name  = name
        self.start = int(start)
        self.stop  = int(stop)

    def __repr__(self):
        return (f'{self.__class__.__name__}{self.as_tuple()}')

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return self.stop - self.start

    def __eq__(self, other):
        if not isinstance(other, ClassRange):
            return False
        return (self.name == other.name) and \
               (self.start == other.start) and \
               (self.stop == other.stop)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __contains__(self, other):
        """
        If other is a ClassRange, only true if other is bounded by self
        """
        if isinstance(other, Number):
            return self.start <= other <= self.stop

        if not isinstance(other, ClassRange):
            return False

        if not other.same_q(self):
            return False

        return other.start in self and other.stop in self


    def same_q(self, other):
        """
        Tests only name propery
        """
        if not isinstance(other, ClassRange):
            return False
        return self.name == other.name

    def min(self, other):
        return min([self.start, self.stop, other.start, other.stop])

    def max(self, other):
        return max([self.start, self.stop, other.start, other.stop])

    def overlap_q(self, other):
        if not self.same_q(other):
            return False
        return any([
            other.start in self, other.stop in self,
            self.start in other, self.stop in other
        ])

    def __add__(self, other):
        if not isinstance(other, ClassRange):
            raise ValueError(f'{other} is not a ClassRange')

        if not self.overlap_q(other):
            from .classranges import ClassRanges
            return ClassRanges([deepcopy(self), deepcopy(other)])

        else:
           return ClassRange(self.name, self.min(other), self.max(other))



    def __iadd__(self, other):
        if self.overlap_q(other):
            self.start = self.min(other)
            self.stop  = self.max(other)
        return self


    def __radd__(self, other):
        print('ClassRange.__radd__', self, other)
