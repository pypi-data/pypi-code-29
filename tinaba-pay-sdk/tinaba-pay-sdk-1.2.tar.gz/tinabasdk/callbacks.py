from hashlib import sha256
from base64 import b64encode
from voluptuous.validators import Schema, Any
from sdkboil.object import Receivable
from tinabasdk.objects import UserAddress

from .exceptions import ValidationError


class CheckoutStateCallback(Receivable):

    @classmethod
    def create(cls, obj, secret):
        cls.validate_dict(obj, secret)
        return cls.from_json(obj)

    @staticmethod
    def get_receiving_schema():
        return Schema({'externalId': str,
                       'checkoutState': str,
                       'signature': str,
                       'userAddress': Any(UserAddress.get_receiving_schema(), None)})

    @classmethod
    def validate_dict(cls, dictionary, secret):
        super(CheckoutStateCallback, cls).validate_dict(dictionary)
        expected = b64encode(sha256((dictionary['externalId'] + dictionary['checkoutState'] + secret).encode()).digest()).decode()
        if expected != dictionary['signature']:
            raise ValidationError('Callback signature {} does not match expected signature {}'.format(dictionary['signature'],
                                                                                                      expected))

    def __init__(self, externalId, checkoutState, userAddress, signature):
        self.externalId = externalId
        self.checkoutState = checkoutState
        self.userAddress = userAddress
        self.signature = signature

    @classmethod
    def from_json(cls, obj):
        try:
            obj['userAddress'] = UserAddress.from_json(obj['userAddress'])
        except KeyError:
            pass

        return super(CheckoutStateCallback, cls).from_json(obj)
