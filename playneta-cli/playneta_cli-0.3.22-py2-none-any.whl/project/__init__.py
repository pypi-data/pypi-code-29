import pyaml
import yaml
import os
import init
import build
import deploy


def help(parser):
    parser.add_argument('--project-file',
                        dest='project_file',
                        default=os.getcwd() + '/playneta.yml',
                        help='target component')

    commands = parser.add_subparsers(title='project commands')

    # initialization
    subparser = commands.add_parser(name='init',
                                    help='project initialization')

    subparser.set_defaults(command=init.command)

    # compilation
    subparser = commands.add_parser(name='build',
                                    help='project compilation')

    build.help(subparser)
    subparser.set_defaults(command=build.command)

    # delivery
    subparser = commands.add_parser(name='deploy',
                                    help='project delivery')

    deploy.help(subparser)
    subparser.set_defaults(command=deploy.command)


def main(args, file_root):
    project = yaml.load(file(args.project_file, 'r'))

    os.chdir(os.path.dirname(args.project_file))
    args.command(project['project'], args, file_root)

    pyaml.pprint(project, file=file(args.project_file, 'w'), vspacing=[2, 1])
