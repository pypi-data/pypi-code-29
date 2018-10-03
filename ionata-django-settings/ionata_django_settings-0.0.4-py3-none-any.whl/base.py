from urllib.parse import urlparse
from typing import List, Tuple

from configurations import Configuration, values  # type: ignore

_pw_validation = 'django.contrib.auth.password_validation'


class RequiredValue(values.Value):
    """Require that a value has been overriden."""

    def __init__(self, *args, **kwargs):
        kwargs['environ'] = False
        kwargs['environ_required'] = True
        super().__init__(*args, **kwargs)

    def setup(self, name):
        value = super().setup(name)
        if value is None:
            raise ValueError(f'Required value {name} is not set')
        return value


# pylint: disable=no-init,invalid-name
class Base(Configuration):
    """Base configuration for our webapps."""

    # Set in environment
    ADMIN_USER: dict = values.DictValue()
    SECRET_KEY: str = values.SecretValue()

    # Required to override
    APP_NAME: str = RequiredValue()
    SITE_URL: str = RequiredValue()
    ALLOWED_HOSTS: List[str] = RequiredValue()
    ADMINS: List[Tuple[str, str]] = RequiredValue()
    MANAGERS: List[Tuple[str, str]] = RequiredValue()

    # Services
    CELERY_BROKER_URL = values.Value(
        'redis://', environ_name='CELERY_BROKER_URL')
    DATABASES = values.DatabaseURLValue(environ_required=True)

    # Storage
    DEFAULT_FILE_STORAGE = 'ionata_settings.storage.MediaS3'
    STATICFILES_STORAGE = 'ionata_settings.storage.StaticS3'
    AWS_S3_REGION_NAME = values.Value(environ_required=True)
    AWS_STORAGE_BUCKET_NAME = values.Value(environ_required=True)
    AWS_S3_ENDPOINT_URL = values.URLValue(environ_required=True)
    AWS_ACCESS_KEY_ID = values.SecretValue()
    AWS_SECRET_ACCESS_KEY = values.SecretValue()

    # Core
    DEBUG = False

    @property
    def INSTALLED_APPS(self):
        return [
            # Our defaults
            'minimal_user',
            'corsheaders',
            'anymail',
            'django_extensions',
            'storages',
            'django_celery_beat',
            'django_celery_results',

            # Core django apps
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.sites',
        ]

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    ]
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ROOT_URLCONF = 'webapp.urls'
    WSGI_APPLICATION = 'webapp.wsgi.application'
    SITE_ID = 1

    # i18n
    LANGUAGE_CODE = 'en-AU'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Auth
    ANONYMOUS_USER_ID = -1
    AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
    AUTH_USER_MODEL = 'minimal_user.User'
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': f'{_pw_validation}.UserAttributeSimilarityValidator'
        },
        {
            'NAME': f'{_pw_validation}.MinimumLengthValidator'
        },
        {
            'NAME': f'{_pw_validation}.CommonPasswordValidator'
        },
        {
            'NAME': f'{_pw_validation}.NumericPasswordValidator'
        },
    ]

    # Security
    INTERNAL_IPS = ['127.0.0.1']
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_PATH = '/backend/'
    CSRF_COOKIE_PATH = '/backend/'
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    AWS_AUTO_CREATE_BUCKET = False
    AWS_DEFAULT_ACL = 'private'
    AWS_BUCKET_ACL = 'private'

    @property
    def CORS_ORIGIN_WHITELIST(self):
        return self.ALLOWED_HOSTS

    @property
    def CSRF_TRUSTED_ORIGINS(self):
        return self.CORS_ORIGIN_WHITELIST

    # URLs
    MEDIA_URL = '/assets/media/'
    STATIC_URL = '/assets/static/'

    # Celery
    CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}  # 1 hour.
    CELERY_RESULT_BACKEND = 'django-db'
    CELERY_TIMEZONE = 'UTC'
    CELERY_ENABLE_UTC = True
    CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

    @property
    def CELERY_APP_NAME(self):
        return self.APP_NAME

    # Email
    @property
    def EMAIL_SUBJECT_PREFIX(self):
        return f'[Django - {self.APP_NAME}] '

    @property
    def DEFAULT_FROM_EMAIL(self):
        return f'no-reply@{self.URL.hostname}'

    @property
    def SERVER_EMAIL(self):
        return f'no-reply@{self.URL.hostname}'

    @property
    def MAILGUN_SENDER_DOMAIN(self):
        return f'mailgun.{self.URL.hostname}'

    # Misc properties
    @property
    def URL(self):
        return urlparse(self.SITE_URL)

    @property
    def FRONTEND_URL(self):
        return self.SITE_URL


# pylint: disable=no-init,invalid-name,abstract-method,no-member
class Dev(Base):
    """Base settings for development."""

    DEBUG = True

    # Required overrides
    SITE_URL = values.URLValue('http://localhost:8000')
    ALLOWED_HOSTS = ['*']
    ADMINS: List[Tuple[str, str]] = []
    MANAGERS: List[Tuple[str, str]] = []
    SECRET_KEY = 'super_secret_secret_key'
    ADMIN_USER = values.DictValue({
        'email': 'test@example.com',
        'password': 'password'
    })

    # Storage
    AWS_S3_REGION_NAME = ''
    AWS_STORAGE_BUCKET_NAME = values.Value('django')
    AWS_S3_ENDPOINT_URL = values.Value('http://minio:9000')
    AWS_ACCESS_KEY_ID = values.Value('djangos3')
    AWS_SECRET_ACCESS_KEY = values.Value('djangos3')

    @property
    def AWS_S3_CUSTOM_DOMAIN(self):
        return values.Value(self.URL.hostname)

    # Core
    @property
    def FRONTEND_URL(self):
        return values.URLValue(self.SITE_URL)

    @property
    def INSTALLED_APPS(self):
        return super().INSTALLED_APPS + [
            'debug_toolbar',
        ]

    # Security
    CORS_ORIGIN_ALLOW_ALL = True
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    AWS_AUTO_CREATE_BUCKET = True

    # Email
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Services
    CELERY_BROKER_URL = values.Value(
        'redis://redis', environ_name='CELERY_BROKER_URL')
    DATABASES = values.DatabaseURLValue(
        'postgis://django:django@db:5432/django')


# pylint: disable=no-init,invalid-name,abstract-method,no-member
class Prod(Base):
    """Base settings for production."""

    EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
    MAILGUN_API_KEY = values.SecretValue()
