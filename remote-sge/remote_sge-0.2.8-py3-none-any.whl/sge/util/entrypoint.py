"""
Console entrypoint for various features:

* Client-Side Installer (remote_sge install_client)
* Server-Side Installer (remote_sge install_server)
"""
from argparse import ArgumentParser, RawTextHelpFormatter, REMAINDER
from sge_client.util.install_client import do_install as install_client
from sge_client.util.install_cert import main as install_cert
from sge_server.util.install_server import main as install_server
from sge_server.util.check_server import main as test_server
from sge_server.util.sign_cert import main as sign_cert
from sge_client.util.request_certificate import main as request_certificate
from sge_client.shuttle import main as shuttle

COMMAND_TEXT = """Available commands are:

install_server - Installs server components.
test_server    - Sends a request to verify that SSL,
                 nginx, and Gunicorn are all configured.
install_client - Initial configuration for client.
request_cert   - Create private key and configure a client config.
sign_cert      - Sign a certificate from a CSR and return the cert to user.

For additional help, type "remote_sge <command>" with no args.
"""

def main():
    parser = ArgumentParser(prog="remote_sge: command utility for Remote SGE",
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument('command', help=COMMAND_TEXT)
    parser.add_argument('args', nargs=REMAINDER)
    args = parser.parse_args()
    if args.command == 'install_client':
        install_client()
    elif args.command == 'install_server':
        install_server()
    elif args.command == 'test_server':
        test_server()
    elif args.command == 'sign_cert':
        sign_cert()
    elif args.command == 'request_cert':
        request_certificate()
    elif args.command == 'install_cert':
        install_cert()
    elif args.command == 'shuttle':
        shuttle()

if __name__ == '__main__':
    main()
