
import posixpath

import boto3
from botocore.exceptions import ClientError

class S3ArtifactStore(object):
    def __init__(self, config):
        self.bucket = config['bucket']
        self.prefix = config['prefix']

    def has_artifact(self, name):
        s3 = boto3.client('s3')

        # Not so easy to check if an S3 object at a key exists
        try:
            obj = s3.head_object(Bucket=self.bucket, Key=posixpath.join(self.prefix, name))
            return True
        except ClientError as exc:
            if exc.response['Error']['Code'] != '404':
                raise
            else:
                return False

    def get_artifact_location(self, name):
        # Not so easy to check if an S3 object at a key exists
        return {
            'type': 's3',
            'bucket': self.bucket,
            'key': posixpath.join(self.prefix, name)
        }

    def store_artifact_file(self, file_path, artifact_name):
        s3 = boto3.resource('s3')

        artifact_object = s3.Object(self.bucket, posixpath.join(self.prefix, artifact_name))
        artifact_object.upload_file(file_path)

        return {
            'type': 's3',
            'bucket': self.bucket,
            'key': artifact_object.key
        }

    def store_artifact_fileobj(self, fileobj, artifact_name):
        s3 = boto3.resource('s3')

        artifact_object = s3.Object(self.bucket, posixpath.join(self.prefix, artifact_name))
        artifact_object.upload_fileobj(fileobj)

        return {
            'type': 's3',
            'bucket': self.bucket,
            'key': artifact_object.key
        }
