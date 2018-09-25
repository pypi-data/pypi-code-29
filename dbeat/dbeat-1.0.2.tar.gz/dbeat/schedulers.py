"""Beat Scheduler Implementation."""
from __future__ import absolute_import, unicode_literals

import logging
import datetime
import time
from multiprocessing.util import Finalize

from celery import current_app
from celery import schedules
from celery.beat import Scheduler, ScheduleEntry, event_t
from celery.five import values, items
from celery.utils.encoding import safe_str, safe_repr
from celery.utils.log import get_logger
from celery.utils.time import maybe_make_aware
from kombu.utils.json import dumps, loads
from heapq import heappush
from bisect import bisect
from .database import database_proxy

from .models import (
    PeriodicTask, PeriodicTasks,
    CrontabSchedule, IntervalSchedule,
    SolarSchedule,
)
from .utils import make_aware

try:
    from celery.utils.time import is_naive
except ImportError:  # pragma: no cover
    from celery.utils.timeutils import is_naive  # noqa

# This scheduler must wake up more frequently than the
# regular of 5 minutes because it needs to take external
# changes to the schedule into account.
DEFAULT_MAX_INTERVAL = 5  # seconds

ADD_ENTRY_ERROR = """\
Cannot add entry %r to database schedule: %r. Contents: %r
"""

logger = get_logger(__name__)
debug, info = logger.debug, logger.info


class ModelEntry(ScheduleEntry):
    """Scheduler entry taken from database row."""

    model_schedules = (
        (schedules.crontab, CrontabSchedule, 'crontab'),
        (schedules.schedule, IntervalSchedule, 'interval'),
        (schedules.solar, SolarSchedule, 'solar'),
    )
    save_fields = ['last_run_at', 'total_run_count', 'no_changes']

    def __init__(self, model, app=None):
        """Initialize the model entry."""
        self.app = app or current_app._get_current_object()
        self.name = model.name
        self.task = model.task
        try:
            self.schedule = model.schedule
        except model.DoesNotExist:
            logger.error(
                'Disabling schedule %s that was removed from database',
                self.name,
            )
            self._disable(model)
        try:
            self.args = loads(model.args or '[]')
            self.kwargs = loads(model.kwargs or '{}')
        except ValueError as exc:
            logger.exception(
                'Removing schedule %s for argument deseralization error: %r',
                self.name, exc,
            )
            self._disable(model)

        self.options = {
            'queue': model.queue,
            'exchange': model.exchange,
            'routing_key': model.routing_key,
            'expires': model.expires,
        }
        self.total_run_count = model.total_run_count
        self.model = model

        if not model.last_run_at:
            model.last_run_at = self._default_now()
        self.last_run_at = make_aware(model.last_run_at)

    def __lt__(self, entry):
        return self.name < entry.name

    def __gt__(self, entry):
        return self.name > entry.name

    def __eq__(self, entry):
        return self.name == entry.name

    def _disable(self, model):
        model.no_changes = True
        model.enabled = False
        model.save()

    def is_due(self):
        if not self.model.enabled:
            return False, 5.0   # 5 second delay for re-enable.

        # START DATE: only run after the `start_time`, if one exists.
        if self.model.start_time is not None:
            if maybe_make_aware(self._default_now()) < self.model.start_time:
                # The datetime is before the start date - don't run.
                _, delay = self.schedule.is_due(self.last_run_at)
                return False, delay  # use original delay for re-check

        # ONE OFF TASK: Disable one off tasks after they've ran once
        if self.model.one_off and self.model.enabled \
                and self.model.total_run_count > 0:
            self.model.enabled = False
            self.model.total_run_count = 0  # Reset
            self.model.save()
            return False, None  # Don't recheck

        return self.schedule.is_due(self.last_run_at)

    def _default_now(self):
        # now = self.app.now()
        now = datetime.datetime.now()
        return now
        # The PyTZ datetime must be localised for the Django-Celery-Beat
        # scheduler to work. Keep in mind that timezone arithmatic
        # with a localized timezone may be inaccurate.
        # return now.tzinfo.localize(now.replace(tzinfo=None))

    def __next__(self):
        # self.model.last_run_at = self.app.now()
        self.model.last_run_at = self._default_now()
        self.model.total_run_count += 1
        self.model.no_changes = True
        return self.__class__(self.model)
    next = __next__  # for 2to3

    def save(self):
        # Object may not be synchronized, so only
        # change the fields we care about.
        obj = type(self.model).get(id=self.model.id)
        for field in self.save_fields:
            setattr(obj, field, getattr(self.model, field))
        obj.save()

    @classmethod
    def to_model_schedule(cls, schedule):
        for schedule_type, model_type, model_field in cls.model_schedules:
            schedule = schedules.maybe_schedule(schedule)
            if isinstance(schedule, schedule_type):

                model_schedule = model_type.from_schedule(schedule)
                model_schedule.save()
                return model_schedule, model_field
        raise ValueError(
            'Cannot convert schedule type {0!r} to model'.format(schedule))

    @classmethod
    def from_entry(cls, name, app=None, **entry):
        try:
            result = PeriodicTask.update_or_create(
                name=name, defaults=cls._unpack_fields(**entry),
            )
        except Exception as tmp:
            debug(tmp)
            result = None
        return cls(result, app=app)

    @classmethod
    def _unpack_fields(cls, schedule,
                       args=None, kwargs=None, relative=None, options=None,
                       **entry):
        try:
            model_schedule, model_field = cls.to_model_schedule(schedule)
        except Exception as tmp:
            debug(tmp)
            print("tmp", tmp, schedule)
        entry.update(
            {model_field: model_schedule},
            args=dumps(args or []),
            kwargs=dumps(kwargs or {}),
            **cls._unpack_options(**options or {})
        )
        print("tmp entry", entry, dir(entry))
        return entry

    @classmethod
    def _unpack_options(cls, queue=None, exchange=None, routing_key=None,
                        **kwargs):
        return {
            'queue': queue,
            'exchange': exchange,
            'routing_key': routing_key,
        }

    def __repr__(self):
        return '<ModelEntry: {0} {1}(*{2}, **{3}) {4}>'.format(
            safe_str(self.name), self.task, safe_repr(self.args),
            safe_repr(self.kwargs), self.schedule,
        )


class DatabaseScheduler(Scheduler):
    """Database-backed Beat Scheduler."""

    Entry = ModelEntry
    Model = PeriodicTask
    Changes = PeriodicTasks

    _schedule = None
    _last_timestamp = None
    _initial_read = False
    sync_every = 60

    def __init__(self, *args, **kwargs):
        database_proxy.initialize(kwargs['app'].database)
        self.database_proxy = database_proxy
        """Initialize the database scheduler."""
        self._dirty = set()
        Scheduler.__init__(self, *args, **kwargs)
        self._finalize = Finalize(self, self.sync, exitpriority=5)
        self.max_interval = (
            kwargs.get('max_interval') or
            self.app.conf.beat_max_loop_interval or
            DEFAULT_MAX_INTERVAL)
        self.database_proxy.create_tables([
            PeriodicTask, PeriodicTasks,
            CrontabSchedule, IntervalSchedule,
            SolarSchedule], safe=True)

    def setup_schedule(self):
        self.install_default_entries(self.schedule)
        self.update_from_dict(self.app.conf.beat_schedule)

    def all_as_schedule(self):
        debug('DatabaseScheduler: Fetching database schedule')
        s = {}
        for model in self.Model.enabled():
            try:
                s[model.name] = self.Entry(model, app=self.app)
            except Exception as tmp:
                logger.exception('all_as_schedule %r', tmp)
        return s

    def delete_out_dated_task(self):
        remove_list = []
        if self._heap:
            for i in self._heap:
                if not self.Model.exist(name=i.entry.name):
                    remove_list.append(i)
        for i in remove_list:
            self._heap.remove(i)

    def get_new_tasks(self):
        debug('DatabaseScheduler: remove non exist data from beat')
        self.delete_out_dated_task()
        debug('DatabaseScheduler: decide whether have new record or not')

        def _when(entry, next_time_to_run):
            mktime = time.mktime
            return (mktime(entry.schedule.now().timetuple()) +
                    (self.adjust(next_time_to_run) or 0))
        if self._heap is None:
            self._heap = []
        if self._schedule is None:
            self._schedule = {}
        query = self.Model.get_new_add(list(self._schedule.keys()))
        if query.count() > 0:
            info('DatabaseScheduler: found new record in database')
            s = {}
            for model in query:
                try:
                    tmp_entry = self.Entry(model, app=self.app)
                    self._heap.append(
                        event_t(_when(tmp_entry, tmp_entry.is_due()[1]) or 0, 5,
                                tmp_entry))
                    s[model.name] = tmp_entry
                    model.modified = False
                    model.save()
                except Exception as tmp:
                    logger.exception('get_new_tasks %r', tmp)
            if s:
                self._schedule.update(s)

    def schedule_changed(self):
        try:
            with self.database_proxy.atomic() as transaction:  # Opens new transaction.
                pass
            last, ts = self._last_timestamp, self.Changes.last_change()
        except DatabaseError as exc:
            logger.exception('Database gave error: %r', exc)
            return False
        try:
            if ts and ts > (last if last else ts):
                return True
        finally:
            self._last_timestamp = ts
        return False

    def reserve(self, entry):
        new_entry = next(entry)
        # Need to store entry by name, because the entry may change
        # in the mean time.
        self._dirty.add(new_entry.name)
        return new_entry

    def sync(self):
        info('Writing entries...')
        _tried = set()
        try:
            with self.database_proxy.atomic() as transaction:  # Opens new transaction.
                while self._dirty:
                    try:
                        name = self._dirty.pop()
                        _tried.add(name)
                        self.schedule[name].save()
                    except Exception as tmp:
                        logger.exception('Database error while sync: %r', exc)
                else:
                    self.schedule
        except Exception as exc:
            self._dirty |= _tried
            logger.exception('Database error while sync: %r', exc)
        info('sync is end ...')

    def update_from_dict(self, mapping):
        s = {}
        for name, entry_fields in items(mapping):
            try:
                try:
                    info("name, entry_fields", name, entry_fields)
                    entry = self.Entry.from_entry(name,
                                                  app=self.app,
                                                  **entry_fields)
                except Exception as tmp:
                    logger.exception("update_from_dict: %r", tmp)
                if entry.model.enabled:
                    s[name] = entry
            except Exception as exc:
                logger.error(ADD_ENTRY_ERROR, name, exc, entry_fields)
        self.schedule.update(s)

    def install_default_entries(self, data):
        entries = {}
        # if self.app.conf.result_expires:
        #     entries.setdefault(
        #         'celery.backend_cleanup', {
        #             'task': 'celery.backend_cleanup',
        #             'schedule': schedules.crontab('*/1', '*', '*'),
        #             'options': {'expires': 12 * 3600},
        #         },
        #     )
        self.update_from_dict(entries)

    @property
    def schedule(self):
        update = False
        if not self._initial_read:
            debug('DatabaseScheduler: initial read')
            update = True
            self._initial_read = True
        elif self.schedule_changed():
            info('DatabaseScheduler: Schedule changed.')
            update = True

        if update:
            self.sync()
            self._schedule = self.all_as_schedule()
            # the schedule changed, invalidate the heap in Scheduler.tick
            self._heap = None
            if logger.isEnabledFor(logging.DEBUG):
                debug('Current schedule:\n%s', '\n'.join(
                    repr(entry) for entry in values(self._schedule)),
                )
        else:
            info('DatabaseScheduler: Detecting new records to Update scheduler.')
            self.get_new_tasks()
        return self._schedule
