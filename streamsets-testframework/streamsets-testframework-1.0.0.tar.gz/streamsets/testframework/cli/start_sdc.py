# Copyright 2018 StreamSets Inc.

import argparse
import io
import logging
import socket
import tarfile
from uuid import uuid4

import docker
from javaproperties import PropertiesFile

from streamsets.testframework import environment, logger as streamsets_logger, sdc
from streamsets.testframework.utils import run_container_shell_commands, ShellCommand, wait_for_container_port_open

logger = logging.getLogger('streamsets.testframework.cli.start_sdc')

docker_client = docker.from_env()

SDC_DIST = '/local_sdc/streamsets-datacollector'


def _main():
    parser = argparse.ArgumentParser(prog='stf start sdc', description='Start StreamSets Data Collector Docker image',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--verbose', action='store_true', help='Be noisier')
    parser.add_argument('--docker-network', metavar='network', default='cluster',
                        help='Docker network to which to attach the STF container')
    parser.add_argument('--https', nargs='?', const='encryption', choices=['encryption'],
                        help='Configure SDC instance for HTTPS encryption')

    non_local_group = parser.add_argument_group('Non local SDC')
    non_local_group.add_argument('-a', '--always-pull', action='store_true',
                                 help='Always pull new SDC/stage lib Docker images')
    non_local_group.add_argument('--version', default=sdc.DEFAULT_SDC_VERSION,
                                 help='Version of SDC to start', metavar='ver')
    non_local_group.add_argument('--stage-lib', nargs='+',
                                 help="One or more stage libs to add (e.g. 'basic jdbc')", metavar='lib')

    local_group = parser.add_argument_group('Local SDC')
    local_group.add_argument('-d', '--directory',
                             help='SDC dist directory to load SDC from', metavar='path')
    local_group.add_argument('--sdc-template-image', default=f'streamsets/datacollector:{sdc.DEFAULT_SDC_VERSION}',
                             help='SDC docker image used as a template', metavar='template')

    environment_group = parser.add_argument_group('Environments')
    environment_group.add_argument('--cluster-server',
                                   help='A cluster server against which to configure the SDC instance')

    args = parser.parse_args()
    streamsets_logger.setLevel(logging.DEBUG if args.verbose else logging.INFO)

    if args.directory:
        _start_sdc_local(args)
    else:
        _start_sdc(args)


def _start_sdc(args):
    data_collector = sdc.DataCollector(always_pull=args.always_pull,
                                       https=args.https,
                                       network=args.docker_network,
                                       version=args.version)

    if args.cluster_server:
        data_collector.configure_for_environment(environment.Cluster(args.cluster_server))

    if args.stage_lib:
        data_collector.add_stage_lib(*['streamsets-datacollector-{}-lib'.format(lib) for lib in args.stage_lib])

    data_collector.start()


def _start_sdc_local(args):
    """
    Given an SDC directory, start it in a container.
    """
    directory = args.directory
    network = args.docker_network
    image = args.sdc_template_image

    sdc_container_id = docker_client.create_container(image=image, host_config=docker_client.create_host_config(
        binds=[f'{directory}:{SDC_DIST}']))
    tarstream = io.BytesIO(docker_client.get_archive(container=sdc_container_id,
                                                     path=f'{SDC_DIST}/etc/sdc.properties')[0].read())
    with tarfile.open(fileobj=tarstream) as tarfile_:
        for tarinfo in tarfile_.getmembers():
            sdc_properties_data = tarfile_.extractfile(tarinfo).read().decode()
    docker_client.remove_container(container=sdc_container_id, v=True, force=True)
    sdc_properties = PropertiesFile.loads(sdc_properties_data)

    server_port = sdc_properties['http.port' if not args.https else 'https.port']
    sentinel_file = '/tmp/{}'.format(uuid4())
    docker_env_vars = {
        'SDC_CONF': '/local_sdc/etc',
        'SDC_DATA': '/local_sdc/data',
        'SDC_DIST': SDC_DIST,
        'SDC_LOG': '/local_sdc/logs',
        'SDC_RESOURCES': '/local_sdc/resources',
        'SDC_USER': 'sdc',
        'STREAMSETS_LIBRARIES_EXTRA_DIR': '/local_sdc/streamsets-datacollector/streamsets-libs-extras',
        'USER_LIBRARIES_DIR': '/opt/streamsets-datacollector-user-libs'
    }
    container_args = {
        'command': ("""'until [ -f "{0}" ]; do sleep 1; done; """
                    """exec "${{SDC_DIST}}/bin/streamsets" """
                    """dc -exec'""".format(sentinel_file)),
        'detach': True,
        'entrypoint': 'bash -c',
        'environment': docker_env_vars,
        'ports': [server_port],
        'image': image,
        'host_config': docker_client.create_host_config(network_mode=args.docker_network,
                                                        publish_all_ports=True,
                                                        binds=[f'{directory}:{SDC_DIST}'])
    }

    container_id = docker_client.create_container(**container_args)['Id']
    docker_client.start(container_id)

    inspect_data = docker_client.inspect_container(container_id)
    sdc_port_on_host = inspect_data['NetworkSettings']['Ports']['{0}/tcp'.format(server_port)][0]['HostPort']
    container_hostname = inspect_data['Config']['Hostname']

    logger.info('Starting StreamSets Data Collector (SDC) in %s container on %s container port ...',
                container_hostname, server_port)

    shell_commands = [
        ShellCommand(command=f'cp -r /local_sdc/streamsets-datacollector/etc /local_sdc/etc', user='root'),
        ShellCommand(command=f'rm -rf /opt/streamsets-datacollector-user-libs', user='root'),
        ShellCommand(command=f'/tmp/sdc-configure.sh', user='root'),
        ShellCommand(command='touch {}'.format(sentinel_file), user='root')
    ]
    run_container_shell_commands(docker_client, container_id, shell_commands, args.verbose)
    try:
        logger.info('SDC is configured. Waiting for SDC to start ...')
        wait_for_container_port_open(docker_client, container_id, port=int(server_port),
                                     timeout_sec=90, verbose=args.verbose)

        scheme = 'https' if args.https else 'http'
        # This is more user-friendly URL so that users can use it from a browser.
        exposed_server_url = f'{scheme}://{socket.gethostname()}:{sdc_port_on_host}'
        logger.info('SDC is now running. SDC container (%s:%s) can be followed along on %s',
                    container_hostname, server_port, exposed_server_url)
    except:
        logger.error('Error reaching SDC. SDC log follows ...')
        print('------------------------- SDC log - Begins -----------------------')
        print(docker_client.logs(container_id).decode())
        print('------------------------- SDC log - Ends -------------------------')
        raise


if __name__ == '__main__':
    _main()
