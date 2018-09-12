import sys

import click
import requests

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('vnf-heal')
@click.argument('id')
@click.option('--inputs', help='File with heal inputs.')
@pass_context
def cli(ctx, id, inputs):
    """Command on heal vnf"""
    url = "http://api-gateway-mano." + ctx.base_url \
          + "/vnf-manager/" + ctx.tenant + "/vnflcm/v1/vnf_instances/" + id + "/heal/"

    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + ctx.access_token
    }

    if inputs is None:
        click.echo('Inputs file not specified.')
        sys.exit(1)

    file = open(inputs, 'rb')
    payload = file.read()

    response = requests.request("POST", url, data=payload, headers=headers)
    log_request(ctx, response)

    if response.status_code != 202:
        click.echo("Operation failed")
        sys.exit(1)

    operation_url = response.headers['Location']
    click.echo(operation_url[operation_url.rfind('/')+1:])
