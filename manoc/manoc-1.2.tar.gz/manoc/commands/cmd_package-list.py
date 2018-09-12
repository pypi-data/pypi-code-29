import click
import jmespath
import requests
from prettytable import PrettyTable

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('package-list')
@click.option('--query', help='JMESPath expression to filter result.')
@pass_context
def cli(ctx, query):
    """Command on list packages"""
    url = "http://api-gateway-mano." + ctx.base_url + "/vnf-manager/" + ctx.tenant + "/vnfpkgm/v1/vnf_packages"

    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer " + ctx.access_token
    }

    response = requests.request("GET", url, headers=headers)
    log_request(ctx, response)

    if query is None:
        t = PrettyTable(['ID', 'VNFD ID', 'VNF Provider', 'VNF Product Name', 'VNF Software Version', 'VNFD Version'])
        for pkg in response.json():
            t.add_row(
                [pkg['id'], pkg['vnfdId'], pkg['vnfProvider'], pkg['vnfProductName'],
                 pkg['vnfSoftwareVersion'], pkg['vnfdVersion']]
            )
        click.echo(t)
    else:
        expression = jmespath.compile(query)
        click.echo(expression.search(response.json()))



