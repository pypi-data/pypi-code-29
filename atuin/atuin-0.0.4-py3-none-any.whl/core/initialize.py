from pathlib import Path
from configparser import ConfigParser
import urllib.request

from atuin.core import CORE_LOGGER as log
import atuin.defaults as default


def check_atuin_init(dir=None):
    """Check if atuin has been initialized in the current directory
        by checking if the '.atuin' file exists"""
    if dir is not None:
        return (dir / default.ATUIN_FILE).exists()

    return default.ATUIN_FILE.exists()


def init_atuin_directory(directory, config_location, force=False):
    """Initializes the directory given to contain a .atuin file
        force will refresh config and try to refresh templates"""

    if directory is None:
        directory = default.ATUIN_FILE
    else:
        directory = Path(directory) / default.ATUIN_FILE

    if '..' in directory.parts:
        # TODO: Better Error Message
        log.warning('Cannot initialize directories above the \
                current working directory: {}'.format(directory.parent))
        return False

    # try to make atuin directory
    try:
        directory.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        log.error(e)
        return False

    config = directory / default.CONFIG_FILE
    # reload config from given config or default config if non-existant or forced
    if config.exists() and not force:
        log.info('Atuin configuration already exists in {}'.format(directory))
    else:
        config_string = resolve_config(config_location)
        try:
            cf = config.open(mode='w')
            cf.write(config_string)
            cf.close()
        except Exception as e:
            log.error(e)
            return False

    # Load Config and initialize Template Values
    try:
        curr_config = ConfigParser()
        curr_config.read([default.INTERNAL_PATH / default.CONFIG_FILE, config])

        for key in curr_config['templates']:
            init_templates(key, curr_config.get('templates', key), directory, force)
    except Exception as e:
        log.error(e)
        log.warning('Unable to initialize all template values')
        return False

    return True


def resolve_config(config):
    """Returns the config for atuin directory given a default, or url"""
    if config is not None:
        log.debug('Initializing Atuin configuration from {}'.format(config))

        try:
            resp = urllib.request.urlopen(config)
            config = resp.read().decode()

            if verify_config(config):
                return config
        except Exception as e:
            log.error(e)

    log.debug('Using default atuin configuration')
    config = (default.INTERNAL_PATH / default.CONFIG_FILE).open().read()
    return config


def verify_config(config_string):
    """Verify the config has at least the minimum required value:
            config['templates']['default']"""
    try:
        test = ConfigParser()
        test.read_string(config_string)
        if 'templates' in test.sections() and test.has_option('templates', 'default'):
            log.debug(test.get('templates', 'default'))
            return True
    except Exception as e:
        log.warning(e)
    return False


def init_templates(key, template, dir=default.ATUIN_FILE, force=False):
    """Load templates, looking checking existence and trying to resolve
        non-existing templates"""

    template_dir = dir / default.TEMPLATE_PATH

    if not template_dir.exists():
        try:
            template_dir.mkdir()
        except Exception as e:
            log.warning(e)

    template_file = template_dir / template

    if not template_file.exists() or force:
        log.debug('Initializing template <{}> from {}'.format(key, template))
        template_string = resolve_template(template)
        try:
            template_file.open(mode='w').write(template_string)
        except (Exception):
            pass


def resolve_template(template_name, dir=default.INTERNAL_PATH / default.TEMPLATE_PATH, uri=None):
    """Produce a string given a template name"""
    template = dir / template_name

    if not template.is_file():
        log.warning('Unable to find {} at {}'.format(template_name, template))
        return resolve_template('default.template')
    else:
        return template.open().read()
