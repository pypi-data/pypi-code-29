# Copyright (C) 2018 Nikita S., Koni Dev Team, All Rights Reserved
# https://github.com/Nekit10/pyloges
#
# This file is part of Pyloges.
#
# Pyloges is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyloges is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pyloges.  If not, see <https://www.gnu.org/licenses/>.

import sys

from pyloges.classes.interfaces.handler import Handler
from pyloges.loglevels import NAMES, ERROR, FATAL


class StdHandler(Handler):
    def print_log(self, msg: str):
        if NAMES[ERROR] in msg or NAMES[FATAL] in msg:
            sys.stderr.write(msg + '\n')
        else:
            print(msg)

    def save(self):
        pass
