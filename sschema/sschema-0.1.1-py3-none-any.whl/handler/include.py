'''
A resolver that searches a list of include paths for YAML files matching the
given name. The include paths must be set prior to validation.
work.
'''

import functools
import pkg_resources
import os

import yaml


HANDLER_NAME = 'include'


def _handler(include_paths, uri):
    '''Handles an URI of form include://'''
    base = 'include://'
    assert(uri.startswith(base))
    uri = uri[len(base):]

    data = None
    for path in include_paths:
        uri = os.path.join(path, uri)
        try:
            f = open(uri, 'r')
        except FileNotFoundError:
            continue
        else:
            with f:
                data = yaml.load(f)
                break
    return data


def make_handler(include_paths):
    '''Returns an include handler and name (for use with make_resolver) that
    uses the give include paths.'''
    return (functools.partial(_handler, include_paths), HANDLER_NAME)


def make_default_handler():
    '''Returns a default handler, which uses the common schemas defined in
    sschema as the include path.'''
    schema_path = pkg_resources.resource_filename('sschema', 'schema')
    return make_handler([schema_path])
