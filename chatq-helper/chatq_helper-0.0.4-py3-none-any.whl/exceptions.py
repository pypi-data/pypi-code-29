class BaseException(Exception):
    def __init__(self, message, code):
        self.code = code
        super(BaseException, self).__init__(message)


class ClientError(BaseException):
    def __init__(self, message="", ext=0):
        code = 400 + ext
        super(ClientError, self).__init__(message, code)


class ServerError(BaseException):
    def __init__(self, message="", ext=0):
        code = 500 + ext
        super(ServerError, self).__init__(message, code)


# ----------------------------------------------------------------------------------------------------------------------------------------
# CLIENT ERROR
class MissingProperty(ClientError):
    def __init__(self, name, key):
        super(MissingProperty, self).__init__(
            message='[{0}] empty require property: {1}'.format(name, key),
            ext=1
        )

class InvalidProperty(ClientError):
    def __init__(self, name, key, properties):
        super(InvalidProperty, self).__init__(
            message='[{0}] invalid poperty: {1}. Allow: {2}'.format(name, key, properties),
            ext=2
        )


class PermissionDenied(ClientError):
    def __init__(self, message=''):
        super(PermissionDenied, self).__init__(message=message, ext=3)


class BadRequest(ClientError):
    def __init__(self, message=''):
        super(BadRequest, self).__init__(message=message, ext=4)


class ValidationError(ClientError):
    def __init__(self, message=''):
        super(ValidationError, self).__init__(message=message, ext=5)


class RoomOwnerNotSet(ClientError):
    def __init__(self):
        super(RoomOwnerNotSet, self).__init__(ext=6)


class EntityNotExist(ClientError):
    def __init__(self, path):
        super(EntityNotExist, self).__init__(
            message='entity ({0}) not exist'.format(path),
            ext=7
        )

class ResourceNotFound(ClientError):
    def __init__(self, path):
        super(ResourceNotFound, self).__init__(ext=8)


class TokenExpired(ClientError):
    def __init__(self):
        super(TokenExpired, self).__init__(ext=97)


class InvalidToken(ClientError):
    def __init__(self):
        super(InvalidToken, self).__init__(ext=98)


# ----------------------------------------------------------------------------------------------------------------------------------------
# SERVER ERROR
class UnableToCreateUserWithFirebase(ServerError):
    def __init__(self, name, key, properties):
        super(UnableToCreateUserWithFirebase, self).__init__(ext=1)


class UnableToUpdateUserWithFirebase(ServerError):
    def __init__(self, name, key, properties):
        super(UnableToUpdateUserWithFirebase, self).__init__(ext=2)
