from logging import getLogger

import ckan.plugins.toolkit as toolkit
import requests
from ckan.logic import NotFound
from requests import HTTPError

from ckanext.odi_certificates_client.lib.request import get_request_path_for, \
    get_ckan_dataset_url, location_request_path, get_auth, campaigns_feed_request_path, campaigns_feed_request_params, \
    location_from_response_headers

log = getLogger(__name__)


@toolkit.side_effect_free
def odi_certificate_get_from_id(context=None, data_dict=None):
    log.debug("entered api get from id...")
    log.debug('data dict is: %r', data_dict)
    package_data_dict = toolkit.get_action('package_show')(context, {'id': data_dict['id']})
    response = odi_certificate_location_head(context, package_data_dict)
    try:
        location_url = location_from_response_headers(response)
        context['odi_certificate'] = {
            'location_url': location_url
        }
        return toolkit.get_action('odi_certificate_get')(context, package_data_dict)
    except HTTPError as e:
        return _json_response(response, e)


@toolkit.side_effect_free
def odi_certificate_location_head(context=None, data_dict=None):
    log.debug("entered api get location head...")
    toolkit.check_access('odi_certificates_client_get', context, data_dict)
    request_path = get_request_path_for(location_request_path)
    dataset_url = get_ckan_dataset_url(data_dict)
    response = requests.head(
        request_path,
        params=dict({'datasetUrl': dataset_url}),
        auth=get_auth()
    )
    log.debug('response headers from get is: %s', response.headers)
    return response

@toolkit.side_effect_free
def odi_certificate_get(context=None, data_dict=None):
    log.debug("entered api get...")
    toolkit.check_access('odi_certificates_client_get', context, data_dict)
    request_path = context['odi_certificate']['location_url']
    log.debug('request path is %s', request_path)
    response = requests.get(
        request_path,
        auth=get_auth()
    )
    log.debug('response from get is: %s', response.text)
    return _json_response(response)


@toolkit.side_effect_free
def odi_certificates_get_all(context=None, data_dict=None):
    log.debug("entered api get all...")
    toolkit.check_access('odi_certificates_client_get_all', context)

    request_path = get_request_path_for(campaigns_feed_request_path)
    response = requests.get(
        request_path,
        params=campaigns_feed_request_params(),
        auth=get_auth()
    )
    log.debug('response from get all is: %s', response.text)
    return _json_response(response)


def _json_response(response, e=None):
    try:
        if toolkit.response and response.status_code == 200:
            log.debug('returning json format...')
            return response.json()
        raise NotFound(getattr(e, 'message', response.text))
    except TypeError as e:
        # no toolkit available when sent as job, so just return response
        log.warn('No toolkit.response available')
        log.debug(e.message)
        return response
