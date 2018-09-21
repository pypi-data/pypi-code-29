#!/usr/bin/env python
import pytest
import unittest
import mock
import os
import httplib2
import json

import sys
try:
  from google.cloud import bigquery
except:
  sys.exit('google cloud bigquery client library not found')

from gcloud.metric_data_upload_client.schema_builder import SchemaBuilder
from gcloud.metric_data_upload_client.frame_metrics_reader import FrameMetricsReader
from gcloud.metric_data_upload_client.video_quality_data_handler import VideoQualityDataHandler
from gcloud.metric_data_upload_client.bigquery_client import BigQueryClient
from gcloud.metric_data_upload_client.bigquery_streaming_insertion_uploader import BigqueryStreamingInsertionUploader
from gcloud.metric_data_upload_client.metric_data_upload_client import MetricDataUploadClient

import gcloud.metric_data_upload_client.metric_data_upload_client_main as main_module

from bigquery_client_integration_test import BigQueryClientIntegrationTestBase


class MetricDataUploadClientMainTest(BigQueryClientIntegrationTestBase):

  def setUp(self):
    self.http_mock = mock.create_autospec(spec=httplib2.Http, spec_set=True)
    self.http_mock.request.side_effect = self._CreateMockHttpSideEffect()

    schema_builder = SchemaBuilder()
    frame_metrics_reader = FrameMetricsReader()
    video_quality_data_handler = VideoQualityDataHandler(
        schema_builder, frame_metrics_reader)

    credential = self._make_credentials()
    bq_client = bigquery.Client(
        project=self.PROJECT, credentials=credential, _http=self.http_mock)
    bigquery_client = BigQueryClient.Create(
        bq_client, self.DS_NAME, self.TABLE_NAME,
        video_quality_data_handler.GetSchema())
    uploader = BigqueryStreamingInsertionUploader(bigquery_client)

    self.metric_data_upload_client = MetricDataUploadClient(
        video_quality_data_handler, uploader)

  @pytest.mark.main
  @pytest.mark.integration
  def testMainWithProvidedMetricDataUploadClient(self):
    from six.moves.urllib.parse import parse_qsl
    from six.moves.urllib.parse import urlsplit

    PROJECT_INFO_PROVIDER = {}
    DATA_PROVIDER = {
        'encoder': 'white_dwarf',
        'file': 'bloat.yuv',
        'avg_psnr': '14.6',
    }

    EXPECTED_PAYLOAD = ('{"rows": [{"json": {"dataset": "bloat.yuv", '
                        '"avg_psnr": "14.6", "encoder": "white_dwarf"}}]}')

    main_module.MetricDataUploadClientMain.Main(
        PROJECT_INFO_PROVIDER, DATA_PROVIDER, self.metric_data_upload_client)

    http_request_args, http_request_kwargs = self.http_mock.request.call_args

    request_uri = http_request_args[
        0] if http_request_args else http_request_kwargs['uri']
    self.assertIsNotNone(request_uri)

    scheme, netloc, path, qs, _ = urlsplit(request_uri)
    self.assertEqual(scheme, 'https')
    self.assertEqual(netloc, 'www.googleapis.com')
    self.assertEqual(
        path, '/bigquery/v2/projects/%s/datasets/%s/tables/%s/insertAll' %
        (self.PROJECT, self.DS_NAME, self.TABLE_NAME))

    self.assertIn(EXPECTED_PAYLOAD, http_request_kwargs['body'])

  @pytest.mark.main
  @pytest.mark.integration
  def testMainWithProvidedMetricDataUploadClientAndFrameMetricData(self):
    import os
    from six.moves.urllib.parse import parse_qsl
    from six.moves.urllib.parse import urlsplit

    PROJECT_INFO_PROVIDER = {}
    rel_path = os.path.dirname(os.path.relpath(__file__))
    DATA_PROVIDER = {
        'encoder': 'white_dwarf',
        'file': 'bloat.yuv',
        'avg_psnr': '14.6',
        'psnr_file': os.path.join(rel_path, 'test_files/sample.psnr'),
        'ssim_file': os.path.join(rel_path, 'test_files/sample.ssim')
    }

    main_module.MetricDataUploadClientMain.Main(
        PROJECT_INFO_PROVIDER, DATA_PROVIDER, self.metric_data_upload_client)

    http_request_args, http_request_kwargs = self.http_mock.request.call_args

    request_uri = http_request_args[
        0] if http_request_args else http_request_kwargs['uri']
    self.assertIsNotNone(request_uri)

    scheme, netloc, path, qs, _ = urlsplit(request_uri)
    self.assertEqual(scheme, 'https')
    self.assertEqual(netloc, 'www.googleapis.com')
    self.assertEqual(
        path, '/bigquery/v2/projects/%s/datasets/%s/tables/%s/insertAll' %
        (self.PROJECT, self.DS_NAME, self.TABLE_NAME))

    # TODO(rxuniverse): Add assertion on the body of the request

  @pytest.mark.main
  @pytest.mark.integration
  @mock.patch.object(main_module.MetricDataUploadClientFactory,
                     'BuildMetricDataUploadClient')
  def testMainWithoutFrameMetricData(self, factory_build_method_mock):
    from six.moves.urllib.parse import parse_qsl
    from six.moves.urllib.parse import urlsplit

    factory_build_method_mock.return_value = self.metric_data_upload_client

    PROJECT_INFO_PROVIDER = {
        'project': self.PROJECT,
        'dataset_name': self.DS_NAME,
        'table_name': self.TABLE_NAME
    }

    DATA_PROVIDER = {
        'encoder': 'white_dwarf',
        'file': 'bloat.yuv',
        'avg_psnr': '14.6',
    }

    EXPECTED_PAYLOAD = ('{"rows": [{"json": {"dataset": "bloat.yuv", '
                        '"avg_psnr": "14.6", "encoder": "white_dwarf"}}]}')

    main_module.MetricDataUploadClientMain.Main(PROJECT_INFO_PROVIDER,
                                                DATA_PROVIDER)

    factory_build_method_mock.assert_called_once_with(
        self.PROJECT, self.DS_NAME, self.TABLE_NAME)

    http_request_args, http_request_kwargs = self.http_mock.request.call_args

    request_uri = http_request_args[
        0] if http_request_args else http_request_kwargs['uri']
    self.assertIsNotNone(request_uri)

    scheme, netloc, path, qs, _ = urlsplit(request_uri)
    self.assertEqual(scheme, 'https')
    self.assertEqual(netloc, 'www.googleapis.com')
    self.assertEqual(
        path, '/bigquery/v2/projects/%s/datasets/%s/tables/%s/insertAll' %
        (self.PROJECT, self.DS_NAME, self.TABLE_NAME))

    self.assertIn(EXPECTED_PAYLOAD, http_request_kwargs['body'])


if __name__ == '__main__':
  unittest.main()
