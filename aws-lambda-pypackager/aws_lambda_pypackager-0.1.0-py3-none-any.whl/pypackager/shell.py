'''CLI entrypoint'''


import argparse
import logging
import os
import boto3

from datetime import datetime
from os import path
from lambda_uploader.package import build_package
from jinja2 import Template

LOG = logging.getLogger(__name__)


def _stack_exists(client, name):
    try:
        resp = client.describe_stacks(
            StackName=name,
        )
    except AmazonCloudFormationException:
        return False

    return True


def _execute(args):
    '''Main execution function'''

    venv = None
    if args.no_virtualenv:
        venv = False
    elif args.virtualenv:
        venv = args.virtualenv

    pkg_pth = args.function_dir or args.package_name
    requirements = args.requirements or []

    LOG.info("Building package " + args.artifact_pth)
    pkg = build_package(pkg_pth, requirements, virtualenv=venv,
                        ignore=args.ignore, extra_files=args.extra_files,
                        zipfile_name=args.artifact_pth,
                        pyexec=args.runtime)
    if not args.no_clean:
        pkg.clean_workspace()

    obj_name = path.basename(pkg.zip_file)
    if args.subparser_name == 'upload':
        aws_session = boto3.session.Session(region_name=args.region,
                              profile_name=args.profile_name)

        LOG.info("Uploading artifact to " + args.bucket_name)
        s3_client = aws_session.client('s3')
        transfer = boto3.s3.transfer.S3Transfer(s3_client)
        transfer.upload_file(pkg.zip_file, args.bucket_name,
                             obj_name)
    # Output Lambda Package Name
    print(obj_name)


def main():
    '''entrypoint'''

    import argparse

    artifact_pth = path.join(os.getcwd(), 'lambda-{}.zip'.format(datetime.now().isoformat('_')))

    parser = argparse.ArgumentParser(
        description = 'Simple opinionated way of packaging Python AWS Lambda functions.')

    package_parent = argparse.ArgumentParser(add_help=False)
    package_parent.add_argument('--artifact', '-A', dest='artifact_pth',
                                default=artifact_pth,
                                help='Custom name and path of the resulting package. (Default {})'.format(
                                    artifact_pth))
    package_parent.add_argument('--no-clean', dest='no_clean',
                                action='store_const',
                                const=True,
                                help='Dont clean up the temporary workspace. Useful for debugging')
    package_parent.add_argument('--virtualenv', '-e',
                                help='Package from existing Virtualenv.')
    package_parent.add_argument('--extra-files', '-x', dest='extra_files',
                                action='append',
                                help='Include file or directory path in package.')
    package_parent.add_argument('--ignore', '-i', dest='ignore',
                                action='append',
                                help='Specify files/directories for the packaging process to ignore.')
    package_parent.add_argument('--no-virtualenv', dest='no_virtualenv',
                                action='store_const',
                                const=True,
                                help='Do not create or include a virtualenv.')
    package_parent.add_argument('--requirements', '-r', dest='requirements',
                                help='Specify a requirements.txt file to include.')
    package_parent.add_argument('--runtime', dest='runtime',
                                default='python3.6',

                                help='Python runtime to package as. (ex: python2.7 or python3.6')
    package_parent.add_argument('function_dir', nargs='?',
                                help='Specify a function directory different from the name.')

    subparsers = parser.add_subparsers(dest="subparser_name")
    # Package parser
    p_parser = subparsers.add_parser('package', help='Package the function locally.',
                                     parents=[package_parent])

    upload_parent = argparse.ArgumentParser(add_help=False)
    upload_parent.add_argument('--bucket-name', '-b', dest='bucket_name',
                               required=True,
                               help='Destination S3 bucket for artifacts to be uploaded and read from. (Optional)')
    upload_parent.add_argument('--region', '-R', dest='region',
                               help='AWS Region')
    upload_parent.add_argument('--profile-name', '-P', dest='profile_name',
                               help='AWS Local config profile name to use with AWS operations.')

    # Upload parser
    u_parser = subparsers.add_parser('upload', help='Package and upload the parser to artifacts bucket.',
                                     parents=[package_parent, upload_parent])

    verbose = parser.add_mutually_exclusive_group()
    verbose.add_argument('-V', dest='loglevel', action='store_const',
                         const=logging.INFO,
                         help='Set log level to INFO')
    verbose.add_argument('-VV', dest='loglevel', action='store_const',
                         const=logging.DEBUG,
                         help='Set log level to DEBUG')
    parser.set_defaults(loglevel=logging.WARNING)
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    _execute(args)
