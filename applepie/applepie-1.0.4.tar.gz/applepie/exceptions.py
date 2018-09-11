class ApplePieException(Exception):
    pass


class InvalidApplePieData(ApplePieException):
    pass


class MissingMerchantId(ApplePieException):
    pass


class InvalidSignature(ApplePieException):
    pass


class InvalidCertificate(ApplePieException):
    pass
