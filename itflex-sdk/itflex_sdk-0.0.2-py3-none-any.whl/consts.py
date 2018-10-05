from enum import Enum


class ResponseStatus(Enum):
    SUCCESS = "success"
    NOT_FOUND_ERROR = "not_found_error"
    VALIDATION_ERROR = "validation_error"
    PERMISSION_ERROR = "permission_error"
    SERVER_ERROR = "server_error"
    CLIENT_ERROR = "client_error"
    AUTHENTICATION = "authentication_error"
