from envinfo.system import EnvInfo
from envinfo.package import Packages


__all__ = ['EnvInfo', 'Packages']


# Import and add Drives to __all__ declaration if running on Windows
if EnvInfo().system.os == 'Windows':
    from envinfo.drives import Drives
    __all__.append('Drives')
