import click
import requests

from manoc.cli import pass_context
from manoc.utils.config import save_config


@click.command('register')
@click.argument('base-url')
@click.option('--client-id', help='IDP Client Id.')
@click.option('--client-secret', help='IDP Client Secret.')
@click.option('--token', '-t', help='IDP Registration Token.')
@click.option('--name', '-n', default='default-client', help='IDP client name.')
@pass_context
def cli(ctx, base_url, client_id, client_secret, token, name):
    """Command on client registration"""

    if (client_id is not None) & (client_secret is not None):
        click.echo("Will save predefined Client ID and Secret.")
    else:
        click.echo("Will register new Client ID and Secret.")
        url = "http://identity-management-idp." + base_url + "/register"

        payload = "{\"client_name\": \"" + name \
                  + "\", \"grant_types\": [\"client_credentials\"], \"scope\": \"profile\"} "
        headers = {
            'Authorization': "Bearer " + token,
            'Accept': "application/json",
            'Content-Type': "application/json"
        }

        response = requests.request("POST", url, data=payload, headers=headers).json()
        client_id = response['client_id']
        client_secret = response['client_secret']

    save_config(base_url, client_id, client_secret)

