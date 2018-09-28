#!/usr/bin/env python3

import os
import sys
from os.path import expanduser
from yaml import (
    safe_load as load,
    YAMLError
)

from .fail import (
    update_details,
    report_details,
    fail,
    gr, rd, yl,
)

from .utils import (
    parse_recipe,
    check_for_compose,
    check_for_kompose,
    check_for_docker,
    dir_parents,
    is_debug
)

from .validate import (
    o_schema_validate,
    ValidationError,
    check_consistency
)


OTTA_FILE_DEFAULT = 'otta/otta.yml'
OTTA_FILE_VAR = 'OTTA_FILE'
OTTA_RECIPE_VAR = 'OTTA_REC'


def get_orchestration_definition():
    try:
        raw_otfp = os.environ[OTTA_FILE_VAR]
        default_otfp = False
    except KeyError:
        raw_otfp = OTTA_FILE_DEFAULT
        default_otfp = True

    otf_source = 'default' if default_otfp else 'taken from ' + yl(OTTA_FILE_VAR) + ' env'
    otf_detail = 'Otta file: {} ({})\n'.format(gr(raw_otfp), otf_source)
    update_details(
        lambda a: a + otf_detail
    )

    if os.path.isabs(raw_otfp):
        otfp = raw_otfp

        if not os.path.isfile(otfp):
            fail('Otta file does not exist')
    else:
        base_path = os.getcwd()

        for x in dir_parents(base_path):
            otfp = os.path.join(x, raw_otfp)

            try:
                with open(otfp, 'r') as f:
                    data = load(f)
            except (FileNotFoundError, IsADirectoryError):
                continue
            except YAMLError as e:
                update_details(
                    lambda a: a + 'Otta file absolute path: {}\n'.format(gr(otfp))
                )
                fail('Otta file YAML parse error: {}'.format(str(e)))
            else:
                break
        else:
            fail('Otta file is not found in CWD or any of it\'s parents')

    try:
        o_schema_validate(data)
    except ValidationError as e:
        msg = e.message
        fail(
            'Otta file is not structurally valid: ' + yl(msg)
        )

    data_dir = os.path.dirname(otfp)

    dir_details = 'Data directory: {}\n'.format(gr(data_dir))
    update_details(
        lambda a: a + dir_details
    )

    return data_dir, data


def process_environment():
    o_dir, o_data = get_orchestration_definition()
    o_files = set([
        f for f in os.listdir(o_dir)
        if os.path.isfile(
            os.path.join(o_dir, f)
        )
    ])

    check_consistency(o_data, o_files)

    try:
        f_recipe = os.environ[OTTA_RECIPE_VAR]
        recipe_details = (
            'Recipe: {} (taken from {} variable)\n'
            .format(gr(f_recipe), yl(OTTA_RECIPE_VAR))
        )
        update_details(
            lambda a: a + recipe_details
        )
        u_recipe, u_options = parse_recipe(f_recipe)
    except KeyError:
        # will never fail
        f_recipe = o_data['default_recipe']
        u_recipe, u_options = parse_recipe(f_recipe)
        recipe_details = 'Recipe: {} (default)\n'.format(gr(f_recipe))
        update_details(
            lambda a: a + recipe_details
        )
    except ValueError:
        fail(
            'Wrong recipe format'
        )

    try:
        recipe_dict = o_data['recipes'][u_recipe]
    except KeyError:
        fail(
            'Recipe not found'
        )

    try:
        spec_options = set(recipe_dict['options'].keys())
    except KeyError:
        spec_options = set()

    missing_options = set(u_options) - spec_options
    if missing_options:
        fail(
            'Unknown options: {}'.format(missing_options)
        )

    files = list(recipe_dict['files'])
    for option in u_options:
        option_files = recipe_dict['options'][option]['files']
        files += option_files

    files = list([os.path.join(o_dir, f) for f in files])
    project_name = recipe_dict.get('project_name', None)

    return project_name, files


def otta():
    check_for_compose()
    in_arguments = sys.argv[1:]
    project_name, files = process_environment()

    dcp_options = []
    for file in files:
        dcp_options.append('-f')
        dcp_options.append(file)

    if project_name is not None:
        dcp_options.append('-p')
        dcp_options.append(project_name)

    dcp_command_array = ['docker-compose'] + dcp_options + in_arguments

    if is_debug():
        command_string = ' '.join(dcp_command_array)
        update_details(
            lambda a: a + 'execvp() command: {}\n\n'.format(gr(command_string))
        )
        report_details()

    os.execvp('docker-compose', dcp_command_array)


def skara():
    check_for_docker()
    in_arguments = sys.argv[1:]

    project_name, files = process_environment()

    docker_options = ['stack', 'deploy']
    for file in files:
        docker_options.append('-c')
        docker_options.append(file)

    docker_command_array = ['docker'] + docker_options + in_arguments

    if is_debug():
        command_string = ' '.join(docker_command_array)
        update_details(
            lambda a: a + 'execvp() command: {}\n\n'.format(gr(command_string))
        )
        report_details()

    os.execvp('docker', docker_command_array)


def kumla():
    check_for_kompose()
    in_arguments = sys.argv[1:]

    project_name, files = process_environment()

    kompose_options = []
    for file in files:
        kompose_options.append('-f')
        kompose_options.append(file)

    kompose_command_array = ['kompose'] + kompose_options + in_arguments

    if is_debug():
        command_string = ' '.join(kompose_command_array)
        update_details(
            lambda a: a + 'execvp() command: {}\n\n'.format(gr(command_string))
        )
        report_details()

    os.execvp('kompose', kompose_command_array)
