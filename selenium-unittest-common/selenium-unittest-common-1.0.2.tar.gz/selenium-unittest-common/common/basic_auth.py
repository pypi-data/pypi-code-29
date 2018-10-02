"""Send credentials to Basic Authentication."""

class BasicAuth():
    """BasicAuth Class"""
    def __init__(self, driver, hosts, is_ssl=True):
        """Constructor for BasicAuth class

        :rtype: selenium.webdriver driver
        :rtype: array hosts
        :rtype: boolean is_ssl
        """
        self.driver = driver
        self.hosts = hosts
        self.is_ssl = is_ssl
        self.login = ''
        self.pwd = ''

    def send_credentials(self, login, pwd):
        """Send credentials, which is as part of URL, to the host.

        :rtype: string login
        :rtype: string pwd
        """
        protocol = 'https://' if self.is_ssl else 'http://'
        for host in self.hosts:
            self.driver.get(protocol + login + ':' + pwd + '@' + host + '/')
