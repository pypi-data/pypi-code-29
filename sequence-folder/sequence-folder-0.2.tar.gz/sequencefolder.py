import itertools
import functools
import operator


class _DimensionAccessor(object):
    def __init__(self, seq, dims, cur_dim):
        self._seq = seq
        self._dims = dims
        self._cur_dim = cur_dim

    def __getitem__(self, key):
        new_dim = self._cur_dim + [key]
        if new_dim[-1] >= self._dims[len(new_dim) - 1]:
            msg = ['[{}]'.format(n) for n in new_dim]
            raise IndexError(''.join(msg))
        if len(new_dim) == len(self._dims):
            pos = 0
            for i, dim in zip(itertools.count(1), new_dim):
                scale = functools.reduce(operator.mul, self._dims[i:], 1)
                pos += scale * dim
            return self._seq[pos]
        return _DimensionAccessor(self._seq, self._dims, new_dim)

    def __setitem__(self, key, value):
        new_dim = self._cur_dim + [key]
        if new_dim[-1] >= self._dims[len(new_dim) - 1]:
            msg = ['[{}]'.format(n) for n in new_dim]
            raise IndexError(''.join(msg))
        if len(new_dim) == len(self._dims):
            pos = 0
            for i, dim in zip(itertools.count(1), new_dim):
                scale = functools.reduce(operator.mul, self._dims[i:], 1)
                pos += scale * dim
            self._seq[pos] = value
        else:
            raise IndexError()


class SequenceFolder(_DimensionAccessor):
    def __init__(self, sequence, dimensions):
        dimensions = tuple(map(int, dimensions))
        size = functools.reduce(operator.mul, dimensions)
        if len(sequence) < size:
            raise ValueError(\
                    'The sequence does not have the proper size'\
                    f' ({len(sequence)} < {size})')
        super().__init__(sequence, dimensions, [])
