import json

import click
import jmespath
import requests

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('vnf-delete')
@click.argument('id')
@pass_context
def cli(ctx, id):
    """Command on delete vnf"""
    url = "http://api-gateway-mano." + ctx.base_url + "/vnf-manager/" + ctx.tenant + "/vnflcm/v1/vnf_instances/" + id

    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer " + ctx.access_token
    }

    response = requests.request("DELETE", url, headers=headers)
    log_request(ctx, response)

    click.echo('VNF deleted.')

