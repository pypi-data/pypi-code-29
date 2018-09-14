from series.store_episode import EpisodeHandler
from golgi.config import ConfigClient, Config
from amino.test import temp_dir

from unit._support.spec import Spec


class EpisodeHandler_(Spec):

    def setup(self):
        super().setup(configs=['series.store_episode'])
        self._series_path = temp_dir('store_episode', 'series')
        Config.override('series', series_dir=self._series_path)
        temp_dir(self._series_path, 'series_name')

    def known_series(self):
        h = EpisodeHandler(ask=False)
        h.add_episode('/foo/Series Name - 01x10 - trailing garbage.srt')
        target_path = (self._series_path / 'series_name' / 's1' / 'sub' /
                       'series_name_01x10.srt')
        h.jobs[0].dest.should.equal(target_path)

    def unknown_series(self):
        c = ConfigClient('series')
        Config.override('store_episode', ask_series=False,
                        auto_choose_new_series=True)
        h = EpisodeHandler(ask=False)
        h.add_episode('/foo/Unknown Series  - 01x10 - trailing garbage.srt')
        target_path = (self._series_path / 'unknown_series' / 's1' / 'sub' /
                       'unknown_series_01x10.srt')
        h.jobs[0].dest.should.equal(target_path)
