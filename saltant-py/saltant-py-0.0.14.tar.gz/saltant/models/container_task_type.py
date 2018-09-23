"""Container task type model and manager."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from .base_task_type import (
    BaseTaskType,
    BaseTaskTypeManager,
)


class ContainerTaskType(BaseTaskType):
    """Model for container task types.

    Attributes:
        id (int): The ID of the task type.
        name (str): The name of the task type.
        description (str): The description of the task type.
        user (str): The user associated with the task type.
        datetime_created (:class:`datetime.datetime`): The datetime when
            the task type was created.
        command_to_run (str): The command to run inside the container to
            execute the task.
        environment_variables (list): The environment variables required
            on the host to execute the task.
        required_arguments (list): The argument names for the task type.
        required_arguments_default_values (dict): Default values for the
            tasks required arguments.
        logs_path (str): The path of the logs directory inside the
            container.
        results_path (str): The path of the results directory inside the
            container.
        container_image (str): The container name and tag. For example,
            ubuntu:14.04 for Docker; and docker://ubuntu:14:04 or
            shub://vsoch/hello-world for Singularity.
        container_type (str): The type of the container.
    """
    def __init__(
            self,
            id,
            name,
            description,
            user,
            datetime_created,
            command_to_run,
            environment_variables,
            required_arguments,
            required_arguments_default_values,
            logs_path,
            results_path,
            container_image,
            container_type,):
        """Initialize a container task type.

        Args:
            id (int): The ID of the task type.
            name (str): The name of the task type.
            description (str): The description of the task type.
            user (str): The user associated with the task type.
            datetime_created (:class:`datetime.datetime`): The datetime
                when the task type was created.
            command_to_run (str): The command to run to execute the task.
            environment_variables (list): The environment variables
                required on the host to execute the task.
            required_arguments (list): The argument names for the task type.
            required_arguments_default_values (dict): Default values for
                the tasks required arguments.
            logs_path (str): The path of the logs directory inside the
                container.
            results_path (str): The path of the results directory inside
                the container.
            container_image (str): The container name and tag. For
                example, ubuntu:14.04 for Docker; and docker://ubuntu:14:04
                or shub://vsoch/hello-world for Singularity.
            container_type (str): The type of the container.
        """
        # Call the parent constructor
        super(ContainerTaskType, self).__init__(
            id=id,
            name=name,
            description=description,
            user=user,
            datetime_created=datetime_created,
            command_to_run=command_to_run,
            environment_variables=environment_variables,
            required_arguments=required_arguments,
            required_arguments_default_values=required_arguments_default_values,
        )

        # Add in the attributes unique to container task types
        self.logs_path = logs_path
        self.results_path = results_path
        self.container_image = container_image
        self.container_type = container_type


class ContainerTaskTypeManager(BaseTaskTypeManager):
    """Manager for Container task types.

    Attributes:
        _client (:py:class:`saltant.client.Client`): An authenticated
            saltant client.
        list_url (str): The URL to list task types.
        detail_url (str): The URL format to get specific task types.
        model (:class:`ExecutableTaskType`): The model of the task
            instance being used.
    """
    list_url = 'containertasktypes/'
    detail_url = 'containertasktypes/{id}/'
    model = ContainerTaskType
