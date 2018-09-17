"""Standalone test runner script, with minimum settings required for tests.

Re-use at your own risk: many Django applications will require
different settings and/or templates to run their tests.
"""
import os
import sys

# Make sure the app is (at least temporarily) on the import path.
APP_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, APP_DIR)


# Minimum settings required for the app's tests.
SETTINGS = {
    "INSTALLED_APPS": (
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "simple_pages",
    ),
    "ROOT_URLCONF": "simple_pages.tests.urls",
    "DATABASES": {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(APP_DIR, "db.sqlite3"),
        },
    },
    "MIDDLEWARE": (
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "simple_pages.middleware.PageFallbackMiddleware",
    ),
    "TEMPLATES": [{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
        },
    }],
}


def run():
    """Configure Django and run the unit tests."""
    # Making Django run this way is a two-step process. First, call
    # settings.configure() to give Django settings to work with:
    from django.conf import settings
    settings.configure(**SETTINGS)

    # Then, call django.setup() to initialize the application cache
    # and other bits:
    import django
    if hasattr(django, "setup"):
        django.setup()

    # Now we instantiate a test runner...
    from django.test.utils import get_runner
    TestRunner = get_runner(settings)

    # And then we run tests and return the results.
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(["simple_pages.tests"])
    sys.exit(bool(failures))


if __name__ == "__main__":
    run()
