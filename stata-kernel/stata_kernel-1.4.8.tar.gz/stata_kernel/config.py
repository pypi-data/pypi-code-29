import re
import platform

from pathlib import Path
from textwrap import dedent
from configparser import ConfigParser


class Config(object):
    def __init__(self):
        self.config_path = Path('~/.stata_kernel.conf').expanduser()
        self.config = ConfigParser()
        self.config.read(self.config_path)

        self.env = dict(self.config.items('stata_kernel'))
        self.env['cache_dir'] = Path(
            self.env.get('cache_directory',
                         '~/.stata_kernel_cache')).expanduser()
        self.env['cache_dir'].mkdir(parents=True, exist_ok=True)

        if platform.system() == 'Darwin':
            self.set('stata_path', self.get_mac_stata_path_variant())
            if not self.get('execution_mode') in ['console', 'automation']:
                self.raise_config_error('execution_mode')
        elif platform.system() == 'Linux':
            self.set('stata_path', self.get_linux_stata_path_variant(), permanent=True)

        if not self.get('stata_path'):
            self.raise_config_error('stata_path')

    def get(self, key, backup=None):
        return self.env.get(key, backup)

    def set(self, key, val, permanent=False):
        if key.startswith('cache_dir'):
            val = Path(val).expanduser()
            val.mkdir(parents=True, exist_ok=True)

        self.env[key] = val

        if permanent:
            if key.startswith('cache_dir'):
                key = 'cache_directory'
                val = str(val)

            if key.startswith('graph_'):
                val = str(val)

            self.config.set('stata_kernel', key, val)
            with self.config_path.open('w') as f:
                self.config.write(f)

    def get_mac_stata_path_variant(self):
        stata_path = self.get('stata_path')
        if stata_path == '':
            return ''

        path = Path(stata_path)
        if self.get('execution_mode') == 'automation':
            d = {'stata': 'Stata', 'stata-se': 'StataSE', 'stata-mp': 'StataMP'}
        else:
            d = {'Stata': 'stata', 'StataSE': 'stata-se', 'StataMP': 'stata-mp'}

        bin_name = d.get(path.name, path.name)
        return str(path.parent / bin_name)

    def get_linux_stata_path_variant(self):
        stata_path = self.get('stata_path')

        d = {
            'xstata': 'stata',
            'xstata-se': 'stata-se',
            'xstata-mp': 'stata-mp'}
        for xname, name in d.items():
            if stata_path.endswith(xname):
                stata_path = re.sub(r'{}$'.format(xname), name, stata_path)
                break

        return stata_path

    def raise_config_error(self, option):
        msg = """\
        {} option in configuration file is missing or invalid
        Refer to the documentation to see how to set it manually:

        https://kylebarron.github.io/stata_kernel/user_guide/configuration/
        """.format(option)
        raise ValueError(dedent(msg))

    def _remove_unsafe(self, key, permanent=False):
        self.env.pop(key, None)
        if permanent:
            self.config.remove_option(option=key, section='stata_kernel')
            with self.config_path.open('w') as f:
                self.config.write(f)
