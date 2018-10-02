import unittest

import pandas as pd

from eqi_analysis.core.analysis import Factor
from eqi_utils.utils.ResourceUtils import get_resource_filename
from eqi_analysis.core import entity

_TEST_FACTOR_PATH = get_resource_filename(__name__,
                                          'resource',
                                          'test_jobscreated.parquet')
_RAW_FACTOR_DF = pd.read_parquet(_TEST_FACTOR_PATH)


class TestAnalysis(unittest.TestCase):
    def test_registry_operations(self):
        factor_name = 'jobscreated_test'
        original_length = len(_RAW_FACTOR_DF)
        factor = Factor(_RAW_FACTOR_DF, 'RIC', factor_name)
        factor.upload_to_registry("A test factor")

        factor_from_db = entity.access.get_factor(factor_name)
        self.assertEqual(factor_from_db.name, factor_name)

        df_from_s3 = Factor.from_registry(factor_name)
        self.assertEqual(len(df_from_s3.raw_df), original_length)

        Factor.delete_from_registry(factor_name)

        factor_from_db = entity.access.find_factors(name=factor_name)
        self.assertEqual(len(factor_from_db), 0)
