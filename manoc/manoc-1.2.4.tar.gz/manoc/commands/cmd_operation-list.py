import click
import jmespath
import requests
from prettytable import PrettyTable

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('operation-list')
@click.option('--query', help='JMESPath expression to filter result.')
@pass_context
def cli(ctx, query):
    """Command on list operations"""
    url = "http://api-gateway-mano." + ctx.base_url + "/vnf-manager/" + ctx.tenant + "/vnflcm/v1/vnf_lcm_op_occs"

    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer " + ctx.access_token
    }

    response = requests.request("GET", url, headers=headers)
    log_request(ctx, response)

    if query is None:
        t = PrettyTable(['ID', 'Operation', 'State', 'Vnf ID', 'Created at', 'Updated at'])
        for pkg in response.json():
            t.add_row(
                [pkg['id'], pkg['operation'], pkg['operationState'], pkg['vnfInstanceId'],
                 pkg['startTime'], pkg['stateEnteredTime']]
            )
        click.echo(t)
    else:
        expression = jmespath.compile(query)
        click.echo(expression.search(response.json()))



