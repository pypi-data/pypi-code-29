#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Test yaml parser
----------------

Test suite for yaml_parser.

"""

from os.path import join
from unittest import TestCase, mock

import yaml

from dataf import YamlParser
from dataf.yaml_parser import YamlConstructor


class TestYamlConstructor(TestCase):
    """
    Test for YamlConstructor classe.
    """
    @property
    def _node(self):
        """
        Create a yaml node object.
        """
        node = yaml.SequenceNode(
            tag='tag:yaml.org,2002:seq',
            value=[
                yaml.ScalarNode(tag='tag:yaml.org,2002:str', value='a'),
                yaml.ScalarNode(tag='tag:yaml.org,2002:str', value='b'),
                yaml.ScalarNode(tag='tag:yaml.org,2002:str', value='c'),
            ]
        )
        return node

    @property
    def _loader(self):
        """
        Create a yaml loader object.
        """
        return yaml.Loader('test')

    def test_simple_join(self):
        """
        Test simple_join method.
        """
        result = YamlConstructor.simple_join(self._loader, self._node)
        self.assertEqual(result, 'abc')

    def test_string_join(self):
        """
        Test string_join method.
        """
        result = YamlConstructor.string_join(self._loader, self._node)
        self.assertEqual(result, 'bac')

    def test_yaml_getter(self):
        """
        Test yaml_getter method.
        """
        data = {'a': 'OK', 'b': 'KO'}
        result = YamlConstructor.yaml_getter(self._loader, self._node, data=data)
        self.assertEqual(result, 'OK')


class TestYamlParser(TestCase):
    """
    Test for YamlParser classe.
    """
    @classmethod
    def setUpClass(cls):
        cls.yaml_parser = YamlParser(True)

    def test_init_attr_default(self):
        """
        Test __init__ method with default arguments.
        """
        self.assertEqual('prod', self.yaml_parser.prod_block)
        self.assertEqual('dev', self.yaml_parser.dev_block)
        self.assertEqual(True, self.yaml_parser.debug)
        self.assertEqual(
            YamlParser.custom_constructors, self.yaml_parser.custom_constructors
        )

    def test_init_attr_custom(self):
        """
        Test __init__ method with custom arguments.
        """
        custom_constructors = {'!test': YamlConstructor.simple_join}
        yaml_parser = YamlParser(
            True, prod_block='test_prod', dev_block='test_dev',
            custom_constructors=custom_constructors
        )
        self.assertEqual('test_prod', yaml_parser.prod_block)
        self.assertEqual('test_dev', yaml_parser.dev_block)
        self.assertEqual(True, yaml_parser.debug)
        custom_constructors.update(YamlParser.custom_constructors)
        self.assertEqual(
            custom_constructors,
            yaml_parser.custom_constructors
        )

    @mock.patch('dataf.YamlParser.add_custom_constructors')
    def test_init_add_custom_constructors(self, mock):
        """
        Test __init__ method call YamlParser.add_custom_constructors.
        """
        yaml_parser = YamlParser(True)
        mock.assert_called_with(yaml_parser.custom_constructors)

    @mock.patch('dataf.yaml_parser.yaml.add_constructor')
    def test_add_custom_constructors(self, mock):
        """
        Test add_custom_constructors method return value and call yaml.add_constructor.
        """
        custom_constructors = {'!test': YamlConstructor.simple_join}
        ret = self.yaml_parser.add_custom_constructors(custom_constructors)
        mock.assert_called_with('!test', custom_constructors['!test'])
        self.assertEqual(self.yaml_parser, ret)

    @mock.patch('dataf.yaml_parser.partial')
    @mock.patch('dataf.yaml_parser.yaml.add_constructor')
    def test_add_getter_constructor(self, mock, mock_partial):
        """
        Test add_getter_constructor method.
        """
        name = '!test'
        data = {}
        ret = self.yaml_parser.add_getter_constructor(name, data)
        mock.assert_called_with(name, mock_partial())
        self.assertEqual(self.yaml_parser, ret)

    def test_update_with_dict(self):
        """
        Test _update method with a dict.
        """
        source = {
            'test': 'KO',
            'test2': {'nested': 'KO'},
            'test3': {'nested1': {'nested2': 'KO'}},
            'test4': {'nested1': {'nested2': 'KO'}}
        }
        update_dict = {
            'test': 'OK',
            'test2': {'nested': 'OK'},
            'test3': {'nested1': {'nested2': 'OK'}}
        }
        expected = {
            'test': 'OK',
            'test2': {'nested': 'OK'},
            'test3': {'nested1': {'nested2': 'OK'}},
            'test4': {'nested1': {'nested2': 'KO'}}
        }
        ret = self.yaml_parser._update(source, update_dict)
        self.assertEqual(ret, expected)

    def test_update_without_dict(self):
        """
        Test _update method without dict.
        """
        source = {'test': 'test'}
        update_dict = ['test']
        ret = self.yaml_parser._update(source, update_dict)
        self.assertEqual(ret, update_dict)

    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data="{'prod': {'data': 'OK'}}")
    def test_parse_without_dev_section(self, mock_open):
        """
        Test parse method without dev section in yaml loaded.
        """
        yaml_var = {}
        yaml_to_dict = {'config.yml': yaml_var}
        yaml_dir_path = '/path/to/yaml'
        ret = self.yaml_parser.parse(yaml_to_dict, yaml_dir_path)
        mock_open.assert_called_with(join(yaml_dir_path, 'config.yml'), 'r')
        self.assertEqual(yaml_var, {'data': 'OK'})
        self.assertEqual(ret, self.yaml_parser)

    @mock.patch(
        'builtins.open', new_callable=mock.mock_open,
        read_data="{'prod': {'data': 'KO'}, 'dev': {'data': 'OK'}}"
    )
    def test_parse_with_dev_section(self, mock_open):
        """
        Test parse method with dev section in yaml loaded.
        """
        yaml_var = {}
        yaml_to_dict = {'config.yml': yaml_var}
        yaml_dir_path = '/path/to/yaml'
        ret = self.yaml_parser.parse(yaml_to_dict, yaml_dir_path)
        mock_open.assert_called_with(join(yaml_dir_path, 'config.yml'), 'r')
        self.assertEqual(yaml_var, {'data': 'OK'})
        self.assertEqual(ret, self.yaml_parser)
