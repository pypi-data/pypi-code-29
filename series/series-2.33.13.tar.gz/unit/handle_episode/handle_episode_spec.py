import shutil
import os
import re

import sure  # NOQA
import httpretty

from golgi import Config
from tek.user_input import input_queue

from series.handle_episode import EpisodeHandler

from amino.test import load_fixture

from unit._support.spec import Spec


class Episode_(Spec):

    def setup(self, *a, **kw):
        super().setup(*a, configs=['series.handle_episode'], **kw)
        Config.override('subsync', base_url='http://fakesubs.com')
        self._data_dir = os.path.join(os.path.dirname(__file__),
                                      os.path.pardir, '_data')
        self._sub = lambda *p: os.path.join(self._data_dir, *p)
        self._temp = self._sub('handle_episode', 'temp')
        self._series = self._sub('handle_episode', 'series')
        shutil.rmtree(self._temp, ignore_errors=True)
        shutil.rmtree(self._series, ignore_errors=True)
        os.makedirs(self._temp)
        os.makedirs(self._series)
        Config.override('series', temp_dir=self._temp, series_dir=self._series)

    @httpretty.activate
    def test_dir(self):
        library_url = 'http://fakelib.com'
        Config.override('series', library_url=library_url)
        Config.override('store_episode', ask_series=False)
        sub_page = load_fixture('subsync', 'game_of_thrones_1x2_sub_page')
        url = re.compile(library_url + '/series/')
        httpretty.register_uri(httpretty.POST, url, body='{}')
        httpretty.register_uri(
            httpretty.GET, 'http://fakesubs.com/serie/game_of_thrones/1/2/1',
            body=sub_page)
        httpretty.register_uri(
            httpretty.GET, 'http://fakesubs.com/serie/game_of_thrones/2/2/1',
            body=sub_page)
        httpretty.register_uri(httpretty.GET,
                               'http://fakesubs.com/serie/dexter/5/99/1',
                               body=sub_page)
        httpretty.register_uri(httpretty.GET, re.compile('original'),
                               body=sub_page)
        input_queue.push('q', 'y', 'q')
        os.mkdir(os.path.join(self._series, 'dexter'))
        os.mkdir(os.path.join(self._series, 'game_of_thrones'))
        os.mkdir(os.path.join(self._series, 'subtitle'))
        os.mkdir(os.path.join(self._series, 'title'))
        handler = EpisodeHandler(pretend_delete=True)
        handler.handle_episodes([self._sub('handle_episode')])
        epis = sorted(handler._episodes, key=lambda f: f.filename)
        epis[0].valid.should.be.false
        out_file_path = os.path.join(self._series, 'title', 's1', 'sub',
                                     'title_01x02.srt')
        os.path.isfile(out_file_path).should.be.true
        epis[3].complete.should.be.false
        shutil.rmtree(self._temp, ignore_errors=True)
        shutil.rmtree(self._series, ignore_errors=True)
