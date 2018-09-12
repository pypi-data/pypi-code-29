import base64
import time

import click
import requests

from manoc.utils.config import save_token, current_env, get_config
from manoc.utils.context import fill_context


def verify_token(ctx):
    if not token_valid(ctx):
        obtain_token(ctx, current_env())
        fill_context(ctx)


def token_valid(ctx):
    if not ctx.expires_at:
        return True
    return float(ctx.expires_at) - time.time() > 0


def obtain_token(ctx, base_url):
    config = get_config()

    if base_url not in config.sections():
        click.echo("Unable to login. Register the environment first.")
        exit()

    client_id = config[base_url]['client_id']
    client_secret = config[base_url]['client_secret']

    url = "http://identity-management-idp." + base_url + "/token"

    auth = client_id + ':' + client_secret
    auth_encoded = base64.b64encode(auth.encode())

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Basic " + auth_encoded.decode("utf-8")
    }

    payload = "grant_type=client_credentials"

    response = requests.request("POST", url, data=payload, headers=headers).json()

    save_token(ctx, base_url, response['access_token'], time.time() + response['expires_in'])
