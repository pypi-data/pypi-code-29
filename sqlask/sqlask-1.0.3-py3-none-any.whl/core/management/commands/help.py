"""
	Author = Venkata Sai Katepalli
	seedings will be happen here
"""
from sqlask.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        raise NotImplementedError("Not yet implemented")

