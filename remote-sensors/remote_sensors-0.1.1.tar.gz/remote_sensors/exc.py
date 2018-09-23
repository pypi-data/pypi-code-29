"""Exceptions module."""


class RemoteSensorsApiError(Exception):
    """Base Exception."""


class InvalidRequest(RemoteSensorsApiError):
    """Invalid request."""


class RequestMarshalerError(RemoteSensorsApiError):
    """Error while parsing the request."""


class InvalidResponse(RemoteSensorsApiError):
    """Invalid Response."""


class ResponseMarshalerError(RemoteSensorsApiError):
    """Error while parsing the response."""
