import oslogmerger.oslogmerger as om
from oslogmerger.tests import base


class PathManipulationTests(base.BaseTestCase):
    def test_get_path_and_alias(self):
        self.assertEqual(
            om.get_path_and_alias('filename', '/base/', '.log'),
            ('/base/filename.log', None, False))

    def test_get_path_and_alias_http(self):
        self.assertEqual(
            om.get_path_and_alias('filename', 'http://server/', '.log'),
            None)
