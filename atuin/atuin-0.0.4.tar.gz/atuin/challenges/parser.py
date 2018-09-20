import re
from collections import defaultdict

import mistletoe

# from atuin.challenges import Challenge
from atuin.core.management import get_template

from atuin.core.colorlogging import getColorLogger, LOG_FORMAT_LEVEL
PARSING_LOGGER = getColorLogger(__name__, LOG_FORMAT_LEVEL)


blocks = re.compile(r'##\s*([\w ]+)\s+?((?:(?!##).*?\n)+)')
title = re.compile(r'^\s*?#\s*([\w ]+)')
points = re.compile(r'^.*\n\s*?(.+)')


def expand_division_definitions(definition: str):
    spit_defs = definition.split(':')
    for i in range(len(spit_defs) - 1):
        # spit_defs[i] = spit_defs[i].replace("&&", ":" + spit_defs[i + 1][:spit_defs[i + 1].find(",") + 1])
        spit_defs[i] = spit_defs[i].replace("&&", ":" + spit_defs[i + 1][:spit_defs[i + 1].find(",")] + ',\n')

    newStr = spit_defs[0]
    for i in range(1, len(spit_defs)):
        newStr += ":" + spit_defs[i]
    return newStr


expand_defs_test = """bots1 = {
  "DivA" : "Each Bot in either order must begin",
  "DivB" && "DivC" && "DivD" : "Bot must begin",
}"""


def localize_division_definitions(definitions: str):
    built_string = ''
    for line in definitions.splitlines():
        if '@' in line:
            tokens = line.split(':')
            line = line.replace('@', '[{}]'.format(tokens[0].strip()))

        built_string += line + '\n'

    return built_string


def parse_challenge(challenge_text: str):
    '''Returns a dictionary comprised of the sections of challenges.
        Does not resolve definitions or create a challenge object'''
    challenge_title = re.findall(title, challenge_text)
    challenge_points = re.findall(points, challenge_text)
    challenge_sections = re.findall(blocks, challenge_text)

    challenge_dict = {}

    if len(challenge_title) == 0:
        PARSING_LOGGER.warn('no title detected')
    else:
        challenge_dict['title'] = challenge_title[0]

    if len(challenge_points) == 0:
        PARSING_LOGGER.warn('no point value detected')
    else:
        challenge_dict['points'] = challenge_points[0]

    for section in challenge_sections:
        section_name = section[0].strip().lower()
        section_contents = section[1]
        challenge_dict[section_name] = section_contents

    return challenge_dict


def process_dictionary(challenge_dict: dict, division: str='DivA'):
    raw_defs = challenge_dict.pop('definitions', '')

    '''
    Apply transformations for && syntax and @ for referencing
    '''
    expanded = expand_division_definitions(raw_defs)
    finalized = localize_division_definitions(expanded)

    '''evaluate code to get dictionary of definitions'''
    var_locals = {}
    exec(finalized, None, var_locals)

    # NOTE: Transforms the dictionaries to the specific division provided
    substitution_dict = {'__DIVISION_KEY': division}
    for k, v in var_locals.items():
        if type(v) is dict:
            v = v.get(division, '')
        substitution_dict[k] = v

    # Handle substitutions within the definitions
    for k, v in substitution_dict.items():
        if type(v) is str:
            substitution_dict[k] = v.format_map(substitution_dict)

    processed_dictionary = {}

    for k, v in challenge_dict.items():
        # solves the issue of not breaking at line endings
        if k != 'scoring':
            v = v.replace('\n', r'<br>')

        processed_dictionary[k] = mistletoe.markdown(v.format_map(substitution_dict))

    return processed_dictionary


simple_styling = """<style>
        * {
          font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
          }
        table {
          border-collapse: collapse;
          width: 100%;
        }

        td, th {
            border: 1px solid #ddd;
            padding: 8px;
        }

        th {
          padding-top: 12px;
          padding-bottom: 12px;
          text-align: left;
        }

        .score {
            float: right;
            font-weight: 700;
            font-size: 20;

        }

        .notes {
          display: none
        }
    </style>"""

debug_styling = """<style>
        .title {
            background-color: orange;
        }

        .score {
            float: right;
            background-color: hotpink;
            margin-top: 5;
            font-weight: 700;
            font-size: 25;
        }

        .background {
            background-color: lightgreen
        }

        .setup {
            background-color: lightblue;
        }

        .objective {
            background-color: wheat;
        }

        .scoring {
            background-color: lightyellow;
        }

        .diagrams {
            background-color: pink;
        }

        .notes {
            background-color: red;
        }
    </style>"""


def challenge_to_html(challenge_dict: dict, division: str, styling: str=simple_styling):


    html = get_template('html').open(mode='r').read()
    dictionary = defaultdict(str, styling=styling, **process_dictionary(challenge_dict, division))
    return html.format_map(dictionary)
