from pelops.abstractmicroservice import AbstractMicroservice
from lysidike.services.servicefactory import ServiceFactory
from lysidike.tasks.taskfactory import TaskFactory
from lysidike.schema.publishgateway import get_schema
import lysidike


class PublishGateway(AbstractMicroservice):
    _version = lysidike.version

    _services = None
    _tasks = None

    def __init__(self, config, mqtt_client=None, logger=None):
        AbstractMicroservice.__init__(self, config, "publish-gateway", mqtt_client, logger)
        self._services = ServiceFactory.get_services(self._config["services"], mqtt_client, logger)
        self._tasks = TaskFactory.get_tasks(self._config["tasks"], self._services, mqtt_client, logger)

    def _start(self):
        self._logger.info("PublishGateway._start - starting services")
        for service in self._services.values():
            service.start()
        self._logger.info("PublishGateway._start - starting tasks")
        for task in self._tasks.values():
            task.start()
        self._logger.info("PublishGateway._start - finished")

    def _stop(self):
        self._logger.info("PublishGateway._stop - stopping tasks")
        for task in self._tasks.values():
            task.stop()
        self._logger.info("PublishGateway._stop - stopping services")
        for service in self._services.values():
            service.stop()
        self._logger.info("PublishGateway._stop - finished")

    @classmethod
    def _get_description(cls):
        return "Lysidike publishes incoming mqtt messages to various internet services like email."

    @classmethod
    def _get_schema(cls):
        return get_schema()


def standalone():
    PublishGateway.standalone()


if __name__ == "__main__":
    PublishGateway.standalone()
