from checkout_sdk.payments import PaymentResponse


class CaptureResponse(PaymentResponse):
    def __init__(self, api_response):
        super().__init__(api_response)

    @property
    def original_id(self):
        return self._response.body['originalId']
