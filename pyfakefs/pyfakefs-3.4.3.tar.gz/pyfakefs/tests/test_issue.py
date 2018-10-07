import shutil, os

from pyfakefs import fake_filesystem_unittest


class Test(fake_filesystem_unittest.TestCase):
    def setUp(self):
        self.setUpPyfakefs()
        print(os)
        self.fs.create_file('c:/src/file_1.txt')
        self.fs.create_file('c:/src/a/file_2.txt')
        shutil.make_archive('c:/archive', 'zip', root_dir='c:/src')

    def test_a(self):
        self.assertTrue(True)

    def test_b(self):
        self.assertTrue(True)
