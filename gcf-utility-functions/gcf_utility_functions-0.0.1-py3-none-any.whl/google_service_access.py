# [START setup]
import json
import os
import pickle
import requests
from googleapiclient.discovery import build
from httplib2 import Http

if 'token' in os.environ:
    config = os.environ
else:
    raise ImportError('Missing credentials. Supply env variables')

SERVICE_VERSION_MAPPING = {
    'slides': 'v1',
    'drive': 'v3',
    'sheets': 'v4',
    'calendar': 'v3',
    'gmail': 'v1'
}
# [END setup]


# [START Credentials]
class OAuthCredentials():
    _credentials = None

    @property
    def oauth_credentials(self):
        "If credential has not already been set, fetch from Google Cloud Function endpoint and deserialize"
        if self._credentials is None:
            creds_obj = requests.post(
                url=config['google_auth_endpoint'],
                json={'token': config['token']}
                ).content
            self._credentials = pickle.loads(creds_obj)
        return self._credentials


service_creds_obj = OAuthCredentials()
# [END Credentials]


# [START build_service_object]
def build_service_object(name: str) -> 'googleapiclient.discovery.Resource':
    "Service object may be used to access Google collections depending on the resource named"
    service_creds = service_creds_obj.oauth_credentials
    version = SERVICE_VERSION_MAPPING[name]
    service = build(name, version, http=service_creds.authorize(Http()))
    return service

# [END build_service_object]
