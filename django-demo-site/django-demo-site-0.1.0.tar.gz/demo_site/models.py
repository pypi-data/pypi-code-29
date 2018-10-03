# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

DEMO_SITE_STATUS = (
    ('alpha', _('Alpha')),
    ('beta', _('Beta')),
    ('rc', _('Release candidate')),
    ('final', _('Final release')),
)


DEMO_SITE_TEXT = _('''This is a website under active development and may have bugs and lack lots of features. If you find anything you want to report use the contact email or issue handler below.''')


if hasattr(settings, 'DEMO_SITE_TEXT'):
    DEMO_SITE_TEXT = getattr(settings, 'DEMO_SITE_TEXT')


class DemoSiteSettings(models.Model):
    """

    """
    title = models.CharField(_('Title'), max_length=100, default=_('Demo site'))
    text = models.TextField(_('Text'), default=DEMO_SITE_TEXT)
    status = models.CharField(_('Status'), max_length=50, choices=DEMO_SITE_STATUS, null=True, blank=True)
    version = models.CharField(_('Version'), max_length=50, null=True, blank=True, default='0.1.0')
    final_release_date = models.DateTimeField(_('Final release date'), null=True, blank=True)
    demo_available_until_date = models.DateTimeField(_('Demo available until date'), null=True, blank=True)
    contact_email = models.EmailField(_('Contact email'), null=True, blank=True)
    issue_handler = models.URLField(_('Issue handler'), null=True, blank=True)
    project_page = models.URLField(_('Project page'), null=True, blank=True)
    requires_access_token = models.BooleanField(_('Requires access token'), default=False)
    default_success_url = models.CharField(_('Default success url'), max_length=50, default='/demo/')

    def __str__(self):
        return self.title

    @classmethod
    def current_settings(cls):
        """

        :return:
        """
        return cls.objects.all().first() or cls.objects.create()


class AccessToken(models.Model):
    """

    """
    token = models.CharField(_('Access token'), max_length=20)
    success_url = models.CharField(_('Success url'), max_length=50, default='/demo/')
    valid = models.BooleanField(_('Valid'), default=True)
    feature_access = models.CharField(_('Feature access'), max_length=20, null=True, blank=True)

    def __str__(self):
        """

        :return:
        """
        return self.token

    @classmethod
    def is_valid(cls, used_token):
        """

        :param token:
        :return:
        """

        if not hasattr(settings, 'DEMO_SITE_ACCESS_TOKEN_REQUIRED'):
            raise Exception("demo-site added to INSTALLED_APPS, but DEMO_SITE_ACCESS_TOKEN_REQUIRED not set in settings.py.")

        atr = getattr(settings, 'DEMO_SITE_ACCESS_TOKEN_REQUIRED')
        if not atr:
            if not hasattr(settings, 'DEMO_SITE_DEFAULT_URL'):
                raise Exception("demo-site added to INSTALLED_APPS, but DEMO_SITE_DEFAULT_URL not set in settings.py.")
            return True, getattr(settings, 'DEMO_SITE_DEFAULT_URL')

        demo_settings = DemoSiteSettings.current_settings()
        if not demo_settings.requires_access_token:
            return True, demo_settings.default_success_url

        token = cls.objects.filter(token=used_token).first()
        if not token:
            return False, None

        if not token.valid:
            return False, None

        return True, token.success_url
