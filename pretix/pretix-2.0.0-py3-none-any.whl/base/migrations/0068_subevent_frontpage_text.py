# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 16:11
from __future__ import unicode_literals

import i18nfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0067_auto_20170712_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='subevent',
            name='frontpage_text',
            field=i18nfield.fields.I18nTextField(blank=True, null=True, verbose_name='Frontpage text'),
        ),
    ]
