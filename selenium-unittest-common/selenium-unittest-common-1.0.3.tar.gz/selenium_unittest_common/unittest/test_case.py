"""Base Test Case"""

import os
import unittest
from selenium_unittest_common.common import driver_factory
from selenium_unittest_common.common import page as html_page

# CONSTANTS
DRIVER_FACTORY = driver_factory.DriverFactory()

class BaseTestCase(unittest.TestCase):
    """Base test case class"""
    @classmethod
    def setUpClass(cls):
        """Initialize browser driver and page modules."""
        super(BaseTestCase, cls).setUpClass()
        cls.driver = DRIVER_FACTORY.create()
        cls.html_page = html_page.Page(cls.driver)

    def tearDown(self):
        """Cleanup operation after each test is executed."""
        self.html_page.close_inactive_tabs()

        # Save a screenshot when error occur
        if hasattr(self, '_outcome'):
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)
            error = self.check_result_flag(result.errors)
            failure = self.check_result_flag(result.failures)
            if error or failure:
                self.save_screenshot()

        super(BaseTestCase, self).tearDown()

    def check_result_flag(self, exc_list):
        """Check if the specified flag is on

        :rtype: array exc_list
        """
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]
        return False

    def shortDescription(self):
        """Do not show function comment upon running test cases"""
        return None

    def save_screenshot(self):
        """Save screenshot"""
        img_dir = 'screenshots'
        if not os.path.exists(img_dir):
            os.mkdir(img_dir)

        img_file = '{}/{}.png'.format(img_dir, self._testMethodName)
        self.driver.save_screenshot(img_file)
