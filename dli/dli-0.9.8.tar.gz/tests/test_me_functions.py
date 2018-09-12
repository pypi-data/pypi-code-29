import logging
import os
import six

from .common import SdkIntegrationTestCase


class MeFunctionsTestCase(SdkIntegrationTestCase):

    def test_get_my_packages_validates_page_size(self):
        with self.assertRaises(ValueError):
            self.client.get_my_packages(count=-1)
        with self.assertRaises(ValueError):
            self.client.get_my_packages(count=0)
        with self.assertRaises(ValueError):
            self.client.get_my_packages(count="test")

    def test_get_my_packages_return_packages(self):
        self.package_id = self.create_package("test_me_functions")
        self.assertGreater(len(self.client.get_my_packages()), 0)
        self.assertEquals(len(self.client.get_my_packages(count=1)), 1)
