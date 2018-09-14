from pathlib import Path
import sure  # NOQA

import series
from golgi import Config

from unit._support.spec import Spec


class EpisodeMetadata_(Spec):

    def setup(self, *a, **kw):
        super().setup(*a, configs=['series'], **kw)

    def parse_a_series_file_name(self):
        path = Path('/home/media/video/series/house/s8/house_08x01.mkv')
        fact = series.EpisodeMetadataFactory()
        md = fact.from_filename(path)
        md.series.should.equal('house')
        md.local_path.should.equal('house/s8/house_08x01.mkv')
        path = Path('house_08x01.srt')
        fact = series.EpisodeMetadataFactory()
        md = fact.from_filename(path)
        md.series.should.equal('house')
        md.local_path.should.equal('house/s8/sub/house_08x01.srt')

    def parse_a_series_file_name_custom_rex(self):
        Config.override(
            'series',
            enumeration_regex=('/(?P<name>[^/]*)/(?P<season>\d+)/' +
                               '(?P<episode>\d+).*\.mkv')
        )
        path = Path('/home/media/video/series/house/8/01.mkv')
        fact = series.EpisodeMetadataFactory()
        md = fact.from_filename(path)
        md.series.should.equal('house')
        md.local_path.should.equal('house/s8/house_08x01.mkv')

    def parse_a_series_file_name_100(self):
        path = Path('/home/media/video/series/house/s8/house_08x100.mkv')
        fact = series.EpisodeMetadataFactory()
        md = fact.from_filename(path)
        md.series.should.equal('house')
        md.local_path.should.equal('house/s8/house_08x100.mkv')
        path = Path('house_08x100.srt')
        fact = series.EpisodeMetadataFactory()
        md = fact.from_filename(path)
        md.series.should.equal('house')
        md.local_path.should.equal('house/s8/sub/house_08x100.srt')
