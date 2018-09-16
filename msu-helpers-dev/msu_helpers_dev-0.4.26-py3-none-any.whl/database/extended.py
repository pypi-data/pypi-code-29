#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .db_constants import *
from .managers import UserManager

__all__ = ('User', 'UserAdmin')


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=64, default=UserDefaults.first_name)
    last_name = models.CharField(max_length=64, default=UserDefaults.last_name)
    study_group = models.CharField(max_length=10, default=UserDefaults.study_group)
    birthday = models.DateField(auto_now_add=True)
    about = models.TextField(max_length=1000, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='media/users/profile_pics', null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    lang = models.CharField(max_length=5, default=UserDefaults.lang)
    activated = models.BooleanField(default=UserDefaults.activated)
    is_staff = models.BooleanField(default=UserDefaults.is_staff, editable=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = '_User'

    def __str__(self):
        return f'{self.email} - {self.first_name} {self.last_name}'

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class UserAdmin(admin.ModelAdmin):
    exclude = ('password', 'last_login', 'user_permissions', 'groups')
