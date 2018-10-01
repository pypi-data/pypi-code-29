"""A subclass of PullSourceReader that fails, for testing purposes."""
from __future__ import print_function

from builtins import range
from threading import Thread
from time import sleep
from datetime import timedelta
import traceback

from .source_reader import (
    PullSourceReader, IrrecoverableError, SourceDispatcher,
    BrokerConnection, ReaderError)
from assembl.lib import config


class DummyFailingSourceReader(PullSourceReader):
    time_between_reads = timedelta(seconds=1)

    def do_read(self):
        iteration = getattr(self, "iteration", 0)
        print("*** start: %d.%d, %s" % (
            self.source.id, iteration,
            self.source.db.bind.pool._pool.queue))
        self.iteration = iteration + 1
        if not iteration:
            raise ReaderError()
        print("*** end", self.source.id)
        raise IrrecoverableError()


def xtest_source_reader(test_session, discussion):
    from ..models import ContentSource

    class DummyFailingSource(ContentSource):
        __mapper_args__ = {
            'polymorphic_identity': 'dummy_failing_source'
        }

        def make_reader(self):
            return DummyFailingSourceReader(self.id)

    for i in range(20):
        discussion.db.add(DummyFailingSource(
            discussion=discussion, name="dummy reader %d" % (i,)))
    discussion.db.commit()
    url = config.get('celery_tasks.imap.broker')
    conn = BrokerConnection(url)
    source_dispatcher = SourceDispatcher(conn)
    sleep(0.1)
    for source in discussion.sources:
        source_dispatcher.read(source.id)
    sleep(3)
    source_dispatcher.shutdown()
    for source in discussion.sources[:]:
        source.delete()
    discussion.db.commit()
