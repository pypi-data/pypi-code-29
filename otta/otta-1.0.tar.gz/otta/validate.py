from jsonschema import (
    validate,
    ValidationError
)

from .utils import parse_recipe
from .fail import fail, gr, rd, yl

files_schema = {
    'type': 'array',
    'items': {
        'type': 'string'
    }
}


schema = {
    'type': 'object',
    'additionalProperties': False,
    'required': ['files', 'default_recipe', 'recipes'],
    'properties': {
        'files': files_schema,
        'default_recipe': {
            'type': 'string'
        },
        'recipes': {
            'type': 'object',
            'additionalProperties': False,
            'patternProperties': {
                '^[a-z0-9_]{1,40}$': {
                    'type': 'object',
                    'required': ['files'],
                    'additionalProperties': False,
                    'properties': {
                        'files': files_schema,
                        'project_name': {
                            'type': 'string',
                            'pattern': '^[a-z0-9_]{1,40}$'
                        },
                        'options': {
                            'type': 'object',
                            'additionalProperties': False,
                            'patternProperties': {
                                '^[a-zA-Z0-9_]{1,20}$': {
                                    'type': 'object',
                                    'additionalProperties': False,
                                    'properties': {
                                        'files': files_schema
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

def o_schema_validate(value):
    validate(value, schema)

def check_consistency(data, files):
    our_files = set(data['files'])
    missing_files = our_files - set(files)

    if missing_files:
        fail(
            'The folowing files are missing: ' +
            yl(' '.join(missing_files))
        )

    recipes = data['recipes']

    for recipe in recipes.values():
        missing_files |= set(recipe['files']) - our_files

        if 'options' in recipe:
            for option in recipe['options'].values():
                missing_files |= set(option['files']) - our_files

    if missing_files:
        fail(
            'The following files not specifed in root `files` are used: ' +
            yl(' '.join(missing_files))
        )

    try:
        d_recipe, d_options = parse_recipe(data['default_recipe'])
    except ValueError:
        fail(
            'Wrong default recipe format'
        )

    if d_recipe not in recipes:
        fail(
            'Unknown default recipe `{}`'.format(data['default_recipe'])
        )

    d_recipe_dict = recipes[d_recipe]
    try:
        defined_options = set(d_recipe_dict['options'].keys())
    except KeyError:
        defined_options = set()

    missing_options = set(d_options) - defined_options
    if missing_options:
        fail(
            'Unknown default options: {}'.format(missing_options)
        )
