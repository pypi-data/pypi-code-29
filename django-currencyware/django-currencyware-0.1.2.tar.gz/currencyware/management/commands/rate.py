import sys
import json
import codecs
import logging
import requests
from datetime import datetime

from django.conf import settings
from django.utils import timezone
from django.utils import translation
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from toolware.utils.generic import get_days_ago

from ...currency import get_display
from ...models import Rate, Currency
from ... import defaults as defs
from ... import utils as util

log = logging.getLogger(__name__)


class Command(BaseCommand):
    # Translators: admin
    help = "Fetches live rates from open exchange rates api"
    MIN_PURGE_DAYS = 2
    MAX_CHECKPOINT_DAYS = 30
    OXR_URL = defs.OPEN_EXCHANGE_RATES_URL
    OXR_KEY = defs.OPEN_EXCHANGE_RATES_API_KEY
    LANGUAGE_CODE = getattr(settings, 'LANGUAGE_CODE', 'en')
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--purge',
            action='store',
            dest='purge_days',
            type=int,
            help='Remove rates older than x days'
        )

        parser.add_argument(
            '-c',
            '--checkpoint',
            action='store',
            dest='checkpoint_days',
            type=int,
            help='Restore missing rates within the last x days'
        )

        parser.add_argument(
            '-f',
            '--fetch',
            action='store_true',
            dest='fetch',
            default=False,
            help='Fetch and load all rates to db'
        )

    def handle(self, *args, **options):
        translation.activate(self.LANGUAGE_CODE)
        self.verbosity = options['verbosity']
        purge_days = options['purge_days']
        checkpoint_days = options['checkpoint_days']
        fetch = options['fetch']

        if not (purge_days or checkpoint_days or fetch):
            self.print_help("", subcommand='rate')
            return

        if purge_days:
            if purge_days < self.MIN_PURGE_DAYS:
                # purge only after `MIN_PURGE_DAYS` days old (compensate for UTC)
                self.stdout.write('Purge only possible for data >= {} days'.format(self.MIN_PURGE_DAYS))
                return
            self.purge(purge_days)

        if checkpoint_days:
            confirm = 'yes'
            if checkpoint_days > self.MAX_CHECKPOINT_DAYS:
                # restore rates within the last `MAX_CHECKPOINT_DAYS` (mind UTC)
                self.stdout.write('Restoring rates will hit the api {} times'.format(checkpoint_days))
                confirm = input('Are you sure? [yes | no]: ')
            if confirm == 'yes':
                self.checkpoint(checkpoint_days)

        if fetch:
            self.fetch()

    def fetch(self):

        if self.verbosity > 2:
            self.stdout.write('Preparing to fetch rates ...')
        latest_rate_url = requests.compat.urljoin(self.OXR_URL, 'latest.json')
        resp = self.fetch_url(latest_rate_url, params={'app_id': self.OXR_KEY, 'base': defs.BASE_CURRENY_CODE})
        if resp.status_code != requests.codes.ok:
            self.stdout.write('Failed to fetch rates ...')
            self.stdout.write(resp.text)
            return

        data = resp.json()
        create_count, update_count = self.add_or_update_rates(data)
        self.stdout.write('Created {count} currenies'.format(count=create_count))
        self.stdout.write('Updated {count} currenies'.format(count=update_count))

    def add_or_update_rates(self, data):
        create_count, update_count = 0, 0
        updated = datetime.fromtimestamp(data['timestamp'], tz=timezone.utc)
        for code, rate in data['rates'].items():
            created = False
            defaults = {
                'code': code,
                'date': updated,
                'rate': rate,
                'name': get_display(code)
            }
            instance, created = Rate.objects.get_or_create_unique(defaults, ['code', 'date'])
            if created:
                create_count += 1
            else:
                update_count += 1
            
            if not instance and self.verbosity >=3:
                sys.stdout.write('Failed to create rate for ({code})\n'.format(code=code))
        return create_count, update_count

    def checkpoint(self, days):
        did_checkpoint = False
        create_count, update_count = 0, 0
        for ago in range(1, days+1):
            exact_date = get_days_ago(ago)
            historical_uri = 'historical/{}.json'.format(exact_date.strftime('%Y-%m-%d'))
            historical_rate_url = requests.compat.urljoin(self.OXR_URL, historical_uri)
            resp = self.fetch_url(historical_rate_url, params={'app_id': self.OXR_KEY, 'base': defs.BASE_CURRENY_CODE})
            if resp.status_code != requests.codes.ok:
                if self.verbosity >= 2:
                    self.stdout.write('Failed to fetch historical rates for {} ...').format(historical_date)
                    self.stdout.write(resp.text)
                continue

            Rate.objects.filter(
                date__year=exact_date.year,
                date__month=exact_date.month,
                date__day=exact_date.day).delete()
        
            data = resp.json()
            create_count, update_count = self.add_or_update_rates(data)

        self.stdout.write('Checkpointed {count} currenies'.format(count=create_count))


    def purge(self, days):
        did_purge = False
        for code in defs.ALL_CURRENCY_CODES:
            for ago in range(self.MIN_PURGE_DAYS, days+1):
                exact_date = get_days_ago(ago)
                try:
                    latest_for_day = Rate.objects.filter(
                        code=code,
                        date__year=exact_date.year,
                        date__month=exact_date.month,
                        date__day=exact_date.day).latest('date')
                except Rate.DoesNotExist as err:
                    continue
                
                old_rates = Rate.objects.filter(
                    code=code,
                    date__year=exact_date.year,
                    date__month=exact_date.month,
                    date__day=exact_date.day).exclude(date=latest_for_day.date)
            
                if old_rates:
                    did_purge = True
                    old_rates.delete()
                    if self.verbosity >= 2:
                        self.stdout.write('Purged rates from ({}) days ago.'.format(ago))

        if did_purge:
            self.stdout.write('Purged rates older than ({}) ago from db.'.format(days))
        else:
            self.stdout.write('Nothing to purge')

    @util.rate_limited(defs.OPEN_EXCHANGE_RATES_API_CALLS_PER_SECONDS)
    def fetch_url(self, url, params):
        resp = requests.get(url, params=params)
        return resp