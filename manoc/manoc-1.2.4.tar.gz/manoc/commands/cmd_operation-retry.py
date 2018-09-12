import json
import sys

import click
import jmespath
import requests

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('operation-retry')
@click.argument('id')
@pass_context
def cli(ctx, id):
    """Command on retry operation"""
    url = "http://api-gateway-mano." + ctx.base_url \
          + "/vnf-manager/" + ctx.tenant + "/vnflcm/v1/vnf_lcm_op_occs/" + id + "/retry"

    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer " + ctx.access_token
    }

    response = requests.request("POST", url, headers=headers)
    log_request(ctx, response)

    if response.status_code != 200:
        click.echo("Operation failed")
        sys.exit(1)

    click.echo(json.dumps(response.json(), indent=4))


