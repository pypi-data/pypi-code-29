import logging
import os
import re
import sys
import inspect
from io import StringIO
from pathlib import Path
from zensols.pybuild import TagUtil
import setuptools

logger = logging.getLogger('zensols.pybuild.su')


class SetupUtilCli(object):
    def __init__(self, **kwargs):
        self.util = SetupUtil(**kwargs)

    def write(self):
        self.util.write()


class SetupUtil(object):
    """Utilities for creating python distributed builds (wheels etc)."""

    FIELDS = """
name packages package_data version description author author_email url
download_url long_description long_description_content_type install_requires
keywords classifiers
"""

    def __init__(self, name, user, project, setup_path=None,
                 package_names=None, readme_file='README.md',
                 req_file='requirements.txt', has_entry_points=True,
                 **kwargs):
        self.name = name
        self.user = user
        self.project = project
        if setup_path is None:
            setup_path = Path(__file__).parent.absolute()
        else:
            setup_path = Path(setup_path)
        self.setup_path = setup_path
        if package_names is None:
            m = re.match(r'^(.+)\..*', name)
            if m:
                package_names = [m.group(1)]
            else:
                package_names = [name]
        self.package_names = package_names
        self.readme_file = readme_file
        self.req_file = req_file
        self.has_entry_points = has_entry_points
        self.__dict__.update(**kwargs)

    @property
    def root_path(self):
        nname, dname = None, self.setup_path
        while nname != dname:
            logger.debug('nname={}, dname={}'.format(nname, dname))
            nname, dname = dname, dname.parent
            rm_file = dname.joinpath(self.readme_file)
            logging.debug('rm file: {}'.format(rm_file))
            if rm_file.is_file():
                break
        logging.debug('found root dir: {}'.format(dname))
        return dname

    @property
    def packages(self):
        dirs = []
        logger.debug('walking on {}'.format(self.package_names))
        for dname in self.package_names:
            for root, subdirs, files in os.walk(dname):
                logger.debug('root: {}'.format(root))
                root = os.path.relpath(root, dname)
                if root != '.':
                    dirs.append(os.path.join(dname, root.replace(os.sep, '.')))
        return dirs

    @property
    def long_description(self):
        path = Path(self.root_path, self.readme_file)
        logger.debug('reading long desc from {}'.format(path))
        with open(path, encoding='utf-8') as f:
            return f.read()

    @property
    def install_requires(self):
        path = Path(self.setup_path, self.req_file)
        with open(path, encoding='utf-8') as f:
            return [x.strip() for x in f.readlines()]

    @property
    def url(self):
        return 'https://github.com/{}/{}'.format(self.user, self.project)

    @property
    def download_url(self):
        params = {'url': self.url,
                  'name': self.name,
                  'version': self.version,
                  'path': 'releases/download',
                  'wheel': 'py3-none-any.whl'}
        return '{url}/{path}/v{version}/{name}-{version}-{wheel}'.\
            format(**params)

    @property
    def tag_util(self):
        tu = TagUtil(self.root_path)
        return tu

    @property
    def author(self):
        commit = self.tag_util.get_last_commit()
        if commit:
            return commit.author.name

    @property
    def author_email(self):
        commit = self.tag_util.get_last_commit()
        if commit:
            return commit.author.email

    @property
    def version(self):
        return self.tag_util.get_last_tag()

    @property
    def entry_points(self):
        if hasattr(self, 'console_script'):
            script = self.console_script
        else:
            m = re.match(r'.*\.(.+?)$', self.name)
            if m:
                script = m.group(1)
            else:
                script = self.name
        return {'console_scripts': ['{}={}:main'.format(script, self.name)]}

    def get_properties(self, paths=False):
        fields = self.FIELDS.split()
        if paths:
            fields.extend('setup_path root_path'.split())
        if self.has_entry_points:
            fields.append('entry_points')
        fset = set(fields)
        props = {'long_description_content_type': 'text/markdown'}
        for mem in filter(lambda x: x[0] in fset, inspect.getmembers(self)):
            logger.debug('member: {}'.format(mem))
            val = mem[1]
            if val is not None:
                props[mem[0]] = mem[1]
        return fields, props

    def write(self, writer=sys.stdout, paths=False):
        fields, props = self.get_properties(paths)
        props['long_description'] = props['long_description'][0:20] + '...'
        for field in fields:
            if field in props:
                writer.write('{}={}\n'.format(field, props[field]))

    def setup(self):
        _, props = self.get_properties()
        sio = StringIO()
        self.write(sio)
        logger.info('setting up with {}'.format(sio.getvalue()))
        setuptools.setup(**props)
