#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Command line
------------

Package CLI.

"""

import os
import sys

from mako.template import Template

from dataf import ArgParser


class CommandLine:
    """
    Dataf CLI.
    """
    templates_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'templates'
    )

    def parse(self):
        """
        Parse command argument.
        """
        commands = {
            'create_project': self.create_project
        }
        ArgParser({'description': 'DataF CLI.'}, commands).parse()

    def _create_main_dir(self, name, dir_path):
        """
        Create main project directory and files.

        :param str name: name of project.
        :param str dir_path: path of directory.
        """
        entry_points = {
            'project_name': name
        }

        os.makedirs(dir_path)
        template = Template(
            filename=os.path.join(self.templates_dir, 'entry_points.py.mako')
        )
        with open(os.path.join(dir_path, '{}.py'.format(name)), 'w') as f:
            f.write(template.render(**entry_points))

    def _create_settings_dir(self, name, dir_path):
        """
        Create settings directory and files.

        :param str name: name of project.
        :param str dir_path: path of directory.
        """
        settings_templates = {
            'directory.yml': {'project_name': name},
            'database.yml': {},
            'logging.yml': {},
            'settings.py': {},
            'swagger.yml': {'project_name': name},
            'views.yml': {},
            '__init__.py': {},
        }

        os.makedirs(os.path.join(dir_path, 'settings'))
        for file, kwargs in settings_templates.items():
            template = Template(
                filename=os.path.join(
                    self.templates_dir,
                    'settings_templates',
                    '{}.mako'.format(file)
                )
            )
            with open(os.path.join(dir_path, 'settings', file), 'w') as f:
                f.write(template.render(**kwargs))

    def create_project(self, name):
        """
        Create directories and files for new project.

        :param str name: name of project.
        """
        dir_path = os.path.join(os.getcwd(), name)
        if not os.path.isdir(dir_path):
            self._create_main_dir(name, dir_path)
            self._create_settings_dir(name, dir_path)
        else:
            print(
                'Error: Directory {} already exists.'.format(name),
                file=sys.stderr
            )


def main():
    CommandLine().parse()
