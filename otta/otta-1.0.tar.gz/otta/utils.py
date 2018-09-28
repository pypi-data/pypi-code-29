import re
import os
from subprocess import call

from .fail import fail


recipe_regex = re.compile(r'^[a-zA-Z0-9_\-]{1,40}(\+[a-zA-Z0-9_\-]{1,20})*$')


def parse_recipe(r_str):
    if not recipe_regex.match(r_str):
        raise ValueError()

    things = r_str.split('+')

    recipe = things[0]
    options = things[1:]

    return recipe, options


def check_for_compose():
    arguments = [
        'docker-compose',
        '--version'
    ]
    DEVNULL = open(os.devnull, 'w')
    try:
        call(arguments, stdout=DEVNULL)
    except:
        fail('docker-compose is not found on your $PATH')


def check_for_docker():
    arguments = [
        'docker',
        '--version'
    ]
    DEVNULL = open(os.devnull, 'w')
    try:
        call(arguments, stdout=DEVNULL)
    except:
        fail('docker is not found on your $PATH')


def check_for_kompose():
    arguments = [
        'kompose',
        'version'
    ]
    DEVNULL = open(os.devnull, 'w')
    try:
        call(arguments, stdout=DEVNULL)
    except:
        fail('kompose is not found on your $PATH')


def dir_parents(directory):
    while True:
        yield directory

        parent_dir = os.path.dirname(directory)
        if parent_dir == directory:
            break
        else:
            directory = parent_dir


OTTA_DEBUG_VAR = 'OTTA_DEBUG'
def is_debug():
    try:
        return bool(os.environ[OTTA_DEBUG_VAR])
    except KeyError:
        return False
