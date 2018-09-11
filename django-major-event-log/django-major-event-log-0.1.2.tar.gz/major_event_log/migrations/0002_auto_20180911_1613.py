# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('major_event_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contact_name',
            field=models.CharField(help_text=b'Appears as the Reporting Agent', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='outcome',
            field=models.CharField(max_length=80, choices=[(b'http://purl.org/NET/UNTL/vocabularies/eventOutcomes/#success', b'Success'), (b'http://purl.org/NET/UNTL/vocabularies/eventOutcomes/#failure', b'Failure')]),
        ),
    ]
