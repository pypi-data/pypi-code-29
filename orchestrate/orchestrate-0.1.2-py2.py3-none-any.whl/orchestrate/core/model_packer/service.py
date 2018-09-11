import json
import os
import shutil

from orchestrate.common import safe_format, TemporaryDirectory
from orchestrate.core.services.base import Service
from orchestrate.version import VERSION

LANGUAGE_MAP = {
  'python3.6': 'python3.6',
  'python3': 'python3.6',
  'python2.7': 'python2.7',
  'python2': 'python2.7',
  'python': 'python2.7',
}
FRAMEWORK_MAP = {
  'python': 'python',
  'cuda': 'cuda-9-0',
  'tensorflow': 'tensorflow-gpu',
  'theano': 'theano-gpu',
  'keras': 'keras-gpu',
  'pytorch': 'pytorch-gpu',
  'mxnet': 'mxnet-gpu',
}
SUPPORTED_LANGUAGES = sorted(set(LANGUAGE_MAP.values()))

def sanitize_command(cmd):
  return '' if cmd is None else str(cmd)

def sanitize_command_list(cmds):
  return [sanitize_command(cmd) for cmd in cmds] if cmds else []

class ModelPackerService(Service):
  def build_image(
    self,
    image_name,
    directory,
    install_commands,
    run_commands,
    optimization_options,
    language,
    framework,
  ):
    actual_language = LANGUAGE_MAP.get(language or 'python')
    actual_framework = framework or 'python'
    if actual_language is None:
      raise Exception(safe_format(
        "The language {} is not currently supported by orchestrate. Supported languages are {}.",
        language,
        ", ".join(SUPPORTED_LANGUAGES),
      ))
    python = actual_language
    pips = {
      'python2.7': 'pip2.7',
      'python3.6': 'pip3.6',
    }
    pip = pips[python]
    base_img = safe_format('orchestrate/{}:{}', FRAMEWORK_MAP[actual_framework], VERSION)
    intermediate_image = safe_format('{}-base', image_name)

    with TemporaryDirectory() as root_dirname:
      source_directory = directory
      destination_directory = os.path.join(root_dirname, 'orchestrate')
      bin_dirname = os.path.join(root_dirname, 'bin')
      etc_dirname = os.path.join(root_dirname, 'etc', 'orchestrate')
      var_dirname = os.path.join(root_dirname, 'var', 'orchestrate')
      shutil.copytree(source_directory, destination_directory)
      for dirname in (bin_dirname, etc_dirname, var_dirname):
        os.makedirs(dirname)

      config = {
        'metrics': optimization_options['metrics'],
        'parameters': optimization_options.get('parameters', []),
        'run_commands': sanitize_command_list(run_commands),
      }
      with open(os.path.join(etc_dirname, 'config.json'), 'w') as config_fp:
        json.dump(config, config_fp)

      self.services.docker_service.build(
        tag=intermediate_image,
        directory=root_dirname,
        dockerfile_contents=self.services.template_service.render_template_from_file(
          'model_packer/Dockerfile.intermediate.ms',
          dict(
            base_image=base_img,
            pip=pip,
            python=python,
          ),
        ),
      )

    with TemporaryDirectory() as temp_dirname:
      return self.services.docker_service.build(
        tag=image_name,
        directory=temp_dirname,
        dockerfile_contents=self.services.template_service.render_template_from_file(
          'model_packer/Dockerfile.setup.ms',
          dict(
            base_image=intermediate_image,
            install_commands=sanitize_command_list(install_commands),
          ),
        ),
        quiet=False,
      )
