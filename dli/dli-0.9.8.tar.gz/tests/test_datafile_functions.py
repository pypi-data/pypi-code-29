import logging
import os

import six

from backports import tempfile
from .common import SdkIntegrationTestCase, build_fake_s3fs
from unittest import skip
from mock import patch, call

from dli.client import utils
from dli.client.exceptions import (
    PackageNotFoundException,
    InvalidPayloadException,
    DatasetNotFoundException,
    DatafileNotFoundException,
    DownloadFailed
)


logger = logging.getLogger(__name__)


class DatafileFunctionsTestCase(SdkIntegrationTestCase):

    def setUp(self):
        super(DatafileFunctionsTestCase, self).setUp()

        self.package_id = self.create_package("test_datafile_functions")
        self.dataset_builder = self.dataset_builder(self.package_id, "test_datafile_functions")

    def create_dummy_datafile(self):
        dataset = self.client.register_dataset(
            self.dataset_builder.with_data_lake_storage("test-bucket")
        )
        datafile = self.client.register_s3_datafile(
            dataset.datasetId,
            "dummy",
            [os.path.relpath(__file__)],
            "prefix/"
        )
        return datafile

    def test_get_unknown_datafile_returns_none(self):
        self.assertIsNone(self.client.get_datafile("unknown"))

    def test_get_unknown_s3_datafile_returns_error(self):
        with self.assertRaises(DatafileNotFoundException):
            self.client.get_s3_datafile("unknown")

    def test_can_get_s3_datafile(self):
        s3_dataset = self.client.register_dataset(self.dataset_builder.with_data_lake_storage("test-bucket"))
        datafile = self.client.register_s3_datafile(
            s3_dataset.datasetId,
            "test_get_s3_datafile",
            [os.path.relpath(__file__)],
            "prefix/"
        )

        s3_datafile = self.client.get_s3_datafile(datafile.datafileId)
        self.assertEqual(s3_datafile.datafileId, datafile.datafileId)

    def test_register_datafile_metadata(self):
        files = [{'path': "/path/to/file/A", 'size': 99999}, {'path': "/path/to/file/B", 'size': 88888}]
        dataset = self.client.register_dataset(self.dataset_builder.with_external_storage(location="jdbc://connectionstring:1232/my-db"))
        datafile = self.client.register_datafile_metadata(
            dataset.datasetId,
            "test_register_dataset_metadata",
            files
        )

        self.assertEqual(datafile.datasetId, dataset.datasetId)
        self.assertEqual(datafile.files, files)

    def test_register_datafile_metadata_fails_when_no_files_provided(self):
        dataset = self.client.register_dataset(self.dataset_builder.with_external_storage(location="jdbc://connectionstring:1232/my-db"))
        with self.assertRaises(Exception):
            self.client.register_datafile_metadata(
                dataset.datasetId,
                "test_register_datafile_metadata_fails_when_no_files_provided",
                files=[]
            )

    def test_update_datafile_fails_for_unknown_datafile(self):
        with self.assertRaises(DatafileNotFoundException):
            self.client.edit_datafile_metadata("unknown")

    def test_register_s3_datafile_can_create_datafile_uploading_files(self):
        dataset = self.client.register_dataset(self.dataset_builder.with_data_lake_storage("test"))
        file = os.path.relpath(__file__)  # upload ourselves as a dataset
        datafile = self.client.register_s3_datafile(
            dataset.datasetId,
            "test_register_s3_datafile_can_create_datafile_uploading_files",
            [file],
            "prefix/"
        )

        self.assertIsNotNone(datafile)
        self.assertEqual(datafile.datasetId, dataset.datasetId)
        self.assertEqual(datafile.files, [
            {"path": "s3://dev-ihsm-dl-pkg-test/prefix/" + os.path.basename(file)}
        ])

    def test_register_datafile_metadata_on_datalake_dataset(self):
        dataset = self.client.register_dataset(self.dataset_builder.with_data_lake_storage("test"))
        file = os.path.relpath(__file__)  # upload ourselves as a dataset
        datafile = self.client.register_datafile_metadata(
            dataset.datasetId,
            "test_register_datafile_metadata_on_datalake_dataset",
            [
                {"path": "s3://dev-ihsm-dl-pkg-test/prefix/test"}
            ]
        )

        self.assertIsNotNone(datafile)
        self.assertEqual(datafile.datasetId, dataset.datasetId)

    def test_update_datafile_merges_changes_with_existing_datafile(self):
        datafile = self.create_dummy_datafile()
        updated = self.client.edit_datafile_metadata(
            datafile.datafileId,
            name="correct name"
        )

        self.assertEqual(datafile.datafileId, updated.datafileId)
        self.assertEqual(datafile.datasetId, updated.datasetId)
        self.assertEqual(datafile.files, updated.files)
        self.assertEqual(updated.name, "correct name")


    def test_can_delete_datafile(self):
        datafile = self.create_dummy_datafile()
        # delete the datafile
        self.client.delete_datafile(datafile.datafileId)
        # can't read it back
        self.assertIsNone(self.client.get_datafile(datafile.datafileId))

    def test_delete_unknown_datafile_raises_exception(self):
        with self.assertRaises(DatafileNotFoundException):
            self.client.delete_datafile("unknown")

    def test_can_add_files_to_existing_datafile(self):
        file = os.path.relpath(__file__)  # upload ourselves as a dataset
        file2 = '../test_sandbox/samples/data/AAPL.csv'

        dataset = self.client.register_dataset(self.dataset_builder.with_data_lake_storage("test"))
        datafile = self.client.register_s3_datafile(
            dataset.datasetId,
            "test_can_add_files_to_existing_datafile",
            [file],
            "prefix/"
        )

        updated = self.client.add_files_to_datafile(datafile.datafileId, 'prefix/', [file2])

        # countEqual asserts that the collections match disrespect of order
        # talk about naming stuff
        six.assertCountEqual(
            self,
            [
                {"path": "s3://dev-ihsm-dl-pkg-test/prefix/" + os.path.basename(file)},
                {"path": "s3://dev-ihsm-dl-pkg-test/prefix/" + os.path.basename(file2)}
            ],
            updated.files
        )

    def test_add_files_to_unknown_datafile_raises_exception(self):
        with self.assertRaises(DatafileNotFoundException):
            self.client.add_files_to_datafile('unknown', 'prefix', ["/path/to/file/A"])

    def test_register_datafile_to_nonexisting_dataset_raises_exception(self):
        with self.assertRaises(DatasetNotFoundException) as context:
            self.client.register_datafile_metadata(
                "unkknown",
                "test_register_datafile_to_nonexisting_dataset_raises_exception",
                [{'path': "/path/to/file/A"}, {'path': "/path/to/file/B"}]
            )
            self.assertTrue('No dataset found with id unknown' in context.exception)


class DownloadDatafileTestCase(SdkIntegrationTestCase):

    def setUp(self):
        super(DownloadDatafileTestCase, self).setUp()
        # create a package
        self.package_id = self.create_package("test download datafile")
        self.dataset_builder = self.dataset_builder(self.package_id, "test download datafile")

    def test_download_datafile_for_unknown_datafile_fails(self):
        with self.assertRaises(Exception):
            self.client.download_datafile("unknown")

    def test_download_datafile_retrieves_all_files_in_datafile(self):
        dataset = self.client.register_dataset(self.dataset_builder.with_data_lake_storage("test"))
        datafile = self.client.register_s3_datafile(
            dataset.datasetId,
            "test_download_dataset_retrieves_all_files_in_dataset",
            [
                '../test_sandbox/samples/data/AAPL.csv',
                '../test_sandbox/samples/data/MSFT.csv'
            ],
            "prefix/"
        )

        with tempfile.TemporaryDirectory() as dest:
            self.client.download_datafile(datafile.datafileId, dest)

            # validate we got the expected calls
            self.s3_download_mock.assert_has_calls([
                call("s3://dev-ihsm-dl-pkg-test/prefix/MSFT.csv", dest),
                call("s3://dev-ihsm-dl-pkg-test/prefix/AAPL.csv", dest),
                ],
                any_order=True
            )

    def test_download_dataset_keeps_going_if_a_file_in_the_dataset_fails(self):
        def _download(_, file, dest):
            if file.endswith("AAPL.csv"):
                raise Exception("")

        dataset = self.client.register_dataset(self.dataset_builder.with_data_lake_storage("test"))
        datafile = self.client.register_s3_datafile(
            dataset.datasetId,
            "test_download_dataset_keeps_going_if_a_file_in_the_dataset_fails",
            [
                '../test_sandbox/samples/data/AAPL.csv',
                '../test_sandbox/samples/data/MSFT.csv'
            ],
            "prefix/"
        )

        with self.assertRaises(DownloadFailed):
            with patch('dli.client.s3.Client.download_file', _download) as s3_download:
                with tempfile.TemporaryDirectory() as dest:
                    self.client.download_datafile(datafile.datafileId, dest)

                    # validate we got the expected calls
                    s3_download.assert_has_calls([
                        call("s3://dev-ihsm-dl-pkg-test/prefix/MSFT.csv", dest),
                        call("s3://dev-ihsm-dl-pkg-test/prefix/AAPL.csv", dest),
                        ],
                        any_order=True
                    )


@patch("dli.client.s3.build_s3fs", build_fake_s3fs)
class RegisterDatafileTestCase(SdkIntegrationTestCase):

    def set_s3_client_mock(self):
        pass

    def test_can_upload_datafile_when_provided_folder_with_relative_path(self):
        package_id = self.create_package(
            "test_can_upload_dataset_providing_folder_with_relative_path"
        )
        dataset = self.client.register_dataset(
            self.dataset_builder(
                package_id,
                "test_can_upload_dataset_providing_folder_with_relative_path"
            ).with_data_lake_storage("test")
        )
        sample_data = os.path.join(
            os.path.dirname(__file__),
            'resources/yahoo'
        )

        datafile = self.client.register_s3_datafile(
            dataset.datasetId,
            "desc",
            [sample_data],
            "prefix/"
        )

        # assert the files were uploaded and that
        # their sizes have been resolved
        self.assertIn({
                "path": "s3://dev-ihsm-dl-pkg-test/prefix/AAPL.csv",
                "size": os.path.getsize(os.path.join(sample_data, "AAPL.csv"))
            },
            datafile.files
        )
        self.assertIn({
                "path": "s3://dev-ihsm-dl-pkg-test/prefix/MSFT.csv",
                "size": os.path.getsize(os.path.join(sample_data, "MSFT.csv"))
            },
            datafile.files
        )

    def test_can_upload_datafile_files_recursively(self):
        package_id = self.create_package(
            "test_can_upload_dataset_files_recursively"
        )
        dataset = self.client.register_dataset(
            self.dataset_builder(
                package_id,
                "test_can_upload_dataset_files_recursively"
            ).with_data_lake_storage("test")
        )

        sample_data = os.path.join(
            os.path.dirname(__file__),
            'resources/stocks'
        )

        datafile = self.client.register_s3_datafile(
            dataset.datasetId,
            "desc",
            [sample_data],
            "prefix/"
        )

        # assert the files were uploaded and that
        # their sizes have been resolved
        self.assertIn({
            "path": "s3://dev-ihsm-dl-pkg-test/prefix/readme.txt",
            "size": os.path.getsize(os.path.join(sample_data, "readme.txt"))
        },
            datafile.files
        )
        self.assertIn({
            "path": "s3://dev-ihsm-dl-pkg-test/prefix/microsoft/MSFT.csv",
            "size": os.path.getsize(os.path.join(sample_data, "microsoft/MSFT.csv"))
        },
            datafile.files
        )
        self.assertIn({
            "path": "s3://dev-ihsm-dl-pkg-test/prefix/microsoft/AAPL.csv",
            "size": os.path.getsize(os.path.join(sample_data, "microsoft/AAPL.csv"))
        },
            datafile.files
        )
        self.assertIn({
            "path": "s3://dev-ihsm-dl-pkg-test/prefix/microsoft/cortana/master.txt",
            "size": os.path.getsize(os.path.join(sample_data, "microsoft/cortana/master.txt"))
        },
            datafile.files
        )

    def test_download_datafile_should_keep_folder_structure_as_in_datafile(self):
        sample_data = os.path.join(
            os.path.dirname(__file__),
            'resources/stocks'
        )

        package_id = self.create_package(
            "tddskfsaid"
        )
        dataset = self.client.register_dataset(
            self.dataset_builder(
                package_id,
                "tddskfsaid"
            ).with_data_lake_storage("test")
        )

        datafile = self.client.register_s3_datafile(
            dataset.datasetId,
            "tddskfsaid",
            [sample_data],
            "prefix/"
        )

        with tempfile.TemporaryDirectory() as dest:
            self.client.download_datafile(datafile.datafileId, dest)

            self.assertTrue(utils.path_for(dest, "prefix").exists())
            self.assertTrue(utils.path_for(dest, "prefix", "microsoft").exists())
            self.assertTrue(utils.path_for(dest, "prefix", "microsoft").exists())
            self.assertTrue(utils.path_for(dest, "prefix", "microsoft", "AAPL.csv").exists())
            self.assertTrue(utils.path_for(dest, "prefix", "microsoft", "MSFT.csv").exists())
            self.assertTrue(utils.path_for(dest, "prefix", "microsoft", "cortana").exists())
            self.assertTrue(utils.path_for(dest, "prefix", "microsoft", "cortana", "master.txt").exists())
