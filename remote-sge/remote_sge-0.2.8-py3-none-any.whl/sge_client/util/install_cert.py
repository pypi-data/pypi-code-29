import shutil
import os
import tarfile
import stat
from subprocess import run
from tempfile import NamedTemporaryFile, TemporaryFile
from string import Template
from os.path import join, expanduser, expandvars, exists
from argparse import RawDescriptionHelpFormatter
from configobj import ConfigObj
from sge.util.arg_parser import ArgParser
from sge_server.util import install_server

parser = ArgParser(prog="remote_sge install_cert",
                   formatter_class=RawDescriptionHelpFormatter)

DESCRIPTION = \
"""Ingests a tgz from server, which includes a signed client certificate and
a copy of the server's root CA certificate for the client to verify the
server TLS certificate.

The files will be placed in the locations stipulated in the client config.

If [endpoint] is given, looks for a named endpoint in the client config and
uses that, defaulting to the primary connection info written at the top of
the [client] section of the config file.

Having succesfully run this script, a new endpoint should be ready to use.
Test configuration by running `remote_sge test_server <endpoint>`.
"""

def parse_args():
    parser.add_argument('install_cert', help='Command being run')
    parser.add_argument('certs', help='Path to certificate archive given by server.')
    parser.add_argument('endpoint', help='Optional. endpoint for server being added.  ' +
                        'Enter "default" or omit to '+
                        'overwrite the existing default connection certificate.',
                        nargs="?", default="default")
    parser.add_argument('-r', '--root',
                        help=install_server.ROOT_DESCRIPTION,
                        default="$HOME/.config/remote_sge")
    parser.description = DESCRIPTION
    return parser.parse_args()

def expandall(path):
    return expanduser(expandvars(path))

ME_RW__GROUP_RO = stat.S_IREAD | stat.S_IWRITE | stat.S_IRGRP

def main():
    args = parse_args()
    config_root = expanduser(expandvars(args.root))
    config = ConfigObj(infile=join(config_root, 'config.ini'))
    certs_path = join(config_root, 'certs')

    if args.endpoint == "default":
        config = config["client"]
    else:
        config = config["client"][args.endpoint]

    cert_path = join(certs_path, config["client_certificate"])
    # os.system("openssl aes-256-cbc -d -in %s -out %s" % (args.certificate, cert_path))
    # os.system("gunzip " + args.certs)
    with TemporaryFile(mode='w+b') as temp_tarfile:
        run(["gunzip", args.certs, '-c'], stdout=temp_tarfile)
        temp_tarfile.seek(0)
        with tarfile.open(mode="r", fileobj=temp_tarfile) as archive:
            for tarinfo in archive.getmembers():
                print(tarinfo.name)
                if tarinfo.name == "cacert.pem":
                    ca_cert_path = expandall(config['ca_certificate'])
                    with open(ca_cert_path, mode='wb') as file:
                        file.write(archive.extractfile(tarinfo).read())
                    os.chmod(ca_cert_path, ME_RW__GROUP_RO)
                else:
                    client_cert_path = expandall(config['client_certificate'])
                    with open(client_cert_path, mode='wb') as file:
                        file.write(archive.extractfile(tarinfo).read())
                    # archive.extract(tarinfo, path=client_cert_path)
                    os.chmod(client_cert_path, ME_RW__GROUP_RO)

    print("You should be good to go.  Have fun...")

if __name__ == '__main__':
    main()
