import os
import sys
import codecs
import logging
import json

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.utils.translation import activate

from ...models import Currency, Rate
from ...currency import get_display
from ... import defaults as defs

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    # Note: admin:skip
    help = 'Load currency data'
    path = os.path.abspath(os.path.join(os.path.realpath(__file__), '../../../', 'currency.json'))

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--path',
            dest='path',
            default=self.path,
            help='Path to a json currency file.'
        )

        parser.add_argument(
            '--flush',
            dest='flush',
            default=False,
            action='store_true',
            help='Delete all existing currencies in db'
        )

        parser.add_argument(
            '-l',
            '--load',
            dest='load',
            action='store_true',
            default=False,
            help='Load currencies from data file'
        )

        parser.add_argument(
            '-o',
            '--overwrite',
            dest='overwrite',
            action='store_true',
            default=False,
            help='Overwrite currencies if already found in db'
        )

    def handle(self, *args, **options):
        self.verbosity = options['verbosity']
        path = options['path']
        overwrite = options['overwrite']
        flush = options['flush']
        load = options['load']
        
        if not (flush or load):
            self.print_help("", subcommand='currency')
            return

        if flush:
            self.flush()

        if load:
            self.load(path, overwrite)
    
    def flush(self):
        self.stdout.write('You are about to delete all currencies from db')
        confirm = input('Are you sure? [yes/no]: ')
        if confirm == 'yes':
            Currency.objects.all().delete()
            self.stdout.write('Currencies deleted from db.')

    def load(self, path, overwrite):
            
        if not os.path.isfile(path):
            self.stdout.write('No currency file found at path')
            self.stdout.write(path)
            self.print_help("", subcommand='currency')
            return

        activate(defs.DEFAULT_CURRENY_LANGUAGE_CODE)

        if self.verbosity > 2:
            self.stdout.write('Preparing currency file ...')

        fp = codecs.open(path, encoding='utf-8')
        self.data = json.load(fp)

        new_count, update_count = 0, 0
        for curr in self.data:
            created = False
            defaults = {
                'code': curr.get('code'),
                'name': get_display(curr.get('code')),
                'number': curr.get('number', 0),
                'symbol': curr.get('symbol', ''),
                'unit': curr.get('unit', 2),
                'country': ' '.join(curr.get('country', [])),
            }
            if overwrite:
                instance, created = Currency.objects.get_or_create_unique(defaults, ['code'])
            else:
                instance = Currency.objects.get_unique_or_none(code=defaults['code'])
                if not instance:
                    instance, created = Currency.objects.get_or_create_unique(defaults, ['code'])

            if created:
                new_count += 1
            elif overwrite:
                update_count += 1
        
        self.stdout.write('Created {count} currenies'.format(count=new_count))
        self.stdout.write('Updated {count} currenies'.format(count=update_count))
