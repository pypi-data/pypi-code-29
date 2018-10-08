from unittest import TestCase
import boto3
import botocore
import os
from laundromat.cli import is_valid
from moto import mock_s3
from botocore.exceptions import ClientError

MY_BUCKET = "streamr-marketplace-pr-bucker"
MY_PREFIX = "mock_folder"


@mock_s3
class TestIs_valid(TestCase):

    def setUp(self):
        s3_client = boto3.client(
            "s3",
            region_name="eu-west-1",
            aws_access_key_id="fake_access_key",
            aws_secret_access_key="fake_secret_key",
        )
        try:
            s3_resource = boto3.resource(
                "s3",
                region_name="eu-west-1",
                aws_access_key_id="fake_access_key",
                aws_secret_access_key="fake_secret_key",
            )
            s3_resource.meta.client.head_bucket(Bucket=MY_BUCKET)
        except botocore.exceptions.ClientError:
            pass
        else:
            err = "{bucket} should not exist.".format(bucket=MY_BUCKET)
            raise EnvironmentError(err)

        s3_client.create_bucket(Bucket=MY_BUCKET)
        current_dir = os.path.dirname(__file__)
        fixtures_dir = os.path.join(current_dir, "fixtures")
        _upload_fixtures(MY_BUCKET, fixtures_dir)

    def tearDown(self):
        s3 = boto3.resource(
            "s3",
            region_name="eu-west-1",
            aws_access_key_id="fake_access_key",
            aws_secret_access_key="fake_secret_key",
        )
        bucket = s3.Bucket(MY_BUCKET)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()

    def test_expired_data(self):
        """
        Should not be valid a valid infra
        """
        self.assertFalse(is_valid(MY_BUCKET, -5))

    def test_valid_date(self):
        """
        Should  be valid a valid infra
        """
        self.assertTrue(is_valid(MY_BUCKET, 5))

    def test_non_int_age_max(self):
        """
        If the max age isn't a int it should throw an exception
        :return:
        """
        self.assertRaises(TypeError, is_valid, MY_BUCKET, "5")

    def test_non_str_bucket_name(self):
        """
         If the bucket name isn't a str it should throw an exception
         :return:
         """

        self.assertRaises(TypeError, is_valid, 0, 5)


def _upload_fixtures(bucket: str, fixtures_dir: str) -> None:
    client = boto3.client("s3")
    fixtures_paths = [
        os.path.join(path, filename)
        for path, _, files in os.walk(fixtures_dir)
        for filename in files
    ]
    for path in fixtures_paths:
        key = os.path.relpath(path, fixtures_dir)
        client.upload_file(Filename=path, Bucket=bucket, Key=key)
