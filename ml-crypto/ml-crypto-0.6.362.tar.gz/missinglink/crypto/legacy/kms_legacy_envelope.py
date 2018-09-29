from ..kms import Kms
from ..legacy.aes_ctc import AesCtc
from ..envelope import Envelope


class KmsLegacyEnvelope(Envelope):
    KEY = 'KmsEnvelopeTriple'

    def __init__(self, kms_arn):
        super(KmsLegacyEnvelope, self).__init__(Kms(kms_arn), AesCtc)
