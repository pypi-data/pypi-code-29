from ._version import version_info, __version__

from .button_execute import *

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'jupyter-button_execute',
        'require': 'jupyter-button_execute/extension'
    }]
