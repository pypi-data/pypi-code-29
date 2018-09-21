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

from gcloud.metric_data_upload_client.bigquery_client import BigQueryClient, StreamingInsertionError


@pytest.mark.skip('google.cloud library updates broke all tests')
class BigQueryClientIntegrationTestBase(unittest.TestCase):
  SOURCE1 = 'http://example.com/source1.csv'
  PROJECT = 'project'
  DS_NAME = 'dataset-name'
  TABLE_NAME = 'table-name'
  JOB_NAME = 'job_name'
  JOB_TYPE = 'load'

  @staticmethod
  def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)

  def _setUpConstants(self):
    import datetime
    from google.cloud._helpers import UTC

    self.WHEN_TS = 1437767599.006
    self.WHEN = datetime.datetime.utcfromtimestamp(
        self.WHEN_TS).replace(tzinfo=UTC)
    self.ETAG = 'ETAG'
    self.TABLE_ID = '%s:%s:%s' % (self.PROJECT, self.DS_NAME, self.TABLE_NAME)
    self.RESOURCE_URL = 'http://example.com/path/to/resource'
    self.NUM_BYTES = 12345
    self.NUM_ROWS = 67
    self.JOB_ID = '%s:%s' % (self.PROJECT, self.JOB_NAME)
    self.USER_EMAIL = 'phred@example.com'

    self.INPUT_FILES = 2
    self.INPUT_BYTES = 12345
    self.OUTPUT_BYTES = 23456
    self.OUTPUT_ROWS = 345

  def _makeTableApiResource(self):
    self._setUpConstants()
    return {
        'creationTime': self.WHEN_TS * 1000,
        'tableReference': {
            'projectId': self.PROJECT,
            'datasetId': self.DS_NAME,
            'tableId': self.TABLE_NAME
        },
        'schema': {
            'fields': [{
                'name': 'encoder',
                'type': 'STRING',
                'mode': 'REQUIRED'
            }, {
                'name': 'dataset',
                'type': 'STRING',
                'mode': 'REQUIRED'
            }, {
                'name': 'avg_psnr',
                'type': 'FLOAT',
                'mode': 'REQUIRED'
            }]
        },
        'etag': 'ETAG',
        'id': self.TABLE_ID,
        'lastModifiedTime': self.WHEN_TS * 1000,
        'location': 'US',
        'selfLink': self.RESOURCE_URL,
        'numRows': self.NUM_ROWS,
        'numBytes': self.NUM_BYTES,
        'type': 'TABLE',
    }

  def _makeJobApiResource(self, ended=False):
    self._setUpConstants()
    resource = {
        'configuration': {
            self.JOB_TYPE: {
                'destinationTable': {
                    'projectId': self.PROJECT,
                    'datasetId': self.DS_NAME,
                    'tableId': self.TABLE_NAME,
                }
            },
        },
        'id': self.JOB_ID,
        'jobReference': {
            'projectId': self.PROJECT,
            'jobId': self.JOB_NAME,
        },
        'status': {
            'state': '',
            'errorResult': {},
            'errors': []
        },
    }

    if ended:
      resource['status']['state'] = 'DONE'

    return resource

  def _makeError(self):
    self._setUpConstants()
    return {
        'error': {
            'errors': [{
                'domain': 'global',
                'reason': 'notFound',
                'message': 'Not found: Table %s' % self.TABLE_ID,
            }],
            'code':
                404,
            'message':
                'Not found: Table %s' % self.TABLE_ID
        }
    }

  @staticmethod
  def _MakeHTTPSuccessResponse():
    from six.moves.http_client import OK
    return httplib2.Response({'status': OK, 'content-type': 'application/json'})

  def _CreateMockHttpSideEffect(self):
    GET_TABLE_URL = 'https://www.googleapis.com/bigquery/v2/projects/%s/datasets/%s/tables/%s' % (
        self.PROJECT, self.DS_NAME, self.TABLE_NAME)
    GET_TABLE_METHOD = 'GET'

    GET_JOB_URL = 'https://www.googleapis.com/bigquery/v2/projects/%s/jobs/%s' % (
        self.PROJECT, self.JOB_NAME)
    GET_JOB_METHOD = 'GET'

    START_JOB_URL = 'https://www.googleapis.com/upload/bigquery/v2/projects/%s/jobs' % (
        self.PROJECT)
    START_JOB_METHOD = 'POST'

    TABLE_INSERTION_URL = 'https://www.googleapis.com/bigquery/v2/projects/%s/datasets/%s/tables/%s/insertAll' % (
        self.PROJECT, self.DS_NAME, self.TABLE_NAME)
    TABLE_INSERTION_METHOD = 'POST'

    TABLE_API_RESOURCE = self._makeTableApiResource()
    JOB_API_RESOURCE = self._makeJobApiResource()
    FINISHED_JOB_API_RESOURCE = self._makeJobApiResource(ended=True)
    SUCCESS_RESPONSE = self._MakeHTTPSuccessResponse()

    def mock_http_side_effect(*args, **kwargs):
      import json
      from six.moves.urllib.parse import parse_qsl
      from six.moves.urllib.parse import urlsplit

      uri = kwargs['uri'] if 'uri' in kwargs else args[0]

      if uri.startswith(GET_TABLE_URL) and kwargs['method'] == GET_TABLE_METHOD:
        return (SUCCESS_RESPONSE, json.dumps(TABLE_API_RESOURCE))
      elif uri.startswith(GET_JOB_URL) and kwargs['method'] == GET_JOB_METHOD:
        return (SUCCESS_RESPONSE, json.dumps(FINISHED_JOB_API_RESOURCE))
      elif uri.startswith(
          START_JOB_URL) and kwargs['method'] == START_JOB_METHOD:
        return (SUCCESS_RESPONSE, json.dumps(JOB_API_RESOURCE))
      elif uri.startswith(
          TABLE_INSERTION_URL) and kwargs['method'] == TABLE_INSERTION_METHOD:
        return (SUCCESS_RESPONSE, {})
      else:
        print args
        print kwargs
        raise httplib2.ServerNotFoundError()

    return mock_http_side_effect


class BigQueryClientIntegrationTest(BigQueryClientIntegrationTestBase):

  def setUp(self):
    self.http_mock = mock.create_autospec(spec=httplib2.Http, spec_set=True)

    credential = self._make_credentials()
    bq_client = bigquery.Client(
        project=self.PROJECT, credentials=credential, _http=self.http_mock)
    self.bigquery_client = BigQueryClient(bq_client)

  @pytest.mark.bqclient
  @pytest.mark.integration
  def testBigQueryClientGetTable(self):
    URL = 'https://www.googleapis.com/bigquery/v2/projects/%s/datasets/%s/tables/%s' % (
        self.PROJECT, self.DS_NAME, self.TABLE_NAME)
    RESOURCE = self._makeTableApiResource()
    SUCCESS_RESPONSE = httplib2.Response({
        'status': 200,
        'content-type': 'application/json'
    })
    self.http_mock.request.return_value = (
        SUCCESS_RESPONSE,
        json.dumps(RESOURCE),
    )
    self.bigquery_client._GetTable(self.DS_NAME, self.TABLE_NAME)

    self.assertTrue(self.http_mock.request.called)

    http_request_args, http_request_kwargs = self.http_mock.request.call_args
    self.assertEqual('GET', http_request_kwargs['method'])
    self.assertEqual(URL, http_request_kwargs['uri'])
    self.assertIsNone(http_request_kwargs['body'])

  @pytest.mark.bqclient
  @pytest.mark.integration
  def testBigQueryClientGetOrCreateTableFetchesTable(self):
    URL = 'https://www.googleapis.com/bigquery/v2/projects/%s/datasets/%s/tables/%s' % (
        self.PROJECT, self.DS_NAME, self.TABLE_NAME)
    RESOURCE = self._makeTableApiResource()
    SUCCESS_RESPONSE = httplib2.Response({
        'status': 200,
        'content-type': 'application/json'
    })
    self.http_mock.request.return_value = (
        SUCCESS_RESPONSE,
        json.dumps(RESOURCE),
    )
    self.bigquery_client._GetOrCreateTable(self.DS_NAME, self.TABLE_NAME, [])

    self.assertTrue(self.http_mock.request.called)

    http_request_args, http_request_kwargs = self.http_mock.request.call_args
    self.assertEqual('GET', http_request_kwargs['method'])
    self.assertEqual(URL, http_request_kwargs['uri'])
    self.assertIsNone(http_request_kwargs['body'])

  @pytest.mark.bqclient
  @pytest.mark.integration
  def testBigQueryClientGetOrCreateTableCreatesTableIfItDoesNotExist(self):
    GET_TABLE_URL = 'https://www.googleapis.com/bigquery/v2/projects/%s/datasets/%s/tables/%s' % (
        self.PROJECT, self.DS_NAME, self.TABLE_NAME)
    GET_TABLE_METHOD = 'GET'

    INSERT_TABLE_URL = 'https://www.googleapis.com/bigquery/v2/projects/%s/datasets/%s/tables' % (
        self.PROJECT, self.DS_NAME)

    INSERT_TABLE_METHOD = 'POST'

    RESOURCE = self._makeTableApiResource()
    ERROR = self._makeError()
    NOT_FOUND_RESPONSE = httplib2.Response({
        'status': 404,
        'content-type': 'application/json'
    })
    SUCCESS_RESPONSE = httplib2.Response({
        'status': 200,
        'content-type': 'application/json'
    })

    def _table_not_found_and_created_side_effect(*args, **kwargs):
      import json
      if kwargs['uri'].startswith(GET_TABLE_URL) and kwargs['method'] == 'GET':
        return (NOT_FOUND_RESPONSE, json.dumps(ERROR))
      elif kwargs['uri'] == INSERT_TABLE_URL and kwargs['method'] == 'POST':
        return (SUCCESS_RESPONSE, json.dumps(RESOURCE))
      else:
        raise httplib2.ServerNotFoundError()

    self.http_mock.request.side_effect = _table_not_found_and_created_side_effect

    full_name = bigquery.SchemaField('full_name', 'STRING', mode='REQUIRED')
    age = bigquery.SchemaField('age', 'INTEGER', mode='REQUIRED')
    self.bigquery_client._GetOrCreateTable(self.DS_NAME, self.TABLE_NAME,
                                           [full_name, age])

    self.assertTrue(self.http_mock.request.called)

    http_request_args, http_request_kwargs = self.http_mock.request.call_args
    self.assertEqual(INSERT_TABLE_METHOD, http_request_kwargs['method'])
    self.assertEqual(INSERT_TABLE_URL, http_request_kwargs['uri'])

    PAYLOAD = {
        'tableReference': {
            'projectId': self.PROJECT,
            'datasetId': self.DS_NAME,
            'tableId': self.TABLE_NAME
        },
        'schema': {
            'fields': [{
                'name': 'full_name',
                'type': 'STRING',
                'mode': 'REQUIRED'
            }, {
                'name': 'age',
                'type': 'INTEGER',
                'mode': 'REQUIRED'
            }]
        },
    }

    self.assertEqual(json.dumps(PAYLOAD), http_request_kwargs['body'])

  @pytest.mark.bqclient
  @pytest.mark.integration
  def testBigQueryClientLoadData(self):
    from six.moves.urllib.parse import parse_qsl
    from six.moves.urllib.parse import urlsplit

    self.http_mock.request.side_effect = self._CreateMockHttpSideEffect()

    self.bigquery_client._GetTable(self.DS_NAME, self.TABLE_NAME)

    self.assertTrue(self.http_mock.request.called)

    data = {'float_field': 27}
    expected_encoded_string = '{"float_field": 27}'

    self.bigquery_client.LoadDictData(data)

    http_request_args, http_request_kwargs = self.http_mock.request.call_args_list[
        -2]

    self.assertEqual('POST', http_request_kwargs['method'])
    scheme, netloc, path, qs, _ = urlsplit(http_request_args[0])
    self.assertEqual(scheme, 'https')
    self.assertEqual(netloc, 'www.googleapis.com')
    self.assertEqual(path,
                     '/upload/bigquery/v2/projects/%s/jobs' % (self.PROJECT))
    self.assertEqual(dict(parse_qsl(qs)), {'uploadType': 'multipart'})
    self.assertIn(expected_encoded_string, http_request_kwargs['body'])

  @pytest.mark.bqclient
  @pytest.mark.integration
  def testBigQueryClientStreamingInsertionOfOneDataRow(self):
    from six.moves.urllib.parse import parse_qsl
    from six.moves.urllib.parse import urlsplit

    self.http_mock.request.side_effect = self._CreateMockHttpSideEffect()

    self.bigquery_client._GetTable(self.DS_NAME, self.TABLE_NAME)

    self.assertTrue(self.http_mock.request.called)

    DATA = [{
        'encoder': 'shrinkgun',
        'dataset': 'bigfatfile.yuv',
        'avg_psnr': 27.05
    }]
    EXPECTED_PAYLOAD = ('{"rows": [{"json": {"dataset": "bigfatfile.yuv", '
                        '"avg_psnr": 27.05, "encoder": "shrinkgun"}}]}')

    self.bigquery_client.StreamingInsertData(DATA)

    http_request_args, http_request_kwargs = self.http_mock.request.call_args

    self.assertEqual('POST', http_request_kwargs['method'])

    request_uri = http_request_args[
        0] if http_request_args else http_request_kwargs['uri']
    self.assertIsNotNone(request_uri)

    scheme, netloc, path, qs, _ = urlsplit(request_uri)
    self.assertEqual(scheme, 'https')
    self.assertEqual(netloc, 'www.googleapis.com')
    self.assertEqual(
        path, '/bigquery/v2/projects/%s/datasets/%s/tables/%s/insertAll' %
        (self.PROJECT, self.DS_NAME, self.TABLE_NAME))

    self.assertMultiLineEqual(EXPECTED_PAYLOAD, http_request_kwargs['body'])

  @pytest.mark.bqclient
  @pytest.mark.integration
  def testBigQueryClientStreamingInsertionOfTwoDataRows(self):
    from six.moves.urllib.parse import parse_qsl
    from six.moves.urllib.parse import urlsplit

    self.http_mock.request.side_effect = self._CreateMockHttpSideEffect()

    self.bigquery_client._GetTable(self.DS_NAME, self.TABLE_NAME)

    self.assertTrue(self.http_mock.request.called)

    DATA = [{
        'encoder': 'shrinkgun',
        'dataset': 'bigfatfile.yuv',
        'avg_psnr': 27.05
    }, {
        'encoder': 'eraser',
        'dataset': 'alien.yuv',
        'avg_psnr': 0.002
    }]
    EXPECTED_PAYLOAD = ('{"rows": [{"json": {"dataset": "bigfatfile.yuv", '
                        '"avg_psnr": 27.05, "encoder": "shrinkgun"}}, {"json": '
                        '{"dataset": "alien.yuv", "avg_psnr": 0.002, "encoder":'
                        ' "eraser"}}]}')

    self.bigquery_client.StreamingInsertData(DATA)

    http_request_args, http_request_kwargs = self.http_mock.request.call_args

    self.assertEqual('POST', http_request_kwargs['method'])

    request_uri = http_request_args[
        0] if http_request_args else http_request_kwargs['uri']
    self.assertIsNotNone(request_uri)

    scheme, netloc, path, qs, _ = urlsplit(request_uri)
    self.assertEqual(scheme, 'https')
    self.assertEqual(netloc, 'www.googleapis.com')
    self.assertEqual(
        path, '/bigquery/v2/projects/%s/datasets/%s/tables/%s/insertAll' %
        (self.PROJECT, self.DS_NAME, self.TABLE_NAME))

    self.assertMultiLineEqual(EXPECTED_PAYLOAD, http_request_kwargs['body'])

  @pytest.mark.bqclient
  @pytest.mark.integration
  def testBigQueryClientStreamingInsertionRaisesExceptionWhenFailed(self):
    self.http_mock.request.side_effect = self._CreateMockHttpSideEffect()

    self.bigquery_client._GetTable(self.DS_NAME, self.TABLE_NAME)

    self.assertTrue(self.http_mock.request.called)

    DATA = [{
        'encoder': 'shrinkgun',
        'dataset': 'bigfatfile.yuv',
        'avg_psnr': 27.05
    }]

    INSERTION_ERROR = {
        'insertErrors': [{
            'index':
                0,
            'errors': [{
                'reason': 'REASON',
                'location': 'LOCATION',
                'debugInfo': 'INFO',
                'message': 'MESSAGE'
            }]
        },]
    }

    self.http_mock.request.side_effect = None
    self.http_mock.request.return_value = (self._MakeHTTPSuccessResponse(),
                                           INSERTION_ERROR)

    with self.assertRaises(StreamingInsertionError):
      self.bigquery_client.StreamingInsertData(DATA)


if __name__ == '__main__':
  unittest.main()
