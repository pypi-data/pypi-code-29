import os
import json
import logging


logger = logging.getLogger('setup_log')


class Secrets:
    '''Get secrets params from "secrets.json" file
       generated with "generator <PROJ_NAME>"
    '''
    def __init__(self, SETTINGS_DIR, *args, **kwargs):
        self.SETTINGS_DIR = SETTINGS_DIR
        self.__dict__.update(self._get_secrets())

    def __getattr__(self, attr):
        logger.warning(f'Secret param {attr} not found!')
        return None

    def _get_secrets(self):
        SECRET_FILE = os.path.join(self.SETTINGS_DIR, 'secrets.json')
        try:
            with open(SECRET_FILE, 'r') as file:
                SECRETS = json.load(file)
        except FileNotFoundError:
            logger.warning('File not found! "generator <PROJ_NAME>" first please!')
            SECRETS = {}
        return SECRETS

# backwards compatibility
get_secrets = Secrets
