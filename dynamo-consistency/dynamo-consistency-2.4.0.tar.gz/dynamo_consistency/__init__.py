""" Module used to perform Consistency Checks using XRootD.

:author: Daniel Abercrombie <dabercro@mit.edu>
"""

# We want everything logged nicely
from . import logsetup

from ._version import __version__

from .parser import OPTS as opts
from .parser import ARGS as args

__all__ = []
