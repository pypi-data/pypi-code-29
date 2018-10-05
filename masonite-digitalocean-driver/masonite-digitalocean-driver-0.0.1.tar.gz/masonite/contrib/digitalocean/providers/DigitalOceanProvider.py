""" A Dropbox Service Provider """

from ..drivers import UploadDigitaloceanDriver
from masonite.provider import ServiceProvider

class DigitalOceanProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('UploadDigitalOceanDriver', UploadDigitaloceanDriver)

    def boot(self):
        pass
