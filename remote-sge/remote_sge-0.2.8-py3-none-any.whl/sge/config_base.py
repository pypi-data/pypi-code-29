"Configuration classes"

class Sections(object):
    "Sections"
    GENERAL = r'general'
    CLIENT = r'client'
    QSUB_SETTINGS = r'qsub_settings'
    QSUB_PARAMS = r'qsub_parameters'
    ENVIRONMENT = r'command_environment'
    SERVER = r'server'

class Settings(object):
    "Settings"
    SHELL = r'shell'
    HOST = r'host'
    PORT = r'port'
    CA_CERTIFICATE = r'ca_certificate'
    CLIENT_CERTIFICATE = r'client_certificate'
    CLIENT_KEY = r'client_key'
    USE_HTTPS = r'use_https'

class Defaults(object):
    "Defaults"
    SHELL = r'/bin/bash'
    HOST = r'remote-sge-host'
    PORT = 8080
    USE_HTTPS = True

class ConfigBase(object):
    "Config Base"


    def __init__(self, configparser):
        """
        Args:
            configparser (:class:`configobj.ConfigObj`): configuration settings.
        """
        pass
        self.general_settings = configparser[Sections.GENERAL]

    def shell(self):
        "The shell to use for calls to qsub and qstat."
        return self.general_settings.get(Settings.SHELL, Defaults.SHELL)
