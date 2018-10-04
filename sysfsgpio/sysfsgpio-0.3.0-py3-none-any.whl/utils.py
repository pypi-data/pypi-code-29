import logging
import os
import sys
import threading

import pkg_resources


def pin2name(id: int) -> str:
    """Convert pin number to name"""
    if not isinstance(id, int):
        raise TypeError('id must be a non-negative integer')
    if id < 0:
        raise ValueError('id must be a non-negative integer')
    ports = 'ABCDEFGHIJKL'
    port_num = id // 32
    pin_num = id - (port_num * 32)
    if pin_num >= 32:
        raise ValueError('id out of range')
    try:
        return 'P{}{}'.format(ports[port_num], pin_num)
    except IndexError:
        raise ValueError('id out of range')


def name2pin(name: str) -> int:
    """Convert pin name to number"""
    if not isinstance(name, str):
        raise TypeError('name must be a string')
    if len(name) < 3:
        raise ValueError('invalid name format')
    name = name.upper()
    if name[0] != 'P':
        raise ValueError('invalid name format')
    ports = 'ABCDEFGHIJKL'
    port_idx = ports.find(name[1])
    if port_idx < 0:
        raise ValueError('port name out of range')
    return int(port_idx * 32 + int(name[2:]))


def get_pins() -> list:
    """Get pins available in the system

    :returns: a list whose entries are tuples in format (id, name)
    :rtype: list[tuple(int, str)]
    """
    pins = []
    try:
        entries = os.listdir('/sys/class/gpio')
    except FileNotFoundError:
        return pins
    logging.debug('there are %d entries in /sys/class/gpio: %s', len(entries), entries)
    for e in entries:
        if e.startswith('gpiochip'):
            logging.debug('ignoring chip device: %s', e)
        elif not e.startswith('gpio'):
            logging.debug('ignoring non-pin entry: %s', e)
        else:
            try:
                idx = int(e[4:])
                name = pin2name(idx)
                pins.append((idx, name))
            except ValueError:
                logging.exception('failed to parse: %s', e, exc_info=False)
                continue
    return pins


def install_service():
    if not sys.platform.startswith('linux'):
        logging.error('Platform not supported.')
        return

    if '--force' in sys.argv:
        mode = 'w'
    else:
        mode = 'x'

    service_data = pkg_resources.resource_string('sysfsgpio', 'resources/gpio-exporter.service').decode()
    try:
        with open('/etc/systemd/system/gpio-exporter.service', mode) as fd:
            fd.write(service_data)
        os.system('systemctl daemon-reload')
        os.system('systemctl enable gpio-exporter')
        print('gpio-exporter service installed and enabled')
    except FileExistsError:
        logging.exception('Service file already exists, use "--force" switch to overwrite.', exc_info=False)
    except PermissionError:
        logging.exception('Access denied, try running as super-user.', exc_info=False)


def install_rules():
    if not sys.platform.startswith('linux'):
        logging.error('Platform not supported.')
        return

    if '--force' in sys.argv:
        mode = 'w'
    else:
        mode = 'x'

    rules_data = pkg_resources.resource_string('sysfsgpio', 'resources/gpio.rules').decode()
    try:
        with open('/etc/udev/rules.d/99-gpio.rules', mode) as fd:
            fd.write(rules_data)
        os.system('udevadm control --reload-rules')
        os.system('udevadm trigger')
        print('sysfsgpio rules installed')
    except FileExistsError:
        logging.exception('Rules file already exists, use "--force" switch to overwrite.', exc_info=False)
    except PermissionError:
        logging.exception('Access denied, try running as super-user.', exc_info=False)


def install():
    if not sys.platform.startswith('linux'):
        logging.error('Platform not supported.')
        return

    install_service()
    install_rules()
