import logging
from logging import Handler


class DBHandler(Handler):
    def emit(self, record):
        from .models import Record
        Record.log_record(record, self.format(record))


class AsyncDBHandler(Handler):

    def __init__(self, level=logging.NOTSET):
        super().__init__(level)
        from .threadqueue import worker
        self._worker = worker

    def emit(self, record):
        self._worker.queue((record, self.format(record)))
