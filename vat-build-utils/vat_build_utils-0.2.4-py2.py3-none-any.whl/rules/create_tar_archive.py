from __future__ import print_function

import os

from build_utils import docker_utils, utils

def create_tar_archive(execution_context, artifact_name, source_dir):
    artifact_store = execution_context.build_context.get_artifact_store()

    full_source_dir = os.path.join(execution_context.dir_path, source_dir)

    artifact_fileobj = docker_utils.create_tar(full_source_dir)
    artifact_hash = utils.compute_file_hash(artifact_fileobj)
    artifact_fileobj.seek(0)

    artifact_file_name = "{0}-{1}.tar".format(artifact_name, artifact_hash)
        
    if artifact_store.has_artifact(artifact_file_name):
        print("Artifact {0} already exists in store, skipping...".format(artifact_file_name))
        artifact_location = artifact_store.get_artifact_location(artifact_file_name)
    else:
        print("Storing artifact {0}".format(artifact_file_name))
        artifact_location = artifact_store.store_artifact_fileobj(
            artifact_fileobj,
            artifact_file_name
        )

    return {
        'files': {
            artifact_name: artifact_location
        }
    }
