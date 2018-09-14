from django.core.management.base import BaseCommand, CommandError
from datetime import datetime

from csgoogleanalytics.utils import create_page_stats
from csgoogleanalytics.models import Page, PageStats, PERIOD_CHOICES_FULL

from django.core.paginator import Paginator

class Command(BaseCommand):
    help = 'Ze egunetako datuak ekarri nahi dituzu, pageviews'

    def add_arguments(self, parser):
        default_eguna = int(datetime.now().strftime('%Y%m%d'))
        parser.add_argument('--eguna', type=int, nargs='?', default=default_eguna)

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS(kwargs['eguna']))
        end_date = datetime.strptime(str(kwargs['eguna']),'%Y%m%d').date()
        end_date_str = end_date.strftime('%Y-%m-%d')

        for period_id, period_value in PERIOD_CHOICES_FULL.items():
            start_date = end_date - period_value[1]
            start_date_int = int(start_date.strftime('%Y%m%d'))
            start_date_str = start_date.strftime('%Y-%m-%d')
            
            pages = Page.objects.filter(added_day=start_date_int)            

            if pages.exists():
                pagepaths = list(pages.values_list('pagepath',flat=True))
                boo = create_page_stats(pagepaths,start_date_str, end_date_str, period_id)

            self.stdout.write(self.style.SUCCESS('{} - {}: {}'.format(start_date,end_date, pages.count())))                                            

