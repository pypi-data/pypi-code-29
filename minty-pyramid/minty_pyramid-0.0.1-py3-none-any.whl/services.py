from minty_cqs.command_and_query import CommandAndQueryConfig


class MintyCqsNoConfiguration(Exception):
    pass


class MintyAppServiceCQS:
    def load(self, config: object) -> bool:
        """Load and configures the Command and Query service for Pyramid

        :param config: Pyramid Configurator object
        :type config: object
        :raises ValueError: When 'minty_service.cqs.domains' is missing
        :raises ValueError: When 'minty_service.cqs.domainprefix' is missing
        :return: True on success
        :rtype: bool
        """

        # Add a directive to Configuratorobject with our CQS Configuration
        config.add_directive(
            "get_cqs_configuration", self._directive_get_cqs_configuration
        )

        settings = config.get_settings()

        if "minty_service.cqs.domains" not in settings:
            raise MintyCqsNoConfiguration(
                "Required configuration 'minty_service.cqs.domains'"
                + " is missing in ini file"
            )

        if "minty_service.cqs.domainprefix" not in settings:
            raise MintyCqsNoConfiguration(
                "Required configuration 'minty_service.cqs.domainprefix'"
                + " is missing in ini file"
            )

        # Get domains from ini file
        domains = [
            domain
            for domain in settings["minty_service.cqs.domains"].split("\n")
            if domain != ""
        ]
        domainprefix = settings["minty_service.cqs.domainprefix"]

        # Load configuration in Configurator
        cqs_config = CommandAndQueryConfig()
        cqs_config.domainprefix = domainprefix

        for domain in domains:
            cqs_config.add_domain(domain=domain)

        config.__cqs_configuration = cqs_config

    @staticmethod
    def _directive_get_cqs_configuration(config):
        return config.__cqs_configuration


class MintyAppServiceConfig:
    def load(self, config):
        pass


class MintyAppService:
    """Application Service for loading extra Minty services into Pyramid."""

    _services = []
    _service_map = {"cqs": MintyAppServiceCQS, "config": MintyAppServiceConfig}

    def load_services(self, config: object) -> bool:
        """Load services from ini directive 'minty_service.enable'.

        :param config: Pyramid Configurator object
        :type config: object
        :return: True on success
        :rtype: bool
        """

        settings = config.get_settings()
        if "minty_service.enable" not in settings.keys():
            return False

        # Make sure we skip empty services
        services = [
            service
            for service in settings["minty_service.enable"].split("\n")
            if service != ""
        ]

        # In the future, we could use importlib here. Keep it simple for now
        self._services = services
        for service in services:
            service_class = self._service_map[service]()
            service_class.load(config)

        return True
