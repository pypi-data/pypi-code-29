#!/usr/bin/env python
import unittest
from StringIO import StringIO

from gcloud.metric_data_upload_client.ssim_reader import SsimFileReader


class TestSsimReader(unittest.TestCase):

  def setUp(self):
    strict_format_raw_file = """Frame numbers       SSIM                 SSIM    Average SSIM
Ready Input Output  Lum    Cb     Cr     Total   Lum    Cb      Cr    Total
0     0     0       0.8461 0.8806 0.8774 0.8527  0.8461 0.8806 0.8774 0.8527
1     1     1       0.8461 0.8806 0.8774 0.8527  0.8461 0.8806 0.8774 0.8527
2     2     2       0.8453 0.8788 0.8813 0.8523  0.8458 0.8800 0.8787 0.8525
Average SSIM= 0.852121
"""

    self.strict_format_stringIO = StringIO(strict_format_raw_file)

  def test_read_on_strict_format_string_io(self):
    reader = SsimFileReader()
    df = reader.read_file(self.strict_format_stringIO)

    self.assertEqual(df.columns.values.tolist(), reader.ssim_columns)
    self.assertEqual(3, len(df.index))

    self.assertEqual(df['Frame_numbers_Ready'].values.tolist(), [
        0,
        1,
        2,
    ])
    self.assertEqual(df['Frame_SSIM_Cb'].values.tolist(),
                     [0.8806, 0.8806, 0.8788])
    self.assertEqual(df['Average_SSIM_Total'].values.tolist(),
                     [0.8527, 0.8527, 0.8525])
    self.assertEqual(df['Frame_numbers_Output'].values.tolist(), [
        0,
        1,
        2,
    ])

    self.assertEqual(df.loc[0].values.tolist(), [
        0.0, 0.0, 0.0, 0.8461, 0.8806, 0.8774, 0.8527, 0.8461, 0.8806, 0.8774,
        0.8527
    ])
    self.assertEqual(df.loc[2].values.tolist(), [
        2.0, 2.0, 2.0, 0.8453, 0.8788, 0.8813, 0.8523, 0.8458, 0.88, 0.8787,
        0.8525
    ])

  def test_read_on_file(self):
    reader = SsimFileReader()
    import os
    rel_path = os.path.dirname(os.path.relpath(__file__))
    df = reader.read_file(os.path.join(rel_path, 'test_files/sample.ssim'))

    self.assertEqual(df.columns.values.tolist(), reader.ssim_columns)
    self.assertEqual(3, len(df.index))

    self.assertEqual(df['Frame_numbers_Ready'].values.tolist(), [
        0,
        1,
        2,
    ])
    self.assertEqual(df['Frame_SSIM_Cb'].values.tolist(),
                     [0.8806, 0.8806, 0.8788])
    self.assertEqual(df['Average_SSIM_Total'].values.tolist(),
                     [0.8527, 0.8527, 0.8525])
    self.assertEqual(df['Frame_numbers_Output'].values.tolist(), [
        0,
        1,
        2,
    ])

    self.assertEqual(df.loc[0].values.tolist(), [
        0.0, 0.0, 0.0, 0.8461, 0.8806, 0.8774, 0.8527, 0.8461, 0.8806, 0.8774,
        0.8527
    ])
    self.assertEqual(df.loc[2].values.tolist(), [
        2.0, 2.0, 2.0, 0.8453, 0.8788, 0.8813, 0.8523, 0.8458, 0.88, 0.8787,
        0.8525
    ])

  def test_read_on_data_containing_NaN(self):
    DATA = """Frame numbers       SSIM                 SSIM    Average SSIM
Ready Input Output  Lum    Cb     Cr     Total   Lum    Cb      Cr    Total
0     0     0       0.8461 0.8806 NaN 0.8527  0.8461 NaN 0.8774 0.8527
Average SSIM= 0.852121
"""
    DATA_STREAM = StringIO(DATA)

    reader = SsimFileReader()
    df = reader.read_file(DATA_STREAM)

    self.assertEqual(1, len(df.index))
    self.assertEqual(df.loc[0].values.tolist(), [
        0.0, 0.0, 0.0, 0.8461, 0.8806, None, 0.8527, 0.8461, None, 0.8774,
        0.8527
    ])


if __name__ == '__main__':
  unittest.main()
