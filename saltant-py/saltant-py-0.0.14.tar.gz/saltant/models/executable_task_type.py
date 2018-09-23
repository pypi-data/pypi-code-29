"""Executable task type model and manager."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from .base_task_type import (
    BaseTaskType,
    BaseTaskTypeManager,
)


class ExecutableTaskType(BaseTaskType):
    """Model for executable task types.

    Attributes:
        id (int): The ID of the task type.
        name (str): The name of the task type.
        description (str): The description of the task type.
        user (str): The user associated with the task type.
        datetime_created (:class:`datetime.datetime`): The datetime when
            the task type was created.
        command_to_run (str): The command to run to execute the task.
        environment_variables (list): The environment variables required
            on the host to execute the task.
        required_arguments (list): The argument names for the task type.
        required_arguments_default_values (dict): Default values for the
            tasks required arguments.
    """
    pass


class ExecutableTaskTypeManager(BaseTaskTypeManager):
    """Manager for executable task types.

    Attributes:
        _client (:py:class:`saltant.client.Client`): An authenticated
            saltant client.
        list_url (str): The URL to list task types.
        detail_url (str): The URL format to get specific task types.
        model (:class:`ExecutableTaskType`): The model of the task
            instance being used.
    """
    list_url = 'executabletasktypes/'
    detail_url = 'executabletasktypes/{id}/'
    model = ExecutableTaskType
