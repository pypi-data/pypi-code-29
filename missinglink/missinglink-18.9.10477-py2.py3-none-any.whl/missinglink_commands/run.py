# -*- coding: utf8 -*-
import json
import logging
import os
import uuid
from traceback import format_exception_only
import six
import click
import yaml
from click import exceptions
import msgpack
from missinglink_commands.commons import output_result
from missinglink_commands.legit.api import ApiCaller
from missinglink_commands.utilities.options import CommonOptions
from missinglink_commands.utils import monitor_logs
from missinglink_kernel.callback.utilities import source_tracking
from mlcrypto import Asymmetric, MultiKeyEnvelope, SshIdentity


@click.group('run', help='runs an experiment on a cluster. By defaults run on a local cluster ')
def run_commands():
    pass


def _load_recipe(r_path):
    if not os.path.isfile(r_path):
        return {}
    else:
        print('loading defaults from recipe: %s' % r_path)
        with open(r_path) as f:
            return yaml.safe_load(f)


DEFAULT_RECIPE_PATH = '.ml_recipe.yaml'


def _source_tracking_data(path_=None):
    if path_ is None:
        path_ = os.getcwd()

    repo_obj = None
    src_data = {}
    try:
        repo_obj = source_tracking.get_repo(path_)
        src_data = _export_repo_state(repo_obj, mode='local')
    except Exception as ex:  # noinspection PyBroadException
        src_data['error'] = export_exception(ex)

    return src_data, repo_obj


def export_exception(ex):
    return ('\n'.join(format_exception_only(ex.__class__, ex))).strip()


def _export_repo_state(repo_obj, mode=None):
    mode = mode or 'local'
    src_data = {}
    try:
        src_data['branch'] = repo_obj.branch.name
        src_data['remote'] = repo_obj.remote_url
        src_data['sha_local'] = repo_obj.head_sha
        src_data['sha_local_url'] = repo_obj.head_sha_url
        src_data['is_dirty'] = not repo_obj.is_clean
        src_data['mode'] = mode

        commit_data = repo_obj.export_commit(repo_obj.repo.head.commit) if repo_obj.has_head else None

        if commit_data is not None:
            src_data.update(commit_data)

    # noinspection PyBroadException
    except Exception as ex:
        logging.exception('Failed to get repo state')
        src_data['error'] = export_exception(ex)

    logging.debug('_export_repo_state: %s', src_data)
    return src_data


def get_tracking_repo(repo_obj):
    repo_path = os.path.join(repo_obj.repo.working_dir, '.ml_tracking_repo')
    if os.path.isfile(repo_path):
        with open(repo_path) as f:
            tracking_repo = f.read().strip()
            logging.info('{} is tracked by {}'.format(repo_obj.repo.working_dir, tracking_repo))
            return tracking_repo
    # TODO: ADD QUERY to track server
    # return "git@github.com:missinglinkai/sim-test-remote-run.git"
    return None


def _validate_tracking_target(repo_obj, shadow_repo):
    if shadow_repo is None:
        return {'error': 'no tracking repository found.'}
    if shadow_repo.startswith('http'):
        return {'error': 'HTTP[S] git repositories are not supported. Please use the git/ssh version of {}'.format(shadow_repo)}
    return {'tracking_repository_url': shadow_repo}


def _sync_working_dir_if_needed(repo_obj, invocation_id):
    try:
        src_data = _validate_tracking_target(repo_obj, get_tracking_repo(repo_obj))
        if 'tracking_repository_url' in src_data:
            tracking_repository_url = src_data['tracking_repository_url']
            logging.info('Repository tracking is enabled. Tracking to repository: {}'.format(tracking_repository_url))
            source_tracking_repo = source_tracking.GitRepoSyncer.clone_tracking_repo(tracking_repository_url)
            commit_tag = source_tracking.GitRepoSyncer.merge_src_to_tracking_repository(repo_obj.repo, source_tracking_repo)
            shadow_repo_obj = source_tracking.get_repo(repo=source_tracking_repo)
            cur_br = source_tracking_repo.active_branch
            source_tracking_repo.git.checkout(commit_tag)
            shadow_repo_obj.refresh()
            src_data = _export_repo_state(shadow_repo_obj, mode='shadow')
            source_tracking_repo.git.checkout(cur_br)

        if 'error' not in src_data:
            logging.info('Tracking repository sync completed. This experiment source code is available here: {}'.format(src_data['sha_local_url']))
        else:
            logging.info('Tracking repository sync Failed. The Error was: {}'.format(src_data['error']))

        return src_data

    except Exception as ex:
        ex_txt = export_exception(ex)
        logging.exception("Failed to init repository tracking. This experiment may not be tracked")
        return {'error': ex_txt}


def parse_env_array_to_dict(env_array):
    if env_array is None:
        return {}

    if isinstance(env_array, six.string_types):
        env_array = json.loads(env_array)

    if isinstance(env_array, dict):
        return env_array

    res = {}
    for env_tuple in env_array:

        if isinstance(env_tuple, (tuple, list)):
            key = str(env_tuple[0])
            value = str(env_tuple[1])
        else:
            key, value = env_tuple.split('=')

        key = key.strip()
        value = value.strip()

        if (value.startswith("'") and value.endswith("'")) or (value.startswith('"') and value.endswith('"')):
            value = value[1:-1]
        res[key] = value
    return res


def _serialise_env_variables(variables):
    return json.dumps(variables)


def _build_run_args(kwargs):
    env = kwargs.pop('env', [])
    persistent_path = kwargs.pop('persistent_path', [])
    # persistent_path is [(s,t)] provided by the cli, persistent_paths is [{'host_path':s , 'mount_path': t}] restored from the yaml template
    persistent_paths = kwargs.pop('persistent_paths', {})
    if len(persistent_path) > 0:
        persistent_paths = []
        for host_path, mount_path in persistent_path:
            persistent_paths.append(dict(host_path=host_path, mount_path=mount_path))

    input_data = {
        'org': kwargs.pop('org', None),
        'requirements_txt': kwargs.pop('requirements_txt', None),
        'project': kwargs.pop('project', None),
        'image': kwargs.pop('image', 'missinglinkai/tensorflow:gce'),
        'git_repo': kwargs.pop('git_repo', None),
        'git_tag': kwargs.pop('git_tag', None),
        'source_dir': kwargs.pop('source_dir', None),
        'command': kwargs.pop('command', None),
        'data_query': kwargs.pop('data_query', None),
        'data_volume': kwargs.pop('data_volume', None),
        'data_use_iterator': kwargs.pop('data_iterator', kwargs.pop('data_use_iterator', None)),
        'data_dest_folder': kwargs.pop('data_dest', None),
        'output_paths': kwargs.pop('output_paths', []),
        'persistent_paths': persistent_paths,
        'gpu': kwargs.pop('gpu', True),
        'git_identity': kwargs.pop('git_identity', None),
        'env': parse_env_array_to_dict(env)
    }

    return input_data


def _read_input_data_and_load_recipe(kwargs):
    # Load Recipe
    recipe = kwargs.pop('recipe', None)
    recipe_data = _load_recipe(recipe or DEFAULT_RECIPE_PATH)
    for k, v in recipe_data.items():
        if k not in kwargs:
            kwargs[k] = v

    # Apply Defaults
    input_data = _build_run_args(kwargs)

    # Data test must reside inside /data as it will reside inside the data folder, until is configurable
    if not (input_data.get('data_dest_folder', ) or '/data').startswith('/data'):
        raise click.BadOptionUsage('`--data_dest` must begin with /data')

    if input_data.get('image') is None and input_data.get('command') is None:
        raise exceptions.BadOptionUsage('No command nor image provided')

    if input_data.get('project') is None:
        raise exceptions.BadOptionUsage('Please provide `project`')

    if input_data.get('org') is None:
        raise exceptions.BadOptionUsage('Please provide `org`')

    return input_data


def _has_valid_git_pointer(input_data):
    logging.debug('is valid git pointer? %s', input_data)
    is_valid = input_data.get('git_repo') is not None
    if is_valid:
        input_data['git_mode'] = input_data.get('git_mode', 'external')
    return is_valid


def _build_src_pointer(input_data):
    if not _has_valid_git_pointer(input_data):
        exp_id = uuid.uuid4().hex[:5]
        src_repo, x = _source_tracking_data(input_data.get('source_dir'))
        sync_res = _sync_working_dir_if_needed(x, exp_id)
        if 'error' in sync_res:
            logging.error(sync_res['error'])
        else:
            input_data['git_repo'] = sync_res['remote']
            input_data['git_tag'] = sync_res['branch']
            input_data['git_mode'] = sync_res['mode']

        if not _has_valid_git_pointer(input_data):  # still
            logging.warning('Failed to obtain git point. input was %s', input_data)
            raise exceptions.BadOptionUsage('Failed to obtain git point to use fo the experiment. please provide --git-repo, or --source-dir if you have shadow repository tracking enabled')
            # todo: find the current git path and get tracing path from the server if we don't have git point
            # todo better handling of ignoring

        return input_data


def _is_none_ish(val):
    return val is None or val == () or val == [] or val == {}


def _save_recipe(input_data, save_recipe):
    with open(save_recipe, 'w') as f:
        save_data = {k: v for k, v in input_data.items() if not _is_none_ish(v)}
        yaml.safe_dump(save_data, f, default_flow_style=False)
        click.echo(yaml.safe_dump(save_data, default_flow_style=False))
        click.echo('Recipe saved to {}'.format(save_recipe))

    return True


def _get_docker_creds(kwargs):
    user = kwargs.pop('docker_user', None)
    password = kwargs.pop('docker_password', None)
    endpoint = kwargs.pop('docker_host', None)
    if endpoint is not None or password is not None:
        return dict(user=user, password=password, endpoint=endpoint)

    return None


def _get_secure_env(kwargs):
    envs = kwargs.pop('secure_env', ())
    res = {}
    for item in envs:
        k, v = item
        res[k] = v
    return res


def _filter_input_dict_value(value):
    if value in (None, (), []):
        return False

    return True


@run_commands.command('track')
@click.pass_context
@CommonOptions.org_option(required=False)
def run_experiment(ctx, **kwargs):
    print(_build_src_pointer({}))


@run_commands.command('xp')
@click.pass_context
@CommonOptions.org_option(required=False)
@CommonOptions.project_id_option(help='Project ID to hold the experiments started by the job')
@click.option('--image', type=str, required=False, help='Docker image to use, defaults to missinglinkai/tensorflow')
@click.option('--git-repo', type=str, required=False, help='Git repository to pull the code from')
@click.option('--git-tag', type=str, required=False, help='Git branch/tag for the git repository. defaults to master. The cloned code will be available under `/code`')
@click.option('--source-dir', type=str, required=False, help='source directory for the experiment (if you have configured tracking repository)')
@click.option('--command', type=str, multiple=True, required=False, help='command to execute')
@click.option('--gpu/--cpu', required=False, default=True, help='Deprecated.')
@click.option('--data-volume', type=str, required=False, help='data volume to clone data from')
@click.option('--data-query', type=str, required=False, help='query to execute on the data volume')
@click.option('--data-dest', type=str, required=False, help='destination folder and format for cloning data. If provided, must begin with /data')
@click.option('--data-iterator', type=bool, required=False, help='When set to True, data will not be cloned before the experiment and the quarry will be available for the SDK iterator')
@click.option('--recipe', '-r', type=click.Path(exists=True), required=False, help='recipe file. recipe file is yaml file with the `flag: value` that allows you to specify default values for all params for this function')
@click.option('--save-recipe', type=str, required=False, help='Saves a recipe for this call to the target file and quits. Note the default values are not encoded into the recipe')
@click.option('--env', multiple=True, type=(str, str), default=None, required=False, help='Environment variables to pass for the invocation in key value format. You can use this flag multiple times')
@click.option('--output-paths', multiple=True, required=False, help='Paths that will be exported to the Data management at the end of the invocation job. The paths will be available to the the running code under `/path_name` by defaults to `/output`')
@click.option('--git-identity', type=click.Path(exists=True), required=False, default=None, help='[Secure] If provided, the provided path will be used as git (ssh) identity when pulling code. otherwise your default organisation identity will be used')
@click.option('--persistent-path', multiple=True, type=(str, str), required=False, help='Maps a path local to the server running the job as path inside the docker')
@click.option('--secure-env', '-se', multiple=True, type=(str, str), required=False, help='[Secure] Provide additional environment variables to the job. The format is  `env_key env_value`')
@click.option('--docker-host', type=str, default=None, required=False, help='[Secure] if docker login is needed to pull the image, login to this host')
@click.option('--docker-user', type=str, default=None, required=False, help='[Secure] if docker login is needed to pull the image, login with this user')
@click.option('--docker-password', type=str, default=None, required=False, help='[Secure] if docker login is needed to pull the image, login with this password')
@click.option('--requirements-txt', type=str, default=None, required=False, help='Install pip requirements from this path (relative to the repo). defaults to `requirements.txt`')
@click.option('--disable-colors', is_flag=True, default=None, required=False, help='Disable colors in logs')
@click.option('--attach', is_flag=True, default=None, required=False, help='Wait and print logs of the submitted job')
def run_experiment(ctx, **kwargs):
    kwargs = {k: v for k, v in kwargs.items() if _filter_input_dict_value(v)}

    save_recipe = kwargs.pop('save_recipe', False)
    disable_colors = kwargs.pop('disable_colors', False)
    attach = kwargs.pop('attach', False)
    docker_creds = _get_docker_creds(kwargs)
    secure_env = _get_secure_env(kwargs)
    input_data = _read_input_data_and_load_recipe(kwargs)
    if save_recipe:
        _save_recipe(input_data, save_recipe)
        return

    _build_src_pointer(input_data)
    input_data = {k: v for k, v in input_data.items() if not _is_none_ish(v)}
    click.echo(err=True)
    click.echo('Job parameters:', err=True)
    click.echo(yaml.safe_dump(input_data), err=True)

    click.echo(err=True)

    org = input_data.pop('org')
    project = input_data.pop('project')

    _prepare_encrypted_data(ctx, org, input_data, docker_creds, secure_env)

    input_data['env'] = _serialise_env_variables(input_data.get('env', {}))

    result = ApiCaller.call(ctx.obj, ctx.obj.session, 'put', '{}/{}/invoke'.format(org, project), input_data)
    output_result(ctx, result, ['ok', 'invocation'])

    _attach(attach, ctx, org, result['invocation'], disable_colors)


def _attach(attach, ctx, org, job_id, disable_colors):
    if attach:
        url = '{org}/run/{job_id}/logs'.format(org=org, job_id=job_id)
        monitor_logs(ctx, url, disable_colors)


def _encode_dict(dict_):
    return msgpack.packb(dict_)


def _secure_identity(data, git_identity):
    if git_identity:
        data.append(
            {
                'type': 'file',
                'path': '@identity',
                'data': SshIdentity(git_identity).export_private_key_bytes()
            })


def _secure_docker_creds(data, docker_creds):
    if docker_creds:
        data.append(
            {
                'type': 'docker',
                'path': '{}'.format(docker_creds['endpoint']).encode('utf-8'),
                'data': '{};{}'.format(docker_creds['user'], docker_creds['password']).encode('utf-8')
            })


def _secure_env_vars(data, secure_env):
    for k, v in secure_env.items():
        data.append(
            {
                'type': 'env',
                'path': k.encode('utf-8'),
                'data': v.encode('utf-8')
            })


def _prepare_encrypted_data(ctx, org, input_data, docker_creds, secure_env):
    secure_data = []
    _secure_identity(secure_data, input_data.get('git_identity'))
    _secure_docker_creds(secure_data, docker_creds)
    _secure_env_vars(secure_data, secure_env)

    if not secure_data:
        return

    encryption_keys = ApiCaller.call(ctx.obj, ctx.obj.session, 'get', '{}/run/security_credentials'.format(org))
    data_dict = {'data': secure_data, 'encryption_path': encryption_keys['keys']}
    ssh_keys = [Asymmetric(key) for key in encryption_keys['keys']]
    cipher = MultiKeyEnvelope(*ssh_keys)
    # encrypt_string does not encode bytes
    input_data['encrypted_data'] = cipher.encrypt_string(_encode_dict(data_dict))


@run_commands.command('logs')
@CommonOptions.org_option(required=False)
@click.option('--job-id', type=str)
@click.option('--disable-colors', is_flag=True, required=False)
@click.pass_context
def job_logs(ctx, org, job_id, disable_colors):
    url = '{org}/run/{job_id}/logs'.format(org=org, job_id=job_id)
    monitor_logs(ctx, url, disable_colors)
