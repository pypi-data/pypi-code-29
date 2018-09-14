#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Create uniform grid.

Grid creation method: Sorting
Input data format: Column store
"""

import time

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
                        grid_edge_length):
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
        Grid cells start Opencl buffer, \
        Number of grid cells OpenCL buffer, \
        Offset coordinates buffer, \
        Total number of offset coordinates, \
        runtimes
    """

    transfer_to_device_events = []
    execute_computations_events = []
    transfer_from_device_events = []

    create_uniform_grid_kernel = kernels[0]

    # Get grid info
    grid_info = GridInfo(settings,
                         sub_matrix,
                         grid_edge_length)

    # Write to buffers

    # Time series Y
    time_series_y = settings.time_series.get_time_series(sub_matrix.start_y,
                                                         sub_matrix.dim_y)

    time_series_y_buffer = cl.Buffer(context,
                                     cl.mem_flags.READ_ONLY,
                                     time_series_y.nbytes)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     time_series_y_buffer,
                                                     time_series_y,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    # Minimum
    minimum = np.array(grid_info.minimum, dtype=np.float32)

    minimum_buffer = cl.Buffer(context,
                               cl.mem_flags.READ_ONLY,
                               minimum.size * minimum.itemsize)

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

    # Grid mapping
    grid_mapping_size = sub_matrix.dim_y
    grid_mapping_itemsize = np.dtype('uint32').itemsize

    grid_mapping_buffer = cl.Buffer(context,
                                    cl.mem_flags.READ_WRITE,
                                    int(grid_mapping_size * grid_mapping_itemsize))

    # Grid cells
    grid_cells_size = grid_mapping_size
    grid_cells_itemsize = np.dtype('uint32').itemsize

    if grid_cells_size * grid_cells_itemsize > device.max_mem_alloc_size:
        raise SubMatrixNotProcessedException("Calculation aborted: The size of the grid cells array is too large.")

    grid_cells_buffer = cl.Buffer(context,
                                  cl.mem_flags.READ_WRITE,
                                  int(grid_cells_size * grid_cells_itemsize))

    # Grid cells start
    grid_cells_start_size = grid_info.total_number_of_grid_cells + 1
    grid_cells_start_itemsize = np.dtype('uint32').itemsize

    if grid_cells_start_size * grid_cells_start_itemsize > device.max_mem_alloc_size:
        raise SubMatrixNotProcessedException("Calculation aborted: The size of the grid cells start array is too large.")

    grid_cells_start_buffer = cl.Buffer(context,
                                        cl.mem_flags.READ_WRITE,
                                        int(grid_cells_start_size * grid_cells_start_itemsize))

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

    # Execute create uniform grid kernel
    create_uniform_grid_args = [time_series_y_buffer,
                                minimum_buffer,
                                multiplicators_buffer,
                                np.uint32(sub_matrix.dim_y),
                                np.uint32(settings.time_series.embedding_dimension),
                                np.uint32(settings.time_series.time_delay),
                                np.float32(grid_edge_length),
                                grid_mapping_buffer]

    OpenCL.set_kernel_args(create_uniform_grid_kernel,
                           create_uniform_grid_args)

    global_work_size = [int(sub_matrix.dim_y + (device.max_work_group_size - (sub_matrix.dim_y % device.max_work_group_size)))]
    local_work_size = None

    execute_computations_events.append(cl.enqueue_nd_range_kernel(command_queue,
                                                                  create_uniform_grid_kernel,
                                                                  global_work_size,
                                                                  local_work_size))

    command_queue.finish()

    # Read from grid mapping buffer
    grid_mapping = np.empty(grid_mapping_size, dtype=np.uint32)

    transfer_from_device_events.append(cl.enqueue_copy(command_queue,
                                                       grid_mapping,
                                                       grid_mapping_buffer,
                                                       device_offset=0,
                                                       wait_for=None,
                                                       is_blocking=False))

    command_queue.finish()

    # Create grid cells and grid cells start
    start_sorting = time.time()

    grid_cells = np.argsort(grid_mapping)

    grid_cells_start = np.insert(np.cumsum(np.bincount(grid_mapping, minlength=grid_info.total_number_of_grid_cells)), 0, 0)

    end_sorting = time.time()

    # Write to grid cells buffer and grid cells start buffer
    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     grid_cells_buffer,
                                                     grid_cells.astype(np.uint32),
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     grid_cells_start_buffer,
                                                     grid_cells_start.astype(np.uint32),
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    command_queue.finish()

    runtimes = OperatorRuntimes()
    runtimes.transfer_to_device += OpenCL.convert_events_runtime(transfer_to_device_events)
    runtimes.execute_computations += OpenCL.convert_events_runtime(execute_computations_events)
    runtimes.execute_computations += (end_sorting - start_sorting)
    runtimes.transfer_from_device += OpenCL.convert_events_runtime(transfer_from_device_events)

    return minimum_buffer, \
        multiplicators_buffer, \
        grid_cells_buffer, \
        grid_cells_start_buffer, \
        number_of_grid_cells_buffer, \
        offset_coordinates_buffer, \
        grid_info.offset_coordinates_count, \
        runtimes
