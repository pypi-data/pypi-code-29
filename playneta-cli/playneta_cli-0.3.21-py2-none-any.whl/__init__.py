import argparse
import os
import playneta.project
import playneta.service

FILE_ROOT = os.getenv('HOME') + '/.playneta/playneta-cli/files'


def main():
    parser = argparse.ArgumentParser(description='Playneta CLI toolkit')

    commands = parser.add_subparsers(title='playneta commands')

    # api code generation
    subparser = commands.add_parser(name='service',
                                    help='service code generation')

    subparser.set_defaults(main=service.main)
    service.help(subparser)

    # project management
    subparser = commands.add_parser(name='project',
                                    help='project management tools')

    subparser.set_defaults(main=project.main)
    project.help(subparser)

    # processing
    args = parser.parse_args()
    args.main(args, FILE_ROOT)


if __name__ == '__main__':
    main()
