from flexmock import flexmock

from tek.tools import find

from series.library.rest_api import RestApi
from series.library.player import Player
from unit.library._support.db import DBSpec
from unit._fixtures.library import create_episodes, create_movies
from unit._support.rest_api import RestApiTestMixin


class RestApiSpec(RestApiTestMixin, DBSpec):

    def setup(self, *a, **kw):
        super().setup()
        episodes = [
            ['series1', 5, 1, 0],
            ['series1', 5, 2, 0],
            ['series1', 5, 3, 0],
            ['series1', 6, 4, 0],
            ['series2', 3, 1, 0],
            ['series2', 3, 2, 0],
        ]
        movies = ['the_title.mkv', 'the_other_title.mkv']
        _, self._episodes = create_episodes(['rest_api'], episodes)
        _, self._movies = create_movies('rest_api_movies', movies)
        self._lib.scan()
        self._lib.episode('series1', 5, 3).new = False
        self._lib.episode('series2', 3, 2).new = False
        player = Player(self._lib)
        self._api = RestApi(self._lib, player)
        self._api.app.config['TESTING'] = True
        self._client = self._api.app.test_client()
        self._api.setup_routes()

    def query_new_episodes(self):
        response = self._query('episode/new')
        def is_epi(s, ss, e):
            return lambda el: (
                el['season']['show']['name'] == s and
                el['season']['number'] == ss and
                el['episode'] == e)
        find(is_epi('Series1', 5, 2), response).should.be.a(dict)
        find(is_epi('Series1', 5, 3), response).should.be.none
        find(is_epi('Series2', 3, 2), response).should.be.none

    def play_a_series(self):
        flexmock(Player).should_receive('start')
        response = self._query('series/series1/5/2/watch', method='put')
        response.should.equal({'msg': 'success'})

    def query_series(self):
        response = self._query('/series')
        response[0]['name'].should.equal('Series1')
        response[0]['new_count'].should.equal(3)
        response[1]['new_count'].should.equal(1)

    def query_season(self):
        response = self._query('series/series1')
        response['series']['name'].should.equal('Series1')
        response['seasons'][0]['new_count'].should.equal(2)
        response['seasons'][1]['new_count'].should.equal(1)

    def query_next_episode(self):
        response = self._query('series/series1/season/5/episode/3/next')
        episode = response['next']
        episode['season']['show']['name'].should.equal('Series1')
        episode['season']['number'].should.equal(6)
        episode['episode'].should.equal(4)
        response = self._query('series/series1/season/6/episode/4/next')
        episode = response['next']
        episode.should.be.none

    def query_previous_episode(self):
        response = self._query('series/series1/season/6/episode/4/previous')
        episode = response['previous']
        episode['season']['show']['name'].should.equal('Series1')
        episode['season']['number'].should.equal(5)
        episode['episode'].should.equal(3)
        response = self._query('series/series1/season/5/episode/1/previous')
        episode = response['previous']
        episode.should.be.none

    def create_episode(self):
        response = self._query('series/create_test/season/1/episode/1',
                               method='post')
        episode = self._lib.episode('create_test', 1, 1)
        response['series'].should.equal(episode.series.formatted_name)

    def get_episode(self):
        response = self._query('series/series2/season/3/episode/1',
                               method='get')
        response['series'].should.equal('Series2')
        response['season'].should.equal(3)
        response['episode'].should.equal(1)

    def alter_episode(self):
        self._lib.episode('series2', 3, 1).new.should.be.true
        data = dict(new=False)
        response = self._query('series/series2/season/3/episode/1',
                               method='put', data=data)
        self._lib.episode('series2', 3, 1).new.should.be.false
        response = self._query('series/series3/season/3/episode/1',
                               method='put', data=data)
        response['error'].should.equal('No such episode')

    def delete_episode(self):
        data = dict(new=False)
        self._query('series/series2/season/3/episode/1', method='delete',
                    data=data)
        self._lib.episode('series2', 3, 1).should.be.none

    def query_movies(self):
        response = self._query('movie')
        response.should.have.length_of(2)
        response[0]['canonical'].should.equal('the_other_title')

    def query_movie(self):
        response = self._query('movie/the_title')
        response['canonical'].should.equal('the_title')

    def play_a_movie(self):
        flexmock(Player).should_receive('start')
        response = self._query('movie/the_title/watch', method='put')
        response.should.equal(dict(msg='success'))

__all__ = ('RestApiSpec',)
