#!/usr/bin/env python3
"""
Run sysmonitor

It loads command line arguments to load configurations
"""
import sys
import logging
import time
import schedule

from sysmonitor.configuration import Configuration
from sysmonitor.orm import migrator
from sysmonitor.models import host

LOGGER = logging.getLogger("sysmonitor")

CONFIG = Configuration()
CONFIG.setlog()


def message(msg, output_file=sys.stdout, log_method=False):
    """
    Send message to output and log

    :param string msg: Messate to print
    :param stream output_file: Where to print the message
    :param method log_method: Log method to register message
    """
    if log_method and callable(log_method):
        log_method(msg)
    print(msg, file=output_file)

def _get_host(name):
    hst = host.Host.select().where(host.Host.name == name)
    if hst.count() == 0:
        message("Unable to find host %s" % name,
                output_file=sys.stderr, log_method=LOGGER.error)
        return False
    return hst[0]


def create_host():
    """Creates a host from cmd args"""
    host_data = CONFIG.get("magic", "add_host")
    if not host_data:
        return False
    new_host = host.Host.create(
        name=host_data[0],
        address=host_data[1],
        authentication_api=host_data[2] if host_data[2] else None,
        requires_authentication=True if host_data[2] else False)
    message("Created host %s" % new_host.name, log_method=LOGGER.info)
    return True

def update_host():
    """Updates a host from cmd args"""
    host_data = CONFIG.get("magic", "update_host")
    if not host_data:
        return False
    hst = _get_host(host_data[0])
    if not hst:
        return False
    hst.address = host_data[1]
    hst.authentication_api = host_data[2] if host_data[2] else None
    hst.requires_authentication = True if host_data[2] else False
    hst.save()
    message("Updated host %s" % hst.name, log_method=LOGGER.info)
    return True

def toggle_host():
    """Active or inactive a host"""
    host_data = CONFIG.get("magic", "toggle_host")
    if not host_data:
        return False
    hst = _get_host(host_data)
    if not hst:
        return False
    hst.active = not hst.active
    hst.save()
    state = "Activated" if hst.active else "Deactivated"
    message("%s host %s" % (state, hst.name), log_method=LOGGER.info)
    return True

def delete_host():
    """delete a host"""
    host_data = CONFIG.get("magic", "delete_host")
    if not host_data:
        return False
    hst = _get_host(host_data)
    if not hst:
        return False
    hst.delete_instance()
    message("Removed host %s" % host_data, log_method=LOGGER.warning)
    return True

if not CONFIG.get("magic", "without_migration"):
    MIGRATOR = migrator.Migrator()
    MIGRATOR.do_migration()

if CONFIG.get("magic", "add_host"):
    create_host()
elif CONFIG.get("magic", "update_host"):
    update_host()
elif CONFIG.get("magic", "toggle_host"):
    toggle_host()
elif CONFIG.get("magic", "delete_host"):
    delete_host()
else:
    schedule.every(int(CONFIG.get("hosts", "query_time"))).seconds.do(host.Host.query_hosts)

    while True:
        schedule.run_pending()
        time.sleep(1)
