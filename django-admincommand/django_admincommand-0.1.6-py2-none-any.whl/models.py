
from sneak.models import SneakModel

from admincommand.utils import generate_instance_name, generate_human_name
from admincommand.forms import GenericCommandForm


class AdminCommand(SneakModel):
    """Subclass this class to create an admin command
    class name should match the name of the command to be executed
    using the reverse algorithm used to construct instance names following
    the PEP8. For instance for a management command named
    ``fixing_management_policy`` the admin command class should be named
    ``FixingManagementPolicy``.
    """

    # :attribute asynchronous: True if the command should be executed
    # asynchronously
    asynchronous = False

    objects = None
    form = GenericCommandForm

    def __init__(self, *args, **kwargs):
        super(AdminCommand, self).__init__(*args, **kwargs)

    def get_help(self):
        if hasattr(self, "help"):
            return self.help
        return self.command().help

    def command(self):
        """Getter of the management command import core"""
        from . import core

        command = core.get_command(self.command_name())
        return command

    @classmethod
    def command_name(cls):
        return generate_instance_name(cls.__name__)

    def name(self):
        return generate_human_name(type(self).__name__)

    def url_name(self):
        return type(self).__name__.lower()

    @classmethod
    def permission_codename(cls):
        return "can_run_command_%s" % cls.command_name()

    @classmethod
    def all(cls):
        from . import core

        for runnable_command in core.get_admin_commands().values():
            yield runnable_command

    def get_command_arguments(self, forms_data, user):
        # TODO check why user was passed over here

        args = []
        for key, value in forms_data.items():

            if value is True:
                args.append("--" + key)
            elif value is False:
                pass  # Django commands does not accepts False options to be explicitly set.
            else:
                args.append("--" + key + "=" + value)

        return args, {}
