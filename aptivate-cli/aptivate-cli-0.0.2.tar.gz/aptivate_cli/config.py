"""A module for generating configuration based on convention.

For each command that needs a configuration to run, we hand it over to the
command logic by using the `@pass_config` decorator that Click provides. The
`Config` objects works hard to accumulate all the configuration context that a
command will need by basing decisions of our naming and location conventions.

"""

import typing
from os import environ, getcwd, listdir
from os.path import abspath, basename, join

import click

from aptivate_cli import settings


class Config():
    """The command configuration."""

    def __init__(self, ) -> None:
        """Initialise the object."""
        self.values: typing.Dict[str, str] = {}
        self.secret_values: typing.Dict[str, str] = {}
        self.sanity_checks()

    def sanity_checks(self) -> None:
        """Sanity checks before building the configuration."""
        cwd_contents = listdir(abspath(getcwd()))

        if 'manage.py' not in cwd_contents:
            message = "No 'manage.py' in current directory"
            raise click.ClickException(click.style(message, fg='red'))

    def prompt_for_values(self,
                          variables: typing.List[str],
                          hide_input: bool = False) -> typing.Dict[str, str]:
        """Ask for values using the Click prompt."""
        PROMPT_MAPPINGS = {
            'mysql': 'MySQL root password required',
            'sudo': 'Sudo password required',
        }

        if not all(var in PROMPT_MAPPINGS for var in variables):
            message = click.secho('Missing prompt mapping', fg='red')
            raise click.ClickException(message)

        for variable in variables:
            env_marker = 'APTIVATE_CLI_{}'.format(variable.upper())
            env_value = environ.get(env_marker, None)

            if env_value is not None:
                self.values[variable] = env_value
                continue

            self.values[variable] = click.prompt(
                PROMPT_MAPPINGS[variable],
                hide_input=hide_input
            )

        return self.values

    def prompt_for_secret_values(self,
                                 variables: typing.List[str],
                                 hide_input: bool = True) -> dict:
        """Ask for values using the Click secret prompt."""
        self.secret_values = self.prompt_for_values(
            variables,
            hide_input=hide_input
        )
        return self.secret_values

    @property
    def project_name(self):
        """The name of the project."""
        return basename(abspath(getcwd()))

    @property
    def project_play_url(self):
        """The project play Git URL."""
        return settings.PROJECT_PLAY_REPOSITORY_URL.format(self.project_name)

    @property
    def project_play_path(self):
        """The project play path."""
        return join(
            abspath(getcwd()),
            self.ansible_home_path,
            '{}-play'.format(self.project_name)
        )

    def playbook_path(self, env: str) -> str:
        """The project playbook path."""
        return join(
            abspath(getcwd()),
            self.ansible_home_path,
            '{}-play'.format(self.project_name),
            settings.ANSIBLE_PLAYBOOKS_DIRECTORY,
            env,
            settings.ANSIBLE_PLAYBOOK_FILE

        )

    @property
    def inventory_path(self) -> str:
        """The project inventory path."""
        return join(
            abspath(getcwd()),
            self.ansible_home_path,
            '{}-play'.format(self.project_name),
            settings.ANSIBLE_INVENTORIES_DIRECTORY,
            settings.ANSIBLE_INVENTORY_FILE,

        )

    @property
    def role_paths(self) -> typing.List[str]:
        """The project roles path."""
        return [
            join(
                abspath(getcwd()),
                self.ansible_home_path,
                '{}-play'.format(self.project_name),
                role_path
            )
            for role_path in settings.ANSIBLE_ROLE_PATHS
        ]

    @property
    def ansible_home_path(self):
        """The home directory for Ansible project files."""
        return settings.ANSIBLE_HOME_DIRECTORY

    @property
    def galaxy_requirements_file(self):
        """The name by convention for the galaxy requirements file."""
        return settings.ANSIBLE_REQUIREMENTS_FILE


pass_config = click.make_pass_decorator(Config, ensure=True)
