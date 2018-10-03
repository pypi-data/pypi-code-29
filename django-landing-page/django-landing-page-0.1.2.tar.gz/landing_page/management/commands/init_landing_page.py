import os

from django.core.management.base import BaseCommand
#from django.contrib.auth import get_user_model

from landing_page.models import Layout


class Command(BaseCommand):
    """

    """
    help = 'Imports a lot of test data'

    def handle(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        if Layout.objects.filter(folder_name='default').exists():
            return

        import landing_page
        layout_folder = os.path.join(os.path.abspath(landing_page.__file__).replace("%s__init__.py" % os.sep, ''), 'templates', 'landing_page', 'layouts')
        for folder_name in [f for f in os.listdir(layout_folder)]:
            if not Layout.objects.filter(folder_name=folder_name).exists():
                Layout.objects.create(title=folder_name.capitalize(), folder_name=folder_name)
        print("Created default layouts for landing page app..")
