import ConfigParser, json, os.path


class Config:
    _ssm = None
    _config = None
    _latest_backup = None
    _domains = []

    def __init__(self, config_file):
        if not os.path.isfile(config_file):
            from cli.lib import InputError
            raise InputError('Unable to find configuration file: ' + config_file)
        from cli.lib.ssm import Ssm
        self._ssm = Ssm()
        self._config = ConfigParser.RawConfigParser()
        self._config.read(config_file)
        self._latest_backup = self._config.get('config', 'latest_backup')
        self._domains = json.loads(self._config.get('config', 'domains'))

    def get_domains(self):
        return self._domains

    def get_backup_folder(self):
        return 'backup/' + self._latest_backup

    def get_secret(self, parameter_name, decrypt=False):
        return self._ssm.get_parameter(parameter_name, decrypt)

    def get_option(self, section, option, parse_json = False):
        if parse_json:
            return json.loads(self._config.get(section, option))
        return self._config.get(section, option)
