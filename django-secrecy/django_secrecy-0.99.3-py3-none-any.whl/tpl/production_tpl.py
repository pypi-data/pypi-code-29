from .base import secrets


DEBUG = False
# CHANGE '*' - on your domain names
ALLOWED_HOSTS = ['*']

# Default MySql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': secrets.NAME,
        'USER': secrets.USER,
        'PASSWORD': secrets.PASSWORD,
        'HOST': '',
        'PORT': '',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_unicode_ci'
        }
    }
}
