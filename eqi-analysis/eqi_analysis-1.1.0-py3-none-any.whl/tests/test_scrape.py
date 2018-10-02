import unittest

from eqi_analysis.admin import scrape
from eqi_utils.utils.ResourceUtils import get_resource_filename


class TestScrape(unittest.TestCase):
    def test_fetch_price(self):
        price_df = scrape.fetch_price_bb('BEKB:BB')
        self.assertTrue(len(price_df) > 0)

        price_df = scrape.fetch_price_ric('IBM.N')
        self.assertTrue(len(price_df) > 0)

    def test_fetch_price_bulk(self):
        price_df = scrape.fetch_price_bulk(['BEKB:BB', 'IBM.N'],
                                           scrape.fetch_price_bb)
        print(price_df)
        self.assertEqual(len(price_df['asset'].unique()), 1)

        price_df = scrape.fetch_price_bulk(['BEKB:BB', 'IBM.N'],
                                           scrape.fetch_price_ric)
        self.assertEqual(len(price_df['asset'].unique()), 1)

    def test_fetch_libor(self):
        libor_df = scrape.fetch_libor()
        self.assertTrue(len(libor_df) > 0)

    def test_fetch_msci(self):
        msci_us_path = get_resource_filename(__name__,
                                             'resource',
                                             'msci_us.xls')
        msci_us_df = scrape.fetch_msci(msci_us_path)
        print(msci_us_df)
        self.assertTrue(len(msci_us_df) > 1)
