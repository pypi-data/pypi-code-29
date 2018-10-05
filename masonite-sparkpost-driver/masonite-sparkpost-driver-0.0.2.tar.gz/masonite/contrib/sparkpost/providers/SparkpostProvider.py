""" A Sparkpost Service Provider """

from masonite.provider import ServiceProvider

from ..drivers import MailSparkpostDriver


class SparkpostProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('MailSparkpostDriver', MailSparkpostDriver)

    def boot(self):
        pass
