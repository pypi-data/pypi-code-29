# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import base64
# import gssapi
# import ssl

# from ldap3 import Server, Connection, Tls, SASL, KERBEROS

# from flask import current_app, request, Response, url_for, redirect
# from flask_security.utils import login_user
# from udata.i18n import I18nBlueprint

# from udata.core.user.models import datastore

from flask_ldap3_login import LDAP3LoginManager
from flask_ldap3_login import AuthenticationResponseStatus

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


# def entry_to_dict(entry):
#     data = entry.to_json()


# def extract_names(text):
#     names = text.split('@')[0]
#     return names.split('.', 1)


# def fetch_user(username, password):
#     '''Verify user credentials and fetch its metadata'''
#     server_url = current_app.config.get('LDAP_SERVER')
#     params = {}
    
#     if current_app.config['LDAP_SSL']:
#         tls = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_TLSv1_2)
#         params['use_ssl'] = True
#         params['tls'] = tls
    
#     server = Server(server_url, **params)

#     print('user', username)


#     # dn = 

#     # conn = Connection(server, 'uid=admin,cn=users,cn=accounts,dc=data,dc=xps', 'password', auto_bind=True)


#     # c = Connection(
#     #     server, authentication=ldap3.SASL, sasl_mechanism=KERBEROS)

#     base_dn = current_app.config['LDAP_BASE_DN']
#     user_dn = current_app.config['LDAP_USER_DN']

#     user = user_dn.format(username=username)
#     print('user dn', user)
#     print('base dn', base_dn)

#     user = ','.join((user, base_dn))

#     print('full user', user)

#     conn_params = {
#         'auto_bind': True,
#         'user': user,
#         'password': password,
#     }
#     if current_app.config['LDAP_KERBEROS']:
#         conn_params['authentication'] = SASL
#         conn_params['sasl_mechanism'] = KERBEROS

#     conn = Connection(server, **conn_params)

#     # # Override server hostname for authentication
#     # c = Connection(
#     #     server, sasl_credentials=('ldap-3.example.com',),
#     #     authentication=SASL, sasl_mechanism=KERBEROS)

#     # # Perform a reverse DNS lookup to determine the hostname to authenticate against.
#     # c = Connection(server, sasl_credentials=(True,), authentication=SASL, sasl_mechanism=KERBEROS)
#     # c.bind()

#     print('whoam i', conn.extend.standard.who_am_i())

#     query = '(&(objectclass=person)(uid={username}))'.format(username=username)

#     conn.search(base_dn, query, attributes='*')
#     print('entries', len(conn.entries), conn.entries)
#     return conn.entries[0]

#     # conn.search('dc=data,dc=xps', '(&(objectclass=person)(uid=axel))', attributes=['cn', 'sn', 'givenName', 'krbLastPwdChange', 'objectclass', 'email'])
#     # print(conn.entries)



# def fetch_trusted_user(username):
#     '''Fetch metadata from a trusted user'''
#     server_url = current_app.config.get('LDAP_SERVER')
#     params = {}
    
#     if current_app.config['LDAP_SSL']:
#         tls = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_TLSv1_2)
#         params['use_ssl'] = True
#         params['tls'] = tls
    
#     server = Server(server_url, **params)

#     print('user', username)

#     base_dn = current_app.config['LDAP_BASE_DN']
#     user_dn = current_app.config['LDAP_USER_DN']

#     user = user_dn.format(username=username)
#     print('user dn', user)
#     print('base dn', base_dn)

#     user = ','.join((user, base_dn))

#     print('full user', user)

#     # TODO: use global credentials
#     conn_params = {
#         'auto_bind': True,
#         'user': user,
#         'password': password,
#     }
#     if current_app.config['LDAP_KERBEROS']:
#         conn_params['authentication'] = SASL
#         conn_params['sasl_mechanism'] = KERBEROS

#     conn = Connection(server, **conn_params)

#     print('whoam i', conn.extend.standard.who_am_i())

#     query = '(&(objectclass=person)(uid={username}))'.format(username=username)

#     conn.search(base_dn, query, attributes='*')
#     print('entries', len(conn.entries), conn.entries)
#     return conn.entries[0]
