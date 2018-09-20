"""
====
Core
====

"""

import numpy as np
import pandas as pd

from functools import lru_cache
from dataclasses import dataclass
from .constants import *


########################################################################
@dataclass
class CircuitDescriptor:
    """"""
    descriptor: pd.DataFrame = None

    # ----------------------------------------------------------------------
    def Y(self, matrix=None):
        """"""
        if matrix is None:
            y = self.descriptor[['terminal 1', 'terminal 2', 'value']][self.descriptor.type == IMPEDANCE]
            return self.__y(z.values)
        else:
            return self.__y(matrix)

    # ----------------------------------------------------------------------
    def I(self, matrix=None):
        """"""
        if matrix is None:
            i = self.descriptor[['terminal 1', 'terminal 2', 'value']][self.descriptor.type == CURRENT_SOURCE]
            return self.__i(i.values)
        else:
            return self.__i(matrix)

    # ----------------------------------------------------------------------
    @staticmethod
    def __y(data):
        """"""
        size = data[:, 0:2].reshape(data.shape[0] * 2).max()

        # q = lambda i:data[[i in d[:2] for d in data]]
        def q(i): return data[[i in d[:2] for d in data]]
        q = lru_cache(maxsize=9)(q)

        # w = lambda i,j:sum((1 if i==j else -1) / q(i)[[j in p[:2] for p in q(i)]][:,2])
        def w(i, j): return sum((1 if i == j else -1) / q(i)[[j in p[:2] for p in q(i)]][:, 2])
        w = np.vectorize(w)

        i, j = np.meshgrid(np.arange(1, size + 1), np.arange(1, size + 1))
        return w(i, j)

    # ----------------------------------------------------------------------
    @staticmethod
    def __i(data):
        """"""
        size = data[:, 0:2].reshape(data.shape[0] * 2).max()

        # c = lambda i:sum(data[[i == d[0] for d in data]][:,2]) - sum(data[[i == d[1] for d in data]][:,2])
        def c(i): return sum(data[[i == d[0] for d in data]][:, 2]) - sum(data[[i == d[1] for d in data]][:, 2])
        c = np.vectorize(c)

        # return c(range(1, size+1)).T
        return c(range(1, size + 1)).reshape(size, 1)
