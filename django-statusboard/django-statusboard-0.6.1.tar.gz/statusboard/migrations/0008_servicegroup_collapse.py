# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-16 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statusboard', '0007_auto_20170213_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicegroup',
            name='collapse',
            field=models.BooleanField(default=True),
        ),
    ]
