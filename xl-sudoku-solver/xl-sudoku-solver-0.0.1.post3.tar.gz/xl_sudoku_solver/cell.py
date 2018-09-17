from collections import Iterable
from .exceptions import InternalError, ComputeError

class Cell():
    
    IMPOSSIBLE_VALUES = [False,False,False,False,False,False,False,False,False]
    ALL_POSSIBLE_VALUES = [True,True,True,True,True,True,True,True,True]

    def __init__(self, values=ALL_POSSIBLE_VALUES):
        if not isinstance(values, Iterable):
            raise InternalError('Expect a list-like value')
        if len(values) > 9 or len(values) < 9:
            raise InternalError('Items of the value must be 9 instead of {}'.format(len(values)))
        self._values = []
        self.set_pos(0, 0)
        try:
            for item in values:
                self._values.append(bool(item))
        except ValueError:
            raise InternalError('Encounter an error when convert a value into boolean')
        self._possible_moves = len(list(filter(None, self._values)))

    def minus(self, *k):
        for i in k:
            if type(i) is not int:
                continue
            if self._values[i-1] == True:
                self._values[i-1] = False
                self._possible_moves -= 1
        return self

    def get_one(self):
        return self._values.index(True) + 1

    def all_possibility(self):
        for i,v in enumerate(self._values):
            if v:
                yield i+1

    def is_certain(self):
        return len(self) == 1

    def get_pos(self):
        return self._pos

    def set_pos(self, x, y):
        self._pos = (x, y)

    def __len__(self):
        return self._possible_moves

    def __eq__(self, other):
        return self._values == other._values

    def __lt__(self, other):
        return len(self) - len(other) <= 0
        