# -*- coding: utf-8 -*-
# Copyright 2018 NS Solutions Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function, absolute_import, with_statement

import os.path

import click

import cli.configuration
import cli.object_storage
import cli.pprint
import cli.util
import kamonohashi


@click.group()
@click.pass_context
def job(ctx):
    """Create and manage KAMONOHASHI jobs"""
    api_client = cli.configuration.get_api_client()
    ctx.obj = kamonohashi.JobApi(api_client)


@job.command('list', help='List jobs filtered by condition')
@click.option('--count', type=click.IntRange(1, 10000), default=1000, show_default=True, help='Maximum number of data to list')
@click.option('--id', help='id')
@click.option('--name', help='name')
@click.option('--started-at', help='started at')
@click.option('--data-set', help='data set')
@click.option('--memo', help='memo')
@click.option('--status', help='status')
@click.pass_obj
def list_job(api, count, id, name, started_at, data_set, memo, status):
    """
    :param kamonohashi.JobApi api:
    """
    per_page = 1000
    command_args = {
        'id': id,
        'name': name,
        'started_at': started_at,
        'data_set': data_set,
        'memo': memo,
        'status': status,
    }
    args = dict((key, value) for key, value in command_args.items() if value is not None)
    if count <= per_page:
        result = api.list_jobs(per_page=count, **args)
    else:
        total_pages = (count - 1) // per_page + 1
        result = page_result = api.list_jobs(page=1, **args)
        for page in range(2, total_pages + 1):
            if len(page_result) < per_page:
                break
            page_result = api.list_jobs(page=page, **args)
            first_valid_index = next((i for i, x in enumerate(page_result) if x.id < result[-1].id), per_page)
            result.extend(page_result[first_valid_index:])

    cli.pprint.pp_table(['id', 'name', 'started_at', 'dataset', 'memo', 'status'],
                        [[x.id, x.name, x.created_at, x.data_set.name, x.memo, x.status] for x in result[:count]])


@job.command(help='Get details of a job')
@click.argument('id', type=int)
@click.pass_obj
def get(api, id):
    """
    :param kamonohashi.JobApi api:
    """
    result = api.get_job(id)
    cli.pprint.pp_dict(cli.util.to_dict(result))


@job.command(help='Submit a new job')
@click.option('-n', '--name', required=True, help='A name of the job')
@click.option('-rim', '--registry-image', required=True, help='A docker image name you want to run')
@click.option('-rt', '--registry-tag', required=True, help='A tag of the docker image')
@click.option('-d', '--data-set-id', type=int, required=True, help='A dataset id you want to use for the job')
@click.option('-e', '--entry-point', help='Job execution command')
@click.option('-go', '--git-owner', required=True,
              help="The owner of the repository which contains source codes you want to execute. Usually owner is the "
                   "first path of the repository's url. In case of this url, "
                   "https://github.com/kamonohashi/kamonohashi-cli, kamonohashi is a owner name.")
@click.option('-gr', '--git-repository', required=True,
              help="The repository name of the repository whichi contains your source codes. Usually repository name is"
                   " the second path of the repository's url. In case of this url,"
                   " https://github.com/kamonohashi/kamonohashi-cli, kamonohashi-cli is a repository name.")
@click.option('-gb', '--git-branch',
              help='The branch of your git repository. If you omit this option, master branch is used.')
@click.option('-gc', '--git-commit',
              help='The git commit of your source code. If you omit this option, the latest one is used.')
@click.option('-c', '--cpu', type=int, required=True, help='A number of core you want to assign to this job')
@click.option('-mem', '--memory', type=int, required=True, help='How much memory(GB) you want to assign to this job ')
@click.option('-g', '--gpu', type=int, required=True, help='A number of GPUs you want to assign to this job')
@click.option('-p', '--partition',
              help='A cluster partition. Partition is an arbitrary string but typically is a type of GPU or cluster.')
@click.option('-m', '--memo', help='A memo of this job.')
@click.option('-pid', '--parent-id',
              help='A parent id of this job. Currently, the system only makes a relationship to the parent job but do nothing.')
@click.option('-o', '--options', type=(str, str), multiple=True,
              help='Options of this job. The options are stored in the environment variables  [multiple]')
@click.pass_obj
def create(api, name, registry_image, registry_tag, data_set_id, entry_point,
           git_owner, git_repository, git_branch, git_commit, cpu, memory, gpu, partition, memo,
           parent_id, options):
    """
    :param kamonohashi.JobApi api:
    """
    container_image = kamonohashi.ComponentsContainerImageInputModel(image=registry_image, tag=registry_tag)
    git_model = kamonohashi.ComponentsGitCommitInputModel(branch=git_branch, commit_id=git_commit, owner=git_owner, repository=git_repository)
    option_dict = None
    if options is not None:
        option_dict = {}
        for option in options:
            option_dict[option[0]] = option[1]
    model = kamonohashi.JobApiModelsCreateInputModel(container_image=container_image, cpu=cpu, data_set_id=data_set_id, entry_point=entry_point,
                                                     git_model=git_model, gpu=gpu, memo=memo, memory=memory, name=name, options=option_dict,
                                                     parent_id=parent_id, partition=partition)
    result = api.create_job(model=model)
    print('created', result.id)


@job.command(help='Delete a job')
@click.argument('id', type=int)
@click.pass_obj
def delete(api, id):
    """
    :param kamonohashi.JobApi api:
    """
    api.delete_job(id)
    print('deleted', id)


@job.command(help='Update a job')
@click.argument('id', type=int)
@click.option('-m', '--memo', required=True, help='A memo to update')
@click.pass_obj
def update(api, id, memo):
    """
    :param kamonohashi.JobApi api:
    """
    model = kamonohashi.JobApiModelsEditInputModel(memo=memo)
    result = api.update_job(id, model=model)
    print('updated', result.id)


@job.command('upload-file', help='Upload a file to a job')
@click.argument('id', type=int)
@click.option('-f', '--file-path', type=click.Path(exists=True, dir_okay=False), help='A file path you want to upload')
@click.pass_obj
def upload_file(api, id, file_path):
    """
    :param kamonohashi.JobApi api:
    """
    attached_info = cli.object_storage.upload_file(api.api_client, file_path, 'TrainingHistoryAttachedFiles')
    model = kamonohashi.ComponentsAddFileInputModel(file_name=attached_info.file_name, stored_path=attached_info.stored_path)
    api.add_job_file(id, model=model)


@job.command('list-files', help='List files of a job')
@click.argument('id', type=int)
@click.pass_obj
def list_files(api, id):
    """
    :param kamonohashi.JobApi api:
    """
    result = api.list_job_files(id)
    cli.pprint.pp_table(['file_id', 'file_name'],
                        [[x.file_id, x.file_name] for x in result])


@job.command('download-files', help='Download files of a job')
@click.argument('id', type=int)
@click.option('-d', '--destination', type=click.Path(exists=True, file_okay=False), required=True,
              help='A path to the output files')
@click.pass_obj
def download_files(api, id, destination):
    """
    :param kamonohashi.JobApi api:
    """
    result = api.list_job_files(id, with_url=True)
    pool_manager = api.api_client.rest_client.pool_manager
    for x in result:
        cli.object_storage.download_file(pool_manager, x.url, destination, x.file_name)


@job.command('download-container-files', help='Download files in a container')
@click.argument('id', type=int)
@click.option('-d', '--destination', type=click.Path(exists=True, file_okay=False), required=True,
              help='A path to the output files')
@click.option('-s', '--source', help='A path to the source root in the container')
@click.pass_obj
def download_container_files(api, id, destination, source):
    """
    :param kamonohashi.JobApi api:
    """
    pool_manager = api.api_client.rest_client.pool_manager

    def download_entries(path):
        result = api.list_job_container_files(id, path=path, with_url=True)
        for x in result.files:
            if os.path.isabs(path):
                _, tail = os.path.splitdrive(path)
                cli.object_storage.download_file(pool_manager, x.url, destination + tail, x.file_name)
            else:
                cli.object_storage.download_file(pool_manager, x.url, os.path.join(destination, path), x.file_name)
        for x in result.dirs:
            download_entries(os.path.join(path, x.dir_name))

    source = source if source is not None else '/'
    download_entries(source)


@job.command('delete-file', help='Delete a file of a job')
@click.argument('id', type=int)
@click.option('-f', '--file-id', type=int, required=True, help='A file id you want to delete')
@click.pass_obj
def delete_file(api, id, file_id):
    """
    :param kamonohashi.JobApi api:
    """
    api.delete_job_file(id, file_id)
    print('deleted', file_id)


@job.command(help='Halt a job')
@click.argument('id', type=int)
@click.pass_obj
def halt(api, id):
    """
    :param kamonohashi.JobApi api:
    """
    result = api.halt_job(id)
    print('halted', result.id)


@job.command(help='Complete a job')
@click.argument('id', type=int)
@click.pass_obj
def complete(api, id):
    """
    :param kamonohashi.JobApi api:
    """
    result = api.complete_job(id)
    print('completed', result.id)
