from .cipher import Cipher


class Kms(Cipher):
    KEY = 'KMS'

    def get_kms_client(self):
        try:
            import boto3
            return boto3.client('kms', region_name=self.key_region)
        except ImportError:
            raise ImportError('boto3 not found. It must be installed for this cipher')

    def __init__(self, kms_arn):
        self.key_arn = kms_arn
        self.key_region = self.key_arn.split(':')[3]

    def encrypt(self, data):
        return self.get_kms_client().encrypt(KeyId=self.key_arn, Plaintext=data)['CiphertextBlob']

    def decrypt(self, data):
        return self.get_kms_client().decrypt(CiphertextBlob=data)['Plaintext']
