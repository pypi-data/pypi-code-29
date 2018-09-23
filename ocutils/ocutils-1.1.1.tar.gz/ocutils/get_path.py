'''get_path function definition'''

from pathlib import Path, PurePath


def get_path(file_name):

    '''Get relative path to specified file assuming either development or deployment environment'''

    pkg_name = __name__.split('.')[0]
    dep_name = 'site-packages'

    estr = 'File ' + file_name + ' could not be found: stopping.'

    cdir = Path.cwd()
    parts = PurePath(cdir).parts
    parts = parts[::-1]

    if pkg_name in parts:
        nlev = parts.index(pkg_name)
    elif dep_name in parts:
        nlev = parts.index(dep_name)
    else:
        raise ValueError(estr)

    if nlev == 0:
        rel_path = './'
    elif nlev >= 1:
        rel_path = nlev * '../'
    else:
        raise ValueError(estr)

    if pkg_name in parts:
        rel_path = Path(rel_path) / file_name
    else:
        rel_path = Path(rel_path) / pkg_name / file_name

    if not rel_path.exists():
        raise ValueError(estr)

    return str(rel_path)
