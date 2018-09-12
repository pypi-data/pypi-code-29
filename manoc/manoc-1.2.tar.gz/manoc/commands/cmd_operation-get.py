import json
import sys

import click
import jmespath
import requests

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('operation-get')
@click.option('--query', help='JMESPath expression to filter result.')
@click.argument('id')
@pass_context
def cli(ctx, id, query):
    """Command on get operation"""
    url = "http://api-gateway-mano." + ctx.base_url + "/vnf-manager/" + ctx.tenant + "/vnflcm/v1/vnf_lcm_op_occs/" + id

    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer " + ctx.access_token
    }

    response = requests.request("GET", url, headers=headers)
    log_request(ctx, response)

    if response.status_code != 200:
        click.echo("No resources found")
        sys.exit(1)

    if query is None:
        click.echo(json.dumps(response.json(), indent=4))
    else:
        expression = jmespath.compile(query)
        click.echo(expression.search(response.json()))


