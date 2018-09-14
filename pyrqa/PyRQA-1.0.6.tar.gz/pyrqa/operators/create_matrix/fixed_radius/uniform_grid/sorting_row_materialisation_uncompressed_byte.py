#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Create recurrence matrix using an uniform grid.

Grid creation method: Sorting
Input data format: Row store
Recurrence matrix materialisation: Yes
Recurrence matrix representation: Uncompressed
Similarity value representation: Byte
"""

import numpy as np
import pyopencl as cl

from pyrqa.exceptions import SubMatrixNotProcessedException
from pyrqa.opencl import OpenCL
from pyrqa.runtimes import OperatorRuntimes


def create_matrix(settings,
                  data_type,
                  sub_matrix,
                  minimum_buffer,
                  multiplicators_buffer,
                  grid_cells_buffer,
                  grid_cells_start_buffer,
                  number_of_grid_cells_buffer,
                  offset_coordinates_buffer,
                  offset_coordinates_count,
                  device,
                  context,
                  command_queue,
                  kernels,
                  grid_edge_length=None,
                  return_sub_matrix_data=False):
    """
    Note: See GridInfo class for more information about grid data structures.

    :param settings: Settings.
    :param data_type: Data type.
    :param sub_matrix: Sub matrix.
    :param minimum_buffer: Minimum vector OpenCL buffer.
    :param multiplicators_buffer: Multiplicators OpenCL buffer.
    :param grid_cells_buffer: Grid cells OpenCL buffer.
    :param grid_cells_start_buffer: Grid cells start OpenCL buffer.
    :param number_of_grid_cells_buffer: Number of grid cells OpenCL buffer.
    :param offset_coordinates_buffer: Offset coordinates OpenCL buffer.
    :param offset_coordinates_count: Offset coordinates count.
    :param device: OpenCL device.
    :param context: OpenCL context.
    :param command_queue: OpenCL command queue.
    :param kernels: OpenCL kernels.
    :param grid_edge_length: Edge length of the uniform grid.
    :param return_sub_matrix_data: Shall the sub matrix data be returned?
    :return: return_sub_matrix_data: OpenCL sub matrix buffer, runtimes / return_sub_matrix_data==True: Sub matrix data, runtimes.
    """

    transfer_to_device_events = []
    execute_computations_events = []
    transfer_from_device_events = []

    clear_buffer_uint8_kernel = kernels[0]
    create_matrix_kernel = kernels[1]

    # Write to buffers

    # Vectors X
    vectors_x = settings.time_series.get_vectors(sub_matrix.start_x,
                                                 sub_matrix.dim_x)

    vectors_x_buffer = cl.Buffer(context,
                                 cl.mem_flags.READ_ONLY,
                                 vectors_x.nbytes)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     vectors_x_buffer,
                                                     vectors_x,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

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

    command_queue.finish()

    # Sub matrix
    if sub_matrix.size_byte(data_type) > device.max_mem_alloc_size:
        raise SubMatrixNotProcessedException("Calculation aborted: The size of the sub matrix is too large.")

    sub_matrix_buffer = cl.Buffer(context,
                                  cl.mem_flags.READ_WRITE,
                                  int(sub_matrix.size_byte(data_type)))

    command_queue.finish()

    # Execute clear buffer uint8 kernel - Sub matrix
    clear_buffer_uint8_args = [sub_matrix_buffer,
                               np.uint8(0)]

    OpenCL.set_kernel_args(clear_buffer_uint8_kernel,
                           clear_buffer_uint8_args)

    global_work_size = [int(sub_matrix.elements_byte())]
    local_work_size = None

    execute_computations_events.append(cl.enqueue_nd_range_kernel(command_queue,
                                                                  clear_buffer_uint8_kernel,
                                                                  global_work_size,
                                                                  local_work_size))

    command_queue.finish()

    # Execute create matrix kernel
    create_matrix_args = [vectors_x_buffer,
                          vectors_y_buffer,
                          minimum_buffer,
                          multiplicators_buffer,
                          grid_cells_buffer,
                          grid_cells_start_buffer,
                          number_of_grid_cells_buffer,
                          offset_coordinates_buffer,
                          np.uint32(sub_matrix.dim_x),
                          np.uint32(settings.time_series.embedding_dimension),
                          np.float32(settings.neighbourhood.radius),
                          np.float32(grid_edge_length),
                          sub_matrix_buffer]

    OpenCL.set_kernel_args(create_matrix_kernel,
                           create_matrix_args)

    global_work_size = [int(sub_matrix.dim_x + (device.max_work_group_size - (sub_matrix.dim_x % device.max_work_group_size))),
                        int(offset_coordinates_count)]

    local_work_size = None

    execute_computations_events.append(cl.enqueue_nd_range_kernel(command_queue,
                                                                  create_matrix_kernel,
                                                                  global_work_size,
                                                                  local_work_size))

    command_queue.finish()

    if return_sub_matrix_data:
        # Read from buffer
        sub_matrix.set_empty_data_byte(data_type)

        transfer_from_device_events.append(cl.enqueue_copy(command_queue,
                                                           sub_matrix.data,
                                                           sub_matrix_buffer,
                                                           device_offset=0,
                                                           wait_for=None,
                                                           is_blocking=False))

        command_queue.finish()

    runtimes = OperatorRuntimes()
    runtimes.transfer_to_device += OpenCL.convert_events_runtime(transfer_to_device_events)
    runtimes.execute_computations += OpenCL.convert_events_runtime(execute_computations_events)
    runtimes.transfer_from_device += OpenCL.convert_events_runtime(transfer_from_device_events)

    return sub_matrix_buffer, \
        runtimes
