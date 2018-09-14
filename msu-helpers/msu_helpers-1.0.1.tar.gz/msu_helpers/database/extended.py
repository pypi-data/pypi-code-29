#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .db_constants import *
from .managers import UserManager


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

    @property
    def serialized(self) -> dict:
        return self._serialize()

    def _serialize(self) -> dict:
        return {
            'id': self.pk,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'study_group': self.study_group,
            'birthday': self.birthday.strftime(Utils.DATETIME_FORMAT),
            'about': self.about,
            'profile_pic': self.profile_pic,
            'email': self.email,
            'lang': self.lang,
            'activated': self.activated,
            'is_staff': self.is_staff,
        }

    @classmethod
    def deserialize(cls, data: dict, save: bool = False):
        user = User()

        user.pk = data.get('id', UserDefaults.id)
        user.first_name = data.get('first_name', UserDefaults.first_name)
        user.last_name = data.get('last_name', UserDefaults.last_name)
        user.study_group = data.get('study_group', UserDefaults.study_group)
        user.about = data.get('about', UserDefaults.about)
        user.profile_pic = data.get('profile_pic', UserDefaults.profile_pic)
        user.email = data.get('email', UserDefaults.email)
        user.lang = data.get('lang', UserDefaults.lang)
        user.activated = data.get('activated', UserDefaults.activated)
        user.is_staff = data.get('is_staff', UserDefaults.is_staff)

        birthday = data.get('birthday', UserDefaults.birthday)
        password = data.get('password', None)

        if password is None or user.email is None:
            raise ValueError('Can not create user without email or password')

        if birthday is not None:
            user.birthday = datetime.strptime(birthday, Utils.DATETIME_FORMAT)

        user.set_password(password)
        if save:
            user.save()

        return user


