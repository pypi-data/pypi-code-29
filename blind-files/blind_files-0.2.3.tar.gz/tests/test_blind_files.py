#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `blind_files` package."""


import logging
import os
import subprocess
import sys
import tempfile
import unittest
from filecmp import cmp, cmpfiles, dircmp
from pathlib import Path
from shutil import copytree
from traceback import print_tb

from click.testing import CliRunner
from hamcrest import assert_that, empty, is_

from blind_files import cli


class TestBlind_files(unittest.TestCase):
    """Tests for `blind_files` package."""

    def test_help(self):
        """Test the CLI."""
        runner = CliRunner()
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message and exit.' in help_result.output

    def check_cli_command(self, runner, fixture_dir, args):
        logging.info(f"Running command: blind_files {' '.join(args)}")

        input_fixture = fixture_dir / 'input'
        gold_dir = fixture_dir / 'gold-output'
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir = Path(temp_dir)
            output_dir = temp_dir / 'output_dir'
            mapping_dir = temp_dir / 'mapping_dir'
            input_dir = temp_dir / 'input_dir'
            copytree(input_fixture, input_dir)

            result = runner.invoke(cli.main, args + [
                '--input-dir',
                str(input_dir),
                '--output-dir',
                str(output_dir),
                '--mapping-dir',
                str(mapping_dir),
            ])

            if result.exit_code != 0:
                sys.stdout.write(result.output)
                if result.exc_info is not None:
                    print_tb(result.exc_info[2])

            assert result.exit_code == 0

            blind_sh = mapping_dir / 'blind.sh'
            unblind_sh = mapping_dir / 'unblind.sh'

            subprocess.check_call(['bash', str(blind_sh)])
            self.check_dirs_equal(
                gold_dir,
                output_dir,
            )

            subprocess.check_call(['bash', str(unblind_sh)])
            self.check_dirs_equal(
                input_fixture,
                input_dir,
            )

            assert_that(cmp(
                fixture_dir / 'gold-mapping.csv',
                mapping_dir / 'mapping.csv',
                shallow=False,
            ), is_(True))

    def check_dirs_equal(self, dir1, dir2):
        diff = dircmp(dir1, dir2)

        assert_that(diff.left_only, is_(empty()))
        assert_that(diff.right_only, is_(empty()))
        assert_that(diff.common_funny, is_(empty()))
        assert_that(diff.diff_files, is_(empty()))
        assert_that(diff.funny_files, is_(empty()))

        match, mismatch, errors = cmpfiles(
            dir1,
            dir2,
            diff.common_files,
            shallow=False,
        )
        assert_that(mismatch, is_(empty()))
        assert_that(errors, is_(empty()))

        for common_dir in diff.common_dirs:
            self.check_dirs_equal(
                dir1 / common_dir,
                dir2 / common_dir,
            )

    def test_delimiter(self):
        runner = CliRunner()

        fixture_dir = (
            Path(os.path.dirname(__file__))
            / 'fixtures'
            / 'delimiter-test'
        )
        args = [
            '--mode',
            'delimiter',
            '--delimiter',
            '_foo',
        ]
        self.check_cli_command(runner, fixture_dir, args)

    def test_identifiers(self):
        runner = CliRunner()

        fixture_dir = (
            Path(os.path.dirname(__file__))
            / 'fixtures'
            / 'identifiers-test'
        )
        args = [
            '--mode',
            'identifiers',
            '--identifiers',
            str(fixture_dir / 'identifiers.txt'),
        ]
        self.check_cli_command(runner, fixture_dir, args)

    def test_substring_identifiers(self):
        runner = CliRunner()
        fixture_dir = (
            Path(os.path.dirname(__file__))
            / 'fixtures'
            / 'identifiers-substring-test'
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir = Path(temp_dir)
            output_dir = temp_dir / 'output_dir'
            input_dir = temp_dir / 'input_dir'
            input_dir.mkdir()

            result = runner.invoke(cli.main, [
                '--mode',
                'identifiers',
                '--identifiers',
                str(fixture_dir / 'identifiers.txt'),
                '--input-dir',
                str(input_dir),
                '--output-dir',
                str(output_dir),
            ])

            assert result.exit_code != 0
