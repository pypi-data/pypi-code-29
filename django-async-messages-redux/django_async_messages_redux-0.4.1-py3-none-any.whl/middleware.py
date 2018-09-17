from distutils.version import StrictVersion

from django.contrib import messages

try:
    from django.utils.version import get_version
except ImportError:
    from django import VERSION as DJANGO_VERSION

    def get_version():
        return ".".join(str(n) for n in DJANGO_VERSION[:3])

from async_messages import get_messages

if StrictVersion(get_version()) >= StrictVersion("1.10.0"):
    from django.utils.deprecation import MiddlewareMixin as _MiddlewareBase

    def _is_user_authenticated(user):
        return bool(user.is_authenticated)
else:
    _MiddlewareBase = object

    def _is_user_authenticated(user):
        return user.is_authenticated()


class AsyncMiddleware(_MiddlewareBase):
    # In Django>=1.10 User.is_authenticated is a property, not a method but a
    # strange one : CallbableBool.
    #  - If default User is used you can use it as a boolean either a method.
    #  - If this property is overrided you may have a bool instead and an
    #    exception.

    def is_authenticated(self, request):
        if hasattr(request, "session") and hasattr(request, "user"):
            return _is_user_authenticated(request.user)
        else:
            return False

    def process_response(self, request, response):
        """
        Check for messages for this user and, if it exists,
        call the messages API with it
        """
        if self.is_authenticated(request):
            msgs = get_messages(request.user)
            if msgs:
                for msg, level in msgs:
                    messages.add_message(request, level, msg)
        return response
