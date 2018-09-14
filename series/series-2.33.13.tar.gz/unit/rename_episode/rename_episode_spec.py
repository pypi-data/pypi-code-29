import sure

from series.rename_episode import rename
from unit._support.spec import Spec


class RenameEpisode_(Spec):

    def setup(self, *a, **kw):
        super().setup(*a, configs=['series'], **kw)

    def it_should_rename_episodes_correctly(self):
        examples = [['-dexter.s04e01.720p.hdtv.x264.mkv', 'dexter_04x01.mkv'],
                    ['Dexter.S04E06.720p.X264.mkv', 'dexter_04x06.mkv'],
                    ['Dexter.04x06.mkv', 'dexter_04x06.mkv'],
                    ['dexter_413-asdfkjhdf.mkv', 'dexter_04x13.mkv'],
                    ['414-asdfkjhdf.mkv', '_04x14.mkv'],
                    ['how.i.met.your.mother.0512.hdtv.xvid-notv.avi',
                     'how_i_met_your_mother_05x12.avi'],
                    ['Zeries_05E09.mp4', 'zeries_05x09.mp4'],
                    ['Black_Books_0104_The_Blackout.avi',
                     'black_books_01x04.avi'],
                    ['Star.Trek.DS9.S04E01.avi', 'star_trek_ds9_04x01.avi'],
                    ['burn_notice_s01_e10.avi', 'burn_notice_01x10.avi']]
        for source, target in examples:
            rename(source).should.equal(target)
