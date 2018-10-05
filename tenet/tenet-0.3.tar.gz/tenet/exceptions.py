class TenetBaseException(Exception):
    pass


class TenetBadRequest(TenetBaseException):
    pass


class TenetServerError(TenetBaseException):
    pass
