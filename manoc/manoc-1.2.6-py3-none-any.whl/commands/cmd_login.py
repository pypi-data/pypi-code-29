import configparser

import click

from manoc.cli import pass_context
from manoc.utils.auth import obtain_token
from manoc.utils.config import save_tenant, get_config


@click.command('login')
@click.argument('base-url')
@click.option('--tenant', help='Tenant ID.', prompt=True)
@pass_context
def cli(ctx, base_url, tenant):
    """Command on login"""

    obtain_token(ctx, base_url)
    save_tenant(base_url, tenant)

