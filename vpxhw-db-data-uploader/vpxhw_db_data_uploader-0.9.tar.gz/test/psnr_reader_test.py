#!/usr/bin/env python
import pytest
import unittest
from StringIO import StringIO

from gcloud.metric_data_upload_client.psnr_reader import PsnrFileReader


class TestPsnrReader(unittest.TestCase):

  def setUp(self):
    strict_format_raw_file = """Frame numbers       Frame PSNR         Average PSNR       Sequence PSNR
Ready Input Output  Lum   Cb    Cr     Lum   Cb    Cr     Lum   Cb    Cr
0     0     0       27.97 35.71 34.82 27.97 35.71 34.82  27.97 35.71 34.82
1     1     1       27.97 35.71 34.82 27.97 35.71 34.82  27.97 35.71 34.82
2     2     2       27.95 35.88 35.10 27.97 35.76 34.91  27.97 35.76 34.91
"""

    self.strict_format_stringIO = StringIO(strict_format_raw_file)

  def test_read_on_strict_format_string_io(self):
    reader = PsnrFileReader()
    df = reader.read_file(self.strict_format_stringIO)

    self.assertEqual(df.columns.values.tolist(), reader.psnr_columns)
    self.assertEqual(3, len(df.index))

    self.assertEqual(df['Average_PSNR_Cr'].values.tolist(), [
        34.82,
        34.82,
        34.91,
    ])
    self.assertEqual(df['Frame_numbers_Output'].values.tolist(), [
        0,
        1,
        2,
    ])

    self.assertEqual(df.loc[0].values.tolist(), [
        0.0, 0.0, 0.0, 27.97, 35.71, 34.82, 27.97, 35.71, 34.82, 27.97, 35.71,
        34.82
    ])
    self.assertEqual(df.loc[2].values.tolist(), [
        2.0, 2.0, 2.0, 27.95, 35.88, 35.1, 27.97, 35.76, 34.91, 27.97, 35.76,
        34.91
    ])

  def test_read_on_file(self):
    reader = PsnrFileReader()
    import os
    rel_path = os.path.dirname(os.path.relpath(__file__))
    df = reader.read_file(os.path.join(rel_path, 'test_files/sample.psnr'))

    self.assertEqual(df.columns.values.tolist(), reader.psnr_columns)
    self.assertEqual(3, len(df.index))

    self.assertEqual(df['Average_PSNR_Cr'].values.tolist(), [
        34.82,
        34.82,
        34.91,
    ])
    self.assertEqual(df['Frame_numbers_Output'].values.tolist(), [
        0,
        1,
        2,
    ])

    self.assertEqual(df.loc[0].values.tolist(), [
        0.0, 0.0, 0.0, 27.97, 35.71, 34.82, 27.97, 35.71, 34.82, 27.97, 35.71,
        34.82
    ])
    self.assertEqual(df.loc[2].values.tolist(), [
        2.0, 2.0, 2.0, 27.95, 35.88, 35.1, 27.97, 35.76, 34.91, 27.97, 35.76,
        34.91
    ])

  def test_read_on_data_containing_NaN(self):
    DATA = """Frame numbers       Frame PSNR         Average PSNR       Sequence PSNR
Ready Input Output  Lum   Cb    Cr     Lum   Cb    Cr     Lum   Cb    Cr
0     0     0       27.97 NaN 34.82 27.97 35.71 34.82  27.97 35.71 NaN
"""
    DATA_STREAM = StringIO(DATA)

    reader = PsnrFileReader()
    df = reader.read_file(DATA_STREAM)

    self.assertEqual(1, len(df.index))
    self.assertEqual(df.loc[0].values.tolist(), [
        0.0, 0.0, 0.0, 27.97, None, 34.82, 27.97, 35.71, 34.82, 27.97, 35.71,
        None
    ])


if __name__ == '__main__':
  unittest.main()
