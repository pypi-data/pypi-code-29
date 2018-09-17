from __future__ import print_function

import os
import posixpath
import sys
import tarfile

import docker

from build_utils import docker_utils, utils

def build_npm_package(execution_context, artifact_name, package_dir, node_version):
    full_package_dir = os.path.join(execution_context.dir_path, package_dir)

    docker_client = docker.from_env(version='auto')

    artifact_store = execution_context.build_context.get_artifact_store()

    # Build docker context only for calculating content hash
    # TODO: add node version argument and build script to hash
    build_context = docker_utils.create_build_context_archive(full_package_dir)
    build_context_hash = utils.compute_file_hash(build_context)
    
    artifact_file_name = "{0}.zip".format(build_context_hash)
    if artifact_store.has_artifact(artifact_file_name):
        print("Artifact {0} already exists in store, skipping...".format(artifact_file_name))
        return {
            'files': {
                artifact_name: artifact_store.get_artifact_location(artifact_file_name)
            }
        }

    bash_script = (
        """
        set -e
        cp -r /app/src/* /app/work
        apt-get update
        apt-get install -y zip
        npm install -q
        zip -rq pkg-dist.zip .
        npm test
        """)

    container = docker_client.containers.run(
        image="node:{0}".format(node_version),
        command="/bin/bash -c '{0}'".format(bash_script),
        detach=True,
        volumes={
            os.path.abspath(full_package_dir): {
                'bind': '/app/src',
                'mode': 'ro'
            }
        },
        working_dir='/app/work'
    )

    for line in container.logs(stdout=True, stderr=True, stream=True):
        sys.stdout.write(line)

    run_result = container.wait()

    if run_result['StatusCode'] != 0:
        raise RuntimeError("Node.js build failed.")

    zip_file_name = 'pkg-dist.zip'
    tar_stream = container.get_archive(posixpath.join('/app/work', zip_file_name))[0]
    tar_file_data = utils.read_file_stream(tar_stream)

    container.remove(v=True)
    
    with tarfile.TarFile(fileobj=tar_file_data) as tar_file:
        zip_file = tar_file.extractfile(zip_file_name)

        return {
            'files': {
                artifact_name: artifact_store.store_artifact_fileobj(
                    zip_file,
                    artifact_file_name
                )
            }
        }
