
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

import platform
import os
import shutil

class Unsupported(Exception):
    pass

class NotAnalytic(Exception):
    pass

class DataError(Exception):
    pass

_OS = platform.system()

root = __path__[0]
user_folder = os.environ.get('EPIC_USER_PATH',
        os.path.join(os.path.expanduser('~'), 'EPIC'))

_defaults_ = {
        'check_interval' : 7200,
        'tolerance' : 1e-2,
        'acceptance_limits' : [0.1, 0.5],
        'sigma_levels' : [1, 2],
        'bins' : 20
        }

color_options = ['tableau', 'xkcd', 'css4', 'base']
for scheme, options in zip(['xkcd', 'css4'], [
    [
    'bright',
    'dark',
    'darkish',
    'very dark',
    'soft',
    'vibrant',
    'ugly',
    'vivid',
    'pastel',
    'pale',
    'neon',
    'off',
    'gold',
    'light',
    'lightish',
    'very light',
    'muted',
    'medium',
    'hot',
    'greyish',
    'faded',
    'electric',
    'dull',
    'dusty',
    'dirty',
    'deep',
    ], [
    'medium',
    'light',
    'dark',
    ]]):
    for option in options:
        color_options.append('%s-%s' % (scheme, option))

pyplot_available_styles = ['default',] + sorted([
        'bmh',
        'dark_background',
        'fivethirtyeight',
        'ggplot',
        'grayscale',
        'Solarize_Light2',
        'seaborn',
        'seaborn-bright',  
        'seaborn-whitegrid',
        'seaborn-dark',
        'seaborn-muted',
        'seaborn-dark-palette',
        'seaborn-pastel',
        'seaborn-white',
        'seaborn-ticks',
        'seaborn-colorblind',
        ])

pyplot_grid_styles = ['default',] + sorted([
        'bmh',
        'dark_background',
        'ggplot',
        'Solarize_Light2',
        'seaborn-bright',  
        'seaborn-colorblind',
        'seaborn-whitegrid',
        'seaborn-muted',
        'seaborn-dark-palette',
        'seaborn-pastel',
        ])
