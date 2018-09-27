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

import click

import cli.configuration
import cli.object_storage
import cli.pprint
import cli.util
import kamonohashi


@click.group(short_help='Handling data related information')
@click.pass_context
def data(ctx):
    """Handling various types of information related to data e.g. Create, Upload, Download, Delete, List. """
    api_client = cli.configuration.get_api_client()
    ctx.obj = kamonohashi.DataApi(api_client)


@data.command('list', help='List data filtered by condition')
@click.option('--count', type=click.IntRange(1, 10000), default=1000, show_default=True, help='Maximum number of data to list')
@click.option('--id', help='id')
@click.option('--name', help='name')
@click.option('--memo', help='memo')
@click.option('--created-at', help='created at')
@click.option('--created-by', help='created by')
@click.option('--tag', multiple=True, help='tag  [multiple]')
@click.pass_obj
def list_data(api, count, id, name, memo, created_at, created_by, tag):
    """
    :param kamonohashi.DataApi api:
    """
    per_page = 1000
    command_args = {
        'id': id,
        'name': name,
        'memo': memo,
        'created_at': created_at,
        'created_by': created_by,
        'tag': tag,
    }
    args = dict((key, value) for key, value in command_args.items() if value is not None)
    if count <= per_page:
        result = api.list_data(per_page=count, **args)
    else:
        total_pages = (count - 1) // per_page + 1
        result = page_result = api.list_data(page=1, **args)
        for page in range(2, total_pages + 1):
            if len(page_result) < per_page:
                break
            page_result = api.list_data(page=page, **args)
            first_valid_index = next((i for i, x in enumerate(page_result) if x.id < result[-1].id), per_page)
            result.extend(page_result[first_valid_index:])

    cli.pprint.pp_table(['id', 'name', 'created_at', 'created_by', 'memo', 'tags'],
                        [[x.id, x.name, x.created_at, x.created_by, x.memo, x.tags] for x in result[:count]])


@data.command(help='Get details of a data by ID')
@click.argument('id', type=int)
@click.pass_obj
def get(api, id):
    """
    :param kamonohashi.DataApi api:
    """
    result = api.get_data(id)
    cli.pprint.pp_dict(cli.util.to_dict(result))


@data.command(help='Create a new data')
@click.option('-n', '--name', required=True, help='The name of this data')
@click.option('-f', '--file', type=click.Path(exists=True, dir_okay=False), required=True, multiple=True,
              help='A file path you want to upload  [multiple]')
@click.option('-m', '--memo', help='Free text that can helpful to explain the data')
@click.option('-t', '--tags', multiple=True, help='Attributes to the data  [multiple]')
@click.pass_obj
def create(api, name, file, memo, tags):
    """
    :param kamonohashi.DataApi api:
    """
    model = kamonohashi.DataApiModelsCreateInputModel(
        memo=memo,
        name=name,
        tags=list(tags)
    )
    result = api.create_data(model=model)
    for x in file:
        upload_info = cli.object_storage.upload_file(api.api_client, x, 'Data')
        model = kamonohashi.ComponentsAddFileInputModel(file_name=upload_info.file_name,
                                                        stored_path=upload_info.stored_path)
        api.add_data_file(result.id, model=model)
    print('created', result.id)


@data.command(help='Update the date properties using data ID')
@click.argument('id', type=int)
@click.option('-n', '--name', help='The name of this data')
@click.option('-m', '--memo', help='Free text that can helpful to explain the data')
@click.option('-t', '--tags', multiple=True, help='Attributes to the data  [multiple]')
@click.pass_obj
def update(api, id, name, memo, tags):
    """
    :param kamonohashi.DataApi api:
    """
    model = kamonohashi.DataApiModelsEditInputModel(name=name, memo=memo, tags=list(tags))
    result = api.update_data(id, model=model)
    print('updated', result.id)


@data.command(help='Delete the data using data ID')
@click.argument('id', type=int)
@click.pass_obj
def delete(api, id):
    """
    :param kamonohashi.DataApi api:
    """
    api.delete_data(id)
    print('deleted', id)


@data.command('list-files', help='List file information using data ID')
@click.argument('id', type=int)
@click.pass_obj
def list_files(api, id):
    """
    :param kamonohashi.DataApi api:
    """
    result = api.list_data_files(id)
    cli.pprint.pp_table(['file_id', 'file_name'],
                        [[x.file_id, x.file_name] for x in result])


@data.command('download-files', help='Download files attached to data')
@click.argument('id', type=int)
@click.option('-d', '--destination', type=click.Path(exists=True, file_okay=False), required=True,
              help='A path to the output files')
@click.pass_obj
def download_files(api, id, destination):
    """
    :param kamonohashi.DataApi api:
    """
    result = api.list_data_files(id, with_url=True)
    pool_manager = api.api_client.rest_client.pool_manager
    for x in result:
        cli.object_storage.download_file(pool_manager, x.url, destination, x.file_name)


@data.command('upload-files', help='Upload files to specified data ID')
@click.argument('id', type=int)
@click.option('-f', '--file', type=click.Path(exists=True, dir_okay=False), required=True, multiple=True,
              help='A file path you want to upload  [multiple]')
@click.pass_obj
def upload_files(api, id, file):
    """
    :param kamonohashi.DataApi api:
    """
    for x in file:
        upload_info = cli.object_storage.upload_file(api.api_client, x, 'Data')
        model = kamonohashi.ComponentsAddFileInputModel(file_name=upload_info.file_name,
                                                        stored_path=upload_info.stored_path)
        api.add_data_file(id, model=model)
