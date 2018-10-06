# __init__.py

__authors__ = ['Todd Salazar', ]
__version__ = '1.0'

# v1.0 (tsalazar) -- 20181006 Initial version.

import logging
import os
from dataclasses import dataclass


@dataclass
class Docker:
    """Methods for working inside a Docker container.

    secrets_dir: Directory for Docker secrets.
    config_dir: Directory for Docker configs.
    """

    secrets_dir: str = '/run/secrets'
    config_dir: str = '/run/secrets'

    def __post_init__(self):

        self.__logger = logging.getLogger(__name__)

    @property
    def secret_list(self):
        """
        :return: A list of secrets
        """

        return os.listdir(self.secrets_dir)

    @property
    def config_list(self):
        """
        :return: A lit of configs
        """
        return os.listdir(self.secrets_dir)

    def get_secret(self, secret_name):
        """Retrieve the value of a Docker secret.

        :param secret_name: The name of the secret to retrieve the value from.
        :return: The value of the secret
        """

        with open(f'{self.secrets_dir}/{secret_name}', 'r') as fp:
            secret_value = fp.read()

        return secret_value

    def get_config(self, config_name):
        """Retrieve the value of a Docker config.

        :param config_name: The name of the config to retrieve the value from.
        :return: The value of the config
        """

        with open(f'{self.config_dir}/{config_name}', 'r') as fp:
            config_value = fp.read()

        return config_value
