import time

from django.test import TestCase
from django.conf import settings
from django.utils import translation
from django.core.management import call_command

from currencyware.currency import get_all_currencies
from currencyware.currency import get_all_currencies_sorted
from currencyware.currency import get_all_currencies_prioritized
from currencyware.currency import get_display
from currencyware import defaults as defs


class TestCountryCase(TestCase):
    """
    Country Test
    """
    def setUp(self):
        # call_command('compilemessages')
        pass

    def test_xlate_display(self):
        name = get_display('AED')
        self.assertEquals(name, 'UAE Dirham')

    def test_xlate_priority(self):
        translation.activate('zh-hant')
        name = get_display('AED')
        self.assertEquals(name, '阿拉伯聯合大公國迪拉姆')

    def test_xlate_en_unsorted(self):
        translation.activate('en')
        currencies = get_all_currencies()
        self.assertEquals(currencies[0][1], 'UAE Dirham')

    def test_xlate_en_sorted(self):
        translation.activate('en')
        currencies = get_all_currencies_sorted()
        self.assertEquals(currencies[0][1], 'Afghani')

    def test_xlate_en_prioritized(self):
        translation.activate('en')
        currencies = get_all_currencies_prioritized()
        self.assertEquals(currencies[0][1], 'Canadian Dollar')

    def test_xlate_fa_prioritized(self):
        translation.activate('fr')
        currencies = get_all_currencies_prioritized()
        self.assertEquals(currencies[0][1], 'Dollar canadien')