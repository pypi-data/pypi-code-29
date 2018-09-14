#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Copy uncompressed recurrence matrices.
"""

import pyopencl as cl

from pyrqa.exceptions import SubMatrixNotProcessedException
from pyrqa.opencl import OpenCL
from pyrqa.runtimes import OperatorRuntimes


def copy_matrix(sub_matrix_data,
                device,
                context,
                command_queue):
    """
    Copy sub matrix data that adheres to the uncompressed matrix representation.

    :param sub_matrix_data: Sub matrix data.
    :param context: OpenCL context.
    :param command_queue: OpenCL command queue.
    :return: OpenCL sub matrix buffer, runtimes.
    """
    transfer_to_device_events = []

    if sub_matrix_data.size * sub_matrix_data.itemsize > device.max_mem_alloc_size:
        raise SubMatrixNotProcessedException("Calculation aborted: The size of the sub matrix is too large.")

    sub_matrix_buffer = cl.Buffer(context,
                                  cl.mem_flags.READ_ONLY,
                                  sub_matrix_data.nbytes)

    transfer_to_device_events.append(cl.enqueue_copy(command_queue,
                                                     sub_matrix_buffer,
                                                     sub_matrix_data,
                                                     device_offset=0,
                                                     wait_for=None,
                                                     is_blocking=False))

    command_queue.finish()

    runtimes = OperatorRuntimes()
    runtimes.transfer_to_device += OpenCL.convert_events_runtime(transfer_to_device_events)

    return sub_matrix_buffer, \
        runtimes
