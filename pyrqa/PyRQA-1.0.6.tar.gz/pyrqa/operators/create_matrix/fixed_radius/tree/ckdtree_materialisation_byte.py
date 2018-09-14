#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Create recurrence matrix using k-d tree.

Recurrence matrix representation: Uncompressed / Compressed
K-d tree implementation: scipy.spatial.cKDTree
"""

import itertools
import time

import numpy as np
from scipy.sparse import csc_matrix
from scipy.spatial.ckdtree import cKDTree

from pyrqa.exceptions import UnsupportedTreeException, UnsupportedMatrixRepresenationException
from pyrqa.runtimes import OperatorRuntimes
from pyrqa.types import Tree, MatrixRepresentation


def create_matrix(settings,
                  data_type,
                  sub_matrix,
                  tree=Tree.KDTree,
                  matrix_representation=MatrixRepresentation.CSC):
    """
    :param settings: Settings.
    :param data_type: Data type.
    :param sub_matrix: Sub matrix.
    :param tree: Tree.
    :param matrix_representation: Matrix representation.
    :return: Sub matrix data, runtimes.
    """
    if tree != Tree.KDTree:
        raise UnsupportedTreeException("Tree type '%s' is not supported." % tree)

    def create_compressed_matrix(q_result):
        """
        Create a compressed matrix.

        :param q_result: Query result.
        :return: Compressed matrix.
        """
        indices = list(itertools.chain.from_iterable(q_result))

        indptr = np.cumsum(np.append([0], [len(column) for column in q_result]))

        data = np.ones(len(indices))

        matrix = csc_matrix((data,
                             indices,
                             indptr),
                            dtype=data_type,
                            shape=(sub_matrix.dim_y,
                                   sub_matrix.dim_x))

        matrix.sort_indices()

        return matrix

    start = time.time()

    vectors_x = settings.time_series.get_vectors_as_2d_array(sub_matrix.start_x,
                                                             sub_matrix.dim_x)

    vectors_y = settings.time_series.get_vectors_as_2d_array(sub_matrix.start_y,
                                                             sub_matrix.dim_y)

    if matrix_representation == MatrixRepresentation.Uncompressed:
        tree = cKDTree(vectors_y)

        query_result = tree.query_ball_point(vectors_x,
                                             settings.neighbourhood.radius,
                                             p=settings.similarity_measure.get_p())

        sub_matrix_data = create_compressed_matrix(query_result).toarray().flatten()

    elif matrix_representation == MatrixRepresentation.CSC:
        tree = cKDTree(vectors_y)

        query_result = tree.query_ball_point(vectors_x,
                                             settings.neighbourhood.radius,
                                             p=settings.similarity_measure.get_p())

        sub_matrix_data = create_compressed_matrix(query_result)

    elif matrix_representation == MatrixRepresentation.CSR:
        tree = cKDTree(vectors_x)

        query_result = tree.query_ball_point(vectors_y,
                                             settings.neighbourhood.radius,
                                             p=settings.similarity_measure.get_p())

        sub_matrix_data = create_compressed_matrix(query_result)

    else:
        raise UnsupportedMatrixRepresenationException("Matrix representation '%s' is not supported." % matrix_representation.__class__.__name__)

    end = time.time()

    runtimes = OperatorRuntimes(execute_computations=end - start)

    return sub_matrix_data, \
        runtimes
