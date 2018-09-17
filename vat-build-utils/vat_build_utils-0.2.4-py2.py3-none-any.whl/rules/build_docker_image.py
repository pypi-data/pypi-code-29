from __future__ import print_function

import os

import docker

from build_utils import docker_utils, utils

def build_docker_image(execution_context, image_name, path, tag=None, dockerfile=None, include=None):
    full_path = os.path.join(execution_context.dir_path, path)

    docker_client = docker.APIClient(version='auto')

    docker_build_context = docker_utils.create_build_context_archive(full_path, include=include)
    docker_build_context_hash = utils.compute_file_hash(docker_build_context)
    docker_build_context.seek(0)

    tag = tag if tag is not None else docker_build_context_hash

    image_registry = execution_context.build_context.get_image_registry()

    full_tag = image_registry.get_full_image_tag(image_name, tag)
    # full_tag = "{0}:{1}".format(image_name, tag)

    if not image_registry.has_image(image_name, tag):
        docker_utils.build_docker_image(
            docker_client,
            tag=full_tag,
            fileobj=docker_build_context,
            custom_context=True,
            dockerfile=dockerfile
        )

        image_registry.push_image(image_name, tag)

    else:
        print("Image {0} already exists in registry, skipping...".format(full_tag))

    return {
        "images": {
            image_name: full_tag
        }
    }
