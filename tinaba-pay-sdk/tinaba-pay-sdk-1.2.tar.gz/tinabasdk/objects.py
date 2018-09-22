from abc import ABCMeta, abstractmethod

from sdkboil.object import Sendable, Receivable
from voluptuous.validators import Schema
from voluptuous import Any


RESPONSE_OK = '000'


class TinabaSendable(Sendable, metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_action():
        raise NotImplemented

    def to_json(self):
        path = self.__class__.get_action().get_request_body_path()
        result = {}
        tmp = result
        for key in path[:-1]:
            tmp[key] = {}
            tmp = tmp[key]
        tmp[path[-1]] = self.__dict__

        return result


class TinabaReceivable(Receivable, metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_action():
        raise NotImplemented

    @classmethod
    def from_json(cls, obj):
        path = cls.get_action().get_response_body_path()
        for key in path:
            obj = obj[key]
        return cls(**obj)

    @classmethod
    def validate_dict(cls, dictionary):
        name = cls.__name__
        return super(TinabaReceivable, cls).validate_dict(dictionary['response'][name[0].lower() + name[1:]])


class ShippingAddress(Receivable):

    @staticmethod
    def get_receiving_schema():
        return Schema({'receiverName': str,
                       'address': str,
                       'streetNumber': str,
                       'city': str,
                       'cap': str,
                       'district': str,
                       'country': str,
                       'sendAt': Any(str, None),
                       'phoneNumber': Any(str, None)})

    def __init__(self, receiverName, address, streetNumber, city, cap,
                 district, country, sendAt=None, phoneNumber=None):
        self.receiverName = receiverName
        self.address = address
        self.streetNumber = streetNumber
        self.city = city
        self.cap = cap
        self.district = district
        self.country = country

        if sendAt is not None:
            self.sendAt = sendAt

        if phoneNumber is not None:
            self.phoneNumber = phoneNumber


class BillingAddress(Receivable):

    @staticmethod
    def get_receiving_schema():
        return Schema({'receiverName': str,
                       'address': str,
                       'streetNumber': str,
                       'city': str,
                       'cap': str,
                       'district': str,
                       'country': str,
                       'fiscalCode': str})

    def __init__(self, receiverName, address, streetNumber, city, cap, district, country, fiscalCode=None):
        self.receiverName = receiverName
        self.address = address
        self.streetNumber = streetNumber
        self.city = city
        self.cap = cap
        self.district = district
        self.country = country
        self.fiscalCode = fiscalCode


class UserAddress(Receivable):

    @staticmethod
    def get_receiving_schema():
        return Schema({'name': str,
                       'surname': str,
                       'email': str,
                       'shippingAddress': Any(ShippingAddress.get_receiving_schema(), None),
                       'billingAddress': Any(BillingAddress.get_receiving_schema(), None)})

    def __init__(self, name, surname, email, shippingAddress=None, billingAddress=None):
        self.name = name
        self.surname = surname
        self.email = email

        if billingAddress is not None:
            self.shippingAddress = shippingAddress

        if shippingAddress is not None:
            self.billingAddress = billingAddress

    @classmethod
    def from_json(cls, obj):
        try:
            obj['shippingAddress'] = ShippingAddress.from_json(obj['shippingAddress'])
        except KeyError:
            pass

        try:
            obj['billingAddress'] = BillingAddress.from_json(obj['billingAddress'])
        except KeyError:
            pass

        return super(UserAddress, cls).from_json(obj)


class InitCheckoutRequest(TinabaSendable):

    MODE_PREAUTH = 'PREAUTH'
    MODE_ECOMMERCE = 'ECOMMERCE'
    MODE_MEDIA = 'MEDIA'

    @staticmethod
    def get_action():
        from .actions import InitCheckout
        return InitCheckout

    @staticmethod
    def get_sending_schema():
        return Schema({'externalId': str,
                       'amount': str,
                       'currency': str,
                       'description': Any(str, None),
                       'validTo': Any(str, None),
                       'creationDate': str,
                       'creationTime': str,
                       'paymentMode': str,
                       'productCodeId': Any(str, None),
                       'metadata': Any(str, None),
                       'signature': str,
                       'notificationCallback': str,
                       'notificationHttpMethod': str,
                       'backCallback': Any(str, None),
                       'successCallback': Any(str, None),
                       'failureCallback': Any(str, None),
                       'sendReceiverAddress': Any(bool, None)})

    def __init__(self, externalId, amount, currency, creationDateTime, paymentMode,
                 notificationCallback, notificationHttpMethod, description=None, validTo=None,
                 productCodeId=None, metadata=None, backCallback=None, successCallback=None, failureCallback=None,
                 sendReceiverAddress=None):
        self.externalId = externalId
        self.amount = amount
        self.currency = currency
        self.creationDate = creationDateTime.strftime('%Y%m%d')
        self.creationTime = creationDateTime.strftime('%H:%M:%S')
        self.paymentMode = paymentMode
        self.notificationCallback = notificationCallback
        self.notificationHttpMethod = notificationHttpMethod

        if description is not None:
            self.description = description

        if validTo is not None:
            self.validTo = validTo

        if productCodeId is not None:
            self.productCodeId = productCodeId

        if metadata is not None:
            self.metadata = metadata

        if backCallback is not None:
            self.backCallback = backCallback

        if successCallback is not None:
            self.successCallback = successCallback

        if failureCallback is not None:
            self.failureCallback = failureCallback

        if sendReceiverAddress is not None:
            self.sendReceiverAddress = sendReceiverAddress


class InitCheckoutResponse(TinabaReceivable):

    @staticmethod
    def get_action():
        from .actions import InitCheckout
        return InitCheckout

    @staticmethod
    def get_receiving_schema():
        return Schema({'status': str,
                       'paymentCode': Any(str, None),
                       'errorCode': Any(str, None),
                       'paymentCodeURL': Any(str, None)})

    def __init__(self, status, paymentCode=None, errorCode=None, paymentCodeURL=None):
        self.status = status

        if paymentCode is not None:
            self.paymentCode = paymentCode

        if errorCode is not None:
            self.errorCode = errorCode

        if paymentCodeURL is not None:
            self.paymentCodeURL = paymentCodeURL


class ConfirmP2PtransferByCaptureRequest(TinabaSendable):

    @staticmethod
    def get_action():
        from .actions import ConfirmP2PtransferByCapture
        return ConfirmP2PtransferByCapture

    @staticmethod
    def get_sending_schema():
        return Schema({'externalId': str,
                       'amount': str})

    def __init__(self, externalId, amount):
        self.externalId = externalId
        self.amount = amount

    def to_json(self):
        name = self.__class__.__name__
        return {'data': {'request': {name[0].lower() + name[1:]: {'confirmPreauthorizedCheckoutRequest': self.__dict__}}}}


class ConfirmP2PtransferByCaptureResponse(TinabaReceivable):

    @staticmethod
    def get_action():
        from .actions import ConfirmP2PtransferByCapture
        return ConfirmP2PtransferByCapture

    @staticmethod
    def get_receiving_schema():
        return Schema({'status': str,
                       'errorCode': Any(str, None)})

    def __init__(self, status, errorCode=None):
        self.status = status

        if errorCode is not None:
            self.errorCode = errorCode


class VerifyCheckoutRequest(TinabaSendable):

    @staticmethod
    def get_action():
        from .actions import VerifyCheckout
        return VerifyCheckout

    @staticmethod
    def get_sending_schema():
        return Schema({'externalId': str})

    def __init__(self, externalId):
        self.externalId = externalId


class VerifyCheckoutResponse(TinabaReceivable):

    @staticmethod
    def get_action():
        from .actions import VerifyCheckout
        return VerifyCheckout

    @staticmethod
    def get_receiving_schema():
        return Schema({'status': str,
                       'checkoutState': Any(str, None),
                       'errorCode': Any(str, None),
                       'externalId': Any(str, None),
                       'merchantId': Any(str, None),
                       'amount': Any(str, None),
                       'currency': Any(str, None),
                       'userAddress': Any(UserAddress.get_receiving_schema(), None)})

    def __init__(self, status, checkoutState=None, errorCode=None, externalId=None, merchantId=None, amount=None,
                 currency=None, userAddress=None):
        self.status = status

        if checkoutState is not None:
            self.checkoutState = checkoutState
        if errorCode is not None:
            self.errorCode = errorCode
        if externalId is not None:
            self.externalId = externalId
        if merchantId is not None:
            self.merchantId = merchantId
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if userAddress is not None:
            self.userAddress = userAddress


class RefundCheckoutRequest(TinabaSendable):

    @staticmethod
    def get_action():
        from .actions import RefundCheckout
        return RefundCheckout

    @staticmethod
    def get_sending_schema():
        return Schema({'externalId': str,
                       'amount': str})

    def __init__(self, externalId, amount):
        self.externalId = externalId
        self.amount = amount


class RefundCheckoutResponse(TinabaReceivable):

    @staticmethod
    def get_action():
        from .actions import RefundCheckout
        return RefundCheckout

    @staticmethod
    def get_receiving_schema():
        return Schema({'status': str,
                       'errorCode': Any(str, None)})

    def __init__(self, status, errorCode=None):
        self.status = status
        if errorCode is not None:
            self.errorCode = errorCode


class GetCheckoutListRequest(TinabaSendable):

    @staticmethod
    def get_action():
        from .actions import GetCheckoutList
        return GetCheckoutList

    @staticmethod
    def get_sending_schema():
        return Schema({'dateFrom': str,
                       'dateTo': str})

    def __init__(self, dateFrom, dateTo):
        self.dateFrom = dateFrom
        self.dateTo = dateTo


class Checkout(Receivable):

    @staticmethod
    def get_receiving_schema():
        return Schema({'externalId': str,
                       'amount': str,
                       'currency': str,
                       'authTime': str,
                       'merchantId': str,
                       'transactionType': str,
                       'internalTransactionId': Any(str, None),
                       'state': str})

    def __init__(self, externalId, amount, currency, authTime, merchantId,
                 transactionType, state, internalTransactionId=None):
        self.externalId = externalId
        self.amount = amount
        self.currency = currency
        self.authTime = authTime
        self.merchantId = merchantId
        self.transactionType = transactionType
        self.state = state

        if internalTransactionId is not None:
            self.internalTransactionId = internalTransactionId


class GetCheckoutListResponse(TinabaReceivable):

    @staticmethod
    def get_action():
        from .actions import GetCheckoutList
        return GetCheckoutList

    @staticmethod
    def get_receiving_schema():
        return Schema({'status': str,
                       'checkoutList': Any([Checkout.get_receiving_schema()], None),
                       'errorCode': Any(str, None)})

    def __init__(self, status, checkoutList=None, errorCode=None):
        self.status = status

        if checkoutList is not None:
            self.checkoutList = checkoutList
        if errorCode is not None:
            self.errorCode = errorCode

    @classmethod
    def from_json(cls, obj):
        result = super().from_json(obj)
        result.checkoutList = [Checkout.from_json(chk) for chk in result.checkoutList]
        return result
