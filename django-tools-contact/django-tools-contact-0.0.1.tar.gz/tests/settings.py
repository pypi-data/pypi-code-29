# Django settings
SECRET_KEY = "tests"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",

    "djtools.contact",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    }
]

# App settings
DJTOOLS_CONTACT_SITE_DOMAIN = "www.example.com"
DJTOOLS_CONTACT_MAIL_FROM = "no-reply@example.com"
DJTOOLS_CONTACT_MAIL_TO = ["admin@example.com"]
