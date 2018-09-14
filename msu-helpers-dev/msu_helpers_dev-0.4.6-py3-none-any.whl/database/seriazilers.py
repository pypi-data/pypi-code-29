from rest_framework import serializers
from .models import User as _User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = _User
        fields = ['pk', 'first_name', 'last_name', 'study_group', 'birthday', 'about', 'profile_pic', 'email', 'lang',
                  'activated', 'is_staff', ]
