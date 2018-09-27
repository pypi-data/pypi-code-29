# -*- coding: utf-8 -*-
# Copyright 2018 NS Solutions Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function, absolute_import, with_statement

import click

import cli.configuration
import kamonohashi


@click.group(short_help='System account related commands')
def account():
    """System account related commands e.g. login, switch tenant, your account information."""


@account.command(help="Login to KAMONOHASHI system. A CLI's configuration file generated to ~/.kqi/config.json")
@click.option('-s', '--server', help='API server name like http://api.kamonohashi.ai')
@click.option('-u', '--user', prompt=True, confirmation_prompt=False, help='User name')
@click.option('-p', '--password', prompt=True, confirmation_prompt=False, hide_input=True, help='Password')
@click.option('-t', '--tenant', type=int, help='A tenant id')
def login(server, user, password, tenant):
    api = kamonohashi.AccountApi(cli.configuration.get_api_client_noauth())
    config_file = cli.configuration.try_read_file()
    if server is None:
        server = config_file.get('server')
        if server is None:
            server = click.prompt('Server')
    server = server.rstrip('/')
    api.api_client.configuration.host = server
    expire_days = config_file.get('expireDays')
    expires_in = expire_days * 24 * 3600 if expire_days is not None else None
    model = kamonohashi.AccountApiModelsLoginInputModel(user_name=user, password=password, tenant_id=tenant, expires_in=expires_in)
    result = api.login(model=model)

    cli.configuration.update_config_file(server=server, token=result.token)
    print('user name:', result.user_name)
    print('tenant:', result.tenant_name)
    print('expires in:', result.expires_in, 'seconds')
    print('token:', result.token)


@account.command('switch-tenant', help='Switch to another tenant using TENANT_ID')
@click.argument('tenant-id', type=int)
def switch_tenant(tenant_id):
    api = kamonohashi.AccountApi(cli.configuration.get_api_client())
    config_file = cli.configuration.try_read_file()
    expire_days = config_file.get('expireDays')
    expires_in = expire_days * 24 * 3600 if expire_days is not None else None
    result = api.switch_tenant(tenant_id, expires_in=expires_in)
    cli.configuration.update_config_file(token=result.token)
    print('user name:', result.user_name)
    print('selected tenant:', result.tenant_id, result.tenant_name)
    print('expires in:', result.expires_in, 'seconds')


@account.command('get', help='Show current account information')
def get_account():
    api = kamonohashi.AccountApi(cli.configuration.get_api_client())
    result = api.get_account()
    print('user name:', result.user_name)
    print('selected tenant:', result.selected_tenant.id, result.selected_tenant.display_name)
    print('assigned tenant:')
    for tenant in result.tenants:
        selected = '*' if tenant.id == result.selected_tenant.id else ' '
        print('   ', selected, tenant.id, tenant.display_name)
