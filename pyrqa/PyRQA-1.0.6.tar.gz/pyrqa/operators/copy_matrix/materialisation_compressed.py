#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Copy compressed recurrence matrices.
"""

import numpy as np
import pyopencl as cl

from pyrqa.exceptions import SubMatrixNotProcessedException
from pyrqa.opencl import OpenCL
from pyrqa.runtimes import OperatorRuntimes


def copy_matrix(sub_matrix_data,
                device,
                context,
                command_queue):
    """
    Copy sub matrix data that adheres to a compressed matrix representation (CSC and CSR).

    :param sub_matrix_data: Sub matrix data.
    :param context: OpenCL context.
    :param command_queue: OpenCL command queue.
    :return: OpenCL indices buffer, OpenCL indptr buffer, runtimes.
    """
    transfer_to_device_events = []

    if sub_matrix_data.indices.nbytes > device.max_mem_alloc_size:
        raise SubMatrixNotProcessedException("Calculation aborted: The size of the indices array is too large.")
    elif sub_matrix_data.indices.nbytes == 0:
        sub_matrix_data.indices = np.array([0], dtype=sub_matrix_data.indices.dtype)

    indices_buffer = cl.Buffer(context,
                               cl.mem_flags.READ_ONLY,
                               sub_matrix_data.indices.nbytes)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     indices_buffer,
                                                     sub_matrix_data.indices,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    if sub_matrix_data.indptr.nbytes > device.max_mem_alloc_size:
        raise SubMatrixNotProcessedException("Calculation aborted: The size of the indptr array is too large.")

    indptr_buffer = cl.Buffer(context,
                              cl.mem_flags.READ_ONLY,
                              sub_matrix_data.indptr.nbytes)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     indptr_buffer,
                                                     sub_matrix_data.indptr,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    command_queue.finish()

    runtimes = OperatorRuntimes()
    runtimes.transfer_to_device += OpenCL.convert_events_runtime(transfer_to_device_events)

    return indices_buffer, \
        indptr_buffer, \
        runtimes
