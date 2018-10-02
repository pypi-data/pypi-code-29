class InvalidRequestParameters(Exception):
    pass


class TokenNotSupported(Exception):
    pass


class UnsupportedCurrency(BaseException):
    pass


class RequestNotFound(BaseException):
    pass


class TransactionNotFound(BaseException):
    pass


class IPFSConnectionFailed(BaseException):
    pass


class RoleNotSupported(BaseException):
    pass


class ArtifactNotFound(BaseException):
    pass


class ImproperlyConfigured(BaseException):
    pass


class InvalidRequestHash(BaseException):
    pass


class InvalidRequestSignature(BaseException):
    pass


class InvalidRequestState(BaseException):
    """ Request is not in a valid state for the desired action"""
    pass
