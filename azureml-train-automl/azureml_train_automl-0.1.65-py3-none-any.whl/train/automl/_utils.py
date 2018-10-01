# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Utility functions used by AutoML"""
import numpy as np
import scipy
from math import sqrt


def sparse_std(x):
    """
    The std is computed by dividing by N and not N-1 to match numpy's
    computation.

    :param x: sparse matrix
    :return: std dev
    """
    if not scipy.sparse.issparse(x):
        raise ValueError("x is not a sparse matrix")

    mean_val = x.mean()
    num_els = x.shape[0] * x.shape[1]
    nzeros = x.nonzero()
    sum = mean_val**2 * (num_els - nzeros[0].shape[0])
    for i, j in zip(*nzeros):
        sum += (x[i, j] - mean_val)**2

    return sqrt(sum / num_els)


def sparse_isnan(x):
    """
    Return whether any element in matrix is nan.

    :param x: sparse matrix
    :return: True/False
    """
    if not scipy.sparse.issparse(x):
        raise ValueError("x is not sparse matrix")

    for i, j in zip(*x.nonzero()):
        if np.isnan(x[i, j]):
            return True

    return False
