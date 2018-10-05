from enum import Enum

from dataclasses import dataclass


class SdkException(Exception):
    pass


class AuthenticationError(SdkException):
    pass


class ErrorTypes(Enum):
    invalid = "invalid"
    duplicated = "duplicated"
    required = "required"
    not_found = "not_found"
    rule = "rule"


HTTP_ERROR_MAP = {
    "invalid": ErrorTypes.invalid,
    "duplicated": ErrorTypes.duplicated,
    "required": ErrorTypes.required,
    "not_found": ErrorTypes.not_found,
    "rule": ErrorTypes.rule,
}


@dataclass
class FieldError:
    field: str
    type: ErrorTypes
    msg: str = ""


def decode_errors(errors):
    if not errors:
        return []

    errors_data = []
    for error in errors["errors"]:
        data = FieldError(
            field=error["field"],
            type=HTTP_ERROR_MAP[error["type"]],
            msg=error["msg"],
        )

        errors_data.append(data)

    return errors_data
