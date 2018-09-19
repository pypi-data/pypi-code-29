# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64
import gssapi

from flask import current_app, request, Response, url_for, redirect
from flask.views import MethodView

from flask_security.utils import login_user

from udata import search, auth, theme
from udata.i18n import I18nBlueprint

from udata.core.user.models import datastore

from .forms import LoginForm
# from .models import UserLdap
from .ldap import manager

from flask_ldap3_login import AuthenticationResponseStatus

bp = I18nBlueprint('ldap', __name__, url_prefix='/ldap',
                   template_folder='templates',)


@bp.before_app_request
def check_remote_user():
    # print('Before request', request.headers)
    remote_user = request.headers.get('REMOTE_USER')
    if not remote_user:
        return
    user = datastore.find_user(ext__remote_user=remote_user)
    if not user:
        # print(fetch_from_ldap(remote_user))
        first_name, last_name = extract_names(remote_user)
        # email, first_name, last_name
        user = datastore.create_user(
            # slug=data['slug'],
            first_name=first_name,
            last_name=last_name,
            email=remote_user,
            active=True,
            ext={'remote_user': remote_user},
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


def redirect_to_login():
    return redirect(url_for('ldap.login'))


@bp.route('/login', endpoint='login')
class LoginView(MethodView):
    def get(self):
        return theme.render('ldap/login.html', form=LoginForm())

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data

            result = manager.authenticate(username, password)

            if result.status == AuthenticationResponseStatus.success:
                data = result.user_info

                user = datastore.find_user(email=result.user_id)
                if not user:
                    user = datastore.create_user(
                        # slug=data['slug'],
                        first_name=data['givenName'][0],
                        last_name=data['sn'][0],
                        email=result.user_id,
                        active=True,
                        # ext={'ldap': UserLdap(id=data.uid.values[0])},
                        # avatar_url=data['profile'].get('avatar') or None,
                        # website=data['profile'].get('website') or None,
                        # about=data['profile'].get('about') or None
                    )
                login_user(user)
                next_url = form.next.data or url_for('site.home')
                return redirect(next_url)
        return theme.render('ldap/login.html', form=form)


# login_view = LoginView.as_view(b'login2')
# Define the rule for the registration url --->  /auth/register
# Then add the rule to the blueprint
# bp.add_url_rule('/login2', view_func=login_view, methods=['GET', 'POST'])

# app.add_url_rule('/users/', view_func=UserAPI.as_view('users'))


@bp.route('/negociate')
def negociate():
    print('negociate', request.headers)
    if request.headers.get('Authorization', '').startswith('Negotiate '):
        in_token = base64.b64decode(request.headers['Authorization'][10:])
        print('in token', in_token)

        try:
            creds = current_app.extensions['ldap']['creds']
        except KeyError:
            raise RuntimeError('flask-gssapi not configured for this app')

        ctx = gssapi.SecurityContext(creds=creds, usage='accept')

        out_token = ctx.step(in_token)

        if ctx.complete:
            username = ctx._inquire(initiator_name=True).initiator_name
            print('name', username, dir(username))
            # print('attr', username.attributes.items())
            # print('canonical', username.canonicalize())
            username = str(username)
            # print('attr', username.attributes)
            # print('username', username, str(username), out_token)
            # manager.get_user_info_from_spnego(str(username))
            result = manager.authenticate_direct_credentials(username, out_token)
            print(result)

            if result.status == AuthenticationResponseStatus.success:
                print(dir(result))
                print(
                    result.user_dn,
                    result.user_id,
                    result.user_info,
                    result.user_groups
                )

            result = manager.authenticate_direct_bind(username, out_token)
            print(result)

            if result.status == AuthenticationResponseStatus.success:
                print(dir(result))
                print(
                    result.user_dn,
                    result.user_id,
                    result.user_info,
                    result.user_groups
                )

            result = manager.authenticate_search_bind(username, out_token)
            print(result)

            if result.status == AuthenticationResponseStatus.success:
                print(dir(result))
                print(
                    result.user_dn,
                    result.user_id,
                    result.user_info,
                    result.user_groups
                )
            
            result = manager.authenticate(username, out_token)
            print(result)

            if result.status == AuthenticationResponseStatus.success:
                print(dir(result))
                print(
                    result.user_dn,
                    result.user_id,
                    result.user_info,
                    result.user_groups
                )

            result = manager.get_user_info(username)
            print(result)

            if result.status == AuthenticationResponseStatus.success:
                print(dir(result))
                print(
                    result.user_dn,
                    result.user_id,
                    result.user_info,
                    result.user_groups
                )

            result = manager.get_user_info_for_username(username)
            print(result)

            if result.status == AuthenticationResponseStatus.success:
                print(dir(result))
                print(
                    result.user_dn,
                    result.user_id,
                    result.user_info,
                    result.user_groups
                )

            next_url = request.args['next'] if 'next' in request.args else url_for('site.home')
            # return str(username), out_token
            return redirect(next_url)

    # return None, None
    # return '', 401, {'WWW-Authenticate': 'Negotiate'}

    return Response(
        status=401,
        headers={'WWW-Authenticate': 'Negotiate'},
    )
