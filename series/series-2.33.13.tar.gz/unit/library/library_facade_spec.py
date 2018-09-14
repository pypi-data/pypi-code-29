from datetime import datetime, timedelta

from golgi import Config
from amino.test import temp_file, create_temp_file
from tek.tools import find

from series.library.model.watch_event import WatchEvent
from series.library.model.series import Series
from series.library.model.season import Season
from series.library.library_facade import LibraryFacade

from unit.library._support.db import DBSpec
from unit._fixtures.library import create_episodes, create_movies


class LibraryFacade_(DBSpec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        episodes = [
            ['series1', 2, 1, 0],
            ['series2', 1, 1, 0],
            ['series1', 2, 2, 1],
        ]
        movies = ['the_title.mkv', 'the_other_title.mkv']
        self._collections, self._episodes = create_episodes(['lib1', 'lib2'],
                                                            episodes)

        self._movie_collection, self._movies = create_movies('movies', movies)
        self._lib = LibraryFacade(self._db)
        self._lib.scan()

    def scan_collections(self):
        series = self._lib.series('series1')
        episode = self._lib.episode(series, 2, 1)
        episode.series.should.equal(series)
        episode.season.should.equal(self._lib.season(series=series, number=2))

    def scan_collections_rex(self):
        Config.override(
            'series',
            enumeration_regex='(?P<name>.*)_(?P<season>\d+)x(?P<episode>\d+)'
        )
        series = self._lib.series('series1')
        episode = self._lib.episode(series, 2, 1)
        episode.series.should.equal(series)
        episode.season.should.equal(self._lib.season(series=series, number=2))

    def determine_episode_path(self):
        _file = 'series1_2x2.mkv'
        _path = temp_file(self._collections[1], 'series1', '2', _file)
        episode = self._lib.episode(series='series1', season=2, number=2)
        self._lib.episode_path(episode).should.equal(_path)

    def determine_subtitle_path(self):
        templ = '{name}/{season}/sub/{name}_{season}x{episode}.{ext}'
        Config.override('library', subtitle_path_template=templ)
        _file = 'series1_2x2.srt'
        _path = temp_file(self._collections[1], 'series1', '2', 'sub', _file)
        create_temp_file(_path)
        episode = self._lib.episode(series='series1', season=2, number=2)
        self._lib.subtitle_path(episode).should.equal(_path)

    def determine_movie_path(self):
        movie = self._lib.movie(title='the_title')
        self._lib.movie_path(movie).should.equal(self._movies[0])

    def determine_movie_subtitle_path(self):
        _file = 'the_title.sub'
        _path = temp_file(self._movie_collection, 'sub', _file)
        create_temp_file(_path)
        movie = self._lib.movie(title='the_title')
        self._lib.movie_subtitle_path(movie).should.equal(_path)

    def add_watch_event(self):
        now = datetime.now()
        before = now - timedelta(minutes=22)
        self._lib.add_watch_event('series1', 2, 1, before, now, 100.)
        event = self._db.query(WatchEvent).first()
        (before - event.begin).total_seconds().should.be.lower_than(1)
        (now - event.end).total_seconds().should.be.lower_than(1)

    def query_recently_watched_episodes(self):
        now = datetime.now()
        first_begin = now - timedelta(hours=12)
        first_end = first_begin + timedelta(minutes=30)
        first_begin_2 = now - timedelta(hours=6)
        first_end_2 = first_begin_2 + timedelta(minutes=30)
        second_begin = now - timedelta(hours=24, minutes=15)
        second_end = second_begin + timedelta(minutes=30)
        third_begin = now - timedelta(hours=48)
        third_end = third_begin + timedelta(minutes=30)
        self._lib.add_watch_event('series1', 2, 1, first_begin, first_end,
                                  100.)
        self._lib.add_watch_event('series1', 2, 1, first_begin_2, first_end_2,
                                  100.)
        self._lib.add_watch_event('series1', 2, 2, second_begin, second_end,
                                  100.)
        self._lib.add_watch_event('series2', 1, 1, third_begin, third_end,
                                  100.)
        episodes = self._lib.recently_watched_episodes(days=1)
        episodes.should.have.length_of(1)
        episodes[0].series.canonical_name.should.equal('series1')
        episodes[0].number.should.equal(1)

    class next_previous_episode(object):

        def no_next_episode(self):
            episodes = [
                ['nepi', 1, 1, 0],
                ['nepi', 1, 2, 0],
                ['nepi', 2, 1, 0],
                ['nepi', 2, 2, 0],
            ]
            create_episodes(['lib1'], episodes)
            self._lib.scan()
            origin = self._lib.episode('nepi', 2, 2)
            self._lib.next_episode(origin).should.be.none
            origin = self._lib.episode('nepi', 1, 1)
            self._lib.previous_episode(origin).should.be.none

        def successive_in_same_season(self):
            episodes = [
                ['nepi', 1, 1, 0],
                ['nepi', 2, 1, 0],
                ['nepi', 2, 2, 0],
                ['nepi', 2, 3, 0],
                ['nepi', 3, 1, 0],
            ]
            create_episodes(['lib1'], episodes)
            self._lib.scan()
            origin = self._lib.episode('nepi', 2, 1)
            target1 = self._lib.episode('nepi', 2, 2)
            target2 = self._lib.episode('nepi', 2, 3)
            _next = self._lib.next_episode(origin)
            _next.should.equal(target1)
            self._lib.previous_episode(_next).should.equal(origin)
            _next = self._lib.next_episode(_next)
            _next.should.equal(target2)
            self._lib.previous_episode(_next).should.equal(target1)

        def nonsuccessive_in_same_season(self):
            episodes = [
                ['nepi', 1, 1, 0],
                ['nepi', 2, 1, 0],
                ['nepi', 2, 3, 0],
                ['nepi', 3, 1, 0],
            ]
            create_episodes(['lib1'], episodes)
            self._lib.scan()
            origin = self._lib.episode('nepi', 2, 1)
            target = self._lib.episode('nepi', 2, 3)
            _next = self._lib.next_episode(origin)
            _next.should.equal(target)
            self._lib.previous_episode(_next).should.equal(origin)

        def successive_season(self):
            episodes = [
                ['nepi', 1, 1, 0],
                ['nepi', 2, 1, 0],
                ['nepi', 2, 3, 0],
                ['nepi', 3, 1, 0],
                ['nepi', 3, 2, 0],
                ['nepi', 4, 5, 0],
            ]
            create_episodes(['lib1'], episodes)
            self._lib.scan()
            origin = self._lib.episode('nepi', 2, 3)
            target = self._lib.episode('nepi', 3, 1)
            _next = self._lib.next_episode(origin)
            _next.should.equal(target)
            self._lib.previous_episode(_next).should.equal(origin)

        def nonsuccessive_season(self):
            episodes = [
                ['nepi', 1, 1, 0],
                ['nepi', 2, 1, 0],
                ['nepi', 2, 3, 0],
                ['nepi', 4, 5, 0],
                ['nepi', 4, 8, 0],
            ]
            create_episodes(['lib1'], episodes)
            self._lib.scan()
            origin = self._lib.episode('nepi', 2, 3)
            target = self._lib.episode('nepi', 4, 5)
            _next = self._lib.next_episode(origin)
            _next.should.equal(target)
            self._lib.previous_episode(_next).should.equal(origin)

    def remove_episode(self):
        self._episodes[0].unlink()
        self._episodes[1].unlink()
        self._lib.episode('series1', 2, 1).number.should.equal(1)
        self._lib.clean()
        self._lib.episode('series1', 2, 1).should.be.none
        self._lib.episode('series1', 2, 1, removed=True).number.should.equal(1)
        self._lib.episode('series1', 2, 1, removed=True).removed.should.be.true
        find(lambda s: s.canonical_name == 'series2',
             self._lib.all_series).should.be.none
        find(lambda s: s.canonical_name == 'series1',
             self._lib.all_series).should_not.be.none

    def empty_series(self):
        name = 'empty_series'
        series = self._lib._create_if_missing(Series, name=name)
        find(lambda s: s.canonical_name == name,
             self._lib.all_series).should.be.none
        self._lib._create_if_missing(Season, series=series, number=1)
        find(lambda s: s.canonical_name == name,
             self._lib.all_series).should.be.none

__all__ = ['LibraryFacade_']
