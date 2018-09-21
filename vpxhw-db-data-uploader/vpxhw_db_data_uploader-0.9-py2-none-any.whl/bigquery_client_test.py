#!/usr/bin/env python
import unittest
import mock
import os

import sys
try:
  from google.cloud import bigquery
except:
  sys.exit('google cloud bigquery client library not found')

from StringIO import StringIO

import gcloud.metric_data_upload_client.bigquery_client as BigqueryClientModule


class TimeOutError(Exception):
  pass


class BigQueryClientTest(unittest.TestCase):

  def setUp(self):
    self.client_mock = mock.create_autospec(spec=bigquery.Client, spec_set=True)

    self.dataset_mock = mock.create_autospec(
        spec=bigquery.dataset.Dataset, spec_set=True)
    self.client_mock.dataset.return_value = self.dataset_mock

    self.table_mock = mock.create_autospec(
        spec=bigquery.table.Table, spec_set=True)
    self.dataset_mock.table.return_value = self.table_mock
    self.table_mock.exists.return_value = True

    self.job_mock = mock.create_autospec(
        spec=bigquery.job.LoadTableFromStorageJob,
        spec_set=True,
        state='DONE',
        error_result=None)

    patcher = mock.patch.object(
        bigquery, 'Client', autospec=True, return_value=self.client_mock)
    self.client_ctor_mock = patcher.start()
    self.addCleanup(patcher.stop)

    patcher = mock.patch.object(
        bigquery.job,
        'LoadTableFromStorageJob',
        autospec=True,
        return_value=self.job_mock)
    self.job_ctor_mock = patcher.start()
    self.addCleanup(patcher.stop)

    patcher = mock.patch.object(
        BigqueryClientModule.time, 'sleep', autospec=True)
    self.sleep_mock = patcher.start()
    self.sleep_mock.side_effect = TimeOutError(
        'time.sleep is not supposed to be called in test')
    self.addCleanup(patcher.stop)

    self.bigquery_client = bigquery.Client(project='test_project')
    self.bq_client = BigqueryClientModule.BigQueryClient(self.bigquery_client)
    self.dataset_name = 'classified'
    self.table_name = 'youtube_cat_videos'
    self.table_schema = [bigquery.schema.SchemaField('video_name', 'STRING')]

  def testGetTableReturnsATableObject(self):
    self.bq_client._GetTable(self.dataset_name, self.table_name)
    self.table_mock.reload.assert_called_once_with()

  def testGetOrCreateTableGetsAnExistingTable(self):
    self.bq_client._GetOrCreateTable(self.dataset_name, self.table_name,
                                     self.table_schema)

    self.table_mock.reload.assert_called_once_with()
    self.table_mock.exists.assert_called_once_with()
    self.assertFalse(self.table_mock.create.called)

  def testGetOrCreateTableCreatesATableIfItDoesNotExist(self):
    self.table_mock.exists.return_value = False

    self.bq_client._GetOrCreateTable(self.dataset_name, self.table_name,
                                     self.table_schema)

    self.table_mock.exists.assert_called_once_with()
    self.table_mock.create.assert_called_once_with()
    self.assertEqual(self.table_schema, self.bq_client._table.schema)

  def testCreateMethodCreatesClientAndSetTable(self):
    bq_client = BigqueryClientModule.BigQueryClient.Create(
        self.bigquery_client, self.dataset_name, self.table_name,
        self.table_schema)

    self.table_mock.reload.assert_called_once_with()
    self.table_mock.exists.assert_called_once_with()
    self.assertFalse(self.table_mock.create.called)

  def testCreateMethodCreatesClientAndTableIfItDoesNotExist(self):
    self.table_mock.exists.return_value = False

    bq_client = BigqueryClientModule.BigQueryClient.Create(
        self.bigquery_client, self.dataset_name, self.table_name,
        self.table_schema)

    self.table_mock.exists.assert_called_once_with()
    self.table_mock.create.assert_called_once_with()
    self.assertEqual(self.table_schema, bq_client._table.schema)

  def testWaitForJobRaisesExceptionIfWaitIsCalledInTest(self):
    self.bq_client._GetTable(self.dataset_name, self.table_name)

    job = bigquery.job.LoadTableFromStorageJob(
        'load_job', self.bq_client._table, 'path_to_local_file',
        self.bq_client._bigquery_client)
    self.job_mock.state = None

    with self.assertRaises(TimeOutError):
      self.bq_client.WaitForJob(job)

    self.job_mock.reload.assert_called_once_with()

  def testWaitForJobReturnsWhenJobIsDone(self):
    self.bq_client._GetTable(self.dataset_name, self.table_name)

    job = bigquery.job.LoadTableFromStorageJob(
        'load_job', self.bq_client._table, 'path_to_local_file',
        self.bq_client._bigquery_client)

    self.bq_client.WaitForJob(job)

    self.job_mock.reload.assert_called_once_with()

  def testWaitForJobRaisesExceptionWhenJobErrors(self):
    self.bq_client._GetTable(self.dataset_name, self.table_name)

    job = bigquery.job.LoadTableFromStorageJob(
        'load_job', self.bq_client._table, 'path_to_local_file',
        self.bq_client._bigquery_client)

    self.job_mock.error_result = 'Job hits an error'

    with self.assertRaises(RuntimeError):
      self.bq_client.WaitForJob(job)

    self.job_mock.reload.assert_called_once_with()

  def testLoadDictDataWithFlatDataField(self):
    self.table_mock.upload_from_file.return_value = self.job_mock

    self.bq_client._GetTable(self.dataset_name, self.table_name)

    data = {'float_field': 27}
    expected_encoded_string = '{"float_field": 27}'

    self.bq_client.LoadDictData(data)

    self.table_mock.upload_from_file.assert_called_once_with(
        mock.ANY,
        source_format='NEWLINE_DELIMITED_JSON',
        size=len(expected_encoded_string))
    upload_from_file_args, upload_from_file_kwargs = self.table_mock.upload_from_file.call_args
    self.assertEqual(1, len(upload_from_file_args))
    self.assertEqual(expected_encoded_string,
                     upload_from_file_args[0].getvalue())

  def testLoadDictDataWithNestedDataField(self):
    self.table_mock.upload_from_file.return_value = self.job_mock

    self.bq_client._GetTable(self.dataset_name, self.table_name)

    nested_record = [{'string_field': 'hello'}]
    data = {'record_field': nested_record}
    expected_encoded_string = '{"record_field": [{"string_field": "hello"}]}'

    self.bq_client.LoadDictData(data)

    self.table_mock.upload_from_file.assert_called_once_with(
        mock.ANY,
        source_format='NEWLINE_DELIMITED_JSON',
        size=len(expected_encoded_string))
    upload_from_file_args, upload_from_file_kwargs = self.table_mock.upload_from_file.call_args
    self.assertEqual(1, len(upload_from_file_args))
    self.assertEqual(expected_encoded_string,
                     upload_from_file_args[0].getvalue())


# TODO(ray): Add this test

  def testLoadDataFromFileWithJsonFile(self):
    pass

  def testStreamingInsertDataWithFlatDataField(self):
    self.table_mock.insert_data.return_value = None

    self.bq_client._GetTable(self.dataset_name, self.table_name)

    DATA = {'float_field': 27}
    ROWS = [DATA]
    EXPECTED_ARG = [(27.0,)]

    self.table_mock.schema = [bigquery.SchemaField('float_field', 'FLOAT')]

    self.assertEqual(self.table_mock, self.bq_client._table)

    self.bq_client.StreamingInsertData(ROWS)

    self.table_mock.insert_data.assert_called_once_with(EXPECTED_ARG)

  def testStreamingInsertDataRaisesErrorWhenFailed(self):
    self.table_mock.insert_data.side_effect = BigqueryClientModule.StreamingInsertionError(
        'failed')

    self.bq_client._GetTable(self.dataset_name, self.table_name)

    DATA = {'float_field': 27}
    ROWS = [DATA]
    EXPECTED_ARG = [(27.0,)]

    self.table_mock.schema = [bigquery.SchemaField('float_field', 'FLOAT')]

    with self.assertRaises(BigqueryClientModule.StreamingInsertionError):
      self.bq_client.StreamingInsertData(ROWS)

    self.table_mock.insert_data.assert_called_once_with(EXPECTED_ARG)

if __name__ == '__main__':
  unittest.main()
