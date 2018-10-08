#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest

from click.testing import CliRunner

from punica.cli import main


class TestDeployCmd(unittest.TestCase):
    def test_deploy_cmd(self):
        project_path = os.path.join(os.getcwd(), 'test_file', 'test_deploy')
        runner = CliRunner()
        result = runner.invoke(main, ['-p', project_path, 'deploy', '--password', 'password'])
        self.assertEqual(0, result.exit_code)


if __name__ == '__main__':
    unittest.main()
