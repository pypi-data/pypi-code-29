import click
import requests

from manoc.cli import pass_context
from manoc.utils.logging import log_request


@click.command('package-onboard')
@click.option('--name', help='Package name')
@click.option('--file', help='ZIP arhive with vnf package.')
@pass_context
def cli(ctx, name, file):
    """Command on onboard package"""
    package_id = create_package(ctx, name)
    upload_package(ctx, package_id, file)
    click.echo(package_id)


def create_package(ctx, name):
    url = "http://api-gateway-mano." + ctx.base_url + "/vnf-manager/" + ctx.tenant + "/vnfpkgm/v1/vnf_packages"

    payload = {}
    if name is not None:
        payload = "{\n  \"name\":\"" + name + "\"\n}"

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'Authorization': "Bearer " + ctx.access_token
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    log_request(ctx, response)

    return response.json()['id']


def upload_package(ctx, package_id, file):
    url = "http://api-gateway-mano." + ctx.base_url + "/vnf-manager/" + ctx.tenant \
          + "/vnfpkgm/v1/vnf_packages/" + package_id + "/package_content"

    headers = {
        'Authorization': "Bearer " + ctx.access_token
    }

    file = open(file, 'rb')
    files = {"file": file}

    response = requests.put(url, files=files, headers=headers)
    log_request(ctx, response)
