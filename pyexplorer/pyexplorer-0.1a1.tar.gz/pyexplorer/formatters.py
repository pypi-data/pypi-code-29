from __future__ import unicode_literals
from . import text
from .extract import extract_basic_information
from prompt_toolkit import print_formatted_text
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import FormattedText
from termcolor import colored
import inspect


def module_format(entity):
    style = Style.from_dict({
        "type": "#ff0066",
        "name": "#44ff44 italic",
        "docstring": "#cccccc italic"
    })

    type_name, entity_name, entity_docstring = extract_basic_information(entity)

    if entity_docstring:
        entity_docstring = inspect.cleandoc(entity_docstring)

    text_fragments = FormattedText([
        ('class:type', text(type_name)),
        ('', ' '),
        ('class:name', text(entity_name)),
        ('', '\n'),
        ('class:docstring', text(entity_docstring)),
        ('', u'\n\n')
    ])

    print_formatted_text(text_fragments, style=style)


def attribute_format(entity):
    style = Style.from_dict({
        "type": "#ff0066",
        "name": "#44ff44 italic",
        "docstring": "#cccccc italic"
    })

    type_name, entity_name, entity_docstring = extract_basic_information(entity)

    if entity_docstring:
        entity_docstring = inspect.cleandoc(entity_docstring)
    else:
        entity_docstring = "No docstring"

    text_fragments = FormattedText([
        ('class:type', text(type_name)),
        ('', ' '),
        ('class:name', text(entity_name)),
        ('', '\n'),
        ('class:docstring', text(entity_docstring)),
        ('', u'\n')
    ])

    print_formatted_text(text_fragments, style=style)