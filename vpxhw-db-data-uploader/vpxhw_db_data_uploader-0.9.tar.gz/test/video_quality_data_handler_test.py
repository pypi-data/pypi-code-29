#!/usr/bin/env python
import unittest
import mock
import os
import pandas as pd
from StringIO import StringIO

from gcloud.metric_data_upload_client.schema_builder import SchemaBuilder
from gcloud.metric_data_upload_client.frame_metrics_reader import FrameMetricsReader
from gcloud.metric_data_upload_client.video_quality_data_handler import VideoQualityDataHandler


class VideoQualityDataHandlerTest(unittest.TestCase):

  def setUp(self):
    self.schema_builder = SchemaBuilder()
    self.frame_metrics_reader = FrameMetricsReader()
    self.video_quality_data_handler = VideoQualityDataHandler(
        self.schema_builder, self.frame_metrics_reader)

  @mock.patch.object(SchemaBuilder, 'build_schema_field_list', autospec=True)
  def testGetSchema(self, mock_method):
    mock_method.return_value = 'lord moldevort manifests'

    self.assertEqual('lord moldevort manifests',
                     self.video_quality_data_handler.GetSchema())

    mock_method.assert_called_once_with(
        self.schema_builder, record_fields=mock.ANY)

  @mock.patch.dict(os.environ, {'file': 'lol.yuv', 'avg_psnr': '14.6'})
  @mock.patch.object(FrameMetricsReader, 'read_metric_file', autospec=True)
  @mock.patch.object(FrameMetricsReader, 'get_frame_metrics', autospec=True)
  def testGetDataFieldsFromOsEnvironWithoutFrameMetricsFiles(
      self, get_frame_metrics_mock, read_metric_mock):

    expected = {'avg_psnr': '14.6', 'dataset': 'lol.yuv', 'user_tags': []}

    self.assertEqual(
        expected,
        self.video_quality_data_handler.GetDataFieldsFromProvider(os.environ))

    self.assertFalse(get_frame_metrics_mock.called)
    self.assertFalse(read_metric_mock.called)

  @mock.patch.dict(os.environ, {
      'file': 'lol.yuv',
      'avg_psnr': '14.6',
      'psnr_file': 'lol.psnr'
  })
  @mock.patch.object(FrameMetricsReader, 'read_metric_file', autospec=True)
  @mock.patch.object(FrameMetricsReader, 'get_frame_metrics', autospec=True)
  def testGetDataFieldsFromOsEnvironWithIncompleteFrameMetricsFiles(
      self, get_frame_metrics_mock, read_metric_mock):

    expected = {'avg_psnr': '14.6', 'dataset': 'lol.yuv', 'user_tags': []}

    self.assertEqual(
        expected,
        self.video_quality_data_handler.GetDataFieldsFromProvider(os.environ))

    self.assertFalse(get_frame_metrics_mock.called)
    self.assertFalse(read_metric_mock.called)

  @mock.patch.dict(
      os.environ, {
          'file': 'lol.yuv',
          'avg_psnr': '14.6',
          'psnr_file': 'lol.psnr',
          'ssim_file': 'lol.ssim',
          'encoded_video_path': 'video.ivf',
      })
  @mock.patch.object(FrameMetricsReader, 'read_metric_file', autospec=True)
  @mock.patch.object(FrameMetricsReader, 'get_frame_metrics', autospec=True)
  def testGetDataFieldsFromOsEnvironWithFrameMetricsFiles(
      self, get_frame_metrics_mock, read_metric_mock):
    expected_frame_metrics = [{
        'frame_seq': 1.0,
        'psnr': 23,
        'ssim': 0.89
    }, {
        'frame_seq': 2.0,
        'psnr': 22.6,
        'ssim': 0.875
    }]

    expected_data_fields = {
        'avg_psnr': '14.6',
        'dataset': 'lol.yuv',
        'frame_data': expected_frame_metrics,
        'user_tags': []
    }

    get_frame_metrics_mock.return_value = pd.DataFrame(expected_frame_metrics)

    self.assertEqual(
        expected_data_fields,
        self.video_quality_data_handler.GetDataFieldsFromProvider(os.environ))

    read_metric_mock.assert_any_call(self.frame_metrics_reader, 'lol.psnr',
                                     'psnr')
    read_metric_mock.assert_any_call(self.frame_metrics_reader, 'lol.ssim',
                                     'ssim')
    read_metric_mock.assert_any_call(self.frame_metrics_reader, 'video.ivf',
                                     'frame_size')

    get_frame_metrics_mock.assert_called_once_with(self.frame_metrics_reader)

  @mock.patch.object(os.environ, 'get', autospec=True)
  def testGetFlatDataFromOsEnvironReturnsCorrectValueForOneField(
      self, mock_method):
    mock_method.side_effect = lambda x: 42.0 if x == 'avg_psnr' else None

    expected = {'avg_psnr': 42.0, 'user_tags': []}

    self.assertEqual(
        expected,
        self.video_quality_data_handler._GetFlatDataFromProvider(os.environ))

    mock_method.assert_any_call('avg_psnr')

  @mock.patch.object(os.environ, 'get', autospec=True)
  def testGetFlatDataFromOsEnvironReturnsCorrectValueForTwoFields(
      self, mock_method):
    mock_method.side_effect = lambda x: {
        'gcstorage_raw_file_path': 'drive/raw.ivf',
        'gcstorage_container_file_path': 'drive/container.ivf',}.get(x, None)

    expected = {
        'encoded_video_file': 'drive/raw.ivf',
        'streaming_video_file': 'drive/container.ivf',
        'user_tags': [],
    }

    self.assertEqual(
        expected,
        self.video_quality_data_handler._GetFlatDataFromProvider(os.environ))

    mock_method.assert_any_call('gcstorage_raw_file_path')
    mock_method.assert_any_call('gcstorage_container_file_path')

  @mock.patch.object(FrameMetricsReader, 'read_metric_file', autospec=True)
  @mock.patch.object(FrameMetricsReader, 'get_frame_metrics', autospec=True)
  def testGetFrameByFrameDataFromFilesReturnsFrameMetrics(
      self, get_frame_metrics_mock, read_metric_mock):
    expected = [{
        'frame_seq': 1.0,
        'psnr': 23,
        'ssim': 0.89
    }, {
        'frame_seq': 2.0,
        'psnr': 22.6,
        'ssim': 0.875
    }]

    get_frame_metrics_mock.return_value = pd.DataFrame(expected)

    self.assertEqual(
        expected,
        self.video_quality_data_handler._GetFrameByFrameDataFromFiles(
            'angry_birds.psnr', 'angry_birds.ssim', 'angry_birds.ivf'))

    read_metric_mock.assert_any_call(self.frame_metrics_reader,
                                     'angry_birds.psnr', 'psnr')
    read_metric_mock.assert_any_call(self.frame_metrics_reader,
                                     'angry_birds.ssim', 'ssim')
    read_metric_mock.assert_any_call(self.frame_metrics_reader,
                                     'angry_birds.ivf', 'frame_size')

    get_frame_metrics_mock.assert_called_once_with(self.frame_metrics_reader)


if __name__ == '__main__':
  unittest.main()
