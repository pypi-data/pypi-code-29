import sure  # NOQA

from series.rest_api import RestApi, route_decorator

from unit._support.spec import Spec


class _TestApi(RestApi):

    routes, route = route_decorator()

    @route('/someuri', methods=['PUT'])
    @route('/someotheruri', methods=['GET'])
    def something(self):
        return 'success'


class RestApi_(Spec):

    def setup(self, *a, **kw):
        super().setup(*a, configs=['series'], **kw)
        self._api = _TestApi('test')
        self._api.app.config['TESTING'] = True
        self._client = self._api.app.test_client()
        self._api.setup_routes()

    def test_double_route(self):
        result1 = self._client.put('/someuri').response
        result2 = self._client.get('/someotheruri').response
        next(result1).should.equal(next(result2))

__all__ = ['RestApi_']
