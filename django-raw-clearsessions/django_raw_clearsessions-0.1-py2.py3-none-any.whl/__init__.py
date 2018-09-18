from django.utils import timezone


class SessionStoreMixin(object):

    # Copied verbatim from Django 1.9+ for backwards compatibility.
    @classmethod
    def get_model_class(cls):
        # Avoids a circular import and allows importing SessionStore when
        # django.contrib.sessions is not in INSTALLED_APPS.
        from django.contrib.sessions.models import Session
        return Session

    # Use `_raw_delete()` instead of `delete()`.
    @classmethod
    def clear_expired(cls):
        qs = cls.get_model_class().objects.filter(
            expire_date__lt=timezone.now())
        qs._raw_delete(qs.db)
