import click
import jmespath
import requests
from prettytable import PrettyTable

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('vnf-list')
@click.option('--query', help='JMESPath expression to filter result.')
@pass_context
def cli(ctx, query):
    """Command on list vnfs"""
    url = "http://api-gateway-mano." + ctx.base_url + "/vnf-manager/" + ctx.tenant + "/vnflcm/v1/vnf_instances"

    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer " + ctx.access_token
    }

    response = requests.request("GET", url, headers=headers)
    log_request(ctx, response)

    if query is None:
        t = PrettyTable(['ID', 'Name', 'VNF Package ID', 'Instantiation State', 'VNFD ID'])
        for pkg in response.json():
            t.add_row(
                [pkg['id'], pkg['vnfInstanceName'], pkg['onboardedVnfPkgInfoId'],
                 pkg['instantiationState'], pkg['vnfdId']]
            )
        click.echo(t)
    else:
        expression = jmespath.compile(query)
        click.echo(expression.search(response.json()))



