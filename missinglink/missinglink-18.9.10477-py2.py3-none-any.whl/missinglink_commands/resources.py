# -*- coding: utf8 -*-
import logging
import click
import six

from missinglink_commands.legit.api import ApiCaller
from missinglink_commands.utilities.options import CommonOptions
from .commons import output_result
from .utilities.click_utils import pop_key_or_prompt_if


def get_home_path():
    from os.path import expanduser
    return expanduser("~")


def get_ssh_path():
    from os.path import join
    return join(get_home_path(), '.ssh', 'id_rsa')


DOCKER_IMAGE = 'docker:latest'


def pull_image_from_image(client, image):
    import docker.errors as docker_errors

    try:
        client.images.get(DOCKER_IMAGE)
    except docker_errors.NotFound:
        click.echo('Pulling docker image')
        client.images.pull(DOCKER_IMAGE)

    cmd = 'docker pull {}'.format(image)
    socket_volumes = {'/var/run/docker.sock': {'bind': '/var/run/docker.sock'}}

    cont = client.containers.run(DOCKER_IMAGE, command=cmd, auto_remove=True, volumes=socket_volumes, environment={'ML_RM_MANAGER': '1'}, detach=True)
    logger_handler = cont.logs(stdout=True, stderr=True, stream=True)
    for log in logger_handler:
        logging.info(log)

    return client.images.get(image)


def auth_resource(ctx, org):
    result = ApiCaller.call(ctx.obj, ctx.obj.session, 'get', '{org}/resource/authorise'.format(org=org))
    return result.get('token')


def validate_and_get_docker_client():
    import docker.errors as docker_errors
    import docker
    import requests

    client = docker.from_env()
    try:
        client.ping()
    except docker_errors.DockerException as ex:
        raise click.BadArgumentUsage('Failed to connect to docker host %s' % (str(ex)))
    except requests.exceptions.ConnectionError as ex:
        raise click.BadArgumentUsage('Failed to connect to docker host %s' % (str(ex)))

    logging.info('Docker host verified')

    return client


def pull_ml_image(config, docker_client):
    click.echo('Getting/updating MissingLinks Resource Manager image')
    img = pull_image_from_image(docker_client, config.rm_manager_image)
    return img


def _get_combined_volume_path(*args):
    res = {}
    for a in args:
        res.update(a)

    return res


def _docker_present_return_instance(command, *args, **kwargs):
    import docker.errors as docker_errors
    try:
        return command(*args, **kwargs)
    except docker_errors.NotFound:
        pass


def _docker_present(command, *args, **kwargs):
    import docker.errors as docker_errors
    try:
        return command(*args, **kwargs) or True  # we are looking only for exceptions here
    except docker_errors.NotFound:
        return False


def validate_running_resource_manager(config, docker_client, force):
    current_rm = _docker_present_return_instance(docker_client.containers.get, config.rm_container_name)
    if current_rm is None:
        return

    if not force:
        raise click.BadOptionUsage('Can not install resource manger while one is running. run `docker kill {}` do stop and reuse config or re-run with `--force` flag to clear all configuration'.format(current_rm.name))

    click.echo('Killing current Resource Manger (%s) due to --force flag' % current_rm.id)
    if current_rm.status == 'running':
        current_rm.kill()

    current_rm.remove(force=True)


def get_config_prefix_and_file(config):
    with open(config.config.config_file_abs_path, 'rb') as f:
        config_data = f.read()
    prefix = None
    if config.config.config_prefix is not None:
        prefix = config.config.config_prefix
    return prefix, config_data


ADMIN_VOLUME = {'/var/run/docker.sock': {'bind': '/var/run/docker.sock'}}


def _apply_config_to_volume(config, docker_client, ssh_key, token, prefix=None, config_data=None, ml_backend=None):
    if token is None and ssh_key is None:
        return

    config_volume = {config.rm_config_volume: {'bind': '/config'}}
    conf_mounts = _get_combined_volume_path(ADMIN_VOLUME, config_volume)

    ws_server = config.rm_socket_server

    if prefix is None and config_data is None:
        id_token = config.id_token
        if id_token is None:
            # TODO: make backend data commands support resource token
            raise click.BadOptionUsage('Please call ml auth init first')
        prefix, config_data = get_config_prefix_and_file(config)

    if config_data and six.PY3 and isinstance(config_data, bytes):
        config_data = config_data.decode('utf-8')

    command = ['config', '--ml-server', ws_server, '--ml-config-file', config_data]

    if prefix is not None:
        command.extend(['--ml-config-prefix', prefix])

    if token is not None:
        command.append('--ml-token')
        command.append(token)

    if ml_backend is not None:
        command.append('--ml-backend')
        command.append(ml_backend)

    if ssh_key is not None:
        command.append('--ssh-private-key')
        command.append(ssh_key)

    cont = docker_client.containers.run(config.rm_manager_image, command=command, volumes=conf_mounts, environment={'ML_RM_MANAGER': '1'}, detach=True)
    exit_code = cont.wait()
    if exit_code != 0:
        click.echo(cont.logs())
    cont.remove()


def _handle_token_and_data_path(ctx, force, org, token=None):
    cur_config = ctx.obj.config.resource_manager_config
    if force:
        click.echo('Current host config is deleted due to `--force` flag')
        cur_config = {}

    new_token = token or cur_config.get('token')

    if new_token is None:
        new_token = auth_resource(ctx, org)
    ctx.obj.config.update_and_save({
        'resource_manager': {
            'token': new_token,
        }
    })
    return new_token


def _validate_apply_config(ctx, docker_client, org, force, ssh_key_path, token):
    config = ctx.obj
    config_volume_name = config.rm_config_volume

    if force and _docker_present(docker_client.volumes.get, config_volume_name):
        click.echo('Deleting config volume (%s) due to --force flag')
        docker_client.volumes.get(config_volume_name).remove(force=True)

    new_image = not _docker_present(docker_client.volumes.get, config_volume_name)

    ssh_key = None
    if new_image:
        docker_client.volumes.create(config_volume_name)
        if ssh_key_path is None:
            ssh_key_path = click.prompt(text='SSH key path (--ssh-key-path)', default=get_ssh_path())

    token = _handle_token_and_data_path(ctx, force, org, token=token)

    if ssh_key_path is not None:
        from .cloud.aws import AwsContext
        ssh_key = AwsContext.export_key_from_path(ssh_key_path).decode('utf-8')

    _apply_config_to_volume(config, docker_client, ssh_key, token)
    return


def _validate_config_volume(config, docker_client):
    if not _docker_present(docker_client.volumes.get, config.rm_config_volume):
        raise click.BadArgumentUsage('Configuration volume is missing. Please re-install')


def _run_resource_manager(config, docker_client):
    _validate_config_volume(config, docker_client)
    click.echo('Starting Resource Manager')
    config_volume = {config.rm_config_volume: {'bind': '/config'}}
    run_mounts = _get_combined_volume_path(ADMIN_VOLUME, config_volume)
    return docker_client.containers.run(
        config.rm_manager_image,
        command=['run'],
        auto_remove=False,
        restart_policy={"Name": 'always'},
        volumes=run_mounts,
        environment={'ML_RM_MANAGER': '1', 'ML_CONFIG_VOLUME': config.rm_config_volume},
        detach=True,
        network='host',
        name=config.rm_container_name)


@click.group('resources', help='Resource Management')
def resource_commands():
    pass


@resource_commands.command('install')
@click.pass_context
@CommonOptions.org_option()
@click.option('--ssh-key-path', type=str, help='Path to the private ssh key to be used by the resource manager', default=None)
@click.option('--force/--no-force', default=False, help='Force installation (stops current resource manager if present')
@click.option('--resource-token', default=None, type=str, help='MissingLink resource token. One will be generated if this instance of ml is authorized')
def install_rm(ctx, org, ssh_key_path, force, resource_token):
    docker_client = validate_and_get_docker_client()
    validate_running_resource_manager(ctx.obj, docker_client, force)

    pull_ml_image(ctx.obj, docker_client)
    _validate_apply_config(ctx, docker_client=docker_client, org=org, force=force, ssh_key_path=ssh_key_path, token=resource_token)
    _run_resource_manager(ctx.obj, docker_client)
    click.echo('The resource manager is configured and running')


def cloud_connector_defaults(ctx, cloud_type, kwargs):
    prefix, config_data = get_config_prefix_and_file(ctx.obj)

    return dict(
        mali_image=ctx.obj.ml_image,
        socket_server=ctx.obj.rm_socket_server,
        config_volume=ctx.obj.rm_config_volume,
        rm_image=ctx.obj.rm_manager_image,
        container_name=ctx.obj.rm_container_name,
        prefix=prefix,
        name=pop_key_or_prompt_if(kwargs, 'connector', text='Connector [--connector]:', default='%s-%s' % (cloud_type, 'default')),
        cloud_type=cloud_type,
    ), config_data


def azure_auth(ctx, kwargs, org):
    from .commons import WaitForHttpResponse
    template, _ = cloud_connector_defaults(ctx, cloud_type='azure', kwargs=kwargs)

    azure_subscription_id = pop_key_or_prompt_if(kwargs, 'azure_subscription_id', text='subscription id [--azure-subscription-id]')
    tenant_id_request_url = '{org}/azure/tenant_id_for/{subscription_id}'.format(org=org, subscription_id=azure_subscription_id)

    tenant_id_response = ApiCaller.call(ctx.obj, ctx.obj.session, 'get', tenant_id_request_url)
    tenant_id = tenant_id_response['tenantId']

    server = WaitForHttpResponse(uri='/console/azure/authorised', port=8002)
    cloud_data = [
        {'key': 'auth_state', 'data': 'pending'},
        {'key': 'auth_return_url', 'data': server.url},
        {'key': 'azure_subscription_id', 'data': azure_subscription_id},
        {'key': 'azure_tenant_id', 'data': tenant_id},
    ]
    template['cloud_data'] = cloud_data
    url = '{org}/cloud_connector/{name}'.format(org=org, name=template['name'])
    ApiCaller.call(ctx.obj, ctx.obj.session, 'post', url, template)

    auth_url = '{org}/azure/authorise_config/{name}'.format(org=org, name=template['name'])
    auth_request = ApiCaller.call(ctx.obj, ctx.obj.session, 'get', auth_url)
    auth_url_path = auth_request['url']
    click.echo(auth_url_path)

    resp = server.run()
    authed_url = '{org}/azure/authorised/{config_id}/code/{code}'.format(
        org=org, config_id=template['name'], code=resp['code'][0])
    authed_request = ApiCaller.call(ctx.obj, ctx.obj.session, 'get', authed_url)
    if authed_request['ok']:
        click.echo('Azure Authorisation for %s completed' % template['name'])
    else:
        click.echo('Azure Authorisation for %s failed' % template['name'])

    return authed_request['result']


def get_cloud_connector_default_connector_name(available_connectors, cloud_type):
    for connector in available_connectors:
        if connector['default']:
            return connector['name']
    if available_connectors:
        return available_connectors[0]['name']
    return '%s-default' % cloud_type


def _get_cloud_connectors(ctx, org, cloud_type):
    click.echo("Checking for available cloud connectors for %s" % cloud_type)
    url = '{org}/{cloud_type}/cloud_connectors'.format(org=org, cloud_type=cloud_type)
    response = ApiCaller.call(ctx.obj, ctx.obj.session, 'get', url)
    return response.get('result', [])


def get_cloud_connector(ctx, org, kwargs, cloud_type, connect_dict=None):
    if connect_dict is None:
        connect_dict = {
            'azure': lambda: azure_auth(ctx, kwargs, org),
        }

    available_connectors = _get_cloud_connectors(ctx, org, cloud_type)
    default_connector = get_cloud_connector_default_connector_name(available_connectors, cloud_type)
    click.echo('List of %s available connectors for %s' % (cloud_type, org))
    output_result(ctx, available_connectors)
    click.echo('You can use easting connector by specifying its name or create a new one by using a name from the list')
    connector_param = 'connector'
    connector_cli_param = '--connector'
    connector_name = pop_key_or_prompt_if(kwargs, connector_param, text='Connector name [%s] ' % connector_cli_param, default=default_connector)
    for x in available_connectors:
        if connector_name == x['name']:
            click.echo('Reusing `%s` connector' % connector_name)
        return x
    kwargs[connector_param] = connector_name

    return connect_dict[cloud_type]()


def _resource_group_defaults(kws, connector, cloud_type):
    is_static = not pop_key_or_prompt_if(kws, 'dynamic_group', type=bool, text=' [--dynamic-group]', default=cloud_type == "aws")
    static_hint = 'static' if is_static else 'dynamic'
    group_name = pop_key_or_prompt_if(kws, 'group_name', text='Group name [--group-name]', default='%s-default' % static_hint)
    click.echo('Creating %s group `%s` ' % (static_hint, group_name))

    return {
        'name': group_name,
        'cloud_type': cloud_type,
        'connector': connector,
        'is_static': is_static,
        'config': '{}',  # todo: add cloud data from the connector here?
        'gpu': pop_key_or_prompt_if(kws, 'group_gpu', text='Is this a GPU group [--group-gpu]', default=False, type=bool),
        'terminate_on_stop': pop_key_or_prompt_if(kws, 'terminate_on_stop', text='Terminate instances (should be %s for %s groups) [--group-terminate-on-stop]' % (not is_static, static_hint), default=not is_static, type=bool),
        'priority': pop_key_or_prompt_if(kws, 'priority', text='Priority (higher is better) [--group-priority]', default=100, type=int),
        'idle_timeout': pop_key_or_prompt_if(kws, 'idle_timeout', text='Idle timeout  [--group-idle-timeout]', default=15, type=int),
    }


def create_group(ctx, kws, org):
    cloud_type = pop_key_or_prompt_if(kws, 'cloud_type', text='Cloud Type [--cloud-type]', default='azure')
    connector = get_cloud_connector(ctx, org, kws, cloud_type)
    request = _resource_group_defaults(kws, connector['name'], connector['cloud_type'])

    if not request['is_static']:
        request['capacity'] = pop_key_or_prompt_if(kws, 'group_capacity', text='Cloud Type [--group-capacity]', default=5, type=int)
    group_name = request['name']
    url = '{org}/resource_group/{name}'.format(org=org, name=group_name)
    response = ApiCaller.call(ctx.obj, ctx.obj.session, 'post', url, request)
    click.echo('Group %s created.' % group_name)
    return response['result']


def select_resource_group(ctx, available_groups, static, kws, org):
    hint_name = '%s-default' % ('dynamic' if not static else 'static')
    available_groups = [x for x in available_groups if x['is_static'] == static]
    if available_groups:
        click.echo('Here is a list of your current groups. You can use one of them or enter a name for new group')
        output_result(ctx, available_groups, fields=['name', 'cloud_type', 'capacity', 'gpu', 'priority'])
        hint_name = available_groups[0]['name']
    group_name = pop_key_or_prompt_if(kws, 'group_name', text='Group name [--group-name]', default=hint_name)
    for group in available_groups:
        if group_name == group['name']:
            click.echo('Selected pre-existing group %s' % group_name)
            return group
    kws['group_name'] = group_name
    kws['dynamic_group'] = False

    return create_group(ctx, kws, org)


def static_resource_groups(ctx, org, kwargs):
    click.echo("Checking for available resource groups for %s" % org)
    url = '{org}/static_resource_groups'.format(org=org)
    response = ApiCaller.call(ctx.obj, ctx.obj.session, 'get', url)
    available_groups = response.get('results', [])
    return select_resource_group(ctx, available_groups, True, kwargs, org)


def get_unmanaged_resources_list(ctx, org, cloud_type, connector):
    url = '{org}/{cloud_type}/unmanaged_machines/{connector}'.format(org=org, cloud_type=cloud_type, connector=connector)
    response = ApiCaller.call(ctx.obj, ctx.obj.session, 'get', url)
    unmanaged_resources = response.get('results', [])
    index = 0
    for res in unmanaged_resources:
        index += 1
        res['index'] = index

    return unmanaged_resources


def select_unmanaged_machine(ctx, org, cloud_type, connector, kws):
    available_resources = get_unmanaged_resources_list(ctx, org, cloud_type, connector)
    max_index = len(available_resources)
    output_result(ctx, available_resources, ['index', 'name', 'region', 'resource_group', 'type'])
    if max_index == 0:
        return None

    while True:
        selected = pop_key_or_prompt_if(kws, 'machine_index', text='Machine Index', default=1, type=int)
        if 0 < selected <= max_index:
            return available_resources[selected - 1]


def register_static_unmanaged_machine(ctx, org, group, machine_data):
    data = [{'key': key, 'data': str(data)} for key, data in machine_data.items()]
    url = '{org}/resource_group/{name}/register_static'.format(org=org, name=group['name'])
    result = ApiCaller.call(ctx.obj, ctx.obj.session, 'post', url, dict(data=data))
    return result


@resource_commands.command('add_to_static_cloud_group', help="Add exsisting cloud machine to managed resource group")
@click.pass_context
@CommonOptions.org_option()
@click.option('--name', type=str, help='configuration name')
@click.option('--group-name', type=str, help='Target group name. Specifying non-existing group will create one')
@click.option('--silent/--no-silent', default=False, help='skip prompts with smart defaults')
def setup_static_template(ctx, org, **kwargs):
    group = static_resource_groups(ctx, org, kwargs)
    machine = select_unmanaged_machine(ctx, org, group['cloud_type'], group['cloud_connector'], kwargs)
    if machine is None:
        click.echo('All of your machines are manged.')
        return
    res = register_static_unmanaged_machine(ctx, org, group, machine)
    click.echo(res)


class RMExpando(object):
    rm_socket_server = None
    rm_manager_image = None
    rm_config_volume = None
    rm_container_name = None


@resource_commands.command('restore_aws_template', help="restores predefined cloud configuration")
@click.pass_context
@click.option('--arn', type=str, help='arn of the KMS encryption key', required=True)
@click.option('--ssh', type=(str, str, str), help='ssh key data', required=True)
@click.option('ml', '--ml', '--mali', type=(str, str, str), help='mali config data', required=True)
@click.option('--prefix', type=str, help='ml prefix type', required=False)
@click.option('--token', type=str, help='ml prefix type', required=True)
@click.option('--rm-socket-server', type=str, help='web socket server', required=True)
@click.option('--rm-manager-image', type=str, required=True)
@click.option('--rm-config-volume', type=str, required=True)
@click.option('--rm-container-name', type=str, required=True)
@click.option('--ml-backend', type=str, required=True)
def apply_aws_template(
        ctx, arn, ssh, ml, prefix, token, rm_socket_server, rm_manager_image,
        rm_config_volume, rm_container_name, ml_backend):
    from .cloud.aws import AwsContext
    if prefix == str(None):
        prefix = None

    click.echo('decrypting data')
    kms = AwsContext.get_kms(arn)
    ssh_key = AwsContext.decrypt(kms, ssh).decode('utf-8')
    ml_data = AwsContext.decrypt(kms, ml).decode('utf-8')
    docker_client = validate_and_get_docker_client()

    click.echo('building installation config')
    config = RMExpando()
    config.rm_socket_server = rm_socket_server
    config.rm_manager_image = rm_manager_image
    config.rm_config_volume = rm_config_volume
    config.rm_container_name = rm_container_name

    click.echo('pulling RM')
    pull_ml_image(ctx.obj, docker_client)

    click.echo('killing RM')
    validate_running_resource_manager(config, docker_client, True)

    click.echo('building volume')
    if _docker_present(docker_client.volumes.get, rm_config_volume):
        docker_client.volumes.get(rm_config_volume).remove(force=True)
    docker_client.volumes.create(rm_config_volume)
    _apply_config_to_volume(config, docker_client, ssh_key, token, prefix=prefix, config_data=ml_data, ml_backend=ml_backend)

    click.echo('Clear containers')
    for container in docker_client.containers.list():
        if container.name == rm_container_name:
            click.echo("\t  KILL: %s" % container.id)
            container.kill()

    for container in docker_client.containers.list(all=True):
        if container.name == rm_container_name:
            click.echo("\t  REMOVE: %s" % container.id)
            container.remove(force=True)

    click.echo('Start RM:')
    inst = _run_resource_manager(config, docker_client)
    click.echo('The resource manager is configured and running %s' % inst.id)
    click.echo('for logs run: docker logs -f %s ' % rm_container_name)
