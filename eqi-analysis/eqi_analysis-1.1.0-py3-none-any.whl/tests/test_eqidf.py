import unittest

import pandas as pd
from pandas.core.groupby.groupby import DataFrameGroupBy

from eqi_analysis.core.extension import EQIDF
from eqi_utils.utils.ResourceUtils import get_resource_filename

_TEST_DF = pd.read_parquet(get_resource_filename(__name__,
                                                 'resource',
                                                 'test_categories.parquet'))

_CATEGORY_ID = 'category_id'
_CATEGORY_NAME = 'category_name'

_TEST_DF_FULL_IDX = _TEST_DF.reset_index().set_index(
    [_CATEGORY_ID, _CATEGORY_NAME])
_TEST_DF_BY_ID = _TEST_DF.reset_index().set_index([_CATEGORY_ID])
_TEST_DF_BY_NAME = _TEST_DF.reset_index().set_index([_CATEGORY_NAME])


class TestEQIDF(unittest.TestCase):
    def test_set_index(self):
        self.assertEquals(len(_TEST_DF_FULL_IDX.index.levels), 2)

        # Test set index on columns
        df_index_cols = (_TEST_DF.to_eqi()
                         .e_set_index(_CATEGORY_ID, _CATEGORY_NAME)
                         .to_pandas())
        self.assertListEqual(
            df_index_cols.index.names, [_CATEGORY_ID, _CATEGORY_NAME])

        # Test set index on existing indexes
        df_index_index = (_TEST_DF.to_eqi()
                          .e_set_index(_CATEGORY_NAME)
                          .to_pandas())
        self.assertListEqual(df_index_index.index.names, [_CATEGORY_NAME])

        # Test set index on both columns and indexes
        df_index_mix = (_TEST_DF_BY_ID.to_eqi()
                        .e_set_index(_CATEGORY_NAME, _CATEGORY_ID)
                        .to_pandas())
        self.assertListEqual(
            df_index_mix.index.names, [_CATEGORY_NAME, _CATEGORY_ID])

        # Test reset all
        df_index_reset = (_TEST_DF_BY_ID.to_eqi()
                          .e_set_index()
                          .to_pandas())

        self.assertNotIn(_CATEGORY_ID, df_index_reset.index.names)

    def test_not_null(self):
        original_len = len(_TEST_DF)
        original_none = _TEST_DF.copy()
        original_none.loc[original_len] = [None, 'test']
        self.assertEquals(len(original_none), original_len + 1)

        # Test none removal
        none_removed = (original_none.to_eqi()
                        .e_notnull(_CATEGORY_ID)
                        .to_pandas())

        self.assertEquals(len(none_removed), original_len)

        # Test nothing removed
        nothing_removed = (_TEST_DF.to_eqi()
                           .e_notnull(_CATEGORY_ID)
                           .to_pandas())
        self.assertEquals(len(nothing_removed), original_len)

        # Test passing empty names
        nothing_removed = (_TEST_DF.to_eqi()
                           .e_notnull()
                           .to_pandas())
        self.assertEquals(len(nothing_removed), original_len)

    def test_in(self):
        one_five = (_TEST_DF.to_eqi()
                    .e_in(_CATEGORY_ID, [1, 5])
                    .to_pandas())
        self.assertEquals(len(one_five), 2)

        non_exist = (_TEST_DF.to_eqi()
                     .e_in(_CATEGORY_ID, [-100])
                     .to_pandas())
        self.assertEquals(len(non_exist), 0)

        non_exist = (_TEST_DF.to_eqi()
                     .e_in(_CATEGORY_ID, {})
                     .to_pandas())
        self.assertEquals(len(non_exist), 0)

    def test_is(self):
        one = (_TEST_DF.to_eqi()
               .e_is(_CATEGORY_ID, 1)
               .to_pandas())
        self.assertEquals(len(one), 1)

        non_exist = (_TEST_DF.to_eqi()
                     .e_is(_CATEGORY_ID, -100)
                     .to_pandas())
        self.assertEquals(len(non_exist), 0)

    def test_is_between(self):
        one_to_ten = (_TEST_DF_BY_ID.to_eqi()
                      .e_between('index', 1, 10)
                      .to_pandas())
        self.assertEquals(len(one_to_ten), 10)

        ten_to_one = (_TEST_DF_BY_ID.to_eqi()
                      .e_between('index', 10, 1)
                      .to_pandas())
        self.assertEquals(len(ten_to_one), 0)

        length = len(_TEST_DF_BY_ID)

        one_to_end = (_TEST_DF_BY_ID.to_eqi()
                      .e_between('index', 1)
                      .to_pandas())
        self.assertEquals(len(one_to_end), length - 1)

        zero_to_end = (_TEST_DF_BY_ID.to_eqi()
                       .e_between('index', None, length - 1)
                       .to_pandas())
        self.assertEquals(len(zero_to_end), length)

        identity = (_TEST_DF_BY_ID.to_eqi()
                    .e_between('index')
                    .to_pandas())
        self.assertEquals(len(identity), length)

    def test_gt(self):
        length = len(_TEST_DF_BY_ID)

        two_to_end = (_TEST_DF_BY_ID.to_eqi()
                      .e_greater_than('index', 1)
                      .to_pandas())
        self.assertEquals(len(two_to_end), length - 2)

        nothing = (_TEST_DF_BY_ID.to_eqi()
                   .e_greater_than('index', 20000)
                   .to_pandas())
        self.assertEquals(len(nothing), 0)

    def test_lt(self):
        length = len(_TEST_DF_BY_ID)

        identity = (_TEST_DF_BY_ID.to_eqi()
                    .e_less_than('index', length)
                    .to_pandas())
        self.assertEquals(len(identity), length)

        nothing = (_TEST_DF_BY_ID.to_eqi()
                   .e_less_than('index', -1)
                   .to_pandas())
        self.assertEquals(len(nothing), 0)

    def test_select(self):
        category_ids = (_TEST_DF.to_eqi()
                        .e_select(_CATEGORY_ID)
                        .to_pandas())
        self.assertEquals(len(category_ids.columns), 1)
        self.assertEqual(category_ids.columns[0], _CATEGORY_ID)

        identity = (_TEST_DF.to_eqi()
                    .e_select(_CATEGORY_ID, _CATEGORY_NAME)
                    .to_pandas())
        self.assertEquals(len(identity.columns), 2)
        self.assertEqual(identity.columns[0], _CATEGORY_ID)
        self.assertEqual(identity.columns[1], _CATEGORY_NAME)

        identity = (_TEST_DF.to_eqi()
                    .e_select()
                    .to_pandas())
        self.assertEquals(len(identity), len(_TEST_DF))

    def test_groupby(self):
        groupby_index = (_TEST_DF_BY_ID.append(_TEST_DF_BY_ID).to_eqi()
                         .e_groupby(_CATEGORY_ID)
                         .to_pandas())
        self.assertIsInstance(groupby_index,
                              DataFrameGroupBy)
        self.assertEquals(len(groupby_index), len(_TEST_DF_BY_ID))

        groupby_column = (_TEST_DF.append(_TEST_DF).to_eqi()
                          .e_groupby(_CATEGORY_ID, _CATEGORY_NAME)
                          .to_pandas())
        self.assertIsInstance(groupby_column,
                              DataFrameGroupBy)
        self.assertEquals(len(groupby_column), len(_TEST_DF))
        self.assertListEqual(groupby_column.count().index.names,
                             [_CATEGORY_ID, _CATEGORY_NAME])

        groupby_mixed = (_TEST_DF_BY_ID.append(_TEST_DF_BY_ID).to_eqi()
                         .e_groupby(_CATEGORY_ID, _CATEGORY_NAME)
                         .to_pandas())
        self.assertIsInstance(groupby_mixed,
                              DataFrameGroupBy)
        self.assertEquals(len(groupby_mixed), len(_TEST_DF_BY_ID))
        self.assertListEqual(groupby_mixed.count().index.names,
                             [_CATEGORY_ID, _CATEGORY_NAME])

    def test_apply(self):
        def cnt(df):
            return len(df)

        cnted = (_TEST_DF_BY_ID.append(_TEST_DF_BY_ID).to_eqi()
                 .e_groupby(_CATEGORY_ID, _CATEGORY_NAME)
                 .e_apply(cnt)
                 .to_pandas())

        self.assertTrue((cnted == 2).all())

    def test_rename(self):
        renamed_mixed = (_TEST_DF_BY_ID.to_eqi()
                         .e_rename(
            {_CATEGORY_NAME: 'c_name', _CATEGORY_ID: 'c_id'})
                         .to_pandas())
        self.assertListEqual(renamed_mixed.index.names, ['c_id'])
        self.assertEquals(renamed_mixed.columns[1], 'c_name')

        renamed_colunn = (_TEST_DF_BY_ID.to_eqi()
                          .e_rename({_CATEGORY_NAME: 'c_name'})
                          .to_pandas())
        self.assertListEqual(renamed_colunn.index.names, [_CATEGORY_ID])
        self.assertEquals(renamed_colunn.columns[1], 'c_name')

        renamed_index = (_TEST_DF_BY_ID.to_eqi()
                         .e_rename({_CATEGORY_ID: 'c_id'})
                         .to_pandas())
        self.assertListEqual(renamed_index.index.names, ['c_id'])
        self.assertEquals(renamed_index.columns[1], _CATEGORY_NAME)

    def test_skip(self):
        length = len(_TEST_DF)
        skip_10 = (_TEST_DF.to_eqi()
                   .e_skip(10)
                   .to_pandas())
        self.assertEquals(len(skip_10), length - 10)

    def test_index_names(self):
        index_names = (_TEST_DF_FULL_IDX.to_eqi()
                       .e_index_names())
        self.assertListEqual(index_names, [_CATEGORY_ID, _CATEGORY_NAME])

    def test_limit(self):
        limit_10 = (_TEST_DF.to_eqi()
                    .e_limit(10)
                    .to_pandas())
        self.assertEquals(len(limit_10), 10)

    def test_normalize_by(self):
        all_ones = (_TEST_DF_FULL_IDX.to_eqi()
                    .e_normalize_by(_TEST_DF_FULL_IDX)
                    .to_pandas())
        is_one = all_ones.dropna() == 1
        self.assertTrue(is_one.iloc[:, 0].all())

    def test_has_dup_index(self):
        no_dup = (_TEST_DF_FULL_IDX.to_eqi()
                  .e_has_dup_index())
        self.assertFalse(no_dup)

        has_dup = (_TEST_DF_FULL_IDX.append(_TEST_DF_FULL_IDX).to_eqi()
                   .e_has_dup_index())
        self.assertTrue(has_dup)

    def test_set(self):
        df = (_TEST_DF_FULL_IDX.to_eqi()
              .e_set('index', 'index_plus_one', lambda v: v + 1)
              .to_pandas())
        is_one = (df['index_plus_one'] - df['index']).dropna() == 1
        self.assertTrue(is_one.all())

    def test_drop_dup_index(self):
        no_dup = (_TEST_DF_FULL_IDX.append(_TEST_DF_FULL_IDX).to_eqi()
                  .e_drop_dup_index()
                  .to_pandas())
        self.assertEquals(len(no_dup), len(_TEST_DF_FULL_IDX))

    def test_drop_level(self):
        no_c_id = (_TEST_DF_FULL_IDX.to_eqi()
                   .e_drop_level(_CATEGORY_ID)
                   .to_pandas())
        self.assertListEqual(no_c_id.index.names, [_CATEGORY_NAME])

    def test_drop(self):
        no_c_id = (_TEST_DF_FULL_IDX.to_eqi()
                   .e_drop(_CATEGORY_ID)
                   .to_pandas())
        self.assertListEqual(no_c_id.index.names, [_CATEGORY_NAME])

        no_c_name = (_TEST_DF.to_eqi()
                     .e_drop(_CATEGORY_NAME)
                     .to_pandas())
        self.assertEquals(len(no_c_name.columns), 1)
        self.assertEquals(no_c_name.columns[0], _CATEGORY_ID)

        no_c_id = (_TEST_DF_BY_ID.to_eqi()
                   .e_drop(_CATEGORY_ID)
                   .to_pandas())
        self.assertNotIn(_CATEGORY_ID, no_c_id.index.names)

    def test_unique(self):
        unique_ids = (_TEST_DF_FULL_IDX.to_eqi()
                      .e_unique(_CATEGORY_ID)
                      .to_pandas())
        self.assertEquals(len(unique_ids), len(_TEST_DF_FULL_IDX))

        unique_ids = (_TEST_DF.to_eqi()
                      .e_unique(_CATEGORY_ID)
                      .to_pandas())
        self.assertEquals(len(unique_ids), len(_TEST_DF_FULL_IDX))

    def test_where(self):
        even_indexes = (_TEST_DF_FULL_IDX.to_eqi()
                        .e_where('index', lambda i: i % 2 == 0)
                        .to_pandas())
        self.assertTrue(len(even_indexes), len(_TEST_DF_FULL_IDX) / 2)

    def test_astype(self):
        float_index = (_TEST_DF_BY_ID.to_eqi()
                       .e_astype({_CATEGORY_ID: float})
                       .to_pandas())
        self.assertEquals(float_index.index.dtype, 'float64')

        float_column = (_TEST_DF.to_eqi()
                        .e_astype({_CATEGORY_ID: float})
                        .to_pandas())
        self.assertEquals(float_column[_CATEGORY_ID].dtype, 'float64')

        float_index = (_TEST_DF_FULL_IDX.to_eqi()
                       .e_astype({_CATEGORY_ID: float})
                       .to_pandas())
        self.assertEquals(
            float_index.index.get_level_values(_CATEGORY_ID).dtype, 'float64')

    def test_to_set(self):
        id_set = (_TEST_DF_BY_ID.to_eqi()
                  .e_to_set(_CATEGORY_ID))
        self.assertIsInstance(id_set, set)
        self.assertEquals(len(id_set), len(_TEST_DF_BY_ID))

        id_set = (_TEST_DF.to_eqi()
                  .e_to_set(_CATEGORY_ID))
        self.assertIsInstance(id_set, set)
        self.assertEquals(len(id_set), len(_TEST_DF_BY_ID))

    def test_to_dict(self):
        id_name_map = (_TEST_DF_BY_ID.to_eqi()
                       .e_to_dict(_CATEGORY_NAME))
        self.assertIsInstance(id_name_map, dict)
        self.assertEquals(len(id_name_map), len(id_name_map))

    def test_draft(self):
        draft_df = (_TEST_DF_BY_ID.to_eqi()
                    .e_draft(force=True)
                    .e_select(_CATEGORY_NAME)
                    .to_pandas())
        self.assertEquals(len(draft_df), round(len(_TEST_DF_BY_ID) * 0.1))
