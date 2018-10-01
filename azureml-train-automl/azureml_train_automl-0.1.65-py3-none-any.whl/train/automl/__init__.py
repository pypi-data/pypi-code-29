# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Init for standard AutoML modules."""
from .automl import fit_pipeline
from .automlconfig import AutoMLConfig
from .utilities import extract_user_data, get_sdk_dependencies

__all__ = [
    'AutoMLConfig',
    'fit_pipeline',
    'extract_user_data',
    'get_sdk_dependencies']

try:
    from ._version import ver
    __version__ = ver
except ImportError:
    __version__ = '0.0.0+dev'
