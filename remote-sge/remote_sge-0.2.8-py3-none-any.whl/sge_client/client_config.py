from os.path import expanduser, expandvars
from sge.config_base import ConfigBase, Sections, Settings, Defaults

class ClientConfig(ConfigBase):
    "Client App Configuration"
    def __init__(self, configobj, endpoint="default"):
        """
        Args:
            configparser (:class:`configobj.ConfigObj`): configuration settings.
        """

        super().__init__(configobj)
        self.client_settings = configobj[Sections.CLIENT]
        if endpoint and endpoint != "default":
            self.client_settings = self.client_settings[endpoint]

    @property
    def host(self):
        "Host"
        return self.client_settings.get(Settings.HOST, Defaults.HOST)

    @property
    def port(self):
        "Port"
        return self.client_settings.as_int(Settings.PORT)

    @property
    def ssl_config(self):
        if self.use_https:
            return dict(cert=self.client_key_config, verify=self.ca_certificate)
        else:
            return dict()

    @property
    def ca_certificate(self):
        if self.client_settings.get(Settings.CA_CERTIFICATE):
            return expanduser(expandvars(self.client_settings.get(Settings.CA_CERTIFICATE)))

    @property
    def client_key_config(self):
        "Returns a tuple containing client cert+key pair, or None if not given."
        if self.client_settings.get(Settings.CLIENT_CERTIFICATE):
            return (expanduser(expandvars(self.client_settings.get(Settings.CLIENT_CERTIFICATE))),
                    expanduser(expandvars(self.client_settings.get(Settings.CLIENT_KEY))))
        else:
            return None

    @property
    def use_https(self):
        return self.client_settings.as_bool(Settings.USE_HTTPS)

    @property
    def request_schema(self):
        if self.use_https:
            return 'https'
        else:
            return 'http'
