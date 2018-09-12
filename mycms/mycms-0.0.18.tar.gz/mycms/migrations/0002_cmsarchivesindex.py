# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-12 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSArchivesIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=1975)),
                ('entries', models.ManyToManyField(blank=True, to='mycms.CMSEntries')),
            ],
        ),
    ]
