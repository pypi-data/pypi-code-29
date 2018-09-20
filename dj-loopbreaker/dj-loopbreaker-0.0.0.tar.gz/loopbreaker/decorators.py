from functools import wraps
from django.core.cache import cache
from django.conf import settings

# def throttle(signal_id, instance):
#     def inner_render(fn):
#         def wrapped(request, *args, **kwargs):
#             key = "{}.{}.{}".format(
#                 signal_id,
#                 instance.__meta.model_name,
#                 instance.pk
#             )
#             print(key)
#             timeout = getattr(settings, 'SIGNAL_THROTTLE_KEY', 1)
#             cache.set(key, 'true', timeout)
#         return wraps(fn)(wrapped)
#     return inner_render


def throttle(signal_id, expire_after=1, **kwargs):
    def throttler(throttledfunc):
        @wraps(throttledfunc)
        def throttled(*args, **kw):
            instance = kw.get('instance')
            model_label = "{}.{}".format(
                instance._meta.app_label,
                instance._meta.model_name
            )
            key = "{}.{}.{}".format(
                signal_id,
                model_label,
                instance.pk
            )
            if cache.get(key) is None:
                cache.set(key, 'true', expire_after)
                return throttledfunc(*args, **kw)

            # else:
            #     print('blocked')

        return throttled
    return throttler


