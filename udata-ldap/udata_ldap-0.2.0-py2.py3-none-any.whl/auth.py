# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64
import gssapi

from flask import current_app, request, Response, url_for, redirect
from flask_security.utils import login_user
from udata.i18n import I18nBlueprint

from udata.core.user.models import datastore

bp = I18nBlueprint('kerberos', __name__)


def extract_names(text):
    names = text.split('@')[0]
    return names.split('.', 1)


def fetch_from_ldap(remote_user):
    from ldap3 import Server, Connection, Tls, SASL, KERBEROS
    import ssl
    tls = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_TLSv1_2)

    print('remote_user', remote_user)

    server_url = current_app.config.get('LDAP_SERVER')
    server = Server(server_url, use_ssl=True, tls=tls)

    # dn = 

    # conn = Connection(server, 'uid=admin,cn=users,cn=accounts,dc=data,dc=xps', 'password', auto_bind=True)


    # c = Connection(
    #     server, authentication=ldap3.SASL, sasl_mechanism=KERBEROS)

    conn = Connection(
            # server, user='HTTP/data.xps@DATA.XPS',
            server, user='admin@DATA.XPS',
            authentication=SASL, sasl_mechanism=KERBEROS,
            auto_bind=True)

    # # Override server hostname for authentication
    # c = Connection(
    #     server, sasl_credentials=('ldap-3.example.com',),
    #     authentication=SASL, sasl_mechanism=KERBEROS)

    # # Perform a reverse DNS lookup to determine the hostname to authenticate against.
    # c = Connection(server, sasl_credentials=(True,), authentication=SASL, sasl_mechanism=KERBEROS)
    # c.bind()

    print(conn.extend.standard.who_am_i())

    query = '(&(objectclass=person)(uid={remote_user}))'.format(remote_user=remote_user)

    conn.search('dc=data,dc=xps', query, attributes='*')
    print(conn.entries)

    # conn.search('dc=data,dc=xps', '(&(objectclass=person)(uid=axel))', attributes=['cn', 'sn', 'givenName', 'krbLastPwdChange', 'objectclass', 'email'])
    # print(conn.entries)


@bp.before_app_request
def check_remote_user():
    print('Before request', request.headers)
    remote_user = request.headers.get('REMOTE_USER')
    if not remote_user:
        return
    user = datastore.find_user(ext__remote_user=remote_user)
    if not user:
        print(fetch_from_ldap(remote_user))
        first_name, last_name = extract_names(remote_user)
        # email, first_name, last_name
        user = datastore.create_user(
            # slug=data['slug'],
            first_name=first_name,
            last_name=last_name,
            email=remote_user,
            active=True,
            ext={remote_user: remote_user},
            # avatar_url=data['profile'].get('avatar') or None,
            # website=data['profile'].get('website') or None,
            # about=data['profile'].get('about') or None
        )
    # else:
    #     user.first_name = data['first_name']
    #     user.last_name = data['last_name']
    #     user.active = data['is_active']
    #     user.avatar_url = data['profile'].get('avatar') or None
    #     user.website = data['profile'].get('website') or None
    #     user.about = data['profile'].get('about') or None

    # admin_role = datastore.find_or_create_role('admin')
    # if data['is_superuser'] and not user.has_role(admin_role):
    #     datastore.add_role_to_user(user, admin_role)

    # user.save()
    login_user(user)


# # @bp.route('/login')
# def login():
#     if request.headers.get('Authorization', '').startswith('Negotiate '):
#         in_token = base64.b64decode(request.headers['Authorization'][10:])

#         try:
#             creds = current_app.extensions['kerberos']['creds']
#         except KeyError:
#             raise RuntimeError('flask-gssapi not configured for this app')

#         ctx = gssapi.SecurityContext(creds=creds, usage='accept')

#         out_token = ctx.step(in_token)

#         if ctx.complete:
#             username = ctx._inquire(initiator_name=True).initiator_name
#             print('username', str(username), out_token)
#             return str(username), out_token

#     # return None, None
#     # return '', 401, {'WWW-Authenticate': 'Negotiate'}

#     return Response(
#         status=401,
#         headers={'WWW-Authenticate': 'Negotiate'},
#     )


# def spnego():
#     if request.headers.get('Authorization', '').startswith('Negotiate '):
#         in_token = base64.b64decode(request.headers['Authorization'][10:])

#         try:
#             creds = current_app.extensions['kerberos']['creds']
#         except KeyError:
#             raise RuntimeError('flask-gssapi not configured for this app')

#         ctx = gssapi.SecurityContext(creds=creds, usage='accept')

#         out_token = ctx.step(in_token)

#         if ctx.complete:
#             username = ctx._inquire(initiator_name=True).initiator_name
#             print('username', str(username), out_token)
#             next_url = request.args['next'] if 'next' in request.args else url_for('site.home')
#             # return str(username), out_token
#             return redirect(next_url)

#     # return None, None
#     # return '', 401, {'WWW-Authenticate': 'Negotiate'}

#     return Response(
#         status=401,
#         headers={'WWW-Authenticate': 'Negotiate'},
#     )
