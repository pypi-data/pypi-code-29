"""Create Chrome driver for Selenium"""

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class DriverFactory():
    """Class for creating Chrome driver for Selenium"""
    def __init__(self):
        """Constructor for DockerDriverFactory"""
        self.cmd_executor = 'http://selenium-hub:4444/wd/hub'
        self.capabilities = DesiredCapabilities.CHROME

    def set_capabilities(self, capabilities):
        """Set browser capabilities"""
        self.capabilities = capabilities

    def create(self):
        """Create Chrome driver"""
        return webdriver.Remote(
            command_executor=self.cmd_executor,
            desired_capabilities=self.capabilities)
