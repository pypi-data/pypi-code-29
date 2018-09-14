from datetime import timedelta

from ionata_settings import base


_auth = 'minimal_user.drf.serializers'


# pylint: disable=no-init,invalid-name,abstract-method,no-member
class DRF:
    """Base configuration for our drf webapps."""

    LOGIN_URL = '/backend/api/v1/login/'
    LOGIN_REDIRECT_URL = '/backend/api/v1/'

    @property
    def INSTALLED_APPS(self):
        return super().INSTALLED_APPS + [
            'rest_framework',
            'rest_framework.authtoken',
            'rest_auth',
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
            'rest_auth.registration',
            'django_filters',
        ]

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ],
        'DEFAULT_FILTER_BACKENDS': [
            'rest_framework_filters.backends.DjangoFilterBackend',
        ]
    }

    # Auth
    ACCOUNT_AUTHENTICATION_METHOD = 'email'
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = 'none'
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_REGISTRATION = 'enabled'
    REST_USE_JWT = True
    JWT_AUTH = {
        'JWT_EXPIRATION_DELTA': timedelta(hours=24),
        'JWT_AUTH_HEADER_PREFIX': 'Token',
    }
    REST_AUTH_SERIALIZERS = {
        'USER_DETAILS_SERIALIZER': f'{_auth}.UserDetailsSerializer',
        'PASSWORD_RESET_SERIALIZER': f'{_auth}.PasswordResetSerializer',
        'LOGIN_SERIALIZER': f'{_auth}.LoginSerializer',
    }
    REST_AUTH_REGISTER_SERIALIZERS = {
        'REGISTER_SERIALIZER': f'{_auth}.RegisterSerializer',
    }


class Dev(DRF, base.Dev):
    """Base settings for development."""


class Prod(DRF, base.Prod):
    """Base settings for production."""
