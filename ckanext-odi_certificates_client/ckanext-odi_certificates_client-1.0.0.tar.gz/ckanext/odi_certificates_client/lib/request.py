from logging import getLogger
from urlparse import urljoin, urlsplit

import ckan.plugins.toolkit as t
from ckan.common import config

log = getLogger(__name__)

_certs_config = dict({
    'server': config['ckanext.odi_certificates.server'],
    'username': config['ckanext.odi_certificates.username'],
    'token': config['ckanext.odi_certificates.token'],
    'jurisdiction': config['ckanext.odi_certificates.jurisdiction'],
    'locale': config.get('ckanext.odi_certificates.locale', 'en')
})

_ckan_site_url = config.get('ckan.site.alias_url', config['ckan.site_url'])


def get_auth():
    '''
    Returns Basic Authentication user and password for ODC API.
    '''
    return (_certs_config['username'], _certs_config['token'])


def get_request_path_for(path_function, params_function=None):
    request_path = _certs_config['server'] + path_function()
    if params_function:
        request_path = t['h']._url_with_params(request_path, params_function())
    log.debug('Returning request path: %s', request_path)
    return request_path


def campaigns_feed_request_path():
    return location_request_path() + '.json'


def campaigns_feed_request_params():
    return {'datahub': _get_ckan_hostname(), 'jurisdiction': _certs_config['jurisdiction']}


def location_request_path():
    return '/' + _certs_config['locale'] + '/datasets'


def _get_ckan_hostname():
    split_url = urlsplit(_ckan_site_url)
    log.debug('split url is %r', split_url)
    return split_url[1]


def get_ckan_dataset_url(data_dict):
    name = t.get_or_bust(data_dict, 'name')
    ckan_dataset_url = urljoin(_ckan_site_url, t.url_for(controller='package', action='read', id=name))
    log.debug('Returning ckan dataset url: %s', ckan_dataset_url)
    return ckan_dataset_url


def location_from_response_headers(response):
    if not response.headers or not response.headers.get('Location', ''):
        setattr(response, 'status_code', 404)
        response.raise_for_status()
    else:
        return response.headers['Location'] + '.json'
