"""
Django settings for mgp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from os.path import join
from os.path import dirname
from trix.trix_admin import css_icon_map


# The base directory with manage.py
BASE_DIR = dirname(dirname(dirname(dirname(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(%a+ly@5m4g6fl2yhc2(i#cfz+x&_$uyh9o8%z6srhk)-)yzm('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_extensions',
    'crispy_forms',
    'trix.trix_core',
    'trix.trix_admin',
    'trix.trix_student',
    'cradmin_legacy',  # Important: Must come after trix_admin because of template overrides
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'trix.trix_student.middleware.consent.ConsentMiddleware',
]


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Oslo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# https://docs.djangoproject.com/en/1.11/ref/clickjacking/
# X_FRAME_OPTIONS = 'DENY'

# Setup static files to be served at /s/.
# - Gives us short urls for angular apps (I.E.: /s/v1/).
STATIC_URL = '/static/'

# Custom authentication model
AUTH_USER_MODEL = 'trix_core.User'

# Redirect logins and logouts to the frontpage by default
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = '/login'
LOGOUT_URL = '/logout'

# Use bootstrap3 template pack to django-crispy-forms.
CRISPY_TEMPLATE_PACK = 'bootstrap3'

MEDIA_ROOT = join(BASE_DIR, 'media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Insert TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "cradmin_legacy.context_processors.cradmin",
            ],
        },
    }
]

TRIX_ADMIN_DOCUMENTATION_URL = 'http://trix2.readthedocs.org/'
TRIX_ADMIN_DOCUMENTATION_LABEL = 'trix2.readthedocs.org'
TRIX_STUDENT_GETTINGSTARTEDGUIDE_URL = 'http://trix2.readthedocs.org/en/latest/' \
                                       'student/gettingstarted.html'

# Used to update the icon map since the legacy version is outdated or does not include what we need.
CRADMIN_LEGACY_CSS_ICON_MAP = css_icon_map.FONT_AWESOME
