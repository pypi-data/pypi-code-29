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

import datetime

from pyloges.classes.config import Config
from pyloges.loglevels import NAMES, TRACE, DEBUG, INFO, WARNING, ERROR, FATAL


class Logger:

    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def log(self, msg: str, log_level: int):
        if log_level >= self.config.log_level:
            for handler in self.config.get_handlers():
                handler.print_log(_process_msg(self.config.log_message_format, NAMES[log_level], msg))
                handler.save()

    def trace(self, msg: str):
        self.log(msg, TRACE)

    def t(self, msg: str):
        self.trace(msg)

    def debug(self, msg: str):
        self.log(msg, DEBUG)

    def d(self, msg: str):
        self.debug(msg)

    def info(self, msg: str):
        self.log(msg, INFO)

    def i(self, msg: str):
        self.info(msg)

    def warn(self, msg: str):
        self.log(msg, WARNING)

    def w(self, msg: str):
        self.warn(msg)

    def error(self, msg: str):
        self.log(msg, ERROR)

    def e(self, msg: str):
        self.error(msg)

    def fatal(self, msg: str):
        self.log(msg, FATAL)
        if self.config.exit_on_fatal:
            exit(1)

    def f(self, msg: str):
        self.fatal(msg)


def _process_msg(format_: str, log_level: str, msg: str) -> str:
    tt = datetime.datetime.now().timetuple()

    new_str = format_
    new_str = new_str.replace("{level}", log_level)
    new_str = new_str.replace("%y", str(tt.tm_year))
    new_str = new_str.replace("%M", str(tt.tm_mon))
    new_str = new_str.replace("%d", str(tt.tm_mday))
    new_str = new_str.replace("%h", str(tt.tm_hour))
    new_str = new_str.replace("%m", str(tt.tm_min))
    new_str = new_str.replace("%s", str(tt.tm_sec))
    new_str = new_str.replace("{msg}", msg)

    return new_str
