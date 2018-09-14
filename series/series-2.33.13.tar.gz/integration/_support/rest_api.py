import time
import socket

from flexmock import flexmock_teardown

from golgi import Config

from amino.lazy import lazy

from integration._support.spec import Spec


def _free_ports():
    for num in range(1024, 65535):
        sock = socket.socket()
        try:
            sock.bind(('localhost', num))
        except OSError:
            pass
        else:
            yield num
        finally:
            sock.close()


class ApiSpec(Spec):

    def setup(self, **kw):
        Spec.setup(self, configs=['series.get', 'series.library'], **kw)
        port = next(_free_ports())
        Config.override('get', rest_api_port=port)
        Config.override('get_client', rest_api_port=port)
        Config.override('library', rest_api_port=port)
        Config.override('library_client', rest_api_port=port)


class ApiClientSpec(ApiSpec):

    @lazy
    def api(self):
        api = self._create_api
        api.app.config['TESTING'] = True
        api.start()
        time.sleep(0.1)
        return api

    def teardown(self):
        self.api.stop()
        self.api.join()
        flexmock_teardown()

__all__ = ('ApiClientSpec',)
