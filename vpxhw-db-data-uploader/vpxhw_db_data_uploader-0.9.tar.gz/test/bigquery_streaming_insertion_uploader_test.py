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

from gcloud.metric_data_upload_client.bigquery_streaming_insertion_uploader import BigqueryStreamingInsertionUploader
from gcloud.metric_data_upload_client.bigquery_client import BigQueryClient


class BigqueryStreamingInsertionUploaderTest(unittest.TestCase):

  def setUp(self):
    self.bigquery_client_mock = mock.create_autospec(
        spec=BigQueryClient, spec_set=True)

    self.bigquery_streaming_insertion_uploader = BigqueryStreamingInsertionUploader(
        self.bigquery_client_mock)

  @pytest.mark.uploader
  @pytest.mark.bigquery
  def testUploadWithFlatData(self):
    DATA = {'float_field': 27.73}

    self.bigquery_streaming_insertion_uploader.Upload(DATA)

    expected_arg = [DATA]
    self.bigquery_client_mock.StreamingInsertData.assert_called_once_with(
        expected_arg)

  @pytest.mark.uploader
  @pytest.mark.bigquery
  def testUploadWithNestedData(self):
    DATA = {
        'float_field': 27.73,
        'nested_field': {
            'int_field': 6,
            'string_field': 's'
        }
    }

    self.bigquery_streaming_insertion_uploader.Upload(DATA)

    expected_arg = [DATA]
    self.bigquery_client_mock.StreamingInsertData.assert_called_once_with(
        expected_arg)

  @pytest.mark.uploader
  @pytest.mark.bigquery
  def testUploadRaisesErrorIfFailed(self):
    DATA = {'float_field': 27.73}

    class StreamingInsertionError(Exception):
      pass

    self.bigquery_client_mock.StreamingInsertData.side_effect = StreamingInsertionError(
        'Died horribly')

    with self.assertRaises(StreamingInsertionError):
      self.bigquery_streaming_insertion_uploader.Upload(DATA)


if __name__ == '__main__':
  unittest.main()
