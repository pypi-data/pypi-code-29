from zensols.actioncli import OneConfPerActionOptionsCliEnv
from zensols.hostcon import Connector, AppConfig


class ConfAppCommandLine(OneConfPerActionOptionsCliEnv):
    """Command line entry point.

    """
    def __init__(self):
        host_op = ['-n', '--hostname', False,
                   {'dest': 'host_name',
                    'help': 'the host to connect to'}]
        dryrun_op = ['-d', '--dryrun', False,
                     {'dest': 'dry_run',
                      'action': 'store_true',
                      'help': 'don\'t actually connect, but act like it'}]
        output_file_op = ['-o', '--output', False,
                          {'dest': 'output_file',
                           'metavar': 'FILE',
                           'help': 'output file for the script actions'}]
        cnf = {'executors':
               [{'name': 'fixer',
                 'executor': lambda params: Connector(**params),
                 'actions': [{'name': 'info',
                              'meth': 'print_info',
                              'doc': 'print configuration info',
                              'opts': [host_op, dryrun_op]},
                             {'name': 'env',
                              'meth': 'print_environment',
                              'doc': 'print info as environment variables',
                              'opts': [host_op, dryrun_op]},
                             {'name': 'script',
                              'meth': 'create_bourne',
                              'doc': 'create a script using current network',
                              'opts': [host_op, output_file_op]},
                             {'name': 'xterm',
                              'meth': 'exec_xterm',
                              'doc': 'start an xterm on host',
                              'opts': [host_op, dryrun_op]},
                             {'name': 'emacs',
                              'meth': 'exec_emacs',
                              'doc': 'start emacs on the host',
                              'opts': [host_op, dryrun_op]},
                             {'name': 'mount',
                              'meth': 'exec_mount',
                              'doc': 'mount directories from host locally',
                              'opts': [host_op, dryrun_op]},
                             {'name': 'umount',
                              'meth': 'exec_umount',
                              'doc': 'un-mount directories',
                              'opts': [host_op, dryrun_op]},
                             {'name': 'login',
                              'meth': 'exec_login',
                              'doc': 'slogin to host',
                              'opts': [host_op, dryrun_op]}]}],
               'config_option': {'name': 'config',
                                 'opt': ['-c', '--config', False,
                                         {'dest': 'config', 'metavar': 'FILE',
                                          'help': 'configuration file'}]},
               'whine': 1}
        super(ConfAppCommandLine, self).__init__(
            cnf, config_env_name='hostconrc', config_type=AppConfig,
            pkg_dist='zensols.hostcon')

    def config_parser(self):
        super(ConfAppCommandLine, self).config_parser()
        self._add_short_option(self.parser)
        if self.default_config_file is not None:
            config = AppConfig(self.default_config_file)
            self.default_action = config.get_option('action')

def main():
    cl = ConfAppCommandLine()
    cl.invoke()
