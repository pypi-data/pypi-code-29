import shutil
import os

import boto3
from botocore.exceptions import ClientError

class LocalArtifactStore(object):
    def __init__(self, config):
        self.path = config['path']

    def has_artifact(self, name):
        artifact_path = self._get_artifact_path(name)
        return os.path.isfile(artifact_path)

    def get_artifact_location(self, artifact_name):
        # Not so easy to check if an S3 object at a key exists
        return {
            'type': 'local',
            'path': self._get_artifact_path(artifact_name)
        }

    def store_artifact_file(self, file_path, artifact_name):
        artifact_path = self._get_artifact_path(artifact_name)

        shutil.copyfile(file_path, artifact_path)

        return {
            'type': 'local',
            'path': artifact_path
        }

    def store_artifact_fileobj(self, fileobj, artifact_name):
        artifact_path = self._get_artifact_path(artifact_name)

        with open(artifact_path, 'wb') as artifact_fileobj:
            shutil.copyfileobj(fileobj, artifact_fileobj)

        return {
            'type': 'local',
            'path': artifact_path
        }

    def _get_artifact_path(self, artifact_name):
        return os.path.join(self.path, artifact_name)
