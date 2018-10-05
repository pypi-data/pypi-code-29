__version__ = '0.0.1'
__versionfull__ = __version__

import boto3
import logging
from json import loads

logger = logging.getLogger(__name__)

class DjangoKeychain():

    def __init__(self, region):
        self.region = region
        self.endpoint_url = "https://secretsmanager.{}.amazonaws.com".format(region)

    def _pull_secrets(self, secret_id):
        client = boto3.client('secretsmanager', region_name=self.region, endpoint_url=self.endpoint_url)
        r = client.get_secret_value(SecretId=secret_id)
        return r.get('SecretString')

    def get_secret(self, secret_id, key=None):
        secrets = self._pull_secrets(secret_id)
        if key:
            return loads(secrets).get(key)
        else:
            return secrets