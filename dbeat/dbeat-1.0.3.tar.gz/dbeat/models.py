"""Database models."""

from __future__ import absolute_import, unicode_literals
import peewee
import pytz
from datetime import timedelta
from django.db import models
# from django.db.models import signals
from playhouse import signals


def post_save_handler(sender, instance, created):
    print('%s was just saved' % instance)


from celery import schedules
from celery.five import python_2_unicode_compatible
from .database import database_proxy

from .tzcrontab import TzAwareCrontab
from .utils import now, make_aware, timezone_to_tz

# import timezone_field


def handle(str):
    return str


_ = handle

DAYS = 'days'
HOURS = 'hours'
MINUTES = 'minutes'
SECONDS = 'seconds'
MICROSECONDS = 'microseconds'

PERIOD_CHOICES = (
    (DAYS, _('Days')),
    (HOURS, _('Hours')),
    (MINUTES, _('Minutes')),
    (SECONDS, _('Seconds')),
    (MICROSECONDS, _('Microseconds')),
)

SOLAR_SCHEDULES = [(x, _(x)) for x in sorted(schedules.solar._all_events)]


def cronexp(field):
    """Representation of cron expression."""
    return field and str(field).replace(' ', '') or '*'


@python_2_unicode_compatible
class SolarSchedule(peewee.Model):
    """Schedule following astronomical patterns."""

    event = peewee.CharField(
        verbose_name=_('event'), max_length=24, choices=SOLAR_SCHEDULES
    )
    latitude = peewee.DecimalField(
        verbose_name=_('latitude'), max_digits=9, decimal_places=6
    )
    longitude = peewee.DecimalField(
        verbose_name=_('longitude'), max_digits=9, decimal_places=6
    )

    class Meta:
        """Table information."""

        verbose_name = _('solar event')
        verbose_name_plural = _('solar events')
        ordering = ('event', 'latitude', 'longitude')
        unique_together = ('event', 'latitude', 'longitude')
        database = database_proxy

    @property
    def schedule(self):
        return schedules.solar(self.event,
                               self.latitude,
                               self.longitude,
                               nowfun=lambda: make_aware(now()))

    @classmethod
    def from_schedule(cls, schedule):
        spec = {'event': schedule.event,
                'latitude': schedule.lat,
                'longitude': schedule.lon}
        try:
            return cls.get(**spec)
        except peewee.DoesNotExist:
            return cls(**spec)

    def __str__(self):
        return '{0} ({1}, {2})'.format(
            self.get_event_display(),
            self.latitude,
            self.longitude
        )


@python_2_unicode_compatible
class IntervalSchedule(peewee.Model):
    """Schedule executing every n seconds."""

    DAYS = DAYS
    HOURS = HOURS
    MINUTES = MINUTES
    SECONDS = SECONDS
    MICROSECONDS = MICROSECONDS

    PERIOD_CHOICES = PERIOD_CHOICES

    every = peewee.IntegerField(verbose_name=_('every'), null=False)
    period = peewee.CharField(
        verbose_name=_('period'), max_length=24, choices=PERIOD_CHOICES,
    )

    class Meta:
        """Table information."""

        verbose_name = _('interval')
        verbose_name_plural = _('intervals')
        ordering = ['period', 'every']
        database = database_proxy

    @property
    def schedule(self):
        return schedules.schedule(
            timedelta(**{self.period: self.every}),
            nowfun=lambda: make_aware(now())
        )

    @classmethod
    def from_schedule(cls, schedule, period=SECONDS):
        every = max(schedule.run_every.total_seconds(), 0)
        return cls.get_or_create(every=every, period=period)[0]

    def __str__(self):
        if self.every == 1:
            return _('every {0.period_singular}').format(self)
        return _('every {0.every} {0.period}').format(self)

    @property
    def period_singular(self):
        return self.period[:-1]

    def is_due(self, last_run_at):
        pass
        # """Calculate when the next run will take place.

        # Return tuple of (is_due, next_time_to_check).
        # The last_run_at argument needs to be timezone aware.

        # """
        # convert last_run_at to the schedule timezone
        # last_run_at = last_run_at.astimezone(self.tz)

        # rem_delta = self.remaining_estimate(last_run_at)
        # rem = max(rem_delta.total_seconds(), 0)
        # due = rem == 0
        # if due:
        #     rem_delta = self.remaining_estimate(self.now())
        #     rem = max(rem_delta.tota


@python_2_unicode_compatible
class CrontabSchedule(peewee.Model):
    """Timezone Aware Crontab-like schedule."""

    #
    # The worst case scenario for day of month is a list of all 31 day numbers
    # '[1, 2, ..., 31]' which has a length of 115. Likewise, minute can be
    # 0..59 and hour can be 0..23. Ensure we can accomodate these by allowing
    # 4 chars for each value (what we save on 0-9 accomodates the []).
    # We leave the other fields at their historical length.
    #
    minute = peewee.CharField(verbose_name=_(
        'minute'), max_length=60 * 4, default='*')
    hour = peewee.CharField(verbose_name=_(
        'hour'), max_length=24 * 4, default='*')
    day_of_week = peewee.CharField(
        verbose_name=_('day of week'), max_length=64, default='*',
    )
    day_of_month = peewee.CharField(
        verbose_name=_('day of month'), max_length=31 * 4, default='*',
    )
    month_of_year = peewee.CharField(
        verbose_name=_('month of year'), max_length=64, default='*',
    )

    timezone = peewee.CharField(
        verbose_name=_('timezone'), max_length=64, default='*',
    )

    class Meta:
        """Table information."""

        verbose_name = _('crontab')
        verbose_name_plural = _('crontabs')
        ordering = ['month_of_year', 'day_of_month',
                    'day_of_week', 'hour', 'minute', 'timezone']
        database = database_proxy

    def __str__(self):
        return 'CrontabModel:{0} {1} {2} {3} {4} (m/h/d/dM/MY) {5}'.format(
            cronexp(self.minute), cronexp(self.hour),
            cronexp(self.day_of_week), cronexp(self.day_of_month),
            cronexp(self.month_of_year), str(self.timezone)
        )

    @property
    def schedule(self):
        print(self.timezone)
        return TzAwareCrontab(
            minute=self.minute,
            hour=self.hour, day_of_week=self.day_of_week,
            day_of_month=self.day_of_month,
            month_of_year=self.month_of_year,
            tz=timezone_to_tz(str(self.timezone))
        )

    @classmethod
    def from_schedule(cls, schedule):
        spec = {'minute': schedule._orig_minute,
                'hour': schedule._orig_hour,
                'day_of_week': schedule._orig_day_of_week,
                'day_of_month': schedule._orig_day_of_month,
                'month_of_year': schedule._orig_month_of_year,
                'timezone': schedule.tz.zone
                }
        return cls.get_or_create(**spec)[0]


class PeriodicTasks(peewee.Model):
    """Helper table for tracking updates to periodic tasks."""

    ident = peewee.SmallIntegerField(default=1, primary_key=True, unique=True)
    last_update = peewee.DateTimeField(null=False)

    # objects = managers.ExtendedManager()

    class Meta:
        database = database_proxy

    @classmethod
    def changed(cls, instance, **kwargs):
        if not instance.no_changes:
            cls.update_changed()

    @classmethod
    def update_changed(cls, **kwargs):
        cls.update_or_create(ident=1, defaults={'last_update': now()})

    @classmethod
    def update_or_create(cls, **kwargs):
        print("update_or_create")
        try:
            with self.database.atomic():
                return cls.create(**kwargs)
        except peewee.IntegrityError:
            # `username` is a unique column, so this username already exists,
            # making it safe to call .get().
            defaults = kwargs.pop("defaults", {})
            with self.database.atomic():
                instance = cls.get(**kwargs)
                for key, value in defaults.items():
                    setattr(instance, key, value)
                instance.save()
                return instance

    @classmethod
    def last_change(cls):
        try:
            return cls.get(ident=1).last_update
        except peewee.DoesNotExist:
            pass


@python_2_unicode_compatible
class PeriodicTask(peewee.Model):
    """Model representing a periodic task."""

    name = peewee.CharField(
        verbose_name=_('name'), max_length=200, unique=True,
        help_text=_('Useful description'),
    )
    task = peewee.CharField(verbose_name=_('task name'), max_length=200)
    interval = peewee.ForeignKeyField(
        IntervalSchedule, on_delete='CASCADE',
        null=True,  verbose_name=_('interval'),
    )
    crontab = peewee.ForeignKeyField(
        CrontabSchedule, on_delete='CASCADE', null=True,
        verbose_name=_('crontab'), help_text=_('Use one of interval/crontab'),
    )
    solar = peewee.ForeignKeyField(
        SolarSchedule, on_delete='CASCADE', null=True,
        verbose_name=_('solar'), help_text=_('Use a solar schedule')
    )
    args = peewee.TextField(
        verbose_name=_('Arguments'),  default='[]',
        help_text=_('JSON encoded positional arguments'),
    )
    kwargs = peewee.TextField(
        verbose_name=_('Keyword arguments'),  default='{}',
        help_text=_('JSON encoded keyword arguments'),
    )
    queue = peewee.CharField(
        verbose_name=_('queue'), max_length=200, null=True, default=None,
        help_text=_('Queue defined in CELERY_TASK_QUEUES'),
    )
    exchange = peewee.CharField(
        verbose_name=_('exchange'), max_length=200, null=True, default=None,
    )
    routing_key = peewee.CharField(
        verbose_name=_('routing key'), max_length=200, null=True, default=None,
    )
    expires = peewee.DateTimeField(
        verbose_name=_('expires'), null=True,
    )
    one_off = peewee.BooleanField(
        verbose_name=_('one-off task'), default=False,
    )
    start_time = peewee.DateTimeField(
        verbose_name=_('start_time'), null=True,
    )
    enable = peewee.BooleanField(
        verbose_name=_('enable'), default=True,
    )
    modified = peewee.BooleanField(
        verbose_name=_('modified'), default=True,
    )
    last_run_at = peewee.DateTimeField(null=True)
    total_run_count = peewee.IntegerField(default=0)
    date_changed = peewee.DateTimeField(null=True)
    description = peewee.TextField(verbose_name=_('description'), null=True)

    no_changes = False

    class Meta:
        """Table information."""

        verbose_name = _('periodic task')
        verbose_name_plural = _('periodic tasks')
        database = database_proxy

    @classmethod
    def enabled(cls):
        aa = cls.select().where(cls.enable == True)
        return aa

    @classmethod
    def get_new_add(cls, name_list=None):
        if name_list is None:
            name_list = []
        aa = cls.select().where((cls.enable == True)
                                & (cls.modified == True))
        return aa

    @classmethod
    def exist(cls, name=None):
        if name is None:
            name = ""
        aa = cls.select().where(cls.name == name).count()
        if aa > 0:
            return True
        else:
            return False

    @classmethod
    def update_or_create(cls, **kwargs):
        defaults = kwargs.pop("defaults", {})
        print("update_or_create", kwargs,
              defaults, dir(kwargs), dir(defaults))
        result = None
        try:

            with cls._meta.database.atomic():
                kwargs.update(defaults)
                print("try to create,", kwargs)
                try:
                    result = cls.create(**kwargs)
                except Exception as tmp:
                    print("create_successful,", tmp)
        except peewee.IntegrityError:
            # `username` is a unique column, so this username already exists,
            # making it safe to call .get().
            with cls._meta.database.atomic():
                instance = cls.get(**kwargs)
                for key, value in defaults.items():
                    setattr(instance, key, value)
                instance.save()
                result = instance
        except Exception as tmp:
            print("update_or_create_error", tmp)
        if result is not None:
            print("success_full update_or_create", result)
        return result

    def validate_unique(self, *args, **kwargs):
        super(PeriodicTask, self).validate_unique(*args, **kwargs)
        if not self.interval and not self.crontab and not self.solar:
            raise ValidationError({
                'interval': [
                    'One of interval, crontab, or solar must be set.'
                ]
            })
        if self.interval and self.crontab and self.solar:
            raise ValidationError({
                'crontab': [
                    'Only one of interval, crontab, or solar must be set'
                ]
            })

    def save(self, *args, **kwargs):
        print("save", args, kwargs)
        self.exchange = self.exchange or None
        self.routing_key = self.routing_key or None
        self.queue = self.queue or None
        if not self.enabled:
            self.last_run_at = None
        super(PeriodicTask, self).save(*args, **kwargs)

    def __str__(self):
        fmt = '{0.name}: {{no schedule}}'
        if self.interval:
            fmt = '{0.name}: {0.interval}'
        if self.crontab:
            fmt = '{0.name}: {0.crontab}'
        if self.solar:
            fmt = '{0.name}: {0.solar}'
        return fmt.format(self)

    @property
    def schedule(self):
        if self.interval:
            return self.interval.schedule
        if self.crontab:
            return self.crontab.schedule
        if self.solar:
            return self.solar.schedule
