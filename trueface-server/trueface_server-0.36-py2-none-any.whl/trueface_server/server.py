# coding: utf-8
"""identify demo"""
# import mxnet as mx
# from mtcnn_detector import MtcnnDetector
# from imutils.object_detection import non_max_suppression
import time
import base64
import json
import traceback
import random
import string
import mss
import argparse
import docker
import os
from utilities import id_generator

def start_container(image_name, api_key, secret, port, use_gpu, sdk_token):
    """starts a trueface image"""
    client = docker.from_env()
    try:
        client.images.get(image_name)
    except docker.errors.ImageNotFound as err:
        print 'image %s not found, attempting to pull...' % image_name
        try:
            client.images.pull(image_name)
        except docker.errors.ImageNotFound as err:
            print err.explanation
            exit(1)
    name = "truefaceServer_%s" % id_generator()
    runtime = 'nvidia' if use_gpu else ''
    try:
        container = client.containers.run(image_name, ports={'8085/tcp': int(port)}, detach=True, tty=True, stdin_open=True, name=name, runtime=runtime)
        if sdk_token:
            creds = '{"api_key": "%s","secret": "%s", "sdk_token": "%s"}' % (api_key, secret, sdk_token)
        else:
            creds = '{"api_key": "%s","secret": "%s"}' % (api_key, secret)
        tar_stream = creds_to_tar(creds)
        success = container.put_archive('/', tar_stream)
        if not success:
            print 'Failed to copy creds file to server, aborting...'
            exit(1)
        container.exec_run(['pm2', 'start', 'app'])
    except docker.errors.APIError as err:
        print err.explanation
        exit(1)
    print container.id

def main():
    ap = argparse.ArgumentParser(description="Trueface.ai Server Management")
    ap.add_argument("-sc", "--start-server", default=False,
                    help="start a new server", action='store_true')
    ap.add_argument("-i", "--image-name", required=True,
                    help="the image name you'd like to start")
    ap.add_argument("-a", "--api-key", required=True,
                    help="your api key")
    ap.add_argument("-s", "--secret", required=True,
                    help="your secret")
    ap.add_argument("-t", "--sdk-token",
                    help="your sdk token (newer versions only)")
    ap.add_argument("-p", "--port", type=int, default=8085,
                    help="port to expose the container on")
    ap.add_argument("-g", "--use-gpu", default=False,
                    help="start server with GPU capabilities")

    args = vars(ap.parse_args())
    if args['start_server']:
        start_container(args["image_name"], args['api_key'], args['secret'], args['port'], args['use_gpu'], args['sdk_token'])

def creds_to_tar(creds):
    import tarfile
    import time
    from io import BytesIO

    tar_stream = BytesIO()
    creds_tar = tarfile.TarFile(fileobj=tar_stream, mode='w')
    file_data = creds.encode('utf8')
    tarinfo = tarfile.TarInfo(name='creds.json')
    tarinfo.size = len(file_data)
    tarinfo.mtime = time.time()
    creds_tar.addfile(tarinfo, BytesIO(file_data))
    creds_tar.close()
    tar_stream.seek(0)
    return tar_stream
