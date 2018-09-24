from six import StringIO

import logging
import contextlib

from importlib import import_module

from django.conf import settings
from django.core import management
from django.core.management import get_commands
from django.core.management import load_command_class
from django.core.management.base import BaseCommand

try:
    from async import schedule
except ImportError:
    schedule = None

from admincommand.models import AdminCommand

# Cache variable to store runnable commands configuration
_command_configs = {}
output = StringIO()


def get_admin_commands():
    if not _command_configs:
        for app_module_path in settings.INSTALLED_APPS:
            try:
                admin_commands_path = "%s.admincommands" % app_module_path
                module = import_module(admin_commands_path)
            except ImportError:
                pass
            else:
                configs = dir(module)
                for config_name in configs:
                    AdminCommandClass = getattr(module, config_name)
                    if (
                        isinstance(AdminCommandClass, type)
                        and AdminCommandClass is not AdminCommand
                        and issubclass(AdminCommandClass, AdminCommand)
                    ):
                        command_config = AdminCommandClass()
                        _command_configs[command_config.url_name()] = command_config
    return _command_configs


def get_command(name):
    # this is a copy pasted from django.core.management.call_command
    app_name = get_commands()[name]
    if isinstance(app_name, BaseCommand):
        # If the command is already loaded, use it directly.
        klass = app_name
    else:
        klass = load_command_class(app_name, name)
    return klass


def call_command(command_name, user_pk, args=None, kwargs=None):
    """Call command and store output"""
    # user = User.objects.get(pk=user_pk) useless ?
    kwargs = kwargs if kwargs else {}
    args = args if args else []
    output = StringIO()
    kwargs["stdout"] = output
    management.call_command(command_name, *args, **kwargs)
    return output.getvalue()


@contextlib.contextmanager
def monkeypatched(object, name, patch):
    """ Temporarily monkeypatches an object. """

    pre_patched_value = getattr(object, name)
    setattr(object, name, patch)
    yield object
    setattr(object, name, pre_patched_value)


def getMessage(self):
    msg = str(self.msg)
    if self.args:
        msg = msg % self.args
    output.write(msg + "<br>")
    return msg


def run_command(command_config, cleaned_data, user):
    if hasattr(command_config, "get_command_arguments"):
        args, kwargs = command_config.get_command_arguments(cleaned_data, user)
    else:
        args, kwargs = list(), dict()

    if command_config.asynchronous:
        if not callable(schedule):
            return "This task is asynchronous but django-async is not installed"
        task = schedule(call_command, [command_config.command_name(), user.pk, args, kwargs])
        return task

    # Synchronous call
    # Change stdout to a StringIO to be able to retrieve output and display it to the admin
    # TODO put back here legacy code with settings if needed

    with monkeypatched(logging.LogRecord, "getMessage", getMessage):
        management.call_command(command_config.command_name(), *args, **kwargs)

    value = output.getvalue()
    output.seek(0)
    output.truncate(0)
    return value
