import shutil
import os
from golgi import Config, ConfigClient  # NOQA
from amino.test import temp_dir

from series.get import SeriesGetD
from series.get.client.rest_api import ApiClient

from unit.get._support.spec import Spec


class Cli_(Spec):

    def setup(self, *a, **kw):
        super().setup(*a, allow_files=True, **kw)
        # self._client = ApiClient()

    def run_the_get(self):
        Config.override('get', run=['torrent_handler'])
        get = SeriesGetD()
        get.run()

    def test(self):
        run = [
            # 'rest_api',
            # 'torrent_cleaner',
            # 'show_planner',
            'show_scheduler',
            # 'torrent_finder',
            # 'torrent_handler',
            # 'downloader',
            # 'archiver',
        ]
        Config.override('general', debug=True, verbose=True)
        Config.override('get', run=run)
        lib_dir = temp_dir('get', 'cli')
        series_dir = temp_dir('get', 'cli', 'series')
        Config.override('series', series_dir=series_dir)
        Config.override('get',
                        db_path=lib_dir / 'series.db',
                        # torrent_recheck_interval=1
                        )
        Config.override('get_client', rest_api_url='http://localhost')
        Config.override('torrent', search_engine='piratebay')
        Config.override('show_planner', check_interval=1000)
        shutil.copy(os.path.expanduser('~/series.db'), str(lib_dir))
        get = SeriesGetD()
        s = get.shows.by_id(27).value
        sched = get.show_scheduler
        sched._handle(s)
        # self._wait(5)
        # get.torrent_finder._cleanup()
        # get.run()

__all__ = ('Cli_',)
