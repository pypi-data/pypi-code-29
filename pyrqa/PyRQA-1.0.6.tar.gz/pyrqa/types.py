#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Types.
"""


class MatrixRepresentation(object):
    """
    Representation of the matrix data.
    """
    class Uncompressed(object):
        """
        Dense matrix representation.
        """
        pass

    class CSC(object):
        """
        Compressed sparse column matrix representation.
        """
        pass

    class CSR(object):
        """
        Compressed sparse row matrix representation.
        """
        pass


class Tree(object):
    """
    Space partitioning tree.
    """
    class KDTree(object):
        """
        k-d-tree.
        """
        pass

    class BallTree(object):
        """
        Ball tree.
        """
        pass

