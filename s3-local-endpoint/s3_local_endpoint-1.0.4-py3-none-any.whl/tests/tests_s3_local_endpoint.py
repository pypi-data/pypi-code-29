from unittest import TestCase
from ..s3_local_endpoint import s3_local_endpoint as s3
from os.path import realpath, dirname, join

from os import environ

AWS_ACCESS_KEY_ID = environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = environ['AWS_SECRET_ACCESS_KEY']
AWS_S3_ENDPOINT_URL = environ['AWS_S3_ENDPOINT_URL']


class S3TestCase(TestCase):
    """
    " Unittests for the s3 library.
    """

    def setUp(self):
        """
        " Connect to the S3 gateway and create the unittest bucket.
        """

        # bucket name
        self.bucket = 'unittest'

        self.s3_client = s3(
            AWS_ACCESS_KEY_ID,
            AWS_SECRET_ACCESS_KEY,
            AWS_S3_ENDPOINT_URL,
            self.bucket)

    def tearDown(self):
        """
        " Delete the unittest bucket.
        """
        self.s3_client.delete_bucket(self.bucket)

    def test_s3_create_list_and_delete_bucket(self):
        """
        " Test bucket life cycle: creation, listing and deletion.
        """
        # bucket name
        bucket_test = 'unittest_test'

        # Test bucket creation
        res = self.s3_client.create_bucket(bucket_test)
        self.assertTrue(res)
        # Test bucket listing
        res = self.s3_client.list_buckets()
        self.assertTrue(bucket_test in res)
        # Test bucket deletion
        res = self.s3_client.delete_bucket(bucket_test)
        self.assertTrue(res)
        # Test bucket really deleted
        res = self.s3_client.list_buckets()
        self.assertTrue(bucket_test not in res)

    def test_s3_upload_list_generateurl_delete_file(self):
        """
        " Test s3 file upload, list, url generation and deletion.
        """
        # file for testing : this file
        src_file = realpath(__file__)

        # Test file upload
        res = self.s3_client.upload_file(src_file)
        self.assertTrue(res)
        # Test file list
        res = self.s3_client.list_files()
        self.assertTrue(src_file in res)
        # Test file url generation
        res = self.s3_client.generate_url(src_file)
        self.assertNotEqual(res, None)
        # Test file deletion
        res = self.s3_client.delete_file(src_file)
        self.assertTrue(res)

    def test_s3_multiple_files(self):
        """
        " Test s3 multiple file operation.
        """
        # file for testing : this file and the tested sourcefile
        tst_file = realpath(__file__)
        src_file = join(dirname(tst_file), '..', 's3_local_endpoint.py')
        # Test file uploads
        res = self.s3_client.upload_file(src_file)
        res = self.s3_client.upload_file(tst_file)
        res = self.s3_client.list_files()
        self.assertTrue(src_file in res)
        self.assertTrue(tst_file in res)
        # Test multiple file deletion
        res = self.s3_client.delete_all_files()
        self.assertTrue(res)
