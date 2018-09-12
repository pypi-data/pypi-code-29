import json

import click
import jmespath
import requests

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('vnf-create')
@click.argument('vnfd-id')
@click.option('--name', help='VNF Name')
@click.option('--description', help='VNF Description')
@pass_context
def cli(ctx, vnfd_id, name, description):
    """Command on create vnf"""
    url = "http://api-gateway-mano." + ctx.base_url + "/vnf-manager/" + ctx.tenant + "/vnflcm/v1/vnf_instances"

    if description is None:
        description = ''

    payload = "{\"vnfdId\": \"" + vnfd_id + "\", \"vnfInstanceName\": \"" + name \
              + "\", \"vnfInstanceDescription\": \"" + description + "\", \"shared\": false, \"shares\": []}"

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'Authorization': "Bearer " + ctx.access_token
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    log_request(ctx, response)

    click.echo(response.json()['id'])


