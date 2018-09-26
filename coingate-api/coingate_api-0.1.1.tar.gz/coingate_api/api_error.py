
class APIError(Exception):
    pass


# HTTP Status 400
class BadRequest(APIError):
    pass


class CredentialsMissing(BadRequest):
    pass


class BadEnvironment(BadRequest):
    pass


# HTTP Status 401
class Unauthorized(APIError):
    pass


class BadCredentials(Unauthorized):
    pass


class BadAuthToken(Unauthorized):
    pass


class AccountBlocked(Unauthorized):
    pass


class IPAddressIsNotAllowed(Unauthorized):
    pass


# HTTP Status 404
class NotFound(APIError):
    pass


class PageNotFound(NotFound):
    pass


class RecordNotFound(NotFound):
    pass


class OrderNotFound(NotFound):
    pass


# HTTP Status 422
class UnprocessableEntity(APIError):
    pass


class OrderIsNotValid(UnprocessableEntity):
    pass


# HTTP Status 429
class RateLimitError(APIError):
    pass


# HTTP Status 500, 504
class InternalServerError(APIError):
    pass
