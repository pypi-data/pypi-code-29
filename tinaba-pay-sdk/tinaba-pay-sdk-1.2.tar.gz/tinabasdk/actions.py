from collections import OrderedDict
from itertools import chain
from hashlib import sha256
from base64 import b64encode
from abc import ABCMeta, abstractmethod

from sdkboil.action import Action, EventHook, Factory

from .objects import (InitCheckoutRequest, InitCheckoutResponse, GetCheckoutListRequest, GetCheckoutListResponse,
                      ConfirmP2PtransferByCaptureRequest, ConfirmP2PtransferByCaptureResponse, VerifyCheckoutRequest,
                      VerifyCheckoutResponse, RefundCheckoutRequest, RefundCheckoutResponse)
from .exceptions import (UnknownError, FormatError, MerchantConfigError, CheckoutCreationError, PaymentValidationError,
                         SignatureValidationError, RefundError)


class TinabaFactory(Factory):

    @staticmethod
    def get_actions():
        return {'init.checkout': InitCheckout,
                'confirm.preauthorized.checkout': ConfirmP2PtransferByCapture,
                'verify.checkout': VerifyCheckout,
                'refund.checkout': RefundCheckout,
                'get.checkout.list': GetCheckoutList}


class HeaderHook(EventHook):

    def __call__(self, request, *args, **kwargs):
        request.headers['Content-Type'] = 'application/json'


class ErrorHook(EventHook):

    states = {'IGE': UnknownError,
              'EPE': FormatError,
              'MCE': MerchantConfigError,
              'CKE': CheckoutCreationError,
              'PYE': PaymentValidationError,
              'SGE': SignatureValidationError,
              'RFE': RefundError}

    def __call__(self, request, response, action, *args, **kwargs):
        body = response.json()
        resp_core = body['response'][action.resp_name()]
        if resp_core['status'] != '000':
            raise self.states[resp_core['errorCode'][:3]](resp_core['errorCode'])


class SignHook(EventHook):

    def __call__(self, request, action, api_context, *args, **kwargs):
        dic = request.body_params
        for key in action.__class__.get_request_body_path():
            dic = dic[key]
        message = ''.join(dic[field] for field in action.get_sig_fields())
        message += api_context.secret
        request.body_params['data']['request'][action.req_name()]['signature'] = b64encode(sha256(message.encode()).digest()).decode()


class MerchantHook(EventHook):

    def __call__(self, request, api_context, action, *args, **kwargs):
        body = request.body_params
        for key in action.__class__.get_request_body_path():
            body = body[key]
        body['merchantId'] = api_context.merchant_id


class TinabaAction(Action, metaclass=ABCMeta):

    @classmethod
    def req_name(cls):
        return cls.__name__[0].lower() + cls.__name__[1:] + 'Request'

    @classmethod
    def resp_name(cls):
        return cls.__name__[0].lower() + cls.__name__[1:] + 'Response'

    @staticmethod
    def get_presend_hooks():
        return OrderedDict([('merchant_id', MerchantHook()), ('content_type_header', HeaderHook())])

    @staticmethod
    def get_success_hooks():
        return OrderedDict([('errors', ErrorHook())])

    @classmethod
    def get_request_body_path(cls):
        return 'data', 'request', cls.req_name()

    @classmethod
    def get_response_body_path(cls):
        return 'response', cls.resp_name()


class TinabaSignedAction(TinabaAction, metaclass=ABCMeta):

    @staticmethod
    def get_presend_hooks():
        new_hooks = OrderedDict([('signature', SignHook())])
        old_hooks = super(TinabaSignedAction, TinabaSignedAction).get_presend_hooks()
        return OrderedDict(chain(old_hooks.items(), new_hooks.items()))

    @staticmethod
    @abstractmethod
    def get_sig_fields():
        raise NotImplemented


class InitCheckout(TinabaSignedAction):

    @staticmethod
    def get_sig_fields():
        return 'merchantId', 'externalId', 'amount', 'currency', 'creationDate', 'creationTime'

    @staticmethod
    def get_body_schema():
        return InitCheckoutRequest

    @staticmethod
    def get_route():
        return '/initCheckout'

    @staticmethod
    def get_verb():
        return 'POST'

    @staticmethod
    def get_response_schema():
        return InitCheckoutResponse

    @staticmethod
    def get_query_schema():
        return {}

    @staticmethod
    def get_status_exceptions():
        return {}

    @staticmethod
    def get_url_schema():
        return {}


class ConfirmP2PtransferByCapture(TinabaSignedAction):

    @staticmethod
    def get_sig_fields():
        return 'merchantId', 'externalId', 'amount'

    @staticmethod
    def get_body_schema():
        return ConfirmP2PtransferByCaptureRequest

    @staticmethod
    def get_route():
        return '/confirmPreauthorizedCheckout'

    @staticmethod
    def get_verb():
        return 'POST'

    @staticmethod
    def get_response_schema():
        return ConfirmP2PtransferByCaptureResponse

    @staticmethod
    def get_query_schema():
        return {}

    @staticmethod
    def get_status_exceptions():
        return {}

    @staticmethod
    def get_url_schema():
        return {}

    @classmethod
    def get_request_body_path(cls):
        return 'data', 'request', cls.req_name(), 'confirmPreauthorizedCheckoutRequest'

    @classmethod
    def get_response_body_path(cls):
        return 'response', cls.req_name(), 'confirmPreauthorizedCheckoutRequest'


class VerifyCheckout(TinabaSignedAction):

    @staticmethod
    def get_sig_fields():
        return 'merchantId', 'externalId'

    @staticmethod
    def get_body_schema():
        return VerifyCheckoutRequest

    @staticmethod
    def get_route():
        return '/verifyCheckout'

    @staticmethod
    def get_verb():
        return 'POST'

    @staticmethod
    def get_response_schema():
        return VerifyCheckoutResponse

    @staticmethod
    def get_query_schema():
        return {}

    @staticmethod
    def get_status_exceptions():
        return {}

    @staticmethod
    def get_url_schema():
        return {}


class RefundCheckout(TinabaSignedAction):

    @staticmethod
    def get_sig_fields():
        return 'merchantId', 'externalId', 'amount'

    @staticmethod
    def get_body_schema():
        return RefundCheckoutRequest

    @staticmethod
    def get_route():
        return '/refundCheckout'

    @staticmethod
    def get_verb():
        return 'POST'

    @staticmethod
    def get_response_schema():
        return RefundCheckoutResponse

    @staticmethod
    def get_query_schema():
        return {}

    @staticmethod
    def get_status_exceptions():
        return {}

    @staticmethod
    def get_url_schema():
        return {}


class GetCheckoutList(TinabaSignedAction):

    @staticmethod
    def get_sig_fields():
        return 'merchantId',

    @staticmethod
    def get_body_schema():
        return GetCheckoutListRequest

    @staticmethod
    def get_route():
        return '/getCheckoutList'

    @staticmethod
    def get_verb():
        return 'POST'

    @staticmethod
    def get_response_schema():
        return GetCheckoutListResponse

    @staticmethod
    def get_query_schema():
        return {}

    @staticmethod
    def get_status_exceptions():
        return {}

    @staticmethod
    def get_url_schema():
        return {}
