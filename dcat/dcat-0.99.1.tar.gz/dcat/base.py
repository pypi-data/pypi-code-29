import requests
from requests.auth import HTTPBasicAuth

import json
import os


class Base:
    def __init__(self, verbosity=0):
        self.verbosity = verbosity
        self.resource_name = "{}s".format(self.__class__.__name__.lower())

    def list(self, project_drn, attributes={}, lineages=[]):
        return self._request(
            "GET",
            self._get_url(self._get_key(project_drn)),
            {"attributes": attributes, "lineages": lineages}
            )

    def create(self, project_drn, path,
               attributes={}, lineages=[], version=None, notes=None):
        return self._request(
            "POST",
            self._get_url(self._get_key(project_drn)),
            {"attributes": attributes,
             "lineages": lineages,
             "path": path,
             "version": version,
             "notes": notes}
            )

    def modify(self, res_drn, attributes={},
               lineages=[], remove=False, version=None, notes=None):
        return self._request(
            "PUT",
            self._get_url(res_drn),
            {"attributes": attributes,
             "lineages": lineages,
             "remove": remove,
             "version": version,
             "notes": notes}
            )

    def delete(self, res_drn):
        return self._request(
            "DELETE",
            self._get_url(res_drn)
            )

    def _get_url(self, key=None):
        url = "{}/{}".format(os.environ.get('DCAT_HOST'), self.resource_name)

        if key is not None:
            url = "{}/{}".format(url, key)
        return url

    def _get_key(self, project=None):
        if project is not None:
            return "?project_id={}".format(project)
        else:
            return None

    def _request(self, method, url, payload={}):
        if self.verbosity == 3:
            print(method, url, payload)
        return requests.request(auth=HTTPBasicAuth(os.environ.get('DCAT_AUTH_USER'), os.environ.get('DCAT_AUTH_PASSWORD')), method=method, url=url, json=payload).json()
