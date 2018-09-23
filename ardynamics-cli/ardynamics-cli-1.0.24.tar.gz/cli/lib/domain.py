class Domain:
    _config = None

    domain_name = None
    ftp_username = None
    ftp_password = None
    db_username = None
    db_password = None
    alias = []

    def __init__(self, domain_name, config):
        """
        :type domain_name: str
        :type config: Config
        """
        self._config = config
        self.domain_name = domain_name
        self.alias = self._config.get_option(self.domain_name, 'alias', True)
        self.ftp_username = self._config.get_secret(self.domain_name + '/' + 'ftp_username')
        self.ftp_password = self._config.get_secret(self.domain_name + '/' + 'ftp_password', True)
        self.db_username = self._config.get_secret(self.domain_name + '/' + 'db_username')
        self.db_password = self._config.get_secret(self.domain_name + '/' + 'db_password', True)

    def get_archive_name(self):
        return self.domain_name + '.tgz'
