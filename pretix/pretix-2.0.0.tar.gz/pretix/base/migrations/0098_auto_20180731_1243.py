# Generated by Django 2.0.7 on 2018-07-31 12:43

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import pretix.base.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0097_auto_20180722_0804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logentry',
            options={'ordering': ('-datetime', '-id')},
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='fee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to='pretixbase.OrderFee'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='slug',
            field=models.SlugField(help_text='Should be short, only contain lowercase letters, numbers, dots, and dashes. Every slug can only be used once. This is being used in URLs to refer to your organizer accounts and your events.', unique=True, validators=[django.core.validators.RegexValidator(message='The slug may only contain letters, numbers, dots and dashes.', regex='^[a-zA-Z0-9.-]+$'), pretix.base.validators.OrganizerSlugBlacklistValidator()], verbose_name='Short form'),
        ),
        migrations.AlterField(
            model_name='staffsession',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='staffsessionauditlog',
            name='impersonating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='staffsessionauditlog',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='logs', to='pretixbase.StaffSession'),
        ),
        migrations.AlterField(
            model_name='user',
            name='locale',
            field=models.CharField(choices=[('en', 'English'), ('de', 'German'), ('de-informal', 'German (informal)'), ('nl', 'Dutch'), ('da', 'Danish'), ('tr', 'Turkish'), ('pt-br', 'Portuguese (Brazil)')], default='en', max_length=50, verbose_name='Language'),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together={('organizer', 'slug')},
        ),
    ]
