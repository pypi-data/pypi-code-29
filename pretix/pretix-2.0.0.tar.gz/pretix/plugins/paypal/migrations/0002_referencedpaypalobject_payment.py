# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-23 09:19
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0097_auto_20180722_0804'),
        ('paypal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencedpaypalobject',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.OrderPayment'),
        ),
    ]
