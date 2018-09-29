from .envelope import Envelope
from .kms import Kms


class KmsEnvelope(Envelope):
    KEY = 'KMS_ENVELOPE'

    def __init__(self, kms_arn):
        super(KmsEnvelope, self).__init__(Kms(kms_arn))
