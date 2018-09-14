import os
import time

import sure  # NOQA
from flexmock import flexmock

from golgi import Config

from series.get.subsyncer import Subsyncer
from series.subsync.errors import NoSubsForEpisode
from series.subsync import Subtitle
from series import subsync, SubtitleMetadata

from unit.get._support.db import DBSpec
from amino.test import temp_dir


class Subsyncer_(DBSpec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        self._subject = Subsyncer(self._releases)
        self._monitor = self._releases.all[0]

    def handle_an_existing_subtitle(self):
        flexmock(subsync).should_receive('get_episode')
        flexmock(Subsyncer).should_receive('_write_sub').once()
        self._monitor = self._releases.all[0]
        self._subject._handle(self._monitor)

    def handle_a_missing_subtitle(self):
        Config.override('get', subtitle_retry_coefficient=1./30.)
        release = self._monitor.release
        self._monitor.archived = True
        (flexmock(subsync)
            .should_receive('get_episode')
            .and_raise(NoSubsForEpisode, release.name, release.season,
                       release.episode)
            .and_raise(NoSubsForEpisode, release.name, release.season,
                       release.episode)
            .and_return())
        flexmock(Subsyncer).should_receive('_write_sub').once()
        self._subject._handle(self._monitor)
        self._monitor.subtitle_failures.should.equal(1)
        self._subject._handle(self._monitor)
        self._monitor.subtitle_failures.should.equal(2)
        self._subject._qualify(self._monitor).should.be.false
        time.sleep(4)
        self._subject._qualify(self._monitor).should.be.true
        self._subject._handle(self._monitor)

    def excluded_series(self):
        Config.override('get', sub_exclude=['series1'])
        one = self._releases[0]
        two = self._releases[2]
        one.archived = True
        two.archived = True
        self._subject._qualify(one).should_not.be.ok
        self._subject._qualify(two).should.be.ok

    def write_a_subtitle(self):
        release = self._monitor.release
        name = release.name
        season = release.season
        episode = release.episode
        fname = '{}_{:0>2}x{:0>2}.srt'.format(name, season, episode)
        Config.override('series', series_dir=temp_dir('get',
                                                              'subsyncer',
                                                              'series'))
        info = SubtitleMetadata(name, season, episode)
        subtitle = Subtitle(info, 'group', 'dummy', False)
        flexmock(subtitle).should_receive('content').and_return('success')
        self._subject._write_sub(self._monitor, subtitle)
        sub_path = (temp_dir('get', 'subsyncer', 'series') /
                    name / 's{}'.format(season) / 'sub' / fname)
        sub_path.read_text().should.equal('success')

__all__ = ['Subsyncer_']
