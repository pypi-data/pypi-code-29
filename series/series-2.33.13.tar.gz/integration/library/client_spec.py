from series.library.rest_api import RestApi
from series.library import Player
from series.library.client.rest_api import LibClient

from unit.library._support.db import DBTestMixin

from integration._support.rest_api import ApiClientSpec


class _ApiSpec(ApiClientSpec, DBTestMixin):

    def setup(self) -> None:
        ApiClientSpec.setup(self)
        DBTestMixin.setup(self)
        self.api

    @property
    def _create_api(self):
        player = Player(self._lib)
        return RestApi(self._lib, player)


class ClientSpec(_ApiSpec):

    def setup(self):
        _ApiSpec.setup(self)
        self._client = LibClient()

    def create_episode(self):
        data = ('series_name', 5, 3)
        self._client.create_episode(*data)
        episode = self._lib.episode(*data)
        episode.series.name.should.equal('series_name')
        episode.season.number.should.equal(5)
        episode.number.should.equal(3)

    def subfps(self):
        data = ('series_name', 5, 3)
        self._lib.create_episode(*data)
        self._client.subfps(*(data + ('24',)))

__all__ = ['ClientSpec']
