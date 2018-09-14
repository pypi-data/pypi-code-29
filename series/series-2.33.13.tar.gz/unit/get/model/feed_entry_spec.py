import re
import pprint
import importlib
import os

from flexmock import flexmock

import feedparser
from feedparser import FeedParserDict

from golgi import Config
from amino.test import fixture_path

from series.get.model.feed_entry import (FeedEntryFactory, RlsbbParser,
                                         WrzkoParser, EzrssParser,
                                         ShowrssParser)
from series.etvdb import ETVDB
from unit.get._support.spec import Spec


def _fixture_entry(domain, number):
    mod_name = 'unit._fixtures.get.{}.entry{}'.format(domain, number)
    module = importlib.import_module(mod_name)
    entry = module.entry
    fact = FeedEntryFactory('http://{}.foo'.format(domain))
    fdict = FeedParserDict(entry)
    fdict['summary_detail'] = FeedParserDict(fdict['summary_detail'])
    if 'content' in fdict:
        fdict['content'][0] = FeedParserDict(fdict['content'][0])
    return fact.process_item(fdict)


class EntryParser_(Spec):

    class wrzko(Spec):

        def setup(self):
            self._parent.setup(self)
            Config.override('search', providers=['uploaded'])
            self._subject = WrzkoParser({}, [])

        def it_should_parse_a_title(self):
            title = ('series.name.s99e11.episode.title5x3s5e1'
                     '.1080p.type.codec-group')
            release = self._subject._release_from_title(title)
            release.is_series.should.be.ok
            release.title.should.equal(title)
            release.name.should.equal('series_name')
            str(release.season).should.equal('99')
            str(release.episode).should.equal('11')
            release.resolution.should.equal('1080p')
            release.is_hd.should.be.ok
            release.group.should.equal('group')
            release.is_fix.should_not.be.ok

        def it_should_parse_a_title_without_title(self):
            title = 'Series.Name.S07E11.720p.HDTV.x264-IMMERSE'
            release = self._subject._release_from_title(title)
            release.is_series.should.be.ok
            release.name.should.equal('series_name')
            str(release.episode).should.equal('11')

        def it_should_create_a_search_string(self):
            title = 'Series.Name.S05E10.PROPER.720p.HDTV.x264-ORENJI'
            release = self._subject._release_from_title(title)
            strng = '3968699907/series.name_s05e10.720p_hdtv.x264-orenji'
            re.search(release.search_string, strng).should.be.ok

        def it_should_compare_releases(self):
            title = 'Series.Name.S01E10.720p.HDTV.x264-IMMERSE'
            r1 = self._subject._release_from_title(title)
            r2 = self._subject._release_from_title(title)
            r1.should.equal(r2)

        def it_should_detect_a_fix(self):
            title = 'Series.Name.S01E10.REPACK.720p.HDTV.x264-IMMERSE'
            release = self._subject._release_from_title(title)
            release.name.should.equal('series_name')
            release.is_fix.should.be.ok

        def it_should_not_choke_on_a_minus(self):
            title = 'Series-Name.S09E10.720p.HDTV.x264-IMMERSE'
            release = self._subject._release_from_title(title)
            release.name.should.equal('series-name')

        def accept_double_episodes(self):
            title = ('series.name.s99e10e11.episode.title5x3s5e1'
                     '.1080p.type.codec-group')
            release = self._subject._release_from_title(title)
            release.is_series.should.be.ok
            release.title.should.equal(title)
            release.name.should.equal('series_name')
            str(release.season).should.equal('99')
            str(release.episode).should.equal('10')
            release.resolution.should.equal('1080p')
            release.is_hd.should.be.ok
            release.group.should.equal('group')
            release.is_fix.shouldnot.be.ok

        def entry(self):
            entry = _fixture_entry('wrzko', 1)
            entry.links.should.equal(
                ['http://ul.to/oijoycsw/ddlsource.com_burn.notice.s07e05.'
                 'proper.720p.hdtv.x264-2hd.mkv']
            )

    class rlsbb(Spec):

        def setup(self):
            self._parent.setup(self)
            Config.override('search', providers=['uploaded'])
            self._subject = RlsbbParser({}, [])

        def it_should_parse_a_title(self):
            title = ('series.name.s99e11.episode.title5x3s5e1'
                     '.1080p.type.codec-group')
            release = self._subject._release_from_title(title)
            release.is_series.should.be.ok
            release.title.should.equal(title)
            release.name.should.equal('series_name')
            str(release.season).should.equal('99')
            str(release.episode).should.equal('11')
            release.resolution.should.equal('1080p')
            release.is_hd.should.be.ok
            release.group.should.equal('group')
            release.is_fix.shouldnot.be.ok

        def entry1(self):
            entry = _fixture_entry('rlsbb', 1)
            entry.links.should.equal(
                ['http://ul.to/56ofvz3k/Hulk.and.the.Agents.of.S.M.A.S.H.'
                 'S01E24.Monsters.No.More.720p.WEB-DL.x264.AAC.mp4']
            )

    class ezrss(Spec):

        def setup(self):
            self._parent.setup(self)
            self._subject = EzrssParser({}, [])

        def entry1(self):
            entry = _fixture_entry('ezrss', 1)
            entry.links.should.equal(
                ['magnet:?xt=urn:btih:JGC3MRI2HC76VMRGQGU7QU5U7SHMHNRP'
                 '&dn=Under.the.Dome.S02E05.720p.HDTV.X264-DIMENSION']
            )

    class showrss(Spec):

        def setup(self):
            self._parent.setup(self)
            self._subject = ShowrssParser({}, [])

        def entry1(self):
            entry = _fixture_entry('showrss', 1)
            entry.links.should.equal(
                ['magnet:?xt=urn:btih:FA2249DFE98E527D134C41FF5D091746E1F9BA24'
                 '&dn=The+Daily+Show+2014+07+29+Sara+Firth+720p+HDTV+x264'
                 '+LMAO']
            )

        def date_enum(self):
            output = ['99|11|111111|title||description|3311-04-12']
            flexmock(ETVDB).should_receive('__call__').and_return(output)
            title = ('series.name.2014.08.13.1080p.type.codec-group')
            release = self._subject._release_from_title(title)
            release.is_series.should.be.ok
            release.title.should.equal(title)
            release.name.should.equal('series_name')
            str(release.season).should.equal('99')
            str(release.episode).should.equal('11')
            release.resolution.should.equal('1080p')
            release.is_hd.should.be.ok
            release.group.should.equal('group')
            release.is_fix.should_not.be.ok

        def it_should_parse_a_title(self):
            title = 'series.name.2014.04.14.episode.title.1080p-groupie'
            release = self._subject._release_from_title(title)
            release.is_series.should.be.ok
            release.title.should.equal(title)
            release.name.should.equal('series_name')
            str(release.season).should.equal('4')
            str(release.episode).should.equal('14')
            release.resolution.should.equal('1080p')
            release.is_hd.should.be.ok
            release.group.should.equal('groupie')
            release.is_fix.shouldnot.be.ok

    class _fixtures(Spec):
        urls = {
            'rlsbb': 'http://feeds.feedburner.com/rlsbb/MrCi',
            'ezrss': 'https://ezrss.it/feed/',
            'showrss': 'http://showrss.info/feeds/all.rss',
        }

        def _entries(self, domain):
            return feedparser.parse(self.urls[domain]).entries

        def extract_entry(self, domain, index, number):
            entry = self._entries(domain)[index]
            entry['author'] = None
            entry['tags'] = None
            entry['published_parsed'] = None
            data = pprint.pformat(entry)
            path = fixture_path('get', domain, 'entry{}.py'.format(number))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'x') as _file:
                _file.write('entry = ' + data)

        def extract_entry_rlsbb(self, index, number):
            self.extract_entry('rlsbb', index, number)

        def extract_entry_ezrss(self, index, number):
            self.extract_entry('ezrss', index, number)

        def extract_entry_showrss(self, index, number):
            self.extract_entry('showrss', index, number)

        def task(self):
            self.extract_entry_showrss(45, 1)

        def print_titles(self):
            for index, entry in enumerate(self._entries('showrss')):
                self.log.debug('{}: {}'.format(index, entry['title']))
