"""
Client installer
"""

import os
from os.path import join, expandvars, exists, expanduser
import tarfile
import argparse
from sge.util.arg_parser import ArgParser
from sge_server.util.install_server import (EDITOR_TEXT, ROOT_DESCRIPTION, get_editor,
                                            edit_config_file, maybe_sudo, sudo, CONFIG)
from sge_client.io.database import initialize as initialize_db

parser = ArgParser(prog="remote_sge install_client",
                                 formatter_class=argparse.RawTextHelpFormatter)


END_MESSAGE = """
Installation is complete.  The certificates have been placed in %s. Please verify
permissions on the certificate files.  I've deleted the archive file at %s.  Now would be
a good time to verify that you deleted the file from the server as well.

Use "remote_sge shuttle" to move jobs to the remote server.  Thanks for playing the game!
"""

def do_install():
    args = parse_args()
    if args.install:
        editor = args.editor
        if args.development:
            CONFIG['development'] = True
        certs_location = join(args.root, "certs")
        maybe_sudo("mkdir -p " + certs_location)
        maybe_sudo("tar zxfp %s -C %s" % (args.certificates, certs_location))
        if args.force or not exists(join(expandvars(expanduser(args.root)), 'config.ini')):
            edit_config_file("Config file", "config.ini", args.root, editor=editor, unattended=args.unattended)
        os.system("rm " + args.certificates)
        initialize_db()
        print(END_MESSAGE % (certs_location, args.certificates))
    else:
        parser.error("You need to signal '-i' in order to install.  Also consider supplying -e if you don't like vim.")

def parse_args():
    parser.add_argument("install_client", help="The name of this command")
    parser.add_argument('-i', '--install',
                        help="Perform the installation.",
                        action="store_true")
    parser.add_argument('-u', '--unattended',
                        help="Unattended installation",
                        action="store_true")
    parser.add_argument('-c', '--certificates',
                        help=("Location of tarfile archive containing certificates.  " +
                              "Defaults to $HOME/remote_sge_client_certs.tgz"),
                        default=expandvars("$HOME/remote_sge_client_certs.tgz"))
    parser.add_argument('-e', '--editor',
                        help=EDITOR_TEXT, default='vim')
    parser.add_argument('-r', '--root',
                        help=ROOT_DESCRIPTION,
                        default="$HOME/.config/remote_sge")
    parser.add_argument('-f', '--force',
                        help="Overwrite config.ini even if it exists already.",
                        action="store_true")
    parser.add_argument('-s', '--sudo',
                        help="Use sudo for placing config files (e.g. if installing into /etc).",
                        action="store_true")
    parser.add_argument('-d', '--development',
                        help="Development mode.  Install from PYTHONPATH.",
                        action="store_true")
    return parser.parse_args()
