from __future__ import print_function

class BaseCommand(object):

    def execute(self, **_kwargs):
        pass

class Command(BaseCommand):

    def __init__(self, name, execute, kwargs=None, **_kwargs):
        self.name = name
        self._execute_handler = execute
        if not kwargs:
            self.kwargs = dict()
        else:
            self.kwargs = kwargs

    def __str__(self):
        return  '<{} :: {} :: {}>'.format(self.name, self._execute_handler, self.kwargs)

    def execute(self, **kwargs):
        param = self.kwargs.copy() # external parameters have greater priority
        param.update(kwargs)
        self._execute_handler(**param)


def _get_full_interface(module, interface):
    if interface.startswith(module):
        return interface
    else:
        return module + '.' + interface


def parse_command(**_kwargs):
    '''
    parse one command from settings
    :param **kwargs:    setting for command
    :return command:    command parsed from settings
    available settings :
        import      -- the module will import
        kwargs      -- parameters for command execution
        execute     -- attribute of module, used as execute handler for common command (LRC.Server.Command.Command)
        command     -- command class
    '''
    if 'import' in _kwargs:
        module = _kwargs['import']
        exec('import ' + module)
        del _kwargs['import']
    else:
        module = ''

    if 'kwargs' in _kwargs:
        kwargs = eval(_kwargs['kwargs'])
        del _kwargs['kwargs']
    else:
        kwargs = dict()

    if 'interface' in _kwargs: # interface to get command instance
        interface = _get_full_interface(module, _kwargs['interface'])
        del _kwargs['interface']
        return eval(interface)(kwargs=kwargs, **_kwargs)

    if 'command' in _kwargs: # command class
        command_class = _get_full_interface(module, _kwargs['command'])
        del _kwargs['command']
        return eval(command_class)(kwargs=kwargs, **_kwargs)

    if 'execute_interface' in _kwargs: # interface to get execute handler for a common command (LRC.Server.Command.Command)
        execute_interface = _get_full_interface(module, _kwargs['execute_interface'])
        del _kwargs['execute_interface']
        return Command(name="parsed from string", execute=eval(execute_interface)(), kwargs=kwargs, **_kwargs)

    if 'execute' in _kwargs: # execute handler for a common command (LRC.Server.Command.Command)
        execute = _get_full_interface(module, _kwargs['execute'])
        del _kwargs['execute']
        return Command(name="parsed from string", execute=eval(execute), kwargs=kwargs, **_kwargs)

    raise ValueError('parse_command : one of the following should be specified : {}'.format(
            {'interface','command','execute_interface','execute'}))


if '__main__' == __name__:
    command_config={'import':'LRC.Server.Commands.CommandTest', 'interface':'get_command_instance'}
    command = parse_command(**command_config)
    print(command)
    command.execute()
