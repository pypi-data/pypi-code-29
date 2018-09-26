from coingate_api.api_error import *


class Error:

    errors_map = {
        400: {
            'CredentialsMissing': CredentialsMissing,
            'BadEnvironment': BadEnvironment,
            '': BadRequest
        },
        401: {
            'BadCredentials': BadCredentials,
            'BadAuthToken': BadAuthToken,
            'AccountBlocked': AccountBlocked,
            'IpAddressIsNotAllowed': IPAddressIsNotAllowed,
            '': Unauthorized
        },
        404: {
            'PageNotFound': PageNotFound,
            'RecordNotFound': RecordNotFound,
            'OrderNotFound': OrderNotFound,
            '': NotFound
        },
        422: {
            'OrderIsNotValid': OrderIsNotValid,
            '': UnprocessableEntity
        },
        429: {
            '': RateLimitError
        },
        500: {
            '': InternalServerError
        },
        504: {
            '': InternalServerError
        },
        0: {  # default
            '': APIError
        }
    }

    @staticmethod
    def format_error(error):
        if isinstance(error, dict):
            reason = error.get('reason', '')
            message = error.get('message', '')
            return f'{reason} {message}'

        return error

    @staticmethod
    def raise_error(http_status, error):
        reason = error.get('reason', '') if isinstance(error, dict) else ''

        errors_map = Error.errors_map.get(http_status if http_status in Error.errors_map else 0)
        error_class = errors_map.get(reason if reason in errors_map else '')

        raise error_class(Error.format_error(error))
