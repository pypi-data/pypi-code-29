from __future__ import unicode_literals


def extract_basic_information(entity):
    if hasattr(entity, "__name__"):
        entity_name = entity.__name__
    else:
        entity_name = "No name"

    type_name = type(entity).__name__

    if hasattr(entity, "__doc__"):
        entity_docstring = entity.__doc__
    else:
        entity_docstring = "No docstring"

    return type_name, entity_name, entity_docstring
