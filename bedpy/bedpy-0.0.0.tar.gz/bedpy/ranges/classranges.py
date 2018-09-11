from numbers import Number
from copy import copy, deepcopy

from .classrange import ClassRange
class ClassRanges:
    def __init__(self, ranges:list=[]):
        self.ranges = ranges

    def classes(self):
        return set([rng.name for rng in self])
    def as_list(self):
        return [rng.as_list() for rng in self]
    def as_tuple(self):
        return tuple([rng.as_tuple() for rng in self])


    @property
    def ranges(self):
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        rngs = []
        for rng in ranges:
            if isinstance(rng, ClassRange):
                rngs.append(rng)
            else:
                rngs.append(ClassRange(*rng))
        self._ranges = list(set(rngs))

    @ranges.deleter
    def ranges(self):
        del self._ranges


    def __iter__(self):
        return (rng for rng in self.ranges)

    def __getitem__(self, key):
        return self.ranges[key]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        s = f'{self.__class__.__name__}('
        if len(self.ranges) == 0:
            return s + ')'
        else:
            s += '\n'
        for i, rng in enumerate(self.ranges):
            s += '\t' + repr(rng) + '\n'
        s += ')'
        return s



    def __eq__(self, other):
        if isinstance(other, ClassRanges):
            return all([rng in other for rng in self.ranges]) and \
                   all([rng in self for rng in other.ranges])
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


    def __contains__(self, other):
        if isinstance(other, str):
            return any([rng.name == other for rng in self])

        if isinstance(other, ClassRange):
            return any([rng == other for rng in self])

        if isinstance(other, ClassRanges):
            return all([self.__contains__(rng) for rng in other])

        return False



    def overlap_q(self, other):
        return any([rng.overlap_q(other) for rng in self.ranges])







    def append(self, other):

        # Append a range
        if isinstance(other, ClassRange):
            found_q = False
            for rng in self:
                if rng.overlap_q(other):
                    found_q = True
                    rng += other
            if not found_q:
                self.ranges.append(other)

        # Map each range to the above block
        if isinstance(other, ClassRanges):
            for rng in other:
                self.append(other)

        return self




    def __give__(self, other):
        if isinstance(other, ClassRange):
            self.append(other)

        if isinstance(other, ClassRanges):
            for rng in other:
                self.append(rng)

        return self.simplify()

    def simplify(self):
        for rng in self:
            self.append(rng)
        self.ranges = list(set(self.ranges))
        return self

    def __add__(self, other):
        cp = deepcopy(self)
        cp.__give__(other)
        return cp

    def __iadd__(self, other):
        self.__give__(other)
        return self

    def __radd__(self, other):
        cp = deepcopy(self)
        if not isinstance(other, ClassRange):
            return cp
        cp.__iadd__(other)
        return cp
