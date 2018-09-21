#!/usr/bin/env python
import pytest
import unittest
import mock

from gcloud.metric_data_upload_client.video_quality_data_handler import VideoQualityDataHandler
from gcloud.metric_data_upload_client.uploader_interface import IUploader
from gcloud.metric_data_upload_client.metric_data_upload_client import MetricDataUploadClient


class MetricDataUploadClientTest(unittest.TestCase):

  def setUp(self):
    self.video_quality_data_handler_mock = mock.create_autospec(
        spec=VideoQualityDataHandler, spec_set=True)

    self.uploader_mock = mock.create_autospec(spec=IUploader, spec_set=True)

    self.metric_data_upload_client = MetricDataUploadClient(
        self.video_quality_data_handler_mock, self.uploader_mock)

  @pytest.mark.client
  def testConstructorRaisesAssertionErrorIfUploaderDoesNotImplementIUploader(
      self):
    with self.assertRaises(AssertionError):
      MetricDataUploadClient(self.video_quality_data_handler_mock, object())

  @pytest.mark.client
  def testUploadData(self):
    DATA = {'string_field': 'hello', 'float_field': 27.3}
    self.video_quality_data_handler_mock.GetDataFieldsFromProvider.return_value = DATA

    input_data_provider = {'encoder': 'white_dwarf'}
    self.metric_data_upload_client.UploadData(input_data_provider)

    self.video_quality_data_handler_mock.GetDataFieldsFromProvider.assert_called_once_with(
        input_data_provider)
    self.uploader_mock.Upload.assert_called_once_with(DATA)


if __name__ == '__main__':
  unittest.main()
