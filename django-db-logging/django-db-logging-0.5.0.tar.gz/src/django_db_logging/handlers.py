import logging
from logging import Handler

from django.apps import apps
from django.utils.functional import cached_property


class DBHandler(Handler):

    def __init__(self, model='django_db_logging.Record', level=logging.NOTSET):
        self.model_fqn = model
        super().__init__(level)

    @cached_property
    def model(self):
        m = apps.get_model(self.model_fqn)
        return m

    def emit(self, record):
        self.model.log_record(record, self.format(record))


class AsyncDBHandler(DBHandler):

    def __init__(self, model='django_db_logging.Record', level=logging.NOTSET):
        super().__init__(model, level)
        from .threadqueue import worker
        self._worker = worker

    def emit(self, record):
        self._worker.queue((self.model, record, self.format(record)))
