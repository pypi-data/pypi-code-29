import click
from datadog_deployer import dump
from datadog_deployer import deploy
from datadog_deployer import connect


@click.group()
def cli():
    pass


@cli.command(name='dump')
@click.option(
    '--account',
    required=False,
    default="DEFAULT",
    help='name of the Datadog account.')
@click.option(
    '--filename',
    type=click.Path(exists=False, file_okay=True),
    help='to dump the monitors to.')
def do_dump(account, filename):
    connect(account)
    dump(filename)


@cli.command(name='deploy')
@click.option(
    '--account',
    required=False,
    default="DEFAULT",
    help='name of the Datadog account.')
@click.option(
    '--filename',
    type=click.Path(exists=False, file_okay=True),
    help='to deploy the monitors from.')
def do_deploy(account, filename):
    connect(account)
    deploy(filename)


if __name__ == '__main__':
    cli()
