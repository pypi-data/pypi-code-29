from pelops import mylogger


class ServiceFactory:
    @staticmethod
    def get_service(service_type, config, mqtt_client, logger):
        factory_logger = mylogger.get_child(logger, __name__)
        factory_logger.info(" - creating service")
        factory_logger.debug(" - service config: ".format(config))

        if service_type == "email":
            from lysidike.services.emailservice import EmailService
            service = EmailService(config, mqtt_client, logger)
        elif service_type == "stdout":
            from lysidike.services.stdoutservice import StdOutService
            service = StdOutService(config, mqtt_client, logger)
        else:
            factory_logger.error("ServiceFactory.get_service - unknown type '{}'.".format(service_type))
            raise ValueError("ServiceFactory.get_service - unknown type '{}'.".format(service_type))

        return service

    @staticmethod
    def get_services(config, mqtt_client, logger):
        factory_logger = mylogger.get_child(logger, __name__)
        factory_logger.info("creating services - starting")
        factory_logger.debug("service configs: ".format(config))
        services = {}
        for service_type, service_config in config.items():
            service_type = service_type.lower()
            services[service_type] = ServiceFactory.get_service(service_type, service_config, mqtt_client, logger)
            factory_logger.info("added service {}".format(service_type))

        factory_logger.info("creating services - finished")

        return services
