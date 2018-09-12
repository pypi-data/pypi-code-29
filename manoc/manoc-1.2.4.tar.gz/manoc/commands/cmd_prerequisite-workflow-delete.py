import click
import requests

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('prerequisite-workflow-delete')
@click.argument('workflow_id')
@pass_context
def cli(ctx, workflow_id):
    """Command on delete prerequisites mistral workflow"""
    url = "http://api-gateway-mano." + ctx.base_url + "/prerequisite-manager/" + ctx.tenant + "/workflows/" + workflow_id

    headers = {
        'Authorization': "Bearer " + ctx.access_token
    }

    response = requests.delete(url, headers=headers)
    log_request(ctx, response)

    click.echo('Prerequisite workflow deleted.')
