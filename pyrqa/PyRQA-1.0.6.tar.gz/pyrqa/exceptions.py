#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Custom exceptions.
"""


class UnsupportedNeighbourhoodException(Exception):
    """
    Neighbourhood chosen is not supported.
    """

    def __init__(self,
                 message):
        super(UnsupportedNeighbourhoodException, self).__init__(message)


class UnsupportedMatrixRepresenationException(Exception):
    """
    Neighbourhood chosen is not supported.
    """

    def __init__(self,
                 message):
        super(UnsupportedMatrixRepresenationException, self).__init__(message)


class UnsupportedTreeException(Exception):
    """
    Neighbourhood chosen is not supported.
    """

    def __init__(self,
                 message):
        super(UnsupportedTreeException, self).__init__(message)


class NoOpenCLPlatformDetectedException(Exception):
    """
    No OpenCL platform could be detected.
    """

    def __init__(self,
                 message):
        super(NoOpenCLPlatformDetectedException, self).__init__(message)


class NoOpenCLDeviceDetectedException(Exception):
    """
    No OpenCL device could be detected.
    """

    def __init__(self,
                 message):
        super(NoOpenCLDeviceDetectedException, self).__init__(message)


class OpenCLPlatformIndexOutOfBoundsException(Exception):
    """
    OpenCL platform index is out of bounds.
    """

    def __init__(self,
                 message):
        super(OpenCLPlatformIndexOutOfBoundsException, self).__init__(message)


class OpenCLDeviceIndexOutOfBoundsException(Exception):
    """
    OpenCL device index is out of bounds.
    """

    def __init__(self,
                 message):
        super(OpenCLDeviceIndexOutOfBoundsException, self).__init__(message)


class NoOpenCLKernelFoundException(Exception):
    """
    No OpenCL kernel has been found.
    """

    def __init__(self,
                 message):
        super(NoOpenCLKernelFoundException, self).__init__(message)


class SelectorNotFullySetupException(Exception):
    """
    No variant execption.
    """

    def __init__(self,
                 message):
        super(SelectorNotFullySetupException, self).__init__(message)


class NoLoopUnrollException(Exception):
    """
    No loop unroll factor execption.
    """

    def __init__(self,
                 message):
        super(NoLoopUnrollException, self).__init__(message)


class NoFlavorException(Exception):
    """
    No flavor execption.
    """

    def __init__(self,
                 message):
        super(NoFlavorException, self).__init__(message)


class NoSubMatrixRuntimesAvailableException(Exception):
    """
    No sub matrix runtimes are available.
    """

    def __init__(self,
                 message):
        super(NoSubMatrixRuntimesAvailableException, self).__init__(message)


class SubMatrixNotProcessedException(Exception):
    """
    Sub matrix was not processed.
    """

    def __init__(self,
                 message):
        super(SubMatrixNotProcessedException, self).__init__(message)


class DeviceFissionNotSupportedException(Exception):
    """
    Device fission not support by OpenCL platform.
    """

    def __init__(self,
                 message):
        super(DeviceFissionNotSupportedException, self).__init__(message)


class NoSubDevicePropertiesException(Exception):
    """
    No sub device properties are specified.
    """

    def __init__(self,
                 message):
        super(NoSubDevicePropertiesException, self).__init__(message)


class DeviatingNumberOfSubDevicePropertiesException(Exception):
    """
    Deviating number of sub device properties specified.
    """

    def __init__(self,
                 message):
        super(DeviatingNumberOfSubDevicePropertiesException, self).__init__(message)


class InvalidSubDevicePropertiesException(Exception):
    """
    Invalid sub device properties.
    """

    def __init__(self,
                 message):
        super(InvalidSubDevicePropertiesException, self).__init__(message)


class OpenCLSubDeviceIndexOutOfBoundsException(Exception):
    """
    OpenCL device index is out of bounds.
    """

    def __init__(self,
                 message):
        super(OpenCLSubDeviceIndexOutOfBoundsException, self).__init__(message)


class TimeDelayReconstructionNotSupportedException(Exception):
    """
    Time series class does not support recurrence vector reconstruction according to the time delay method.
    """

    def __init__(self,
                 message):
        super(TimeDelayReconstructionNotSupportedException, self).__init__(message)
