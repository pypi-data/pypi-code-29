import unittest

import pandas as pd

from eqi_analysis.core import refdata
from eqi_utils.utils.ResourceUtils import get_resource_filename


class TestRefdata(unittest.TestCase):

    def test_refdata_operations(self):
        soc_df = pd.read_parquet(get_resource_filename(__name__,
                                                       'resource',
                                                       'SOC_major_groups.parquet'))
        name = 'soc_major_group'
        refdata.save_refdata_s3(soc_df, name=name, desc='soc major groups', ticker_type='')

        soc_from_db = refdata.get_refdata(name)
        self.assertEqual(soc_from_db.name, name)

        df_from_db = refdata.load_to_df(name)
        self.assertTrue(df_from_db.equals(soc_df))

        refdata.delete_refdata(name)

        soc_from_db = refdata.find_refdata(name=name)
        self.assertEqual(len(soc_from_db), 0)

    def test_refdata_queryable_operations(self):
        mv_df = pd.read_parquet(get_resource_filename(__name__,
                                                      'resource',
                                                      'ibm_tgt_mktval.parquet'))
        name = 'ibm_tgt_mktval'
        refdata.save_refdata_s3(mv_df, name=name, desc='market value for ibm/tgt', ticker_type='RIC')

        refdata_from_db = refdata.get_refdata(name)
        self.assertEqual(refdata_from_db.name, name)

        full_mv = refdata.load_to_df(name)
        self.assertTrue(full_mv.equals(mv_df))

        ibm_mv = refdata.load_to_df(name, tickers=['IBM.N'])
        ibm_mv_original = mv_df.to_eqi().e_in('asset', ['IBM.N']).to_pandas()
        self.assertTrue(ibm_mv.equals(ibm_mv_original))

        start_date = '2010-01-01'
        end_date = '2010-10-10'
        ibm_mv_partial = refdata.load_to_df(name, tickers=['IBM.N'], start_date=start_date, end_date=end_date)
        self.assertTrue((ibm_mv_partial.index.get_level_values('date') >= start_date).all())
        self.assertTrue((ibm_mv_partial.index.get_level_values('date') <= end_date).all())

        refdata.delete_refdata(name)
        refdata_from_db = refdata.find_refdata(name=name)
        self.assertEqual(len(refdata_from_db), 0)

        name = 'return_index_from_oracle'
        query = 'select * from playbox1.MAT_eqi_return_index'
        refdata.save_refdata_oracle(name=name, desc='return index from oracle', query=query, ticker_type='RIC',
                                    ticker_col_name='RIC_CD', date_col_name='MARKETDATE')

        refdata_from_db = refdata.get_refdata(name)
        self.assertEqual(refdata_from_db.name, name)

        ibm_mv = refdata.load_to_df(name, tickers=['IBM.N'])
        self.assertTrue((ibm_mv['RIC_CD'] == 'IBM.N').all())

        start_date_oracle = '01-jan-2010'
        end_date_oracle = '10-oct-2010'
        ibm_mv_partial = refdata.load_to_df(name, tickers=['IBM.N'], start_date=start_date_oracle,
                                            end_date=end_date_oracle)
        self.assertTrue((ibm_mv_partial['MARKETDATE'] >= start_date).all())
        self.assertTrue((ibm_mv_partial['MARKETDATE'] <= end_date).all())

        refdata.delete_refdata(name)
        refdata_from_db = refdata.find_refdata(name=name)
        self.assertEqual(len(refdata_from_db), 0)
