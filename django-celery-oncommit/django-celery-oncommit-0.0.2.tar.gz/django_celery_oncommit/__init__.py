import celery
from django.db import transaction


def task(*args, **kwargs):
    celery_task = celery.task(*args, **kwargs)

    # rewrite .apply_async
    orig_apply_async = celery_task.apply_async

    def apply_async(*apply_async_args, **apply_async_kwargs):
        transaction.on_commit(lambda: orig_apply_async(*apply_async_args, **apply_async_kwargs))
    celery_task.apply_async = apply_async

    # rewrite .delay
    orig_delay = celery_task.delay

    def delay(*delay_args, **delay_kwargs):
        transaction.on_commit(lambda: orig_delay(*delay_args, **delay_kwargs))
    celery_task.delay = delay

    return celery_task


def Celery(*args, **kwargs):
    celery_c = celery.Celery(*args, **kwargs)
    celery_c.task = task

    return celery_c
