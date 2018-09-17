from __future__ import print_function

import hashlib
import io
import json
import os
import zipfile

from build_utils import docker_utils, utils

def create_elastic_beanstalk_docker_app_bundle(
        execution_context, artifact_name, image_name, container_port):
    # Get image tag from the output of previously run rules
    image_tag = execution_context.output['images'][image_name]

    dockerrun_config = {
        "AWSEBDockerrunVersion": "1",
        "Image": {
            "Name": image_tag,
            "Update": "false"
        },
        "Ports": [
            {
                "ContainerPort": str(container_port)
            }
        ],
        "Logging": "/var/log/nginx"
    }
    dockerrun_config_str = json.dumps(dockerrun_config)

    artifact_file_name = "{0}.zip".format(hashlib.sha1(dockerrun_config_str.encode()).hexdigest())
    artifact_store = execution_context.build_context.get_artifact_store()
    if artifact_store.has_artifact(artifact_file_name):
        print("Artifact {0} already exists in store, skipping...".format(artifact_file_name))
        artifact_location = artifact_store.get_artifact_location(artifact_file_name)
    else:
        print("Storing artifact {0}".format(artifact_file_name))

        artifact_fileobj = io.BytesIO()
        with zipfile.ZipFile(artifact_fileobj, 'w') as zip_file:
            zip_file.writestr(zipfile.ZipInfo('Dockerrun.aws.json'), dockerrun_config_str)
        artifact_fileobj.seek(0)
        artifact_location = artifact_store.store_artifact_fileobj(
            artifact_fileobj,
            artifact_file_name
        )

    return {
        'files': {
            artifact_name: artifact_location
        }
    }
