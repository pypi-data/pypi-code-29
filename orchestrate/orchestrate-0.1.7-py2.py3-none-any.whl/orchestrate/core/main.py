from __future__ import print_function
import os
import six
import sys

from botocore.exceptions import NoRegionError
from cement.core.foundation import CementApp
from cement.ext.ext_argparse import ArgparseController
import yaml

from orchestrate.version import VERSION

from orchestrate.common import safe_format
from orchestrate.core.cement_utils import ArgparseArgumentHandler, expose
from orchestrate.core.exceptions import (
  CheckExecutableError
)
from orchestrate.core.paths import (
  check_iam_authenticator_executable,
  check_kubectl_executable,
  download_kubectl_executable,
  download_iam_authenticator_executable,
  get_bin_dir,
  ensure_dir,
)
from orchestrate.core.services.orchestrate_bag import OrchestrateServiceBag
from orchestrate.core.kubernetes.service import KubernetesError

class OrchestrateController(ArgparseController):
  class Meta(object):
    label = 'base'
    description = 'A machine learning training and tuning management tool built for parameter optimization'

  def default(self):
    print('usage: sigopt [options] <command> [<subcommand> ...]')
    print('\nLearn more at: https://app.sigopt.com/docs/orchestrate')
    print('\nTo see help messages, you can run:')
    print('  sigopt --help')
    print('  sigopt <command> --help')
    print('  sigopt <command> <subcommand> --help')

  @expose(help="Current version")
  def version(self):
    print(VERSION)

  def runner(self, local=False, quiet=False):
    directory = self.app.pargs.directory

    options = self.app.user_options
    self.app.services.options_validator_service.validate_orchestrate_options(**options)

    name = options.get('name')
    optimization_options = options.get('optimization')
    resource_options = options.get('resources_per_model')
    language = options.get('language')
    framework = options.get('framework')

    repository_name = options.get('aws', {}).get('ecr', {}).get('repository')

    if not local:
      self.app.services.aws_service.login_to_container_registry(repository_name)

    image_name = repository_name

    image = self.app.services.model_packer_service.build_image(
      image_name=image_name,
      directory=directory,
      install_commands=options.get('install'),
      run_commands=options.get('run'),
      optimization_options=optimization_options,
      language=language,
      framework=framework,
      quiet=quiet,
    )

    if local:
      return self.app.services.job_runner_service.run_local_job(
        name=name,
        image_name=repository_name,
        optimization_options=optimization_options,
      )
    else:
      descriptions = self.app.services.ecr_service.describe_repositories([repository_name])
      target = descriptions['repositories'][0]['repositoryUri']
      image.tag(repository=target)
      self.app.services.docker_service.push(target)
      return self.app.services.job_runner_service.run_job(
        name=name,
        image_name=target,
        optimization_options=optimization_options,
        resource_options=resource_options,
      )

  @expose(
    help="Initialize a directory for orchestrate. Use with sigopt init >> orchestrate.yml",
  )
  def init(self):
    print(
        """name: My Orchestrate Experiment
install:
  -  # Fill in install commands, such as pip install -r requirements.txt
run:
  -  # Fill in run command, such as python model.py
optimization:
  parameters:  # Fill in parameters to optimize
  parallel_bandwidth: 1
  observation_budget: 10
""")

  @expose(
    arguments=[
      (['--directory'], dict(help='orchestrate project directory, default: current directory', default='.')),
      (['-f', '--filename'], dict(help='orchestrate yaml file, default: orchestrate.yml', default='orchestrate.yml')),
      (['-q', '--quiet'], dict(help='only print the experiment id', action='store_true')),
    ],
    help="Run orchestrate experiment",
  )
  def run(self):
    self.app.services.cluster_service.assert_is_connected()

    quiet = self.app.pargs.quiet
    if not quiet:
      print('Containerizing your model and starting your experiment, this may take a few minutes...')

    experiment_id = self.runner(local=False, quiet=quiet)
    if self.app.pargs.quiet:
      print(experiment_id)
    else:
      print(safe_format('Started experiment "{}"', experiment_id))

  @expose(
    arguments=[
      (['--directory'], dict(help='orchestrate project directory, default: current directory', default='.')),
      (['-f', '--filename'], dict(help='orchestrate yaml file, default: orchestrate.yml', default='orchestrate.yml'))
    ],
    help="Run a orchestrate experiment in a local docker container",
  )
  def run_local(self):
    self.runner(local=True)

  @expose(
    arguments=[
      (['experiment'], dict(help='An experiment id')),
    ],
    help='Deletes an experiment on the cluster (experiment will still exist on sigopt.com)',
  )
  def delete(self):
    self.app.services.cluster_service.assert_is_connected()
    experiment_id = self.app.pargs.experiment

    job_name = self.app.services.job_runner_service.job_name(experiment_id)
    try:
      self.app.services.kubernetes_service.delete_jobs(job_name)
    except KubernetesError as e:
      if 'NotFound' in str(e):
        raise Exception(safe_format('We could not find an experiment {} running on your cluster', experiment_id))
      else:
        raise e

  @expose(
    arguments=[
      (['experiment'], dict(help='An experiment id')),
    ],
    help='Retrieve experiment status',
  )
  def status(self):
    self.app.services.cluster_service.assert_is_connected()
    experiment_id = self.app.pargs.experiment

    job_name = self.app.services.job_runner_service.job_name(experiment_id)
    try:
      job = self.app.services.kubernetes_service.get_jobs(job_name)
    except KubernetesError as e:
      if 'NotFound' in str(e):
        raise Exception(safe_format('We could not find an experiment {} running on your cluster', experiment_id))
      else:
        raise e

    parsed_job = self.app.services.job_status_service.parse_job(job)

    observations_by_pod = self.app.services.job_status_service.get_observations_by_pod(experiment_id)
    total_failures = sum(v['failed'] for v in observations_by_pod.values())
    parsed_pods = [
      self.app.services.job_status_service.parse_pod(pod, observations_by_pod)
      for pod
      in self.app.services.kubernetes_service.get_pods(job_name=job_name)['items']
    ]
    unschedulable_pods = [pod for pod in parsed_pods if pod['status'] == 'Unschedulable']

    print(safe_format('Job Name: {name}', **parsed_job))
    print(safe_format('Job Status: {status}', **parsed_job))
    print(safe_format(
      '\n{observation_count} / {observation_budget} Observations',
      **parsed_job
    ))
    print(safe_format('{} Observation(s) failed', total_failures))

    print('\nPod status:')
    print(safe_format(
      '\n{:20}\t{:25}\t{:20}\t{:20}',
      "Pod Name",
      "Status",
      "Success",
      "Failed",
    ))
    for parsed_pod in parsed_pods:
      print(safe_format(
        '{name:20}\t{status:25}\t{success:<20}\t{failed:<20}',
        **parsed_pod
      ))

    print(safe_format(
      '\nView more at: https://app.sigopt.com/experiment/{}',
      experiment_id
    ))
    if unschedulable_pods:
      print("The following pods are unable to be scheduled:", file=sys.stderr)
      for pod in unschedulable_pods:
        print(pod['name'], file=sys.stderr)
      print(
        "Check that your cluster has sufficient resources to schedule them."
        " Maybe you're missing some nodes?",
        file=sys.stderr,
      )

  @expose(
    help='Retrieve all experiments\' statuses',
  )
  def status_all(self):
    self.app.services.cluster_service.assert_is_connected()
    parsed_jobs = [
      self.app.services.job_status_service.parse_job(job)
      for job in
      self.app.services.kubernetes_service.get_jobs()['items']
    ]

    print(safe_format('Total Jobs: {}', len(parsed_jobs)))
    experiment_base_path = 'https://app.sigopt.com/experiment'
    print(safe_format(
      '{:20}\t{:40}\t{:20}\t{:20}',
      "Experiment ID",
      "Experiment URL",
      "Job Status",
      "Observations",
    ))
    for parsed_job in parsed_jobs:
      observation_progress = safe_format(
        '{observation_count} / {observation_budget}',
        **parsed_job
      )
      print(safe_format(
        '{experiment_id:20}\t{experiment_url:40}'
        '\t{status:20}'
        '\t{observation_progress:<20}',
        experiment_url=safe_format('{}/{}', experiment_base_path, parsed_job['experiment_id']),
        observation_progress=observation_progress,
        **parsed_job
      ))

  @expose(
    arguments=[
      (['experiment'], dict(help='An experiment id')),
      (['--tail', '-t'], dict(help='Option to tail all logs', action='store_true')),
      (['--color-off', '-c'], dict(help='Remove color from tailed logs', action='store_true')),
    ],
    help='Retrieve experiment logs',
  )
  def logs(self):
    self.app.services.cluster_service.assert_is_connected()
    if self.app.pargs.tail:
      self.app.services.job_logs_service.tail_logs(self.app.pargs.experiment, self.app.pargs.color_off)
    else:
      self.app.services.job_logs_service.get_logs(self.app.pargs.experiment)

  @expose(
    add_help=False,
    ignore_unknown_arguments=True,
  )
  def kubectl(self):
    self.app.services.cluster_service.assert_is_connected()
    cmd = self.app.services.kubernetes_service.kubectl_command
    args = [cmd] + self.app.args.unknown_args
    os.execvpe(
      cmd,
      args,
      self.app.services.kubernetes_service.kubectl_env(),
    )

  @expose(
    help='Check that Orchestrate is installed properly',
  )
  def test(self):
    print('Testing your installation of SigOpt Orchestrate, this make take a minute...')
    failed = False
    for name, check, extra in [
      (
        'kubectl',
        lambda: check_kubectl_executable(full_check=True),
        None,
      ),
      (
        'aws-iam-authenticator',
        lambda: check_iam_authenticator_executable(full_check=True),
        None,
      ),
      (
        'docker',
        self.app.services.docker_service.check_connection,
        None,
      ),
      (
        'SigOpt connection',
        self.app.services.sigopt_service.check_connection,
        "You can get your API token from https://app.sigopt.com/tokens/info."
        " See https://app.sigopt.com/docs/overview/authentication for more information.",
      ),
    ]:
      try:
        check()
      except Exception as e:
        print(safe_format("{} error: {}", name, str(e)))
        if extra:
          print(extra)
        failed = True

    if failed:
      print(
        "One or more checks failed."
        " Correct the issues and run `sigopt test` again."
      )
    else:
      print("All checks passed, you can start using SigOpt Orchestrate!")


class OrchestrateClusterController(ArgparseController):
  class Meta(object):
    label = 'cluster'
    stacked_on = 'base'
    stacked_type = 'nested'
    description = 'Handle the cluster interface'

  def default(self):
    print('run sigopt cluster -h to see a list of commands')

  @expose(
    help='create a cluster',
    arguments=[
      (['-f', '--filename'], dict(help='cluster config yaml file, default: cluster.yml', default='cluster.yml')),
    ],
  )
  def create(self):
    print('Creating your cluster, this process may take 10-15 minutes or longer...')

    cluster_name = self.app.services.cluster_service.create(options=self.app.user_options)

    print(safe_format('Successfully created kubernetes cluster: {}', cluster_name))

    filename = self.app.services.ec2_service.key_pair_location(cluster_name)
    print('*Optional:')
    print('\tTo ssh into any ec2 node in your cluster, use the username `ec2-user` with the key pair located at:')
    print(safe_format('\t\t{}', filename))
    print('\tExample:')
    print(safe_format('\t\tssh -i {} ec2-user@<node_dns_name>', filename))
    print('\tYou may be required to:')
    print('\t\t* change file permissions for the key pair')
    print('\t\t* change security groups on your ec2 instances')
    print('\tInstructions: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html')

  @expose(
    help='destroy a cluster',
    arguments=[
      (['--cluster-name', '-n'], dict(help='cluster name', required=True)),
    ],
  )
  def destroy(self):
    cluster_name = self.app.pargs.cluster_name
    print(safe_format('Destroying cluster {}, this process may take 10-15 minutes or longer...', cluster_name))
    self.app.services.cluster_service.destroy(cluster_name=cluster_name)
    print(safe_format('Successfully destroyed kubernetes cluster: {}', cluster_name))

  @expose(
    help='connect to a cluster',
    arguments=[
      (['--cluster-name', '-n'], dict(help='cluster name', required=True)),
    ],
  )
  def connect(self):
    cluster_name = self.app.pargs.cluster_name
    print(safe_format('Connecting to cluster...', cluster_name))
    self.app.services.cluster_service.connect(cluster_name=cluster_name)
    print(safe_format('Successfully connected to kubernetes cluster: {}', cluster_name))

  @expose(
    help='disconnect from a cluster',
    arguments=[
      (['--cluster-name', '-n'], dict(help='cluster name')),
      (['--all', '-a'], dict(help='disconnect from all connected clusters', action='store_true')),
    ],
  )
  def disconnect(self):
    cluster_name = self.app.pargs.cluster_name
    disconnect_all = self.app.pargs.all

    if cluster_name:
      print(safe_format('Disconnecting from cluster {}...', cluster_name))
    if disconnect_all:
      print('Disconnecting from all clusters...')

    self.app.services.cluster_service.disconnect(cluster_name, disconnect_all)
    if cluster_name:
      print(safe_format('Successfully disconnected from kubernetes cluster: {}', cluster_name))
    else:
      # TODO(alexandra): if we keep the --all option around we'll want to print out the cluster names again
      print(safe_format('Successfully disconnected from all kubernetes clusters'))

  @expose(help='test your current cluster connection')
  def test(self):
    print('Testing if you are connected to a cluster, this make take a moment...')
    cluster_name = self.app.services.cluster_service.test()
    print(safe_format('Successfully connected to kubernetes cluster: {}', cluster_name))


def check_binaries(app):
  ensure_dir(get_bin_dir())

  for check, download, name in [
    (check_kubectl_executable, download_kubectl_executable, 'kubernetes'),
    (check_iam_authenticator_executable, download_iam_authenticator_executable, 'aws iam-authentication'),
  ]:
    try:
      check()
    except CheckExecutableError:
      print(safe_format("Downloading {} executable, this could take some time...", name))
      download()
      check(full_check=True)

def load_options(app):
  try:
    with open(app.pargs.filename) as f:
      options = yaml.safe_load(f) or {}
    app.extend('user_options', options)
  except AttributeError:
    app.extend('user_options', None)


# TODO(alexandra): accept credentials as command line arguments for SigOpt and AWS
def extend_app_services(app):
  try:
    services = OrchestrateServiceBag(app.user_options)
  except NoRegionError as e:
    six.raise_from(
      Exception("No default region is selected, please run `aws configure`"),
      e,
    )
  app.extend('services', services)

class OrchestrateApp(CementApp):
  class Meta(object):
    label = 'sigopt'
    base_controller = 'base'
    argument_handler = ArgparseArgumentHandler
    handlers = [
      OrchestrateController,
      OrchestrateClusterController,
    ]
    hooks = [
      ('post_argument_parsing', check_binaries),
      ('post_argument_parsing', load_options),
      ('post_argument_parsing', extend_app_services),
    ]

def main():
  with OrchestrateApp() as app:
    app.run()
