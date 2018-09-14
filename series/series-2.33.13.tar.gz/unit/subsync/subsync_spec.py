import os
import re
from pathlib import Path

import sure  # NOQA
from flexmock import flexmock

import requests

from golgi import Config
from amino.test import load_fixture, temp_dir, temp_path

from series import subsync
import series
from series import SubtitleMetadata
from series.subsync import Subtitle, target_episodes, HTMLParser

from unit._support.spec import Spec


class SubsyncerSpec(Spec):

    def setup(self, *a, **kw):
        super().setup(*a, configs=['series.subsync'], **kw)
        Config.override('subsync', base_url='http://fakesubs.com')

    def download_a_subtitle_file(self):
        sub_page = load_fixture('subsync', 'house_8x1_sub_page')
        subtitles = load_fixture('subsync', 'house_8x1_sub')
        (flexmock(subsync.SubtitleHTTPHandler).should_receive('get')
         .with_args('serie/house/8/1/1')
         .and_return(sub_page))
        (flexmock(subsync.SubtitleHTTPHandler).should_receive('get')
         .with_args(re.compile('original'))
         .and_return(subtitles))
        path = Path('/home/media/video/series/house/s8/house_08x01.mkv')
        data = series.EpisodeMetadataFactory().from_filename(path)
        sub = subsync.subsync_episode(data, write=False)
        sub.hearing_impaired.should.be.false
        sub._content.should.be.none
        sub.content.should_not.be.none
        sub.content.should.contain('Friday the 10th')

    def write_a_subtitle_file(self):
        Config.override('series', series_dir=temp_dir('subsync', 'series'))
        (flexmock(requests).should_receive('get')
         .and_return(flexmock(text='subtitle content')))
        info = SubtitleMetadata('house', 8, 1)
        sub = Subtitle(info, 'group', 'dummy', False)
        sub.write()
        outfile = temp_path('subsync', 'series', 'house', 's8', 'sub',
                            'house_08x01.srt')
        with outfile.open() as sub_file:
            sub_file.read().should.equal('subtitle content')
        outfile.unlink()

    def select_target_subtitles(self):
        vids = [2, 4, 6, 8, 9, 10, 11, 12]
        subs = [4, 8, 9, 10]
        Config.override('subsync', episodes=[], only_latest=True)
        target_episodes(vids, subs).should.equal([11, 12])
        Config.override('subsync', episodes=[], only_latest=False)
        target_episodes(vids, subs).should.equal([2, 6, 11, 12])
        Config.override('subsync', episodes=[3, 10])
        target_episodes(vids, subs).should.equal([3, 10])

    def url_map(self):
        Config.override('subsync', series_url_map=dict(series1='alt_spelling'))
        (flexmock(subsync.SubtitleHTTPHandler).should_receive('get')
         .with_args('serie/alt_spelling/1/1/1')
         .and_return('success'))
        flexmock(HTMLParser).should_receive('_parse').with_args('success')
        path = Path('series1_01x01.mkv')
        data = series.EpisodeMetadataFactory().from_filename(path)
        subsync.subsync_episode(data, write=False)
        (flexmock(subsync.SubtitleHTTPHandler).should_receive('get')
         .with_args('serie/series2/1/1/1')
         .and_return('success'))
        path = Path('series2_01x01.mkv')
        data = series.EpisodeMetadataFactory().from_filename(path)
        subsync.subsync_episode(data, write=False)

__all__ = ('SubsyncerSpec',)
