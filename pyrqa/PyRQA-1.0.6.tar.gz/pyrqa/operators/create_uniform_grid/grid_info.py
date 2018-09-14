#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Grid information.
"""

import itertools

import numpy as np


class GridInfo(object):
    """
    Grid information.

    :ivar minimum: Vector, having a size adhering to number of dimensions, containing the minimum values of the state space.
    :ivar number_of_grid_cells: Number of grid cells per embedding dimension.
    :ivar multiplicators: Multiplicator for accessing a certain grid cell per embedding dimension.
    :ivar total_number_of_grid_cells: Total number of grid cells.
    :ivar offset_coordinates: Offset coordinates for all neighbouring grid cells of any given grid cell.
    :ivar offset_coordinates_count: Total number of all neighbouring grid cells of any given grid cell.
    """

    def __init__(self,
                 settings,
                 sub_matrix,
                 grid_edge_length):
        """
        :param settings: Settings.
        :param sub_matrix: Sub matrix.
        :param grid_edge_length: Grid edge length.
        """

        # Determine grid cell counts
        minimum_x, \
            maximum_x = settings.time_series.get_minimum_and_maximum_vector(sub_matrix.start_x,
                                                                            sub_matrix.dim_x)

        minimum_y, \
            maximum_y = settings.time_series.get_minimum_and_maximum_vector(sub_matrix.start_y,
                                                                            sub_matrix.dim_y)

        minimum = np.minimum(minimum_x, minimum_y)
        maximum = np.maximum(maximum_x, maximum_y)

        extent = maximum - minimum

        number_of_grid_cells = np.zeros(settings.time_series.embedding_dimension,
                                        dtype=np.int32)

        for dim in np.arange(settings.time_series.embedding_dimension):
            if extent[dim] == 0:
                number_of_grid_cells[dim] = 1
            else:
                number_of_grid_cells[dim] = np.ceil(extent[dim] / grid_edge_length)

        multiplicators = []
        multiplicator = 1

        for count in number_of_grid_cells:
            multiplicators.append(multiplicator)
            multiplicator *= count

        multiplicators = np.array(multiplicators, dtype=np.int32)

        total_number_of_grid_cells = multiplicator

        offset_coordinates = []

        for coordinates in itertools.product(np.arange(3), repeat=settings.time_series.embedding_dimension):
            offset_coordinates.append(np.array(coordinates))

        offset_coordinates = np.array(offset_coordinates)
        offset_coordinates_count = len(offset_coordinates)
        offset_coordinates = offset_coordinates.flatten()
        offset_coordinates = np.array(offset_coordinates, dtype=np.int32)
        offset_coordinates -= 1

        self.minimum = minimum
        self.number_of_grid_cells = number_of_grid_cells
        self.multiplicators = multiplicators
        self.total_number_of_grid_cells = total_number_of_grid_cells
        self.offset_coordinates = offset_coordinates
        self.offset_coordinates_count = offset_coordinates_count
