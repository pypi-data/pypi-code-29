import os
import logging
try:
    from configparser import ConfigParser
except ImportError:
    import ConfigParser


class ConfigNotExistsError(Exception):
    pass


class Config(object):
    def __init__(self):
        self.config_file = os.environ.get('JENNIFER_CONFIG_FILE')
        if self.config_file is None:
            raise EnvironmentError("JENNIFER_CONFIG_FILE is not set")
        self.config_file = os.path.join(os.getcwd(), self.config_file)
        if not os.path.exists(self.config_file):
            raise FileNotFoundError("JENNIFER_CONFIG_FILE not exist")

        self.config = ConfigParser()
        self.config.read(self.config_file)  # Read config file
        self.logger = logging.getLogger('jennifer')

    def validate_config(self):
        # if self.server_address is None:
        #     raise ConfigNotExistsError('server_address is not found')
        # elif self.server_port is None:
        #     raise ConfigNotExistsError('server_port is not found')
        # elif self.domain_id is None:
        #     raise ConfigNotExistsError('domain_id is not found')
        # elif self.instance_id is None:
        #     raise ConfigNotExistsError('instance_id is not found')
        return

    def _get_config(self, item):
        try:
            return self.config.get('JENNIFER', item)
        except configparser.NoSectionError:
            return None
        except configparser.NoOptionError:
            return None

    @property
    def server_address(self):
        v = self._get_config('server_address')
        if v is None:
            return '127.0.0.1'
        return str(v)

    @property
    def server_port(self):
        v = self._get_config('server_port')
        if v is None:
            return 5000
        return int(v)

    @property
    def domain_id(self):
        v = self._get_config('domain_id')
        if v is None:
            return 1000
        return int(v)

    @property
    def instance_id(self):
        v = self._get_config('instance_id')
        if v is None:
            return -1
        return int(v)

    @property
    def log_path(self):
        v = self._get_config('log_path')
        if v is None:
            return '/tmp/jennifer-python-agent.log'
        return v

    def write_instance_id(self, inst_id):
        if inst_id is None or not isinstance(inst_id, int):
            logging.getLogger('jennifer').error('Can not write non-int inst_id')
        self.config.set('JENNIFER', 'instance_id', str(inst_id))
        self.save()

    def save(self):
        f = open(self.config_file, 'w')
        self.config.write(f)
