import ckan.plugins.toolkit as t

@t.auth_disallow_anonymous_access
def odi_certificates_client_get(context=None, data_dict=None):
    return t.check_access('package_update', context, data_dict)

@t.auth_disallow_anonymous_access
def odi_certificates_client_get_all(context=None):
    return {'success': False}