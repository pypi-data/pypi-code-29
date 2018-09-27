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

import io
import json
import logging
import os.path

import click

import cli.configuration
import cli.object_storage
import cli.pprint
import cli.util
import kamonohashi


@click.group()
@click.pass_context
def data_set(ctx):
    """Create and manage KAMONOHASHI datasets"""
    api_client = cli.configuration.get_api_client()
    ctx.obj = kamonohashi.DataSetApi(api_client)


@data_set.command('list', help='List datasets filtered by condition')
@click.option('--count', type=click.IntRange(1, 10000), default=1000, show_default=True, help='Maximum number of data to list')
@click.option('--id', help='id')
@click.option('--name', help='name')
@click.option('--memo', help='memo')
@click.option('--created-at', help='created at')
@click.pass_obj
def list_datasets(api, count, id, name, memo, created_at):
    """
    :param kamonohashi.DataSetApi api:
    """
    per_page = 1000
    command_args = {
        'id': id,
        'name': name,
        'memo': memo,
        'created_at': created_at,
    }
    args = dict((key, value) for key, value in command_args.items() if value is not None)
    if count <= per_page:
        result = api.list_datasets(per_page=count, **args)
    else:
        total_pages = (count - 1) // per_page + 1
        result = page_result = api.list_datasets(page=1, **args)
        for page in range(2, total_pages + 1):
            if len(page_result) < per_page:
                break
            page_result = api.list_datasets(page=page, **args)
            first_valid_index = next((i for i, x in enumerate(page_result) if x.id < result[-1].id), per_page)
            result.extend(page_result[first_valid_index:])

    cli.pprint.pp_table(['id', 'name', 'created_at', 'memo'],
                        [[x.id, x.name, x.created_at, x.memo] for x in result[:count]])


@data_set.command(help='Get details of a detaset')
@click.argument('id', type=int)
@click.option('-d', '--destination', type=click.Path(dir_okay=False), help='A file path of the output as a json file')
@click.pass_obj
def get(api, id, destination):
    """
    :param kamonohashi.DataSetApi api:
    """
    if destination is None:
        result = api.get_dataset(id)
        cli.pprint.pp_dict(cli.util.to_dict(result))
    else:
        with cli.util.release_conn(api.get_dataset(id, _preload_content=False)) as result:
            logging.info('open %s', destination)
            with open(destination, 'wb') as f:
                logging.info('begin io %s', destination)
                f.write(result.data)
                logging.info('end io %s', destination)
        print('save', id, 'as', destination)


@data_set.command(help='Create a new dataset')
@click.option('-f', '--file', required=True, type=click.Path(exists=True, dir_okay=False),
              help="""{
  "name": @name,
  "memo": @memo,
  "entries": {
    "additionalProp1": [
      {
        "id": @dataId
      }
    ],
    "additionalProp2": [
      {
        "id": @dataId
      }
    ],
    "additionalProp3": [
      {
        "id": @dataId
      }
    ]
  }
}""")
@click.pass_obj
def create(api, file):
    """
    :param kamonohashi.DataSetApi api:
    """
    logging.info('open %s', file)
    with io.open(file, 'r', encoding='utf-8') as f:
        logging.info('begin io %s', file)
        json_dict = json.load(f)
        logging.info('end io %s', file)
    result = api.create_dataset(model=json_dict)
    print('created', result.id)


@data_set.command(help='Update a dataset')
@click.argument('id', type=int)
@click.option('-f', '--file', required=True, type=click.Path(exists=True, dir_okay=False),
              help="""{
  "name": @name,
  "memo": @memo,
  "entries": {
    "additionalProp1": [
      {
        "id": @dataId
      }
    ],
    "additionalProp2": [
      {
        "id": @dataId
      }
    ],
    "additionalProp3": [
      {
        "id": @dataId
      }
    ]
  }
}""")
@click.pass_obj
def update(api, id, file):
    """
    :param kamonohashi.DataSetApi api:
    """
    logging.info('open %s', file)
    with io.open(file, 'r', encoding='utf-8') as f:
        logging.info('begin io %s', file)
        json_dict = json.load(f)
        logging.info('end io %s', file)
    result = api.update_dataset(id, model=json_dict)
    print('updated', result.id)


@data_set.command('update-meta-info', help='Update meta information of a dataset')
@click.argument('id', type=int)
@click.option('-n', '--name', help='A new name')
@click.option('-m', '--memo', help='A new memo')
@click.pass_obj
def update_meta_info(api, id, name, memo):
    """
    :param kamonohashi.DataSetApi api:
    """
    model = kamonohashi.DataSetApiModelsEditInputModel(name=name, memo=memo)
    result = api.patch_dataset(id, model=model)
    print('meta-info updated', result.id)


@data_set.command(help='Delete a dataset')
@click.argument('id', type=int)
@click.pass_obj
def delete(api, id):
    """
    :param kamonohashi.DataSetApi api:
    """
    api.delete_dataset(id)
    print('deleted', id)


@data_set.command('download-files', help='Download files of a dataset')
@click.argument('id', type=int)
@click.option('-d', '--destination', type=click.Path(exists=True, file_okay=False), required=True,
              help='An output directory path')
@click.option('-t', '--type', 'data_type', type=click.Choice(['training', 'testing', 'validation']), multiple=True,
              help='A data type to download  [multiple]')
@click.pass_obj
def download_files(api, id, destination, data_type):
    """
    :param kamonohashi.DataSetApi api:
    """
    result = api.list_dataset_files(id, with_url=True)
    pool_manager = api.api_client.rest_client.pool_manager
    for entry in result.entries:
        if not data_type or entry.type in data_type:
            for file in entry.files:
                destination_dir_path = os.path.join(destination, entry.type, str(file.id))
                cli.object_storage.download_file(pool_manager, file.url, destination_dir_path, file.file_name)


@data_set.command('list-data-types', help='List data types of a dataset')
@click.pass_obj
def list_data_types(api):
    """
    :param kamonohashi.DataSetApi api:
    """
    result = api.list_dataset_datatypes()
    for x in result:
        print(x.name)
