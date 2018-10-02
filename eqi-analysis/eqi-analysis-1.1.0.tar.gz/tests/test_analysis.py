import unittest

import pandas as pd

from eqi_analysis.core.analysis import Factor, Portfolio
from eqi_utils.utils.ResourceUtils import get_resource_filename

_TEST_FACTOR_PATH = get_resource_filename(__name__,
                                          'resource',
                                          'test_jobscreated.parquet')
_RAW_FACTOR_DF = pd.read_parquet(_TEST_FACTOR_PATH)


class TestAnalysis(unittest.TestCase):
    def test_generate_alphalens_factor(self):
        factor = Factor(_RAW_FACTOR_DF, 'RIC', 'jobscreated')
        portfolio = Portfolio(factor)
        portfolio.join_price()
        portfolio.to_alphalens_factor(resample_period='month_end')
        self.assertEquals(
            portfolio.alphalens_factor.index.get_level_values(0).freqstr, 'M')

        portfolio.to_alphalens_factor(resample_period='month_start')
        self.assertEquals(
            portfolio.alphalens_factor.index.get_level_values(0).freqstr, 'MS')

    def test_analyze(self):
        factor = Factor(_RAW_FACTOR_DF, 'RIC', 'jobscreated')
        portfolio = Portfolio(factor)
        portfolio.join_price()
        portfolio.to_alphalens_factor(resample_period='month_end')
        portfolio.analyze_by_alphalens()
    