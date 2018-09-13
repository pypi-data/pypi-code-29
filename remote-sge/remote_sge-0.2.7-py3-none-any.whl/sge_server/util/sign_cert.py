from os import system, remove
from os.path import expanduser, expandvars, join, basename
from argparse import RawDescriptionHelpFormatter
from string import Template
from sge.util.arg_parser import ArgParser
from sge_server.util import install_server
from sge_server.util.install_server import SslKeyCommands

parser = ArgParser(prog="remote_sge sign_cert",
                   formatter_class=RawDescriptionHelpFormatter)

DESCRIPTION = """Adds a new client key to the Certificate Authority.

Requires a CSR from a given client.  See [remote_sge request_cert].
"""

def parse_args():
    parser.add_argument('sign_cert', help='Command being run')
    parser.add_argument('csr_file', help="Path to CSR to import.")
    parser.add_argument('-r', '--root',
                        help=install_server.ROOT_DESCRIPTION,
                        default="$HOME/.config/remote_sge")
    parser.description = DESCRIPTION
    return parser.parse_args()

CLI_CRT = ("openssl ca -batch -config ${conf_file} -policy signing_policy " +
           "-extensions signing_req -out ~/${cert_name}.pem -infiles ${csr_path}")


MESSAGE = """
Your certificate was signed and added to the CA.
The certificate file is bundled with the CA's root certificate at 
~/%s.tgz.  The CSR file you submitted was deleted.

Now copy the cert to client and install with `remote_sge install_cert`.
"""

from sge_client.util.request_certificate import print_important

def archive_certs(cert_name, client_cert, ca_dir):
    system("tar -cvf $HOME/%s.tar " % cert_name + " -C $HOME " + basename(client_cert) )
    system("tar -vuf $HOME/%s.tar " % cert_name + "-C %s cacert.pem" % ca_dir)
    system("gzip $HOME/%s.tar" % cert_name)
    system("mv $HOME/%s.tar.gz $HOME/%s.tgz" % (cert_name, cert_name))
    system("rm " + client_cert)
    

def main():
    args = parse_args()
    csr_path = expanduser(expandvars(args.csr_file))
    config_root = expanduser(expandvars(args.root))
    certs_path  = join(config_root, 'certs')
    
    cert_name  = basename(args.csr_file)[:-4]
    cmd_templ = Template(CLI_CRT)
    result = system(cmd_templ.substitute(conf_file=join(config_root, 'openssl-ca.ini'),
                                         csr_path=csr_path,
                                         cert_name=cert_name))
    if result != 0:
        print_important("Something went wrong signing the certificate.\n" + 
                        "OpenSSL returned %s\n" % result + 
                        "Check terminal output and maybe verify the contents of the CSR.")
        exit(result)
    else:
        archive_certs(cert_name, "$HOME/%s.pem" % cert_name, join(certs_path, 'ca'))
        remove(csr_path)
        print_important(MESSAGE % cert_name)
        exit(0)
        
if __name__ == '__main__':
    main()
