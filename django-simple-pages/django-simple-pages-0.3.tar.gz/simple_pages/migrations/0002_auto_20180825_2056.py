from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template_name',
            field=models.CharField(blank=True, help_text='The name of the template to use when rendering this page. If blank or invalid, the simple_pages/default.html template will be used.', max_length=255, null=True, verbose_name='template name'),
        ),
    ]
