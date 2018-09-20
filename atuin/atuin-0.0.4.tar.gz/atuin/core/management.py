from configparser import ConfigParser
from collections import defaultdict
from pathlib import Path
import string
import atuin.defaults as default
from atuin.core import CORE_LOGGER as log


def get_template(template_name):
    """Gets a template based off name or returns default.template if not found"""
    config = ConfigParser()
    config.read(default.ATUIN_FILE / default.CONFIG_FILE)
    template_name = config.get('templates', template_name, fallback=template_name)
    log.debug('Trying getting template {}'.format(template_name))

    template = default.ATUIN_FILE / default.TEMPLATE_PATH / template_name
    log.debug(template)

    # TODO:make this search more robust and potentially return something else
    if template.is_file():
        return template
    else:
        return default.INTERNAL_PATH / 'default.template'


def sanitize_challenge_name(challenge_name):
    """Produces a set filename for any challenge name by removing 'invalid'
        characters, eliminating spaces, and making it lowercase"""
    valid_chars = '-_. {}{}'.format(string.ascii_letters, string.digits)
    filename = ''.join(c for c in challenge_name if c in valid_chars)
    if ' ' in filename:
        filename = filename.title()
        filename = filename.replace(' ', '')
    return filename


def get_challenge(challenge_name):
    '''Get the main (markdown) file for a given challenge'''
    path = Path(challenge_name) / '{}.md'.format(challenge_name)

    if path.exists():
        return path
    else:
        return None


def create_challenge_tree(challenge_name):
    """Creates folder for templates if they don't already exist
        Returns the given path,"""

    path = Path(challenge_name)

    if path.is_dir():
        return path
    else:
        try:
            path.mkdir(parents=True, exist_ok=True)
            return path
        except Exception as e:
            log.error('Failed to create challenge directory')
            log.debug(e)
        # TODO: Make this more robust
    return None


def challenge_add_template(name, filename, path, template, points):
    """Adds a given template to a challenge"""
    log.info('Creating {} in {} with from {}'.format(filename, path, template))

    template_string = template.open().read()
    template_string = template_string.format_map(defaultdict(str, title=name, points=points))
    suffix = Path(template.stem).suffix
    stem = '{}{}'.format(filename, suffix)
    log.debug("{} - {}".format(path, stem))
    file = path / stem

    if file.exists():
        log.warning('Challenge Already Exists')
        return

    file.write_text(template_string)
