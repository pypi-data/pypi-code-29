#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
__all__ = ['passFrame']

def passFrame(*args):
    """Say frame is valid no matter what arguments are.

    Parameters
    ----------
    *args
        Any arguments required by API.

    Returns
    -------
    bool
        Always True to pass the frame check.
    """
    return True
