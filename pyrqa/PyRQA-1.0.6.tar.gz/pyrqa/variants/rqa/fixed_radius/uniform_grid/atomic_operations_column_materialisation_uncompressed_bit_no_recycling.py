#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Conduct recurrence quantification analysis.

Grid creation method: Atomic operations
Input data representation: Column store
Recurrence matrix materialisation: Yes
Recurrence matrix representation: Uncompressed
Similarity value representation: Bit
Intermediate results recycling: No
"""

import numpy as np

from pyrqa.base_classes import BaseSettings
from pyrqa.operators.create_uniform_grid.atomic_operations_column import create_uniform_grid
from pyrqa.operators.create_matrix.fixed_radius.uniform_grid.atomic_operations_column_materialisation_uncompressed_bit import create_matrix
from pyrqa.operators.detect_diagonal_lines.materialisation_uncompressed_bit import detect_diagonal_lines
from pyrqa.operators.detect_vertical_lines.materialisation_uncompressed_bit_no_recycling import detect_vertical_lines
from pyrqa.runtimes import FlavourRuntimesMultipleOperators


class AtomicOperationsColumnMaterialisationUncompressedBitNoRecycling(BaseSettings):
    """
    See module description regarding computational properties.

    :ivar opencl: OpenCL environment.
    :ivar device: OpenCL device.
    :ivar data_type: Data type to represent the similarity values.
    :ivar optimisations_enabled: Are the default OpenCL compiler optimisations enabled?
    :ivar loop_unroll: Loop unrolling factor.
    :ivar grid_edge_length: Grid edge length.
    :ivar program: OpenCL program.
    :ivar program_created: Has the OpenCL program already been created?
    :ivar kernels: OpenCL kernels.
    :ivar kernels_created: Have the OpenCL kernels already been created?
    """

    def __init__(self,
                 settings,
                 opencl,
                 device,
                 **kwargs):
        """
        :param settings: Settings.
        :param opencl: OpenCL environment.
        :param device: OpenCL device.
        :param kwargs: Keyword arguments.
        """

        BaseSettings.__init__(self,
                              settings)

        self.opencl = opencl
        self.device = device

        self.data_type = kwargs['data_type'] if 'data_type' in list(kwargs.keys()) else np.uint32
        self.optimisations_enabled = kwargs['optimisations_enabled'] if 'optimisations_enabled' in list(kwargs.keys()) else False
        self.loop_unroll = kwargs['loop_unroll'] if 'loop_unroll' in list(kwargs.keys()) else 1
        self.grid_edge_length = self.settings.validate_grid_edge_length(kwargs['grid_edge_length'] if 'grid_edge_length' in list(kwargs.keys()) else None)

        self.program = None
        self.program_created = False

        self.kernels = {}
        self.kernels_created = False

        self.__initialize()

    def __initialize(self):
        """
        Initialization of the variant.
        """
        if not self.program_created:
            self.program = self.opencl.create_program(self.device,
                                                      (create_uniform_grid,
                                                       create_matrix,
                                                       detect_vertical_lines,
                                                       detect_diagonal_lines),
                                                      self.settings.kernels_sub_dir,
                                                      optimisations_enabled=self.optimisations_enabled,
                                                      loop_unroll=self.loop_unroll)

            self.program_created = True

        if not self.kernels_created:
            self.kernels = self.opencl.create_kernels(self.program,
                                                      (self.settings.clear_buffer_kernel_name(np.uint32),
                                                       'create_uniform_grid',
                                                       'create_matrix',
                                                       'detect_vertical_lines',
                                                       self.settings.diagonal_kernel_name))

            self.kernels_created = True

    def process_sub_matrix(self,
                           sub_matrix):
        """
        Processing of a single sub matrix.

        :param sub_matrix: Sub matrix.
        :return: Runtimes for processing the sub matrix.
        """
        # Create variant runtimes
        variant_runtimes = FlavourRuntimesMultipleOperators()

        # Create uniform grid
        minimum_buffer, \
            multiplicators_buffer, \
            grid_cells_buffer, \
            grid_counters_buffer, \
            number_of_grid_cells_buffer, \
            offset_coordinates_buffer, \
            offset_coordinates_count, \
            create_uniform_grid_runtimes = create_uniform_grid(self.settings,
                                                               sub_matrix,
                                                               self.device,
                                                               self.opencl.contexts[self.device],
                                                               self.opencl.command_queues[self.device],
                                                               (self.kernels[self.settings.clear_buffer_kernel_name(np.uint32)],
                                                                self.kernels['create_uniform_grid']),
                                                               self.grid_edge_length)

        variant_runtimes.create_matrix_runtimes = create_uniform_grid_runtimes

        # Create matrix
        sub_matrix_buffer, \
            create_matrix_runtimes = create_matrix(self.settings,
                                                   self.data_type,
                                                   sub_matrix,
                                                   minimum_buffer,
                                                   multiplicators_buffer,
                                                   grid_cells_buffer,
                                                   grid_counters_buffer,
                                                   number_of_grid_cells_buffer,
                                                   offset_coordinates_buffer,
                                                   offset_coordinates_count,
                                                   self.device,
                                                   self.opencl.contexts[self.device],
                                                   self.opencl.command_queues[self.device],
                                                   (self.kernels[self.settings.clear_buffer_kernel_name(np.uint32)],
                                                    self.kernels['create_matrix']),
                                                   self.grid_edge_length)

        variant_runtimes.create_matrix_runtimes += create_matrix_runtimes

        # Detect vertical lines
        detect_vertical_lines_runtimes = detect_vertical_lines(self.data_type,
                                                               sub_matrix,
                                                               sub_matrix_buffer,
                                                               self.device,
                                                               self.opencl.contexts[self.device],
                                                               self.opencl.command_queues[self.device],
                                                               (self.kernels['detect_vertical_lines'],))

        variant_runtimes.detect_vertical_lines_runtimes = detect_vertical_lines_runtimes

        # Detect diagonal lines
        detect_diagonal_lines_runtimes = detect_diagonal_lines(self.settings,
                                                               self.data_type,
                                                               sub_matrix,
                                                               sub_matrix_buffer,
                                                               self.device,
                                                               self.opencl.contexts[self.device],
                                                               self.opencl.command_queues[self.device],
                                                               (self.kernels[self.settings.diagonal_kernel_name],))

        variant_runtimes.detect_diagonal_lines_runtimes = detect_diagonal_lines_runtimes

        return variant_runtimes
