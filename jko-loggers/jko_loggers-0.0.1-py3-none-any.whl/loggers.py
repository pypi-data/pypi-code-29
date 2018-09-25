import logging
import os
import time


class DailyFileHandler(logging.FileHandler):
    def __init__(self, filename, suffix='', date_fmt=None, *args, **kwargs):
        self._filename = filename
        self._suffix = suffix
        self._date_fmt = date_fmt or '%Y%m%d'
        self.mkdir(filename)
        self._day = self.format_today()
        filename = self.filename_on_day(self._day)
        super(DailyFileHandler, self).__init__(filename, *args, **kwargs)

    def format_today(self):
        return time.strftime(self._date_fmt, time.localtime())

    def filename_on_day(self, day):
        return '%s%s%s' % (self._filename, day, self._suffix)

    @staticmethod
    def mkdir(filename):
        folder = os.path.dirname(filename)
        if not os.path.exists(folder):
            os.makedirs(folder)

    def emit(self, record):
        day = self.format_today()
        if self._day != day:
            self._day = day
            if self.stream:
                try:
                    self.flush()
                finally:
                    stream = self.stream
                    self.stream = None
                    if hasattr(stream, "close"):
                        stream.close()
            self.baseFilename = self.filename_on_day(self._day)
        super(DailyFileHandler, self).emit(record)
