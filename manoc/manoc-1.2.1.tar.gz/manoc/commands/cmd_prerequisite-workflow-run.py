import click
import requests

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('prerequisite-workflow-run')
@click.argument('workflow_id')
@click.option('--inputs-file', help='Inputs file.')
@click.option('--vim-id', help='VIM ID.')
@click.option('--tenant-id', help='VIM Tenant ID.')
@click.option('--descriptor-id', help='Descriptor ID.')
@click.option('--version', help='Version.')
@pass_context
def cli(ctx, workflow_id, inputs_file, vim_id, tenant_id, descriptor_id, version):
    """Command on run prerequisites mistral workflow"""
    url = "http://api-gateway-mano." + ctx.base_url \
          + "/prerequisite-manager/" + ctx.tenant + "/workflows/" + workflow_id + "/start"

    headers = {
        'Content-Type': "application/x-yaml",
        'Authorization': "Bearer " + ctx.access_token
    }

    file = open(inputs_file, 'rb')
    payload = file.read()

    query_params = {'vim_id': vim_id, 'tenant_id': tenant_id, 'descriptor_id': descriptor_id, 'version': version}

    response = requests.post(url, data=payload, headers=headers, params=query_params)
    log_request(ctx, response)

    click.echo(response.json()['id'])
