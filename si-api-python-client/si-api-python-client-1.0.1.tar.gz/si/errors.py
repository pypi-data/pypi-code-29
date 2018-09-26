import json


class HttpError(Exception):
    """ Base of all other errors"""

    def __init__(self, response):
        self.status_code = response.status_code
        # self.reason = error.reason
        try:
            self.body = response.json()
        except:
            self.body = response.text

        self.headers = response.headers

    @property
    def to_dict(self):
        """
        :return: dict of response error from the API
        """
        return json.loads(self.body.decode('utf-8'))

    # @property
    # def message(self):
    #     '''Returns the first argument used to construct this error.'''
    #     return self.args[0]

    # def __init__(self, status_code, error_type, error_message, *args, **kwargs):
    #     self.status_code = status_code
    #     self.error_type = error_type
    #     self.error_message = error_message

    # def __str__(self):
    #     return "(%s) %s-%s" % (self.status_code, self.error_type, self.error_message)


class UnauthorizedError(HttpError):
    pass


class InternalServerError(HttpError):
    pass


err_dict = {
    # 400: BadRequestsError,
    401: UnauthorizedError,
    # 403: ForbiddenError,
    # 404: NotFoundError,
    # 405: MethodNotAllowedError,
    # 413: PayloadTooLargeError,
    # 415: UnsupportedMediaTypeError,
    # 429: TooManyRequestsError,
    500: InternalServerError,
    # 503: ServiceUnavailableError,
    # 504: GatewayTimeoutError
}


def handle_error(response):
    try:
        # print("handle_error", response.status_code)
        exc = err_dict[response.status_code](response)
    except KeyError:
        return HttpError(response)
    return exc

