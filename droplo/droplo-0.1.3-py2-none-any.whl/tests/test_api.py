import droplo
import unittest


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.url = "https://api.dev.droplo.io"
        self.token = "c471fb87d07eee1e16c34e5d47d2e721ea141e7d05b1092938e5ff943b0bd09f"

    def tearDown(self):
        pass

    def test_api_missing_accesstoken(self):
        with self.assertRaises(TypeError):
            droplo.Api()

    def test_api_endpoints(self):
        api = droplo.Api(self.token, api_url=self.url)
        endpoints = api.get()
        self.assertEqual(endpoints.folders[0].endpoint, '{0}/posts'.format(self.url))

    def test_api_files(self):
        api = droplo.Api(self.token, api_url=self.url)
        endpoints = api.get()
        self.assertEqual(endpoints.files[0].type, 'application/json')


if __name__ == '__main__':
    unittest.main()
