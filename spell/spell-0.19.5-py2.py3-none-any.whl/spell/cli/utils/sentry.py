import os
import traceback

import sentry_sdk
from sentry_sdk.integrations.atexit import AtexitIntegration


SENTRY_URL = "https://9a9530b86ed74e11a28e7f410f31bab7@sentry.io/1285204"
ENVIRONMENT_SUPPRESS_VALUE = "SPELL_QUIET"


def _init_sentry():
    def noop(*args, **kwargs):
        pass
    atexit_override = AtexitIntegration(noop)
    sentry_sdk.init(SENTRY_URL, integrations=[atexit_override])
_init_sentry() # noqa


def capture_exception(error):
    if ENVIRONMENT_SUPPRESS_VALUE not in os.environ:
        sentry_sdk.capture_exception(error)
    else:
        traceback.print_exc()


def capture_message(message, level=None):
    if ENVIRONMENT_SUPPRESS_VALUE not in os.environ:
        sentry_sdk.capture_message(message, level)
    else:
        traceback.print_exc()
