"""
# Filename: errorcodes.py
"""


class ErrorCodes():
    ERROR_EXCEPTION = -3
    ERROR_UNKNOWN = -1
    SESSION_EXPIRED = -2
    ERROR_SUCCESS = 0

    ERROR_TABLE_NOT_FOUND = 98
    ERROR_PERMISSION_DENIED = 99
    ERROR_USERPASS_MISMATCH = 100
    ERROR_SESSION_EXPIRED = 101
    ERROR_USER_BLOCKED = 102
    ERROR_ACCOUNT_NOT_ACTIVE = 103
    ERROR_VERIFICATION_CODE_INVALID = 104
    ERROR_VERIFICATION_CODE_EXPIRED = 105
    ERROR_INCORRECT_PASSWORD = 106
    ERROR_DEVICE_NOT_AUTHORIZED = 107

    ERROR_REQUIRED_FIELD_MISSING = 201
    ERROR_REQUIRED_FIELD_EMPTY = 202
    ERROR_FOREIGN_KEY_CONSTRAINT_FAILED = 203
    ERROR_INVALID_COLUMN = 204
    ERROR_TABLE_COLUMN_NOT_FOUND = 205
    ERROR_RECORD_NOT_FOUND = 206
