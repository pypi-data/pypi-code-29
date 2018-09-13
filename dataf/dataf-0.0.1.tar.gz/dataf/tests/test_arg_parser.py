#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Test arg parser
---------------

Test suite for arg_parser.

"""

import io
import argparse
import inspect
from unittest import TestCase, mock
from contextlib import redirect_stdout

from dataf import ArgParser


class CommandTest:
    def run(self):
        """
        Test command.
        """
        raise NotImplementedError


class CustomSubParser:
    def run(self, param):
        """
        Test command.
        """
        raise NotImplementedError

    @staticmethod
    def setup_sub_parser(sub_pars, signature, docstring):
        sub_pars.add_argument(
            'param', metavar='custom_sub_parser',
            help='Custom sub parser.'
        )


def command_without_param(): pass


def command_with_param(self, param): pass


def command_with_opt_param(param=None): pass


def command_with_annotation(param: ['a', 'b']): pass


class TestArgParserFunc(TestCase):
    """
    Test for ArgParser class with a function as command.
    """
    @classmethod
    def setUpClass(cls):
        cls.arg_parser = cls._create_arg_parser()

    @staticmethod
    def _test_command():
        """
        Test command.
        """
        raise NotImplementedError

    @classmethod
    def _create_arg_parser(cls, opt=None, commands=None):
        """
        Create an ArgParser.

        :param dict opt: options for ArgParser.
        :param dict commands: commands for ArgParser.
        """
        opt = opt or {'description': 'Test'}
        commands = commands or {'test': cls._test_command}
        arg_parser = ArgParser(opt, commands)
        return arg_parser

    def test_init_set_commands(self):
        """
        Test __init__ method set commands.
        """
        test_cmd = next(filter(
            lambda x: getattr(x, '_name_parser_map', None) is not None,
            self.arg_parser.parser._actions
        ))
        self.assertIn('test', test_cmd.choices.keys())

    def test_init_command_helper(self):
        """
        Test __init__ method set commands help.
        """
        test_cmd = next(filter(
            lambda x: getattr(x, '_name_parser_map', None) is not None,
            self.arg_parser.parser._actions
        ))
        self.assertEqual('Test command.', test_cmd._choices_actions[0].help)

    def test_parse(self):
        """
        Test parse function.
        """
        with mock.patch('sys.argv', ['test', 'test']):
            with self.assertRaises(NotImplementedError):
                self.arg_parser.parse()

    def test_parse_without_command(self):
        """
        Test parse function without command.
        """
        f = io.StringIO()
        with mock.patch('sys.argv', ['test']):
            with redirect_stdout(f):
                self.arg_parser.parse()
        parse = f.getvalue()
        self.assertEqual(parse, self.arg_parser.parser.format_help())


class TestArgParserClass(TestArgParserFunc):
    """
    Test for ArgParser class with a class as command.
    """
    @classmethod
    def setUpClass(cls):
        cls.arg_parser = cls._create_arg_parser(commands={'test': CommandTest})

    def test_init_create_arg_parser(self):
        """
        Test __init__ method create and ArgParser instance.
        """
        self.assertIsInstance(self.arg_parser, ArgParser)

    def test_init_create_argument_parser(self):
        """
        Test __init__ method create and ArgumentParser instance.
        """
        self.assertIsInstance(self.arg_parser.parser, argparse.ArgumentParser)

    def test_init_set_description(self):
        """
        Test __init__ method set parser description.
        """
        self.assertEqual(self.arg_parser.parser.description, 'Test')

    def test_init_with_custom_set_sub_parser(self):
        """
        Test __init__ method with a class containing a custom set_sub_parser method.
        """
        parser = self._create_arg_parser(commands={'test': CustomSubParser})
        test_cmd = next(filter(
            lambda x: getattr(x, '_name_parser_map', None) is not None,
            parser.parser._actions
        ))
        self.assertEqual(
            'custom_sub_parser',
            test_cmd.choices['test']._get_positional_actions()[0].metavar
        )

    def test_docstring_args(self):
        """
        Test _docstring_args return dict with docstring param as ReStructuredText.
        """
        args = ArgParser._docstring_args(
            """
            Test docstring.

            :param str test: test string.
            :param str test2: second test string.
            """
        )
        self.assertEqual(
            {'test': 'test string.', 'test2': 'second test string.'}, args
        )

    def test_docstring_args_with_empty_string(self):
        """
        Test _docstring_args with an empty docstring.
        """
        args = ArgParser._docstring_args("")
        self.assertEqual({}, args)

    def test_docstring_args_with_none(self):
        """
        Test _docstring_args with None (no docstring in function).
        """
        args = ArgParser._docstring_args(None)
        self.assertEqual({}, args)

    def test_docstring_desc(self):
        """
        Test _docstring_desc return first line of docstring.
        """
        description = ArgParser._docstring_desc(
            """
            Test docstring.
            Second line.

            :param str test: test string.
            :param str test2: second test string.
            """
        )
        self.assertEqual('Test docstring.', description)

    def test_docstring_desc_with_empty_string(self):
        """
        Test _docstring_desc with an empty docstring.
        """
        description = ArgParser._docstring_desc('')
        self.assertEqual('', description)

    def test_docstring_desc_with_none(self):
        """
        Test _docstring_desc with None.
        """
        description = ArgParser._docstring_desc(None)
        self.assertEqual('', description)

    @property
    def _sub_pars(self):
        """
        Create a sub_parser object.
        """
        parser = argparse.ArgumentParser()
        sub_parsers = parser.add_subparsers()
        sub_pars = sub_parsers.add_parser('test')
        return sub_pars

    def test_setup_sub_parser_without_param(self):
        """
        Test _setup_sub_parser method with a command without param.
        """
        sub_pars = self._sub_pars
        with mock.patch('dataf.arg_parser.argparse.ArgumentParser.add_argument') as m:
            signature = inspect.signature(command_without_param)
            docstring = self.arg_parser._docstring_args(
                inspect.getdoc(command_without_param)
            )
            self.arg_parser._setup_sub_parser(sub_pars, signature, docstring)
            m.assert_not_called()

    def test_setup_sub_parser_with_param(self):
        """
        Test _setup_sub_parser method with a command with param.
        """
        sub_pars = self._sub_pars
        with mock.patch('dataf.arg_parser.argparse.ArgumentParser.add_argument') as m:
            sub_pars.set_defaults(command=command_with_param)
            signature = inspect.signature(command_with_param)
            docstring = self.arg_parser._docstring_args(
                inspect.getdoc(command_with_param)
            )
            self.arg_parser._setup_sub_parser(sub_pars, signature, docstring)
            m.assert_called_with('param', help='', metavar='param')

    def test_setup_sub_parser_with_opt_param(self):
        """
        Test _setup_sub_parser method with a command with optional param.
        """
        sub_pars = self._sub_pars
        with mock.patch('dataf.arg_parser.argparse.ArgumentParser.add_argument') as m:
            signature = inspect.signature(command_with_opt_param)
            docstring = self.arg_parser._docstring_args(
                inspect.getdoc(command_with_opt_param)
            )
            self.arg_parser._setup_sub_parser(sub_pars, signature, docstring)
            m.assert_called_with(
                '--param', default=None, help='', metavar='param'
            )

    def test_setup_sub_parser_with_annotation(self):
        """
        Test _setup_sub_parser method with a command with param annotation.
        """
        sub_pars = self._sub_pars
        with mock.patch('dataf.arg_parser.argparse.ArgumentParser.add_argument') as m:
            signature = inspect.signature(command_with_annotation)
            docstring = self.arg_parser._docstring_args(
                inspect.getdoc(command_with_annotation)
            )
            self.arg_parser._setup_sub_parser(sub_pars, signature, docstring)
            m.assert_called_with(
                'param', choices=['a', 'b'],
                help=' (choices: %(choices)s)', metavar='param'
            )
