#!/usr/bin/env python
import pytest
import unittest
import pandas as pd
import mock

import gcloud.metric_data_upload_client.frame_size_reader as frame_size_reader


class TestFrameSizeReader(unittest.TestCase):

  def setUp(self):
    self.EXPECTED_DF = pd.DataFrame({
        'Frame_numbers_Ready':
            range(295),
        'Frame_numbers_Input':
            range(295),
        'Frame_numbers_Output':
            range(295),
        'frame_size_in_bits': [
            25264, 3976, 7200, 6624, 7008, 7064, 7232, 7336, 7336, 7912, 6640,
            6480, 6504, 6392, 6104, 5944, 6072, 5896, 6360, 6728, 8440, 7328,
            6224, 7448, 6912, 7032, 6696, 6784, 7256, 6592, 7272, 6840, 6400,
            6360, 6112, 6224, 7016, 6800, 7040, 6584, 6744, 7008, 6448, 5960,
            6432, 6568, 6984, 7080, 6616, 5928, 6208, 6016, 6064, 6016, 6360,
            5840, 5888, 5840, 5336, 5344, 22856, 6208, 5576, 5744, 6120, 6200,
            6576, 6928, 6496, 6424, 6408, 6768, 6312, 6448, 6264, 6376, 6408,
            5792, 5680, 5288, 4960, 5224, 4904, 4936, 4696, 4744, 4544, 4848,
            4888, 4456, 4536, 4864, 4976, 5624, 5048, 5064, 5112, 5480, 5376,
            6240, 6088, 5080, 6624, 5800, 7224, 6192, 7192, 6736, 6576, 6536,
            6336, 7056, 7104, 6648, 6672, 6264, 6800, 7384, 7024, 6992, 26376,
            6792, 6920, 6672, 6352, 5704, 5536, 5584, 6200, 5872, 5992, 5616,
            6536, 5448, 5176, 5592, 5600, 5496, 5552, 5352, 5312, 6080, 5728,
            5592, 5400, 5568, 5872, 5600, 4832, 5584, 5448, 5248, 6072, 7256,
            6616, 6208, 5768, 6040, 6432, 5520, 6272, 5880, 5632, 5888, 5824,
            6720, 6040, 6016, 6864, 5968, 6392, 6096, 5832, 6168, 6312, 5720,
            5968, 5416, 7032, 5928, 24832, 5552, 6168, 6000, 5920, 5800, 5968,
            6376, 5952, 6616, 6776, 6200, 5752, 5664, 5632, 5792, 6224, 6104,
            5872, 6816, 6672, 7440, 7424, 6712, 6776, 6528, 6888, 8048, 6656,
            7136, 7032, 6808, 6568, 6688, 7152, 6944, 6760, 7296, 7552, 6912,
            6952, 6712, 7352, 7648, 7592, 7752, 7936, 7552, 7808, 7880, 7688,
            7528, 7832, 8256, 8240, 7640, 7864, 7416, 7608, 7160, 26928, 7752,
            7168, 6808, 7008, 6840, 6696, 6432, 6504, 6584, 6328, 6264, 5896,
            6672, 6128, 6784, 6448, 5408, 5448, 5912, 5712, 6944, 6528, 5600,
            6880, 6624, 6456, 5680, 5728, 6168, 6544, 5776, 4976, 5736, 5048,
            4992, 4968, 5536, 5104, 5552, 4208, 4736, 5000, 4960, 4936, 5088,
            5392, 5816, 5376, 5256, 5560, 5616, 5560, 6120, 6136
        ],
    })

  @pytest.mark.reader
  @mock.patch.object(
      frame_size_reader.VideoAnalyzer, 'get_frame_sizes', autospec=True)
  def test_reader_reads_correct_file(self, get_frame_size_api_mock):
    reader = frame_size_reader.FrameSizeReader()
    df = reader.read_file('video_file')

    get_frame_size_api_mock.assert_called_once_with(mock.ANY, 'video_file')

  @pytest.mark.reader
  @mock.patch.object(
      frame_size_reader.VideoAnalyzer, 'get_frame_sizes', autospec=True)
  def test_read_formats_DF_correctly(self, get_frame_size_api_mock):
    FRAME_SIZES = [17, 4, 2]
    get_frame_size_api_mock.return_value = FRAME_SIZES

    reader = frame_size_reader.FrameSizeReader()
    df = reader.read_file('video_file')

    EXPECTED_DF = pd.DataFrame({
        'Frame_numbers_Ready': range(3),
        'Frame_numbers_Input': range(3),
        'Frame_numbers_Output': range(3),
        'frame_size_in_bits': FRAME_SIZES,
    })

    pd.testing.assert_frame_equal(df, EXPECTED_DF, check_like=True)

  @pytest.mark.reader
  @pytest.mark.fs
  def test_read_sample_video_file_returns_expected_DF(self):
    reader = frame_size_reader.FrameSizeReader()
    import os
    rel_path = os.path.dirname(os.path.relpath(__file__))
    df = reader.read_file(os.path.join(rel_path, 'test_files/sample.ivf'))

    pd.testing.assert_frame_equal(df, self.EXPECTED_DF, check_like=True)


if __name__ == '__main__':
  unittest.main()
