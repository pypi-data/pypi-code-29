import shortuuid
import sys
from os import system
from time import sleep
from jinja2 import Environment, PackageLoader
from dataflows_serverless.constants import *
from dataflows_serverless.k8s import K8S
from os import path
import subprocess
import signal


def get_serverless_chain(source_chain, num_secondaries, output_datadir, input_datadirs, nfs_uuid, image, no_cleanup, config):
    uuid = get_serverless_uuid()
    print('starting serverless uuid {}'.format(uuid))
    jinja_env = Environment(loader=PackageLoader('dataflows_serverless', 'templates'))
    k8s = K8S(jinja_env)
    signal.signal(signal.SIGINT, lambda s, f: sys.exit(1))
    try:
        nfs_cluster_ip, nfs_pod_name, deployment_exists = start_nfs_server(k8s, nfs_uuid if nfs_uuid else uuid,
                                                                           nfs_uuid is not None,
                                                                           config)
        if not deployment_exists and 'data_init_image' in config:
            system('kubectl logs -c init -f {}'.format(nfs_pod_name))
        print('initializing nfs pod name {}'.format(nfs_pod_name))
        init_nfs_code(nfs_pod_name)
        if input_datadirs:
            print('initializing input data')
            init_nfs_data(nfs_pod_name, input_datadirs)
        if not image:
            image = DEFAULT_IMAGE
        if config.get('debug'):
            print('Running in debug mode - jobs need to be started manually by exec bash on each pod and running /entrypoint.sh')
            print('When done, kill process 1 to signal that job completed - kill 1')
        print('starting primary job')
        start_primary_job(k8s, uuid, nfs_cluster_ip, num_secondaries, image, config)
        primary_job_pod_name = k8s.get_running_pod_name('jobgroup=primary-{}'.format(uuid))
        print('primary job pod name = {}'.format(primary_job_pod_name))
        print('starting {} secondaries'.format(num_secondaries))
        list(start_secondary_jobs(k8s, num_secondaries, uuid, image, nfs_cluster_ip, config))
        print('waiting for primary job to complete')
        wait_primary_job_complete(k8s, uuid)
        print('primary job complete, copying output data to {}'.format(output_datadir))
        assert system('kubectl cp {pod_name}:{remote_dir} {datadir}'.format(
            pod_name=nfs_pod_name,
            remote_dir=path.join(NFS_CODE_DIRECTORY, output_datadir),
            datadir=output_datadir)) == 0
    finally:
        if not no_cleanup:
            cleanup(k8s, uuid)
    return [[]]


def cleanup(k8s, uuid):
    try:
        k8s.delete_jobs('jobgroup=primary-{}'.format(uuid))
    except Exception:
        pass
    try:
        k8s.delete_jobs('jobgroup=secs-{}'.format(uuid))
    except Exception:
        pass
    try:
        k8s.cleanup_resources()
    except Exception:
        pass


def get_serverless_uuid():
    shortuuid.set_alphabet('abcdefghijklmnopqrstuvwxyz')
    return shortuuid.uuid()


def start_nfs_server(k8s, uuid, keep, config):
    deployment_exists = False
    try:
        k8s.create_deployment('nfs-deployment.yaml', dict({'uuid': uuid}, **config), keep)
    except Exception:
        if keep:
            deployment_exists = True
        else:
            raise
    if deployment_exists:
        nfs_service = k8s.get_service('nfs-{}'.format(uuid))
    else:
        nfs_service = k8s.create_service('nfs-service.yaml', {'uuid': uuid}, keep)
    nfs_cluster_ip = nfs_service.to_dict()['spec']['cluster_ip']
    nfs_pod_name = k8s.get_running_pod_name('app=nfs-{}'.format(uuid), return_pending=not deployment_exists and 'data_init_image' in config)
    return nfs_cluster_ip, nfs_pod_name, deployment_exists


def init_nfs_code(nfs_pod_name):
    assert system('kubectl exec {pod_name} -- bash -c \'rm -rf {remote_code_dir} /exports/primary /exports/secondaries; mkdir -p {remote_code_dir}\''.format(
        pod_name=nfs_pod_name, remote_code_dir=NFS_CODE_DIRECTORY)) == 0
    assert system('kubectl cp {local_flow_file} {pod_name}:{remote_code_dir}/flow.py'.format(
        pod_name=nfs_pod_name, local_flow_file=sys.argv[0],
        remote_code_dir=NFS_CODE_DIRECTORY)) == 0


def init_nfs_data(nfs_pod_name, input_datadirs):
    for datadir in input_datadirs:
        assert system('kubectl exec {pod_name} -- bash -c \'mkdir -p {remote_code_dir}/{datadir}; rm -rf {remote_code_dir}/{datadir}\''.format(
            pod_name=nfs_pod_name, remote_code_dir=NFS_CODE_DIRECTORY, datadir=datadir)) == 0
        assert system('kubectl cp {datadir}/ {pod_name}:{remote_codedir}/{datadir}/'.format(
            datadir=datadir, pod_name=nfs_pod_name, remote_codedir=NFS_CODE_DIRECTORY)) == 0


def start_primary_job(k8s, uuid, nfs_cluster_ip, num_secondaries, image, config):
    return k8s.create_job('primary-job.yaml', dict({'secondaries': num_secondaries,
                                                    'uuid': uuid,
                                                    'image': image,
                                                    'nfs': nfs_cluster_ip}, **config))


def start_secondary_jobs(k8s, num_secondaries, uuid, image, nfs_cluster_ip, config):
    for secondary in range(num_secondaries):
        yield k8s.create_job('secondary-job.yaml', dict({'secondary': secondary,
                                                         'secondaries': num_secondaries,
                                                         'uuid': uuid,
                                                         'image': image,
                                                         'nfs': nfs_cluster_ip}, **config))


def wait_primary_job_complete(k8s, uuid):
    primary_pod_name = k8s.get_running_pod_name('jobgroup=primary-{}'.format(uuid))

    process = subprocess.Popen('kubectl logs -f {}'.format(primary_pod_name),
                               shell=True, stdout=subprocess.PIPE)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        print(line.decode())
    while True:
        sleep(WAIT_FOR_PRIMARY_JOB_COMPLETE_DELAY_SECONDS)
        job_pod_phase = k8s.get_pod_phase(primary_pod_name)
        if job_pod_phase == 'Succeeded':
            break
        elif job_pod_phase == 'Failed':
            raise Exception('primary pod failed')
    return primary_pod_name


def k8s_cleanup(k8s, secondary_jobs, primary_job, nfs_deployment, nfs_service):
    if secondary_jobs:
        [k8s.delete_job(secondary_job) for secondary_job in secondary_jobs]
    if primary_job:
        k8s.delete_job(primary_job)
    if nfs_deployment:
        k8s.delete_deployment(nfs_deployment)
    if nfs_service:
        k8s.delete_service(nfs_service)
