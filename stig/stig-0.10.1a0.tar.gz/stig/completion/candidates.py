# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details
# http://www.gnu.org/licenses/gpl-3.0.txt

from ..logging import make_logger
log = make_logger(__name__)

from ..singletons import (localcfg, remotecfg)
from ..singletons import cmdmgr
from ..utils import usertypes


class Candidates(tuple):
    """
    
    """
    def __new__(cls, *candidates, tail=' '):
        obj = super().__new__(cls, candidates)
        obj.tail = tail
        return obj

    def __repr__(self):
        return 'Canididates(%s, tail=%r)' % (
            ', '.join(repr(c) for c in self),
            self.tail)


def commands():
    return Candidates(*(cmdcls.name for cmdcls in cmdmgr.active_commands))


from itertools import chain
def settings():
    return Candidates(*(chain(
        localcfg,
        ('srv.' + name for name in remotecfg)
    )))


def values(name, current_value=''):
    log.debug('Getting value candidates for setting %r with current value %r', name, current_value)
    # Get setting from localcfg or remotecfg
    if name in localcfg:
        setting = localcfg[name]
    elif name.startswith('srv.') and name[4:] in remotecfg:
        setting = remotecfg[name[4:]]
    else:
        return Candidates()

    log.debug('Setting is a %r: %r', type(setting), setting)
    # Get candidates depending on what kind of setting it is (bool, option, etc)
    if isinstance(setting, usertypes.Option):
        return Candidates(setting.options)
    elif isinstance(setting, usertypes.Tuple):
        sep = setting.sep.strip()
        cv = current_value.rstrip(sep)
        cands = []

        items = tuple(item for item in current_value.split(sep))
        log.debug('Items: %r', items)
        current_item = items[-1]
        log.debug('Current items: %r', current_item)


        for opt in setting.options:
            if opt.startswith(current_item):
                missing_part = opt[len(current_item):]
                cands.append(current_value + missing_part)

        return Candidates(*cands, tail=',')

    return Candidates()
