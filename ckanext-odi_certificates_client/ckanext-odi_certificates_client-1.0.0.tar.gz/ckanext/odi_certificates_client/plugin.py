import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckanext.odi_certificates_client.logic.action.get as action_get
import ckanext.odi_certificates_client.logic.auth.get as auth_get


class Odi_Certificates_ClientPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions, inherit=True)
    plugins.implements(plugins.IAuthFunctions, inherit=True)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'odi_certificates_client')

    # IActions
    def get_actions(self):
        return {'odi_certificate_location_head': action_get.odi_certificate_location_head,
                'odi_certificate_get': action_get.odi_certificate_get,
                'odi_certificate_get_from_id': action_get.odi_certificate_get_from_id,
                'odi_certificates_get_all': action_get.odi_certificates_get_all}

    # IAuthFunctions
    def get_auth_functions(self):
        return {'odi_certificates_client_get': auth_get.odi_certificates_client_get,
                'odi_certificates_client_get_all': auth_get.odi_certificates_client_get}
