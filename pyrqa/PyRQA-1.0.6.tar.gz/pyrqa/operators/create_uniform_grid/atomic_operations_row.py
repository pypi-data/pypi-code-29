#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Create uniform grid.

Grid creation method: Atomic operations
Input data format: Row store
"""

import numpy as np
import pyopencl as cl

from pyrqa.exceptions import SubMatrixNotProcessedException
from pyrqa.opencl import OpenCL
from pyrqa.operators.create_uniform_grid.grid_info import GridInfo
from pyrqa.runtimes import OperatorRuntimes


def create_uniform_grid(settings,
                        sub_matrix,
                        device,
                        context,
                        command_queue,
                        kernels,
                        grid_edge_length=None):
    """
    Note: See GridInfo class for more information about grid data structures.

    :param settings: Settings.
    :param sub_matrix: Sub matrix.
    :param device: OpenCL device.
    :param context: OpenCL context.
    :param command_queue: OpenCL command queue.
    :param kernels: OpenCL kernels.
    :param grid_edge_length: Grid edge length.
    :return: Minimum OpenCL buffer,
        Multiplicators Opencl buffer, \
        Grid cells OpenCL buffer, \
        Grid counters Opencl buffer, \
        Number of grid cells OpenCL buffer, \
        Offset coordinates buffer, \
        Total number of offset coordinates, \
        runtimes
    """

    transfer_to_device_events = []
    execute_computations_events = []
    transfer_from_device_events = []

    clear_buffer_uint32_kernel = kernels[0]
    create_grid_kernel = kernels[1]

    if not grid_edge_length or grid_edge_length < 2 * settings.neighbourhood.radius:
        grid_edge_length = 2 * settings.neighbourhood.radius

    # Get grid info
    grid_info = GridInfo(settings,
                         sub_matrix,
                         grid_edge_length)

    # Write to buffers

    # Vectors Y
    vectors_y = settings.time_series.get_vectors(sub_matrix.start_y,
                                                 sub_matrix.dim_y)

    vectors_y_buffer = cl.Buffer(context,
                                 cl.mem_flags.READ_ONLY,
                                 vectors_y.nbytes)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     vectors_y_buffer,
                                                     vectors_y,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    # Minimum
    minimum = np.array(grid_info.minimum, dtype=np.float32)

    minimum_buffer = cl.Buffer(context,
                               cl.mem_flags.READ_ONLY,
                               minimum.nbytes)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     minimum_buffer,
                                                     minimum,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    # Multiplicators
    multiplicators = np.array(grid_info.multiplicators, dtype=np.uint32)

    multiplicators_buffer = cl.Buffer(context,
                                      cl.mem_flags.READ_ONLY,
                                      multiplicators.nbytes)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     multiplicators_buffer,
                                                     multiplicators,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    # Grid cells
    grid_cells_size = grid_info.total_number_of_grid_cells * sub_matrix.dim_y
    grid_cells_itemsize = np.dtype('uint32').itemsize

    if grid_cells_size * grid_cells_itemsize > device.max_mem_alloc_size:
        raise SubMatrixNotProcessedException("Calculation aborted: The size of the grid cells array is too large.")

    grid_cells_buffer = cl.Buffer(context,
                                  cl.mem_flags.READ_WRITE,
                                  int(grid_cells_size * grid_cells_itemsize))

    # Grid counters
    grid_counters_size = grid_info.total_number_of_grid_cells
    grid_counters_itemsize = np.dtype('uint32').itemsize

    grid_counters_buffer = cl.Buffer(context,
                                     cl.mem_flags.READ_WRITE,
                                     int(grid_counters_size * grid_counters_itemsize))

    # Number of grid cells
    number_of_grid_cells = np.array(grid_info.number_of_grid_cells, dtype=np.int32)

    number_of_grid_cells_buffer = cl.Buffer(context,
                                            cl.mem_flags.READ_ONLY,
                                            number_of_grid_cells.nbytes)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     number_of_grid_cells_buffer,
                                                     number_of_grid_cells,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    # Offset coordinates
    offset_coordinates = np.array(grid_info.offset_coordinates, dtype=np.int32)

    offset_coordinates_buffer = cl.Buffer(context,
                                          cl.mem_flags.READ_ONLY,
                                          offset_coordinates.nbytes)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     offset_coordinates_buffer,
                                                     offset_coordinates,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    command_queue.finish()

    # Execute clear buffer uint32 kernel - Grid counters
    clear_buffer_uint32_args = [grid_counters_buffer,
                                np.uint32(0)]

    OpenCL.set_kernel_args(clear_buffer_uint32_kernel,
                           clear_buffer_uint32_args)

    global_work_size = [int(grid_counters_size)]
    local_work_size = None

    execute_computations_events.append(cl.enqueue_nd_range_kernel(command_queue,
                                                                  clear_buffer_uint32_kernel,
                                                                  global_work_size,
                                                                  local_work_size))

    command_queue.finish()

    # Execute create grid kernel
    create_grid_args = [vectors_y_buffer,
                        minimum_buffer,
                        multiplicators_buffer,
                        np.uint32(sub_matrix.dim_y),
                        np.uint32(settings.time_series.embedding_dimension),
                        np.float32(grid_edge_length),
                        grid_cells_buffer,
                        grid_counters_buffer]

    OpenCL.set_kernel_args(create_grid_kernel,
                           create_grid_args)

    global_work_size = [
        int(sub_matrix.dim_y + (device.max_work_group_size - (sub_matrix.dim_y % device.max_work_group_size)))]
    local_work_size = None

    execute_computations_events.append(cl.enqueue_nd_range_kernel(command_queue,
                                                                  create_grid_kernel,
                                                                  global_work_size,
                                                                  local_work_size))

    command_queue.finish()

    runtimes = OperatorRuntimes()
    runtimes.transfer_to_device += OpenCL.convert_events_runtime(transfer_to_device_events)
    runtimes.execute_computations += OpenCL.convert_events_runtime(execute_computations_events)
    runtimes.transfer_from_device += OpenCL.convert_events_runtime(transfer_from_device_events)

    return minimum_buffer, \
        multiplicators_buffer, \
        grid_cells_buffer, \
        grid_counters_buffer, \
        number_of_grid_cells_buffer, \
        offset_coordinates_buffer, \
        grid_info.offset_coordinates_count, \
        runtimes
