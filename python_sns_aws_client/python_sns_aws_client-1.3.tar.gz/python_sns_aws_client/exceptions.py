from botocore.exceptions import ClientError


class PublishError(ClientError):
    MSG_TEMPLATE = (
        'ERROR_PUBLISH:: ({error_code}) when calling the {operation_name} '
        'operation{retry_info}: {error_message} validate ** request')


class SubscriptionError(ClientError):
    MSG_TEMPLATE = (
        'ERROR_SUBSCRIPTION:: ({error_code}) when calling the {operation_name} '
        'operation{retry_info}: {error_message} validate args receive')


class SNSError(Exception):
    MSG_TEMPLATE = (
        'ERROR_{name_error}:: ({expression}) '
        '{message}, no expected values, validate capture.')
    pass


class RequestInvalidError(SNSError):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        self.name_error = self.__class__
        msg = self.MSG_TEMPLATE.format(
            name_error=str(self.name_error).upper(),
            expression=self.expression,
            message=self.message
        )
        super(RequestInvalidError, self).__init__(msg)