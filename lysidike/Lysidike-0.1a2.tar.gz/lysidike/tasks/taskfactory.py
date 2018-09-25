from pelops import mylogger
from lysidike.tasks.task import Task


class TaskFactory:
    @staticmethod
    def get_tasks(config, services, mqtt_client, logger):
        factory_logger = mylogger.get_child(logger, __name__)
        factory_logger.info("creating tasks - starting")
        factory_logger.debug("task configs: ".format(config))
        factory_logger.debug("task configs: ".format(config))

        tasks = {}
        for entry in config:
            task = Task(entry, services, mqtt_client, logger)
            tasks[task.name] = task
            factory_logger.info("added task {}".format(task.name))

        factory_logger.info("creating tasks - finished")
        return tasks
