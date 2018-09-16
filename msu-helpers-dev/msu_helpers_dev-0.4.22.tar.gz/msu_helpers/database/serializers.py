#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import *

# __all__ = ('StudyGroupSerializer', 'UserSerializer')


class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = ('id', 'code')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'code')


class UserSerializer(serializers.ModelSerializer):
    study_group = StudyGroupSerializer()
    lang = LanguageSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'study_group', 'birthday', 'about', 'profile_pic', 'email', 'lang',
                  'activated', 'is_staff', )


class ArticleSerializer(serializers.ModelSerializer):
    study_group = StudyGroupSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'study_group', 'birthday', 'about', 'profile_pic', 'email', 'lang',
                  'activated', 'is_staff', )


SERIALIZERS: dict = {
    'StudyGroup': StudyGroupSerializer,
    'Language': LanguageSerializer,
    'User': UserSerializer,
    'Article': ArticleSerializer,
}


def get(class_name: str):
    return SERIALIZERS.get(class_name)
