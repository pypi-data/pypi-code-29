import logging

from django.conf import settings

DEFAULTS = {
    "MAX_LOG_ENTRIES": 10000,
    "LEVELS": [logging.CRITICAL,
               logging.ERROR,
               logging.WARNING,
               logging.INFO,
               logging.DEBUG],
    "ENABLE_TEST_BUTTON": True,
    "USE_CRASHLOG": False,
    "ALLOW_TRUNCATE": True,
    # "DATABASE": "default"
}


class Config:
    pass


config = Config()

custom = getattr(settings, 'DBLOG', {})

for key, value in DEFAULTS.items():
    custom.setdefault(key, value)
    setattr(config, key, custom[key])
