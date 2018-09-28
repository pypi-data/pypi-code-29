import argparse
import logging
import logging.config
import os
import sys

import pkg_resources

from .application import Application
from .version import VERSION

INSTALL_SERVICE_DESCRIPTION = """\
This program installs BRIO systemd service (copies service file from package resources
to predefined destination, i.e. /etc/systemd/system/brio.service), reloads daemons 
and enables the new service (i.e. issues following commands: "systemctl daemon-reload"
and "systemctl enable brio"). The nature of the program (modification of the system-wide
settings) requires it to be run with elevated privileges, e.g. as super-user. 
"""

INSTALL_CONFIGURATION_DESCRIPTION = """\
This program installs BRIO configuration file (copies default configuration file from
package resources to the pointed location).
"""

INSTALL_DESCRIPTION = """\
This program installs required components of the application, i.e. systemd service
and configuration files. It invokes 'install-service' and 'install-configuration'
programs - they can be run separately. Note that the privilege requirements of the
'install-service' program propagate to this program.
"""

APPLICATION_DESCRIPTION = """\
This program runs the BRIO server application. The server is configured according to the
configuration file passed as argument.
"""

SERVICE_FILE_NAME = 'brio.service'
SERVICE_FILE_DEST = '/etc/systemd/system/brio.service'
CONFIGURATION_FILE_NAME = 'brio.ini'
CONFIGURATION_FILE_DEST = '/etc/brio.ini'

LOGGING_CONFIG = [
    (logging.WARNING, '%(asctime)s %(levelname)s %(name)s: %(message)s'),
    (logging.INFO, '%(asctime)s %(levelname)s %(name)s [%(funcName)s]: %(message)s'),
    (logging.DEBUG, '%(asctime)s %(levelname)s %(name)s [%(funcName)s] [%(filename)s:%(lineno)d]: %(message)s')
]


def install_service(ns: argparse.Namespace = None):
    if ns is None:
        parser = argparse.ArgumentParser(prog='BRIO service installer',
                                         description=INSTALL_SERVICE_DESCRIPTION)
        parser.add_argument('-f', '--force', action='store_true',
                            help='force action, i.e. overwrite service file if already exists')
        parser.add_argument('--no-enable', action='store_true',
                            help='flag indicating that the brio.service should not be enabled')
        parser.add_argument('-v', '--version', action='version', version=VERSION)
        ns = parser.parse_args()
    if not sys.platform.startswith('linux'):
        logging.error('Platform not supported')
        return

    if ns.force:
        mode = 'w'
    else:
        mode = 'x'

    service_data = pkg_resources.resource_string('brio', ''.join(['resources/', SERVICE_FILE_NAME])).decode()
    try:
        with open(SERVICE_FILE_DEST, mode) as fd:
            fd.write(service_data)
        os.system('systemctl daemon-reload')
        if not ns.no_enable:
            os.system('systemctl enable brio')
            print('Service file installed and enabled')
        else:
            print('Service file installed')
    except FileExistsError:
        logging.exception('Service file already exists, use "--force" switch to overwrite', exc_info=False)
    except PermissionError:
        logging.exception('Access denied, try running as super-user', exc_info=False)


def install_configuration(ns: argparse.Namespace = None):
    if ns is None:
        parser = argparse.ArgumentParser(prog='BRIO configuration file installer',
                                         description=INSTALL_CONFIGURATION_DESCRIPTION)
        parser.add_argument('-f', '--force', action='store_true',
                            help='force action, i.e. overwrite configuration file if already exists')
        parser.add_argument('-d', '--destination', type=str, default=CONFIGURATION_FILE_DEST,
                            help='destination of the configuration file, defaults to /etc/brio.ini')
        parser.add_argument('-v', '--version', action='version', version=VERSION)
        ns = parser.parse_args()
    if not sys.platform.startswith('linux'):
        logging.error('Platform not supported')
        return

    if ns.force:
        mode = 'w'
    else:
        mode = 'x'

    config_data = pkg_resources.resource_string('brio', ''.join(['resources/', CONFIGURATION_FILE_NAME])).decode()
    try:
        with open(ns.destination, mode) as fd:
            fd.write(config_data)
        print('Configuration file installed to:', ns.destination)
    except FileExistsError:
        logging.exception('Configuration file already exists, use "--force" switch to overwrite', exc_info=False)
    except PermissionError:
        logging.exception('Access denied, try running as super-user', exc_info=False)


def install():
    parser = argparse.ArgumentParser(prog='BRIO service and configuration file installer',
                                     description=INSTALL_DESCRIPTION)
    parser.add_argument('-f', '--force', action='store_true',
                        help='force action, i.e. overwrite configuration file if already exists')
    parser.add_argument('-d', '--destination', type=str, default=CONFIGURATION_FILE_DEST,
                        help='destination of the configuration file, defaults to /etc/brio.ini')
    parser.add_argument('--no-enable', action='store_true',
                        help='flag indicating that the brio.service should not be enabled')
    parser.add_argument('-v', '--version', action='version', version=VERSION)
    ns = parser.parse_args()
    if not sys.platform.startswith('linux'):
        logging.error('platform not supported')
        return

    install_service(ns)
    install_configuration(ns)


def main():
    parser = argparse.ArgumentParser(prog='BRIO application',
                                     description=APPLICATION_DESCRIPTION)
    parser.add_argument('-c', '--configuration', type=argparse.FileType(mode='r'),
                        help='path to the configuration file')
    parser.add_argument('-ep', '--endpoint', type=str,
                        help='endpoint to which server will bind')
    parser.add_argument('-H', '--hostname', type=str,
                        help='hostname to which server will bind')
    parser.add_argument('-P', '--port', type=int,
                        help='port to which server will bind')
    parser.add_argument('-lc', '--logging-config', type=str,
                        help='path to logging configuration file')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='Increase program verbosity')
    parser.add_argument('-V', '--version', action='version', version=VERSION)
    ns = parser.parse_args()

    if ns.logging_config is not None:
        try:
            logging.config.fileConfig(ns.logging_config)
        except Exception:
            logging.exception('failed to configure logging module, invalid configuration file', exc_info=False)
            raise
    else:
        if ns.verbose >= len(LOGGING_CONFIG):
            ns.verbose = len(LOGGING_CONFIG) - 1
        logging.basicConfig(level=LOGGING_CONFIG[ns.verbose][0], format=LOGGING_CONFIG[ns.verbose][1])

    kwargs = dict(hostname=ns.hostname)
    if ns.configuration is not None:
        try:
            os.stat(ns.configuration)
            kwargs['configuration'] = ns.configuration
        except FileNotFoundError:
            logging.exception('Configuration file does not exist', exc_info=False)
            raise
    else:
        try:
            os.stat(CONFIGURATION_FILE_DEST)
            kwargs['configuration'] = CONFIGURATION_FILE_DEST
        except FileNotFoundError:
            pass
    if ns.port is not None:
        if ns.port not in range(0xFFFF):
            raise ValueError('port number out of range')
        kwargs['port'] = ns.port
    if ns.endpoint is not None:
        ep = ns.endpoint.split(':')
        if len(ep) != 2:
            raise ValueError('invalid format of endpoint string')
        ep[1] = int(ep[1])
        if ep[1] not in range(0xFFFF):
            raise ValueError('port number out of range')
        kwargs['endpoint'] = (ep[0], ep[1])

    app = Application(**kwargs)
    app.run()


if __name__ == '__main__':
    main()
