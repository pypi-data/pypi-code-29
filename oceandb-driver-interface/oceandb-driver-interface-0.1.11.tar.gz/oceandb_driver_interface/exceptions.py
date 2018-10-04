"""Custom exceptions for OceanDB"""


class OceanDbError(Exception):
    """Base class for all OceanDB errors."""


class ConfigError(Exception):
    """Base class for all config errors."""


def __init__(self, message='', error=None):
    self.message = message
    self.error = error


def __str__(self):
    return self.message
