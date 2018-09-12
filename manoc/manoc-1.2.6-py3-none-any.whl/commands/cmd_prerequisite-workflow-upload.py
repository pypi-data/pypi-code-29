import click
import jmespath
import requests

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('prerequisite-workflow-upload')
@click.argument('file')
@pass_context
def cli(ctx, file):
    """Command on upload prerequisites mistral workflow"""
    url = "http://api-gateway-mano." + ctx.base_url \
          + "/prerequisite-manager/" + ctx.tenant + "/workflows/"

    headers = {
        'Content-Type': "application/x-yaml",
        'Authorization': "Bearer " + ctx.access_token
    }

    file = open(file, 'rb')
    payload = file.read()

    response = requests.post(url, data=payload, headers=headers)
    log_request(ctx, response)

    click.echo(jmespath.compile('[].id | [0]').search(response.json()))
