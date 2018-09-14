import re

import sure  # NOQA
from flexmock import flexmock  # NOQA
import httpretty

from golgi import Config, ConfigClient  # NOQA
from amino.test import temp_dir, temp_file, fixture_path

from series.get.model.link import Link, Link
from series.get.db import FileDatabase
from series.get.model.release import ReleaseMonitor
from series.get import SeriesGetD
from series.get.model.torrent import TorrentProxy
from series.get.torrent_handler import TorrentHandler

from integration._support.spec import Spec
from unit.get._support.link import LinkTestMixin
from unit._fixtures.get.monitors import monitors_1


class CreateFeedReleaseSpec(LinkTestMixin, Spec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        download_dir = temp_dir('get', 'db', 'download')
        Config.override('get', download_dir=download_dir,
                        min_size=0, auto_upgrade_db=False)
        Config.override('search', providers=['uploaded', 'put'])
        path = temp_file('get', 'db', 'integration', 'db')
        Config.override('get', db_path=path)

    @httpretty.activate
    def _create_a_release_wrzko(self):
        filename = 'wrzko.rss'
        url = ('http://ul.to/oijoycsw/ddlsource.com_burn.notice.s07e05'
               '.proper.720p.hdtv.x264-2hd.mkv')
        monitor = ['burn_notice']
        self._create_release(monitor, filename, url)

    @httpretty.activate
    def _create_a_release_rlsbb(self):
        filename = 'rlsbb.rss'
        url = ('http://ul.to/56ofvz3k/Hulk.and.the.Agents.of.S.M.A.S.H.S01E24'
               '.Monsters.No.More.720p.WEB-DL.x264.AAC.mp4')
        monitor = ['hulk_and_the_agents_of_s_m_a_s_h']
        self._create_release(monitor, filename, url)

    @httpretty.activate
    def _create_a_release_ezrss(self):
        filename = 'ezrss.rss'
        monitor = ['face_off']
        url = 'http://location'

        class Mock(object):

            def __init__(self):
                self.domain = self.valid = self.cachable = self.cacher = True
                self.download_url = url
                self.cached = False

            def request(self):
                self.cached = True

        mock = Mock()
        flexmock(TorrentProxy).should_receive('__new__').and_return(mock)
        self._create_release(monitor, filename, url)

    def _create_release(self, monitor, filename, url):
        Config.override('sharehoster', link_checker_url=None)
        Config.override('get', run=['feed_poller', 'downloader',
                                    'torrent_handler'],
                        sync_link_check=True)
        Config.override('series', monitor=monitor)
        (flexmock(Link)
         .should_receive('valid')
         .and_return(True))
        (flexmock(TorrentHandler)
         .should_receive('_sanity_check')
         .and_return(True))
        (flexmock(TorrentHandler)
         .should_receive('_check_error')
         .and_return(True))
        get = SeriesGetD()
        get.feed_poller._initial_wait = 0
        get.downloader._initial_wait = 0
        get.downloader._interval = 0.5
        get.torrent_handler._initial_wait = 0.5
        db = get.db
        releases = get.releases
        httpretty.register_uri(httpretty.GET, re.compile('.*'), body='success')
        get.start()
        fname = fixture_path('get', filename)
        get.feed_poller.load_from_xml_file(fname)
        later(lambda: releases.count)
        later(lambda: releases.all[0].downloaded)
        get.interrupt(0, 0)
        db.disconnect()
        db = FileDatabase(temp_file('get', 'db', 'integration', 'db'),
                          auto_upgrade=False)
        monitor = db.query(ReleaseMonitor).first()
        monitor.link.download_url.should.equal(url)
        monitor.downloaded.should.be.true

    @httpretty.activate
    def _check_links(self):
        Config.override('get', run=['link_handler', 'downloader'])
        Config.override('get', link_check_retry_coefficient=1. / 30.)
        get = SeriesGetD()
        db = get.db
        self._releases = get.releases
        db.load_data(monitors_1())
        self._mock_content()
        get.link_handler._initial_wait = 0
        get.downloader._initial_wait = 0
        get.downloader._interval = 0.5
        get.start()
        query = db.query(Link)
        later(lambda: all([l.status == Link.CHECK_FAILED for l in
                                    query.all()]))
        self._mock_link_check()
        self._working = ['file1a']
        monitor = self._releases.all[0]
        later(lambda: monitor.links[0].status == Link.CHECKED)
        later(lambda: self._releases.all[0].downloaded)
        monitor = self._releases.all[0]
        url = 'http://foo.bum/file1a'
        monitor.link.url.should.equal(url)
        monitor.downloaded.should.be.true
        get.interrupt(0, 0)

__all__ = ('CreateFeedReleaseSpec',)
