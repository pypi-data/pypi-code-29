#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name', 'study_group', 'birthday', 'about', 'profile_pic', 'email', 'lang',
                  'activated', 'is_staff', ]