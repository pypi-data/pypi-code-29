from .data_models import data_models
import requests
import urllib.parse

class fhir_client():

    def __init__(self, settings):

        # HTTP settings
        if 'http' in settings and 'timeout' in settings['http']:
            self.http_timeout = settings['http']['timeout']
        else:
            self.http_timeout = 5

        # SSL settings
        if 'ssl' in settings and 'verify' in settings['ssl']:
            # May be True, False or path to a CA bundle or directory containing it.
            self.ssl_verify = settings['ssl']['verify']
        else:
            self.ssl_verify = True

        # Authorization settings
        if 'auth' in settings and 'authorization_header' in settings['auth']:
            self.authorization_header = settings['auth']['authorization_header']
        else:
            self.authorization_header = ""

        # FHIR settings
        if 'fhir' in settings and 'base_url' in settings['fhir']:
            self.fhir_base = settings['fhir']['base_url']
        else:
            exit(1)


    def read(self, resource_type, resource_id):

        r = requests.get(
            url=self.fhir_base + '/' + resource_type + '/' + resource_id,
            headers={"Authorization": self.authorization_header},
            timeout=self.http_timeout,
            verify=self.ssl_verify
        )

        if r.status_code == 200:
            return r.json()
        else:
            return None

    def create(self, resource):
        if data_models().validate(resource):

            r = requests.post(
                url=self.fhir_base + '/' + resource['resourceType'],
                json=resource,
                headers={"Authorization": self.authorization_header},
                timeout=self.http_timeout,
                verify=self.ssl_verify
            )

            if r.status_code == 201:
                return True
            else:
                return None

        else:
            return None

    def update(self):
        pass

    def delete(self):
        pass

    def search(self, resource_type, filter):

        r = requests.get(
            url=self.fhir_base + '/' + resource_type + '?' + urllib.parse.urlencode(filter),
            headers={"Authorization": self.authorization_header},
            timeout=self.http_timeout,
            verify=self.ssl_verify
        )

        if r.status_code == 200:
            return r.json()
        else:
            return None






