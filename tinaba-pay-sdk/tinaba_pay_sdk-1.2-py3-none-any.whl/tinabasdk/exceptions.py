class TinabaException(Exception):
    pass


class UnknownError(TinabaException):
    pass


class ValidationError(TinabaException):
    pass


class FormatError(TinabaException):
    pass


class MerchantConfigError(TinabaException):
    pass


class CheckoutCreationError(TinabaException):
    pass


class PaymentValidationError(TinabaException):
    pass


class SignatureValidationError(TinabaException):
    pass


class RefundError(TinabaException):
    pass
