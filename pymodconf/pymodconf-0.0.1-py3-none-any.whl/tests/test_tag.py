# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2018 by Lars Klitzke, Lars.Klitzke@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os
import unittest

from pymodconf import tag
from pymodconf.io import read
from pymodconf.parser import parse
from pymodconf.tag import Tag, register


class TestTagCreation(unittest.TestCase):

    def test_create_tag(self):
        test_tag = Tag('TestTag: ')

        self.assertTrue('testtag' == str(test_tag))

    def test_register_tag(self):
        test_tag = Tag('TestTag: ')

        register(test_tag)

        from pymodconf.tag import _TAGS
        self.assertTrue(test_tag in _TAGS)

    def test_tag_available(self):
        test_tag = Tag('TestTag: ')

        register(test_tag)

        self.assertTrue(tag.available(test_tag))

    def test_tag_as_str_available(self):

        test_tag = Tag('TestTag: ')

        register(test_tag)

        self.assertTrue(tag.available('TestTag:'))


class TestTagInConfig(unittest.TestCase):

    def setUp(self):
        self.testtag = Tag('TestTag:')

    def test_load_config(self):

        parser = read(os.path.join(os.path.dirname(__file__), 'module_test_config.cfg'))

        config = parse(parser)

        self.assertTrue(str(self.testtag) in config)
        self.assertTrue(len(config[str(self.testtag)]) == 2)
        self.assertTrue(len(list(config.keys())), 1)

        # check if all names are present
        names = [e['name'] for e in config[str(self.testtag)]]

        for name in names:
            self.assertIn(name, ['Test1', 'Test2'])

        # check if the options are available, too.
        options = [e['opt'] for e in config[str(self.testtag)]]

        for o in options:
            self.assertIn(o, ['HalloTest1', 'HalloTest2'])
