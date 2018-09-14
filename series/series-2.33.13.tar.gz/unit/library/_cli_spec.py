import shutil
import os

from golgi import Config
from amino.test import temp_dir

from series.library import SeriesLibraryD

from unit.library._support.spec import Spec


class _CLI(Spec):

    def setup(self, *a, **kw):
        super().setup(*a, allow_files=True, **kw)

    def run_the_daemon(self):
        lib_dir = temp_dir('library', 'cli')
        shutil.copy(os.path.expanduser('~/.local/share/series/library.db'), str(lib_dir))
        Config.override('library', db_path=lib_dir / 'library.db', rest_api_port=8111)
        Config.override('player', player_type='mpv')
        daemon = SeriesLibraryD()
        daemon.rest_api.app.config['TESTING'] = True
        daemon.run()

__all__ = ('_CLI',)
