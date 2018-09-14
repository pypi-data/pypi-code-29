from zensols.actioncli import OneConfPerActionOptionsCli
from zensols.pybuild import TagUtil, SetupUtilCli

VERSION = '0.1'


# recommended app command line
class ConfAppCommandLine(OneConfPerActionOptionsCli):
    def __init__(self):
        repo_dir_op = ['-r', '--repodir', True,
                       {'dest': 'repo_dir',
                        'metavar': 'DIRECTORY',
                        'default': '.',
                        'help': 'path of the repository'}]
        msg_op = ['-m', '--message', True,
                  {'dest': 'message',
                   'default': 'none',
                   'metavar': 'STRING',
                   'help': 'documentation for the new tag'}]
        cnf = {'executors':
               [{'name': 'tag',
                 'executor': lambda params: TagUtil(**params),
                 'actions': [{'name': 'last',
                              'meth': 'print_last_tag',
                              'doc': 'Print the last tag',
                              'opts': [repo_dir_op]},
                             {'name': 'info',
                              'meth': 'dump_info',
                              'doc': 'print repo version information',
                              'opts': [repo_dir_op]},
                             {'name': 'create',
                              'doc': 'Create a new tag',
                              'opts': [repo_dir_op, msg_op]},
                             {'name': 'del',
                              'meth': 'delete_last_tag',
                              'doc': 'Delete the tag',
                              'opts': [repo_dir_op]},
                             {'name': 'recreate',
                              'meth': 'recreate_last_tag',
                              'opts': [repo_dir_op]}],
                 'doc': 'Recreate the tag (delete then add)'},
                {'name': 'setup',
                 'executor': lambda params: SetupUtilCli(**params),
                 'actions': [{'name': 'prsetup',
                              'meth': 'write',
                              'doc': 'print the setup used for setuptools',
                              'opts': [repo_dir_op,
                                       ['-s', '--setupapth', True,
                                        {'metavar': 'DIRECTORY',
                                         'dest': 'setup_path',
                                         'default': 'src/python',
                                         'help': 'the path to the setup directory (setup.py)'}],
                                       ['-n', '--name', True,
                                        {'metavar': 'STRING',
                                         'help': 'the pypi project name (i.e. zensols.someproj)'}],
                                       ['-u', '--user', True,
                                        {'metavar': 'STRING',
                                         'help': 'the git user name (i.e. plandes)'}],
                                       ['-p', '--project', True,
                                        {'metavar': 'STRING',
                                         'help': 'the  name of the project (i.e. someproj)'}]]}]}],
               'whine': 1}
        super(ConfAppCommandLine, self).__init__(cnf, version=VERSION)


def main():
    cl = ConfAppCommandLine()
    cl.invoke()
