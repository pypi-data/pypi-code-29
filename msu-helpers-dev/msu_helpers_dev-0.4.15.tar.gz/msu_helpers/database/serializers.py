#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import *

__all__ = ['StudyGroupSerializer', 'UserSerializer']


class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = ['pk', 'code']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name', 'study_group', 'birthday', 'about', 'profile_pic', 'email', 'lang',
                  'activated', 'is_staff', ]
