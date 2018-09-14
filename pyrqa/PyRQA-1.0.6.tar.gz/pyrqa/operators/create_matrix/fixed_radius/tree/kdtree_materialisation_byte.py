#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Create recurrence matrix using k-d tree.

Recurrence matrix representation: Uncompressed / Compressed
K-d tree implementation: sklearn.neighbors.KDTree (Wrapper: sklearn.neighbors.NearestNeighbours)
"""


import time

from sklearn.neighbors import NearestNeighbors

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
    start = time.time()

    vectors_x = settings.time_series.get_vectors_as_2d_array(sub_matrix.start_x,
                                                             sub_matrix.dim_x)

    vectors_y = settings.time_series.get_vectors_as_2d_array(sub_matrix.start_y,
                                                             sub_matrix.dim_y)

    if tree == Tree.KDTree:
        algorithm = 'kd_tree'

    elif tree == Tree.BallTree:
        algorithm = 'ball_tree'

    else:
        raise UnsupportedTreeException("Tree '%s' is not supported" % tree.__class__.__name__)

    if matrix_representation == MatrixRepresentation.Uncompressed:
        nearest_neighbours = NearestNeighbors(radius=settings.neighbourhood.radius,
                                              algorithm=algorithm,
                                              p=settings.similarity_measure.get_p()).fit(vectors_x)

        sub_matrix_data = nearest_neighbours.radius_neighbors_graph(vectors_y).astype(data_type)

        sub_matrix_data.sort_indices()

        sub_matrix_data = sub_matrix_data.toarray().flatten()

    elif matrix_representation == MatrixRepresentation.CSC:
        nearest_neighbours = NearestNeighbors(radius=settings.neighbourhood.radius,
                                              algorithm=algorithm,
                                              p=settings.similarity_measure.get_p()).fit(vectors_y)

        sub_matrix_data = nearest_neighbours.radius_neighbors_graph(vectors_x).astype(data_type)

        sub_matrix_data.sort_indices()

    elif matrix_representation == MatrixRepresentation.CSR:
        nearest_neighbours = NearestNeighbors(radius=settings.neighbourhood.radius,
                                              algorithm=algorithm,
                                              p=settings.similarity_measure.get_p()).fit(vectors_x)

        sub_matrix_data = nearest_neighbours.radius_neighbors_graph(vectors_y).astype(data_type)

        sub_matrix_data.sort_indices()

    else:
        raise UnsupportedMatrixRepresenationException("Matrix representation '%s' is not supported." % matrix_representation.__class__.__name__)

    end = time.time()

    runtimes = OperatorRuntimes(execute_computations=end - start)

    return sub_matrix_data, \
        runtimes
