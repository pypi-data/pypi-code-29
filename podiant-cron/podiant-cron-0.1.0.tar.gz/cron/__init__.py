from apscheduler.schedulers.blocking import BlockingScheduler
from django_rq import enqueue
from django.conf import settings
from imp import find_module
from importlib import import_module


__version__ = '0.1.0'


scheduler = BlockingScheduler()


def interval(**kwargs):
    def wrapper(f):
        scheduler.add_job(
            func=enqueue,
            args=[f],
            trigger='interval',
            **kwargs
        )

        return f

    return wrapper


def scheduled(**kwargs):
    def wrapper(f):
        scheduler.add_job(
            func=enqueue,
            args=[f],
            trigger='cron',
            **kwargs
        )

        return f

    return wrapper


def autodiscover():
    for app in settings.INSTALLED_APPS:
        import_module(app)
        name = '%s.cron' % app

        try:
            import_module(name)
        except ImportError as ex:
            try:
                find_module(name)
            except ImportError:
                continue

            raise ex
