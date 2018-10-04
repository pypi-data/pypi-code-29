"""Command line entry point."""

import click

from aptivate_cli import cmd
from aptivate_cli.config import pass_config
from aptivate_cli.settings import PLAY_TEMPLATE_URL, ROLE_TEMPLATE_URL


@click.group()
@click.version_option()
def main() -> None:
    """Fully automated luxury Aptivate command line interface."""


@main.command()
@click.option(
    '--env', '-e',
    type=click.Choice(('dev', 'stage', 'prod')),
    help='The target environment',
    required=True,
    default='dev',
    show_default=True,
)
@pass_config
def deploy(config, env: str) -> None:
    """Deploy an application."""
    cmd.create_ansible_home(config)
    cmd.git_clone_project_play(config)
    cmd.pipenv_install_project_play(config)
    cmd.galaxy_install_project_play(config)
    cmd.playbook_run_project_play(config, env)


@main.command()
@click.option(
    '--type', '-t',
    type=click.Choice(('play', 'role',)),
    help='The type of template',
    required=True,
)
def template(type: str) -> None:
    """Generate a new template."""
    if type == 'play':
        cmd.clone_template(PLAY_TEMPLATE_URL)
    elif type == 'role':
        cmd.clone_template(ROLE_TEMPLATE_URL)
    else:
        message = click.style('Unknown type', fg='red')
        raise click.ClickException(message)
