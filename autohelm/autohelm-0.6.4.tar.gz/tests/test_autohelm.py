
import unittest
import autohelm.autohelm as autohelm
import coloredlogs
import logging
import os
import subprocess
import git


test_course = "./tests/test_course.yml"
git_repo_path = "./test"


class TestAutohelm(unittest.TestCase):
    name = "test-pentagon-base"

    def setUp(self):
        coloredlogs.install(level="DEBUG")
        repo = git.Repo.init(git_repo_path)
        os.chdir(git_repo_path)
        subprocess.call(["helm", "create", "chart"])
        # Create git chart in a git repo, then have it checkout the repo from that location
        logging.debug(os.listdir("./"))
        os.chdir("../")
        with open(test_course) as f:
            self.a = autohelm.AutoHelm(file=f, dryrun=True, local_development=True)

    def tearDown(self):
        self.a = None
        subprocess.call(['rm', '-rf', git_repo_path])

    def test_instance(self):
        self.assertIsInstance(self.a, autohelm.AutoHelm)

    # def test_(self):
    #     self.assertEqual(self.p._name, self.name)
