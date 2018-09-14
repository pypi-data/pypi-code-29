#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Settings
"""

import inspect
import os

from scipy.spatial.distance import minkowski, \
    euclidean, \
    chebyshev

from pyrqa.config_parser import ConfigurationParser
from pyrqa.exceptions import NoOpenCLKernelFoundException
from pyrqa.metric import TaxicabMetric, \
    EuclideanMetric, \
    MaximumMetric
from pyrqa.neighbourhood import FixedRadius, \
    FAN


class Settings(object):
    """
    Settings of recurrence analysis computations.

    :ivar time_series: Time series to be analyzed.
    :ivar similarity_measure: Similarity measure, e.g., EuclideanMetric.
    :ivar neighbourhood: Neighbourhood for detecting neighbours, e.g., FixedRadius(1.0).
    :ivar theiler_corrector: Theiler corrector.
    :ivar config_data: Configuration data that specifies the names of the kernel files.
    """

    def __init__(self,
                 time_series,
                 similarity_measure=EuclideanMetric,
                 neighbourhood=FixedRadius(),
                 theiler_corrector=1,
                 config_file_path=os.path.join(os.path.dirname(os.path.relpath(__file__)), "config.json")):
        self.time_series = time_series
        self.similarity_measure = similarity_measure
        self.neighbourhood = neighbourhood
        self.theiler_corrector = theiler_corrector
        self.config_data = ConfigurationParser.parse(config_file_path)

    @property
    def base_path(self):
        """
        Base path of the project.
        """

        return os.path.dirname(os.path.abspath(__file__))

    @property
    def is_matrix_symmetric(self):
        """
        Is the recurrence matrix symmetric?
        """

        return self.similarity_measure.is_symmetric() and not isinstance(self.neighbourhood, FAN)

    @property
    def maximum_phase_space_diameter(self):
        """
        Maximum phase space diameter, depending on the similarity measure applied.
        """

        minimum_vector, \
            maximum_vector = self.time_series.get_minimum_and_maximum_vector(0,
                                                                             self.time_series.number_of_vectors)

        if self.similarity_measure == TaxicabMetric:
            return minkowski(minimum_vector, maximum_vector, 1)

        if self.similarity_measure == EuclideanMetric:
            return euclidean(minimum_vector, maximum_vector)

        if self.similarity_measure == MaximumMetric:
            return chebyshev(minimum_vector, maximum_vector)

    @property
    def diagonal_kernel_name(self):
        """
        Get name of the kernel function to detect the diagonal lines.

        :rtype: String.
        """

        if self.is_matrix_symmetric:
            return "detect_diagonal_lines_symmetric"
        else:
            return "detect_diagonal_lines"

    @property
    def kernels_sub_dir(self):
        """
        Get the path of the kernel sub directory.

        :rtype: String.
        """

        # return os.path.join(self.neighbourhood.name, self.similarity_measure.name)
        return self.similarity_measure.name

    @staticmethod
    def clear_buffer_kernel_name(data_type):
        """
        Get name of the kernel function used to clear a buffer.

        :param data_type: Data type that is used to represent the data values.
        :return: Name of clear buffer kernel.
        :rtype: String.
        """

        return "clear_buffer_%s" % data_type.__name__

    def get_kernel_file_names(self,
                              obj):
        """
        Get kernel function file names.

        :param obj: Computation object.
        :returns: Kernel file names.
        :rtype: 1D array.
        """

        cls_list = [cls.__name__ for cls in inspect.getmro(obj.__class__)]

        for element in self.config_data:
            if (element['computation_class'] in cls_list) \
                    and (element['neighbourhood_class'] == self.neighbourhood.__class__.__name__) \
                    and (element['class'] == obj.__class__.__name__):
                return tuple(element['kernel_file_names'])

        raise NoOpenCLKernelFoundException("Kernels for class '%s' could not be found." % obj.__class__.__name__)

    def validate_grid_edge_length(self,
                                  grid_edge_length):
        """
        Validate the edge length of the uniform grid that partitions the embedding space.

        :param grid_edge_length: Grid edge length.
        :return: Validated grid edge length.
        """

        if not grid_edge_length or grid_edge_length < 2 * self.neighbourhood.radius:
            return 2 * self.neighbourhood.radius
        else:
            return grid_edge_length

    def __str__(self):
        return "Recurrence Analysis Settings\n" \
               "----------------------------\n" \
               "Similarity measure: %s\n" \
               "Neighbourhood: %s\n" \
               "Theiler corrector: %d\n" \
               "Matrix symmetry: %r\n" % (self.similarity_measure.__name__,
                                          self.neighbourhood,
                                          self.theiler_corrector,
                                          self.is_matrix_symmetric)
