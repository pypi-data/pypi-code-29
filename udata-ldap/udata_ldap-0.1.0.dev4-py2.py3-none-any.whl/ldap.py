# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask_ldap3_login import LDAP3LoginManager

from . import settings as DEFAULTS


class LDAPManager(LDAP3LoginManager):
    def init_app(self, app):
        super(LDAPManager, self).init_app(app)

    def init_config(self, config):
        super(LDAPManager, self).init_config(config)
        for key, value in DEFAULTS.__dict__.items():
            self.config.setdefault(key, value)

    def get_user_info_from_spnego(self, username, _connection=None):
        ldap_filter = '(&({0}={1}){2})'.format(
            self.config.get('LDAP_USER_SPNEGO_ATTR'),
            username,
            self.config.get('LDAP_USER_OBJECT_FILTER')
        )

        return self.get_object(
            dn=self.full_user_search_dn,
            filter=ldap_filter,
            attributes=self.config.get("LDAP_GET_USER_ATTRIBUTES"),
            _connection=_connection,
        )

    def extract_user_infos(self, data):
        return {
            'first_name': data['givenName'][0],
            'last_name': data['sn'][0],
            'email': data['mail'][0],
        }


manager = LDAPManager()
