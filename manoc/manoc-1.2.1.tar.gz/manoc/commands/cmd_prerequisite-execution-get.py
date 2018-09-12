import json
import sys

import click
import jmespath
import requests

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('prerequisite-execution-get')
@click.argument('execution_id')
@click.option('--query', help='JMESPath expression to filter result.')
@pass_context
def cli(ctx, execution_id, query):
    """Command on get prerequisites mistral executions"""
    url = "http://api-gateway-mano." + ctx.base_url \
          + "/prerequisite-manager/" + ctx.tenant + "/executions/" + execution_id

    headers = {
        'Authorization': "Bearer " + ctx.access_token
    }

    response = requests.get(url, headers=headers)
    log_request(ctx, response)

    if response.status_code != 200:
        click.echo("No resources found")
        sys.exit(1)

    if query is None:
        click.echo(json.dumps(response.json(), indent=4))
    else:
        expression = jmespath.compile(query)
        click.echo(expression.search(response.json()))
