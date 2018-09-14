from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver

from channels_redux.notify import NotifyConsumer, NotifierMixin


def notifier_only(func):
    def new_func(sender, instance, *args, **kwargs):
        if not isinstance(instance, NotifierMixin):
            return
        return func(sender, instance, *args, **kwargs)
    return new_func


@receiver(post_save, dispatch_uid="channels_redux.signals.object_saved")
@notifier_only
def object_saved(sender, instance: NotifierMixin, created, **kwargs):
    if created:
        NotifyConsumer.object_created(instance)
    else:
        NotifyConsumer.object_updated(instance)


@receiver(post_delete, dispatch_uid="channels_redux.signals.object_deleted")
@notifier_only
def object_deleted(sender, instance: NotifierMixin, **kwargs):
    NotifyConsumer.object_deleted(instance)


@receiver(m2m_changed, dispatch_uid="channels_redux.signals.m2m_changed")
def object_m2m_changed(sender, instance: NotifierMixin, action: str, model, pk_set, **kwargs):
    if action.startswith('pre'):
        return
    if isinstance(instance, NotifierMixin):
        NotifyConsumer.object_updated(instance)
    if issubclass(model, NotifierMixin):
        NotifyConsumer.object_updated_reverse(model, pk_set)
