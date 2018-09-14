#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Detect diagonal lines.

Recurrence matrix representation: Compressed (CSC)
"""

import numpy as np
import pyopencl as cl

from pyrqa.opencl import OpenCL
from pyrqa.runtimes import OperatorRuntimes


def detect_diagonal_lines(settings,
                          sub_matrix,
                          sub_matrix_data,
                          indices_buffer,
                          indptr_buffer,
                          context,
                          command_queue,
                          kernels):
    """
    :param settings: Settings.
    :param sub_matrix: Sub matrix.
    :param sub_matrix_data: Sub matrix data.
    :param indices_buffer: OpenCL indices buffer.
    :param indptr_buffer: OpenCL indptr buffer.
    :param context: OpenCL context.
    :param command_queue: OpenCL command queue.
    :param kernels: OpenCL kernels.
    :return: Runtimes.
    """

    transfer_to_device_events = []
    execute_computations_events = []
    transfer_from_device_events = []

    detect_diagonal_lines_kernel = kernels[0]

    # Write to buffer
    diagonal_length_carryover_buffer = cl.Buffer(context,
                                                 cl.mem_flags.READ_WRITE,
                                                 sub_matrix.diagonal_length_carryover.nbytes)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     diagonal_length_carryover_buffer,
                                                     sub_matrix.diagonal_length_carryover,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    diagonal_index_carryover_buffer = cl.Buffer(context,
                                                cl.mem_flags.READ_WRITE,
                                                sub_matrix.diagonal_index_carryover.nbytes)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     diagonal_index_carryover_buffer,
                                                     sub_matrix.diagonal_index_carryover,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    diagonal_frequency_distribution_buffer = cl.Buffer(context,
                                                       cl.mem_flags.READ_WRITE,
                                                       sub_matrix.diagonal_frequency_distribution.size * sub_matrix.diagonal_frequency_distribution.itemsize)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     diagonal_frequency_distribution_buffer,
                                                     sub_matrix.diagonal_frequency_distribution,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    command_queue.finish()

    # Execute detect diagonal lines kernel
    if settings.is_matrix_symmetric:
        for id_x in np.arange(sub_matrix.dim_x):
            number_of_objects = int(sub_matrix_data.indptr[id_x+1] - sub_matrix_data.indptr[id_x])

            if number_of_objects > 0:
                global_work_size = [number_of_objects]
                local_work_size = None

                detect_diagonal_lines_args = [indices_buffer,
                                              indptr_buffer,
                                              np.uint32(id_x),
                                              np.uint32(sub_matrix.dim_x),
                                              np.uint32(sub_matrix.start_x),
                                              np.uint32(sub_matrix.start_y),
                                              np.uint32(settings.theiler_corrector),
                                              np.uint32(sub_matrix.diagonal_offset),
                                              diagonal_frequency_distribution_buffer,
                                              diagonal_length_carryover_buffer,
                                              diagonal_index_carryover_buffer]

                OpenCL.set_kernel_args(detect_diagonal_lines_kernel,
                                       detect_diagonal_lines_args)

                execute_computations_events.append(cl.enqueue_nd_range_kernel(command_queue,
                                                                              detect_diagonal_lines_kernel,
                                                                              global_work_size,
                                                                              local_work_size))

        command_queue.finish()
    else:
        pass

    # Read from buffer
    transfer_from_device_events.append(cl.enqueue_copy(command_queue,
                                                       sub_matrix.diagonal_length_carryover,
                                                       diagonal_length_carryover_buffer,
                                                       device_offset=0,
                                                       wait_for=None,
                                                       is_blocking=False))

    transfer_from_device_events.append(cl.enqueue_copy(command_queue,
                                                       sub_matrix.diagonal_index_carryover,
                                                       diagonal_index_carryover_buffer,
                                                       device_offset=0,
                                                       wait_for=None,
                                                       is_blocking=False))

    transfer_from_device_events.append(cl.enqueue_copy(command_queue,
                                                       sub_matrix.diagonal_frequency_distribution,
                                                       diagonal_frequency_distribution_buffer,
                                                       device_offset=0,
                                                       wait_for=None,
                                                       is_blocking=False))

    command_queue.finish()

    # Determine runtimes
    runtimes = OperatorRuntimes()
    runtimes.transfer_to_device += OpenCL.convert_events_runtime(transfer_to_device_events)
    runtimes.execute_computations += OpenCL.convert_events_runtime(execute_computations_events)
    runtimes.transfer_from_device += OpenCL.convert_events_runtime(transfer_from_device_events)

    return runtimes
