import random
import json
import sys
import os
import util
import semver

from docker import APIClient
from collections import namedtuple

SWAGGER_FIELD = 'swagger'
DOCKER_FIELD = 'docker'


def help(parser):
    parser.add_argument('--publish',
                        dest='publish',
                        action='store_true',
                        help='publish project components to remote repos')


def command(project, args, file_root):
    build_swagger(project, args, file_root)
    util.project_script('build')

    build_docker(project, args)


def build_swagger(project, args, file_root):
    if SWAGGER_FIELD in project:
        for api_args in project[SWAGGER_FIELD]:
            build_api_target(api_args, file_root)


def build_docker(project, args):
    if DOCKER_FIELD in project:
        base = project[DOCKER_FIELD]['base']
        images = project[DOCKER_FIELD]['images']

        for name, image in images.iteritems():
            build_docker_image(base, name, image, args.publish)


def build_api_target(args, file_root):
    sys.path.append(os.path.dirname(os.path.realpath(__file__ + '/../')))
    import api

    api.main(namedtuple("Args", args.keys())(*args.values()), file_root)


def build_docker_image(base, name, image, publish):
    dockerfile = 'docker/' + name + '/Dockerfile'
    context = 'docker/' + name if 'context' not in image else image['context']

    context_sum = random.getrandbits(128)

    if context_sum != image['checksum'] or publish:
        image['checksum'] = context_sum
        image['version'] = semver.bump_patch(image['version'])

        tag = base + ':' + name
        full_tag = tag + '-' + image['version']

        docker_build(tag, dockerfile, context)
        APIClient().tag(tag, full_tag)

        print
        print 'Image ' + full_tag + ' ready'

        if publish:
            push = APIClient().push(full_tag, stream=True)
            print_docker_result(push)

            print
            print 'Image ' + full_tag + ' pushed'
    else:
        print 'Skip ' + name + ' image building due to the checksum equality'


def docker_build(tag, dockerfile, context):
    build = APIClient().build(tag=tag,
                              dockerfile=os.getcwd() + '/' + dockerfile,
                              path=os.getcwd() + '/' + context)

    print_docker_result(build)


def print_docker_result(build):
    print
    for progress in build:
        message = json.loads(progress)

        if 'stream' in message:
            sys.stdout.write('\t' + message['stream'])

        if 'errorDetail' in message:
            sys.stderr.write(message['errorDetail']['message'] + '\n')
