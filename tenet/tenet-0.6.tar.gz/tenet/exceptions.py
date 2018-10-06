"""
Global TenetAccount exceptions and warnings classes.
"""


class TenetBaseException(Exception):
    """The base exception class for all exceptions this library raises."""
    pass


class TenetBadRequest(TenetBaseException):
    """Bad connection or bad credentials."""
    pass


class TenetServerError(TenetBaseException):
    """Received error message from API."""
    pass
