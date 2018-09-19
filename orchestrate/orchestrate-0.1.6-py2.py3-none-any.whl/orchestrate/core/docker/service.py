from __future__ import print_function
import json
import os
import sys
from tempfile import NamedTemporaryFile

import docker
from six import raise_from

from orchestrate.common import safe_format
from orchestrate.core.exceptions import CheckConnectionError
from orchestrate.core.services.base import Service
from orchestrate.version import DOCKER_IMAGE_VERSION

class DockerService(Service):
  def __init__(self, services):
    super(DockerService, self).__init__(services)
    self._client = docker.from_env()

  @property
  def client(self):
    return self._client

  def check_connection(self):
    try:
      return self.run(
        safe_format('orchestrate/python:{}', DOCKER_IMAGE_VERSION),
        command='true',
        quiet=True,
      )
    except docker.DockerException as e:
      raise_from(
        CheckConnectionError(safe_format('An error occured while checking your docker connection: {}'), str(e)),
        e,
      )

  def print_logs(self, logs):
    for log in logs:
      sys.stdout.write(log)
      sys.stdout.flush()

  def stream_build_log(self, logs):
    for log_line in logs:
      for json_log in log_line.decode('utf-8').splitlines():
        parsed_log = json.loads(json_log)
        if 'error' in parsed_log:
          print(parsed_log['error'], file=sys.stderr)
          raise Exception(safe_format(
            "docker build error: {}",
            parsed_log['error'],
          ))
        try:
          yield parsed_log['stream']
        except KeyError:
          pass

  def build(
    self,
    tag=None,
    dockerfile_name=None,
    dockerfile_contents=None,
    directory=None,
    quiet=True,
    build_args=None,
  ):
    if dockerfile_contents:
      assert not dockerfile_name, \
        "only one of dockerfile_name, dockerfile_contents can be provided"
      with NamedTemporaryFile(mode='w', delete=False) as dockerfile_fp:
        dockerfile_fp.write(dockerfile_contents)
        dockerfile = dockerfile_fp.name
    else:
      dockerfile = dockerfile_name
    try:
      if quiet:
        return self.client.images.build(
          tag=tag,
          dockerfile=dockerfile,
          path=directory,
          quiet=quiet,
          buildargs=build_args,
        )[0]
      else:
        assert tag is not None, \
          "tag must be specified when quiet=False in order to return the appropriate image"
        raw_logs = self.client.api.build(
          tag=tag,
          dockerfile=dockerfile,
          path=directory,
          quiet=quiet,
          buildargs=build_args,
        )
        self.print_logs(self.stream_build_log(raw_logs))
        return self.client.images.get(tag)
    finally:
      if dockerfile_contents:
        os.remove(dockerfile)

  def push(self, repository, tag=None):
    for line in self.client.images.push(repository=repository, tag=tag, stream=True):
      for l in line.decode('utf-8').splitlines():
        obj = json.loads(l)
        if 'error' in obj:
          raise Exception(obj['error'])

  def login(self, username, password, server):
    response = self.client.login(username=username, password=password, registry=server)
    assert response.get('Status') == 'Login Succeeded', 'Failure logging into ECR registry with docker'

  def run(self, image, command=None, env=None, quiet=False):
    env = env or {}
    if quiet:
      self.client.containers.run(
        image,
        command=command,
        environment=env,
      )
    else:
      container = self.client.containers.run(
        image,
        command=command,
        detach=True,
        environment=env,
        stdout=True,
        stderr=True,
      )
      self.print_logs(container.logs(stream=True))
