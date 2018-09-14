import sure  # NOQA
from flexmock import flexmock  # NOQA
import httpretty

from golgi import Config, ConfigClient  # NOQA
from amino.test import temp_dir, temp_file
from amino.test.spec_spec import later

from series.get.model.link import Link
from series.get import SeriesGetD

from integration._support.spec import Spec
from unit.get._support.link import LinkTestMixin
from unit._fixtures.get.monitors import monitors_2


class MultipleReleasesSpec(LinkTestMixin, Spec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        download_dir = temp_dir('get', 'db', 'download')
        Config.override('get', download_dir=download_dir,
                        min_size=0, auto_upgrade_db=False)
        Config.override('search', providers=['uploaded', 'put'])
        path = temp_file('get', 'db', 'integration', 'db')
        Config.override('get', db_path=path)

    @httpretty.activate
    def download(self):
        (flexmock(Link)
            .should_receive('valid')
            .and_return(True))
        Config.override('get', run=['downloader', 'archiver'],
                        library=False)
        series_dir = temp_dir('series', 'archiver', 'series')
        Config.override('series', series_dir=series_dir)
        get = SeriesGetD()
        self._releases = get.releases
        get.downloader._initial_wait = 0
        get.archiver._initial_wait = 0
        get.db.load_data(monitors_2())
        self._mock_content()
        get.pre()
        later(lambda: self._releases.all[1].downloaded)
        later(lambda: self._releases.all[1].archived)
        get.interrupt()

__all__ = ('MultipleReleasesSpec',)
