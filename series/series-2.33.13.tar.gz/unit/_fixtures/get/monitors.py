from datetime import datetime
import itertools

from series.get.model.release import ReleaseFactory, Release, ReleaseMonitor


def monitors(data, links, torrents=None):
    releases = [Release(**epi) for epi in data]
    torr = [[]] * len(releases) if torrents is None else torrents
    return map(ReleaseFactory().monitor, releases, links, torr)


def empty_monitors(data):
    releases = [Release(**epi) for epi in data]
    return [ReleaseMonitor(r) for r in releases]


def monitors_1():
    release_data = [
        dict(title='series1_s01e05', name='series1',
             group='guppy', season=1, episode=5, is_series=True,
             resolution='1080p', airdate=datetime.now()),
        dict(title='series1_s04e02', name='series1',
             group='guppy', season=4, episode=2, is_series=True,
             resolution='1080p'),
        dict(title='series2_s02e07', name='series2',
             group='guppy', season=2, episode=7, is_series=True,
             resolution='1080p'),
    ]
    links = [
        ['http://foo.bum/file1a', 'http://foo.bum/file1b'],
        ['http://foo.bum/file2a', 'http://foo.bum/file2b'],
        ['http://foo.bum/file3a', 'http://foo.bum/file3b'],
    ]
    return list(monitors(release_data, links))


def monitors_2():
    epi = dict(title='series1_s01e05', name='series1',
               group='guppy', season=1, episode=5, is_series=True,
               resolution='1080p')
    release_data = [epi, epi]
    links = [
        ['http://foo.bum/file1a'],
        ['http://foo.bum/file1a'],
    ]
    return list(monitors(release_data, links))


def monitors_3():
    release_data = [
        dict(title='series3_s01e05', name='series3',
             group='guppy', season=1, episode=5, is_series=True,
             resolution='1080p'),
    ]
    links = [
        ['http://foo.bum/file1a', 'http://foo.bum/file1b'],
    ]
    return list(monitors(release_data, links))


def monitors_4():
    def rel():
        for episode in range(3, 18):
            yield dict(title='series3_s01e{}'.format(episode), name='series3',
                       group='guppy', season=1, episode=episode,
                       is_series=True, resolution='1080p')
    links = itertools.repeat('http://foo.bum/file1a')
    return list(monitors(list(rel()), links))
