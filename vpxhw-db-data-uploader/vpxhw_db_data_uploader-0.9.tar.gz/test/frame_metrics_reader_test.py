#!/usr/bin/env python
import unittest
from StringIO import StringIO

from gcloud.metric_data_upload_client.frame_metrics_reader import FrameMetricsReader
from gcloud.metric_data_upload_client.psnr_reader import PsnrFileReader
from gcloud.metric_data_upload_client.ssim_reader import SsimFileReader


class TestFrameMetricsReader(unittest.TestCase):

  def setUp(self):
    psnr_string = """Frame numbers       Frame PSNR         Average PSNR       Sequence PSNR
Ready Input Output  Lum   Cb    Cr     Lum   Cb    Cr     Lum   Cb    Cr
0     0     0       27.97 35.71 34.82 27.97 35.71 34.82  27.97 35.71 34.82
1     1     1       27.97 35.71 34.82 27.97 35.71 34.82  27.97 35.71 34.82
2     2     2       27.95 35.88 35.10 27.97 35.76 34.91  27.97 35.76 34.91
"""

    ssim_string = """Frame numbers       SSIM                 SSIM    Average SSIM
Ready Input Output  Lum    Cb     Cr     Total   Lum    Cb      Cr    Total
0     0     0       0.8461 0.8806 0.8774 0.8527  0.8461 0.8806 0.8774 0.8527
1     1     1       0.8461 0.8806 0.8774 0.8527  0.8461 0.8806 0.8774 0.8527
2     2     2       0.8453 0.8788 0.8813 0.8523  0.8458 0.8800 0.8787 0.8525
Average SSIM= 0.852121
"""

    self.psnr_string_io = StringIO(psnr_string)
    self.ssim_string_io = StringIO(ssim_string)

  def test_read_chooses_correct_reader(self):
    reader = FrameMetricsReader()
    reader.read_metric_file(self.ssim_string_io, 'ssim')

    df = reader.get_frame_metrics()

    expected_num_of_cols = len(SsimFileReader().ssim_columns)
    self.assertEqual(expected_num_of_cols, len(df.columns.values))
    self.assertEqual(3, len(df.index))

    self.assertEqual(df['Frame_SSIM_Cr'].values.tolist(),
                     [0.8774, 0.8774, 0.8813])
    self.assertEqual(df['Frame_SSIM_Total'].values.tolist(),
                     [0.8527, 0.8527, 0.8523])

  def test_read_psnr_and_ssim_string_io(self):
    reader = FrameMetricsReader()
    reader.read_metric_file(self.psnr_string_io, 'psnr')
    reader.read_metric_file(self.ssim_string_io, 'ssim')

    df = reader.get_frame_metrics()

    expected_num_of_cols = len(PsnrFileReader().psnr_columns) + len(
        SsimFileReader().ssim_columns) - len(PsnrFileReader().index_columns)
    self.assertEqual(expected_num_of_cols, len(df.columns.values))
    self.assertEqual(len(df.index), 3)

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

    self.assertEqual(df['Frame_SSIM_Cr'].values.tolist(),
                     [0.8774, 0.8774, 0.8813])
    self.assertEqual(df['Frame_SSIM_Total'].values.tolist(),
                     [0.8527, 0.8527, 0.8523])

  def test_raises_error_if_reader_not_found(self):
    reader = FrameMetricsReader()
    with self.assertRaises(Exception):
      reader.read_metric_file(self.psnr_string_io,
                              'this reader id does not exist')

  def test_read_sample_files(self):
    reader = FrameMetricsReader()
    import os
    rel_path = os.path.dirname(os.path.relpath(__file__))
    reader.read_metric_file(
        os.path.join(rel_path, 'test_files/sample.psnr'), 'psnr')
    reader.read_metric_file(
        os.path.join(rel_path, 'test_files/sample.ssim'), 'ssim')

    df = reader.get_frame_metrics()

    expected_num_of_cols = len(PsnrFileReader().psnr_columns) + len(
        SsimFileReader().ssim_columns) - len(PsnrFileReader().index_columns)
    self.assertEqual(expected_num_of_cols, len(df.columns.values))
    self.assertEqual(len(df.index), 3)

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

    self.assertEqual(df['Frame_SSIM_Cr'].values.tolist(),
                     [0.8774, 0.8774, 0.8813])
    self.assertEqual(df['Frame_SSIM_Total'].values.tolist(),
                     [0.8527, 0.8527, 0.8523])


if __name__ == '__main__':
  unittest.main()
