from django.db import models
from django.contrib.auth.models import AbstractUser

from generic.helpers import get_uuid1


class User(AbstractUser):
    """
    Overrides the default Django User, uuid is changed from an auto incremental
    integer field to a uuidv1 field.
    """
    id = models.UUIDField(default=get_uuid1, primary_key=True)
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=1, blank=True, null=True)
    firstName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50, blank=True, null=True)
    validated_email = models.BooleanField(default=False, blank=False, null=False)
    isFacilityManagement = models.BooleanField(default=False, blank=False, null=False)
    isProprietor = models.BooleanField(default=False, blank=False, null=False)
    isTenant = models.BooleanField(default=False, blank=False, null=False)

    def __unicode__(self):
        return "{0}".format(self.id)

    def __str__(self):
        return "{0}".format(self.id)


class Object(models.Model):
    id = models.UUIDField(default=get_uuid1, primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=False, null=False)
    password = models.CharField(unique=False, max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'object'


class UserObject(models.Model):
    id = models.UUIDField(default=get_uuid1, primary_key=True)
    owner = models.ForeignKey('User', models.CASCADE, related_name='user_objects')
    name = models.CharField(unique=True, max_length=255, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'user_object'


class UserObjectPw(models.Model):
    id = models.UUIDField(default=get_uuid1, primary_key=True)
    owner = models.ForeignKey('User', models.CASCADE, related_name='user_objects_pw')
    name = models.CharField(unique=True, max_length=255, blank=False, null=False)
    password = models.CharField(unique=False, max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_object_pw'
