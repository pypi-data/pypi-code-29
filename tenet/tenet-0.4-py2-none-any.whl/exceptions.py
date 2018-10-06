"""
Global TenetAPI exception and warning classes.
"""


class TenetBaseException(Exception):
    """The base exception class for all exceptions this library raises."""
    pass


class TenetBadRequest(TenetBaseException):
    """Bad connection or bad credentials."""
    pass


class TenetServerError(TenetBaseException):
    """We have got error message from API."""
    pass
