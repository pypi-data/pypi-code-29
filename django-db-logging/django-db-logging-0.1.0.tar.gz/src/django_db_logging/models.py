# -*- coding: utf-8 -*-
import datetime
import json
import logging
import os
import sys
import traceback
from logging import LogRecord

from django.db import models, connections
from django.db.transaction import atomic

from .logging import logger
from .settings import config

LOG_LEVELS = (
    (logging.NOTSET, logging._levelToName[logging.NOTSET]),
    (logging.CRITICAL, logging._levelToName[logging.CRITICAL]),
    (logging.ERROR, logging._levelToName[logging.ERROR]),
    (logging.WARNING, logging._levelToName[logging.WARNING]),
    (logging.INFO, logging._levelToName[logging.INFO]),
    (logging.DEBUG, logging._levelToName[logging.DEBUG]),)

PLAIN_RECORD = LogRecord("name", "level", "pathname", "lineno", "msg", None, None)

KNOWN_FIELDS = ("message",) + tuple(PLAIN_RECORD.__dict__.keys())


class RecordManager(models.Manager):
    def truncate(self):
        connection = connections[self.db]
        cursor = connection.cursor()
        cursor.execute('TRUNCATE TABLE "{0}"'.format(self.model._meta.db_table))

    def cleanup(self):
        with atomic():
            keep = Record.objects.all().order_by('-id').values_list('id', flat=True)[:config.MAX_LOG_ENTRIES]
            Record.objects.exclude(id__in=keep).delete()


class Record(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    logger = models.CharField(max_length=200, blank=True, null=True, db_index=True)
    level = models.PositiveIntegerField(choices=LOG_LEVELS,
                                        default=logging.ERROR, blank=True, db_index=True)

    message = models.TextField(blank=True, null=True)
    formatted = models.TextField(blank=True, null=True)
    server_name = models.CharField(max_length=128, db_index=True)

    pathname = models.TextField(blank=True, null=True)
    lineno = models.IntegerField(blank=True, null=True)

    filename = models.TextField(blank=True, null=True)
    module = models.TextField(blank=True, null=True)
    func_name = models.TextField(blank=True, null=True)
    process = models.TextField(blank=True, null=True)

    traceback = models.TextField(blank=True, null=True)
    exc_type = models.TextField(blank=True, null=True)

    extra = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ("timestamp", "id")
        get_latest_by = 'id'

    objects = RecordManager()

    def __str__(self):
        return '<Record: %s, [%s] %s:%s, "%s">' % (self.logger, self.get_level_display(),
                                                   self.pathname, self.lineno, self.message)

    def extras(self):
        return json.loads(self.extra)

    @staticmethod
    def log_record(record: LogRecord, formatted: str = None):
        try:
            exc_info = {}
            extras = {k: str(v) for k, v in record.__dict__.items() if k not in KNOWN_FIELDS}

            if record.exc_info:
                exception, tb = record.exc_info[1:3]
                if not exception:
                    exc_type, exception, tb = sys.exc_info()
                else:
                    exc_type = exception.__class__
                if exc_type:
                    exc_info.update({'traceback': "\n".join(traceback.format_tb(tb)),
                                     'exc_type': exc_type.__name__})

                if config.USE_CRASHLOG:
                    try:
                        from crashlog.middleware import process_exception
                        process_exception(exception)
                    except ImportError:
                        pass

            Record.objects.create(
                timestamp=datetime.datetime.fromtimestamp(record.created),
                logger=record.name,
                level=record.levelno,
                message=record.getMessage(),
                formatted=formatted,
                pathname=record.pathname,
                filename=os.path.abspath(record.filename),
                module=record.module,
                func_name=record.funcName,
                lineno=record.lineno,
                process=record.process,
                extra=json.dumps(extras),
                **exc_info
            )
        except Exception as e:
            logger.exception(e)
