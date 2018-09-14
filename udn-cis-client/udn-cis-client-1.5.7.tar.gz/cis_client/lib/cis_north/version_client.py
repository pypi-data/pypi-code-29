import json
import requests
import urllib3

from cis_client.lib import base_http_client


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_cis_version(north_host, **kwargs):
    """Gets CIS version

    :param north_host:
    :param kwargs: can contains
        - insecure: True if SSL verification must be skipped
    :return: string CIS version
    """

    version_endpoint_url = "{}/version".format(north_host)
    response = requests.get(
        version_endpoint_url,
        verify=True if not kwargs.get('insecure') else False)
    base_http_client.raise_for_http_response(
        response, 'Getting of CIS version was failed.')
    return json.loads(response.content)
