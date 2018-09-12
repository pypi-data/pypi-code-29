import json
from argparse import ArgumentParser
from subprocess import call
from time import sleep

from cc_agency.commons.conf import Conf

DESCRIPTION = 'Create a MongoDB admin user with read and write access, as specified in cc-agency configuration.'


def attach_args(parser):
    parser.add_argument(
        '-c', '--conf-file', action='store', type=str, metavar='CONF_FILE',
        help='CONF_FILE (yaml) as local path.'
    )
    parser.add_argument(
        '--host', action='store', type=str, metavar='HOST',
        help='Overwrite MongoDB host specified in CONF_FILE.'
    )


def main():
    parser = ArgumentParser(description=DESCRIPTION)
    attach_args(parser)
    args = parser.parse_args()

    return run(**args.__dict__)


def run(conf_file, host):
    conf = Conf(conf_file)

    host = host if host else conf.d['mongo'].get('host', 'localhost')
    port = conf.d['mongo'].get('port', 27017)
    db = conf.d['mongo']['db']
    username = conf.d['mongo']['username']
    password = conf.d['mongo']['password']

    data = {
        'pwd': password,
        'roles': [{
            'role': 'readWrite',
            'db': db
        }]
    }

    dumped = json.dumps(data)

    update_command = 'mongo --host {host} --port {port} --eval \'database = db.getSiblingDB("{db}"); database.updateUser("{username}", {dumped})\''.format(
        host=host,
        port=port,
        db=db,
        username=username,
        dumped=dumped
    )

    data['user'] = username

    dumped = json.dumps(data)

    create_command = 'mongo --host {host} --port {port} --eval \'database = db.getSiblingDB("{db}"); database.createUser({dumped})\''.format(
        host=host,
        port=port,
        db=db,
        dumped=dumped
    )

    for _ in range(10):
        code = call(update_command, shell=True)
        if code == 0:
            break
        else:
            code = call(create_command, shell=True)
            if code == 0:
                break
        sleep(1)
