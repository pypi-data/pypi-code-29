# -*- coding:utf-8 -*-
import logging


class TTYHandler(logging.StreamHandler):

    def format(self, record):
        if hasattr(self.stream, "isatty"):
            record._is_tty = self.stream.isatty()
        else:
            record._is_tty = False
        s = super(TTYHandler, self).format(record)
        del record._is_tty
        return s