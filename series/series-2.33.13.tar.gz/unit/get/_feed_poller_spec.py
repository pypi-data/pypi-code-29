import sure  # NOQA
from flexmock import flexmock

from series.get.feed_poller import FeedPoller
from series.get.model.feed_entry import (FeedEntryFactory, WrzkoParser,
                                            FeedEntry)

from unit.get._support.db import DBTestMixin
from amino.test import fixture_path
from golgi import Configurations
from unit.get._support.spec import Spec


class FeedPoller_(DBTestMixin, Spec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        self._feed_poller = FeedPoller(self._releases)

    def parse_an_rss_feed(self):
        flexmock(FeedPoller).should_receive('_reconstruct_entries')
        fname = fixture_path('get', 'wrzko.rss')
        self._feed_poller.load_from_xml_file(fname)
        entries = self._feed_poller._rss.entries
        entries.should.have.length_of(5)
        entries[0].should.be.a('feedparser.FeedParserDict')

    def discard_seen_entries(self):
        fname = fixture_path('get', 'wrzko.rss')
        self._feed_poller.load_from_xml_file(fname)
        self._feed_poller._feed_entries.should.have.length_of(5)
        self._feed_poller.load_from_xml_file(fname)
        self._feed_poller._feed_entries.should.have.length_of(0)

    def create_monitor(self):
        feed_factory = FeedEntryFactory('')
        title1 = 'series.name.s99e11.episode.title.1080p'
        title2 = 'series.name.s99e11.episode.title2.720p'
        entry1 = feed_factory.from_title(title1)
        entry2 = feed_factory.from_title(title2)
        self._feed_poller._create_monitor(entry1)
        self._releases.all[-1].nuked.should_not.be.ok
        self._feed_poller._create_monitor(entry2)
        self._releases.all[-2].nuked.should.be.ok

    def _update_links(self):
        monitor = ['series_name']
        url1 = 'http://fake.host/file1a'
        url2 = 'http://fake.host/file1b'
        Configurations.override('series', monitor=monitor)
        title = 'series.name.s99e11.episode.title.720p-rls'
        release = WrzkoParser({}, [])._release_from_title(title)
        entry = FeedEntry(release, links=['http://fake.host/file1a'])
        self._feed_poller._feed_entries = [entry]
        self._feed_poller._update_monitors()
        monitor = self._releases.all[-1]
        monitor.release.title.should.equal(title)
        monitor.links.count().should.equal(1)
        monitor.links[0].url.should.equal(url1)
        monitor.has_url(url1).should.be.ok
        monitor.has_url(url2).should_not.be.ok
        entry.links = [url1, url2]
        self._feed_poller._update_monitors()
        self._releases.check_commit()
        monitor.links.count().should.equal(2)
        monitor.links[1].url.should.equal(url2)
