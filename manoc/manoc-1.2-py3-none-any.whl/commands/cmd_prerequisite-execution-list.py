from datetime import datetime

import click
import jmespath
import requests
from prettytable import PrettyTable

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('prerequisite-execution-list')
@click.option('--query', help='JMESPath expression to filter result.')
@pass_context
def cli(ctx, query):
    """Command on list prerequisites mistral executions"""
    url = "http://api-gateway-mano." + ctx.base_url + "/prerequisite-manager/" + ctx.tenant + "/executions"

    headers = {
        'Authorization': "Bearer " + ctx.access_token
    }

    response = requests.get(url, headers=headers)
    log_request(ctx, response)

    if query is None:
        t = PrettyTable(['ID', 'Workflow ID', 'State', 'Created at', 'Updated at'])
        for pkg in response.json()['executions']:
            t.add_row(
                [pkg['id'], pkg['workflow_id'], pkg['state'],
                 datetime.fromtimestamp(pkg['created_at'] / 1000).isoformat(),
                 datetime.fromtimestamp(pkg['updated_at'] / 1000).isoformat()]
            )
        click.echo(t)
        # click.echo(response.json())
    else:
        expression = jmespath.compile(query)
        click.echo(expression.search(response.json()))
