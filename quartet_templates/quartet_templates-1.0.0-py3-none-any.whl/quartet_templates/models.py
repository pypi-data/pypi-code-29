from django.db import models
from django.template import Context, Template as TemplateClass


class Template(models.Model):
    '''
    Stores a Django/Jinja template into the database for use with
    quartet-capture/number range, etc, ...
    The render method will return a string with the template and variables
    updated with the context dictionary.
    '''
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        db_index=True,
        unique=True,
        help_text="A name to identify this template")
    content = models.TextField(
        null=False,
        blank=False,
        help_text="The full Django/Jinja template to be used.")
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True)

    def render(self, context):
        '''
        Renders the template passing a dictionary of key/value pairs
        in the context parameter.
        '''
        template = TemplateClass(self.content)
        return template.render(Context(context))
