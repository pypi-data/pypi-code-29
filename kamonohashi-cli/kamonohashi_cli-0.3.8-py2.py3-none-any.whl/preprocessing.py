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
import os
import os.path

import click

import cli.configuration
import cli.object_storage
import cli.pprint
import cli.util
import kamonohashi


@click.group()
@click.pass_context
def preprocessing(ctx):
    """Create and manage KAMONOHASHI preprocessings"""
    api_client = cli.configuration.get_api_client()
    ctx.obj = kamonohashi.PreprocessingApi(api_client)


@preprocessing.command('list', help='List preprocessings filtered by condition')
@click.option('--count', type=click.IntRange(1, 10000), default=1000, show_default=True, help='Maximum number of data to list')
@click.option('--id', help='id')
@click.option('--name', help='name')
@click.option('--created-at', help='created at')
@click.option('--memo', help='memo')
@click.pass_obj
def list_preprocessings(api, count, id, name, created_at, memo):
    """
    :param kamonohashi.PreprocessingApi api:
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
        result = api.list_preprocessings(per_page=count, **args)
    else:
        total_pages = (count - 1) // per_page + 1
        result = page_result = api.list_preprocessings(page=1, **args)
        for page in range(2, total_pages + 1):
            if len(page_result) < per_page:
                break
            page_result = api.list_preprocessings(page=page, **args)
            first_valid_index = next((i for i, x in enumerate(page_result) if x.id < result[-1].id), per_page)
            result.extend(page_result[first_valid_index:])

    cli.pprint.pp_table(['id', 'name', 'created_at', 'memo'],
                        [[x.id, x.name, x.created_at, x.memo] for x in result[:count]])


@preprocessing.command(help='Get details of a preprocessing')
@click.argument('id', type=int)
@click.option('-d', '--destination', type=click.Path(dir_okay=False), help='A file path of the output as a json file')
@click.pass_obj
def get(api, id, destination):
    """
    :param kamonohashi.PreprocessingApi api:
    """
    if destination is None:
        result = api.get_preprocessing(id)
        cli.pprint.pp_dict(cli.util.to_dict(result))
    else:
        with cli.util.release_conn(api.get_preprocessing(id, _preload_content=False)) as result:
            logging.info('open %s', destination)
            with open(destination, 'wb') as f:
                logging.info('begin io %s', destination)
                f.write(result.data)
                logging.info('end io %s', destination)
        print('save', id, 'as', destination)


@preprocessing.command(help='Create a new preprocessing')
@click.option('-f', '--file', required=True, type=click.Path(exists=True, dir_okay=False),
              help="""{
  "name": @name,
  "entryPoint": @entryPoint,
  "containerImage": {
    "image": @image,
    "tag": "@tag,
  },
  "gitModel": {
    "repository": @repository,
    "owner": @owner,
    "branch": @branch,
    "commitId": @commitId,
  },
  "memo": @memo
}""")
@click.pass_obj
def create(api, file):
    """
    :param kamonohashi.PreprocessingApi api:
    """
    logging.info('open %s', file)
    with io.open(file, 'r', encoding='utf-8') as f:
        logging.info('begin io %s', file)
        json_dict = json.load(f)
        logging.info('end io %s', file)
    result = api.create_preprocessing(model=json_dict)
    print('created', result.id)


@preprocessing.command(help='Update a preprocessing')
@click.argument('id', type=int)
@click.option('-f', '--file', required=True, type=click.Path(exists=True, dir_okay=False),
              help="""{
  "name": @name,
  "entryPoint": @entryPoint,
  "containerImage": {
    "image": @image,
    "tag": "@tag,
  },
  "gitModel": {
    "repository": @repository,
    "owner": @owner,
    "branch": @branch,
    "commitId": @commitId,
  },
  "memo": @memo
}""")
@click.pass_obj
def update(api, id, file):
    """
    :param kamonohashi.PreprocessingApi api:
    """
    logging.info('open %s', file)
    with io.open(file, 'r', encoding='utf-8') as f:
        logging.info('begin io %s', file)
        json_dict = json.load(f)
        logging.info('end io %s', file)
    result = api.update_preprocessing(id, model=json_dict)
    print('updated', result.id)


@preprocessing.command('update-meta-info', help='Update meta information of a preprocessing')
@click.argument('id', type=int)
@click.option('-n', '--name', help='A name to update')
@click.option('-m', '--memo', help='A memo to update')
@click.pass_obj
def patch(api, id, name, memo):
    """
    :param kamonohashi.PreprocessingApi api:
    """
    model = kamonohashi.PreprocessingApiModelsEditInputModel(name=name, memo=memo)
    result = api.patch_preprocessing(id, model=model)
    print('meta-info updated', result.id)


@preprocessing.command(help='Delete a preprocesssing')
@click.argument('id', type=int)
@click.pass_obj
def delete(api, id):
    """
    :param kamonohashi.PreprocessingApi api:
    """
    api.delete_preprocessing(id)
    print('deleted', id)


@preprocessing.command('list-histories', help='List histories of a preprocessing')
@click.argument('id', type=int)
@click.pass_obj
def list_histories(api, id):
    """
    :param kamonohashi.PreprocessingApi api:
    """
    result = api.list_preprocessing_histories(id)
    cli.pprint.pp_table(['data_id', 'data_name', 'created_at', 'status'],
                        [[x.data_id, x.data_name, x.created_at, x.status] for x in result])


@preprocessing.command('build-history', help='Build history structure of a preprocessing')
@click.argument('id', type=int)
@click.option('-did', '--data-id', type=int, required=True, help='A source data id')
@click.option('-s', '--source', type=click.Path(exists=True, file_okay=False), required=True, help='A directory path to the processed data')
@click.option('-m', '--memo', help='Free text that can helpful to explain the data')
@click.option('-t', '--tags', multiple=True, help='Attributes to the data  [multiple]')
@click.pass_obj
def build_history(api, id, data_id, source, memo, tags):
    """
    :param kamonohashi.PreprocessingApi api:
    """
    api.create_preprocessing_history(id, data_id)

    for entry in os.listdir(source):
        if os.path.isdir(os.path.join(source, entry)):
            uploaded_files = []
            for root, _, files in os.walk(os.path.join(source, entry)):
                for file in files:
                    upload_info = cli.object_storage.upload_file(api.api_client, os.path.join(root, file), 'Data')
                    uploaded_files.append(kamonohashi.ComponentsAddFileInputModel(file_name=upload_info.file_name,
                                                                                  stored_path=upload_info.stored_path))
            model = kamonohashi.PreprocessingApiModelsAddOutputDataInputModel(files=uploaded_files, name=entry,
                                                                              memo=memo, tags=list(tags))
            api.add_preprocessing_history_files(id, data_id, model=model)

    result = api.complete_preprocessing_history(id, data_id)
    print('built ', result.preprocess_id, '.', result.data_id, sep='')


@preprocessing.command('build-history-files', help='Build file structure for existing history')
@click.argument('id', type=int)
@click.option('-did', '--data-id', type=int, required=True, help='A source data id')
@click.option('-s', '--source', type=click.Path(exists=True, file_okay=False), required=True, help='A directory path to the processed data')
@click.option('-m', '--memo', help='Free text that can helpful to explain the data')
@click.option('-t', '--tags', multiple=True, help='Attributes to the data  [multiple]')
@click.pass_obj
def build_history_files(api, id, data_id, source, memo, tags):
    """
    :param kamonohashi.PreprocessingApi api:
    """
    for entry in os.listdir(source):
        if os.path.isdir(os.path.join(source, entry)):
            uploaded_files = []
            for root, _, files in os.walk(os.path.join(source, entry)):
                for file in files:
                    upload_info = cli.object_storage.upload_file(api.api_client, os.path.join(root, file), 'Data')
                    uploaded_files.append(kamonohashi.ComponentsAddFileInputModel(file_name=upload_info.file_name,
                                                                                  stored_path=upload_info.stored_path))
            model = kamonohashi.PreprocessingApiModelsAddOutputDataInputModel(files=uploaded_files, name=entry,
                                                                              memo=memo, tags=list(tags))
            api.add_preprocessing_history_files(id, data_id, model=model)

    api.complete_preprocessing_history(id, data_id)


@preprocessing.command('delete-history', help='Delete a history of a preprocessing')
@click.argument('id', type=int)
@click.option('-did', '--data-id', type=int, required=True, help='A source data id')
@click.pass_obj
def delete_history(api, id, data_id):
    """
    :param kamonohashi.PreprocessingApi api:
    """
    api.delete_preprocessing_history(id, data_id)
    print('deleted ', id, '.', data_id, sep='')


@preprocessing.command('halt-history', help='Halt a preprocessing of a history')
@click.argument('id', type=int)
@click.option('-did', '--data-id', type=int, required=True, help='A source data id')
@click.pass_obj
def halt_history(api, id, data_id):
    """
    :param kamonohashi.PreprocessingApi api:
    """
    result = api.halt_preprocessing_history(id, data_id)
    print('halted ', result.preprocess_id, '.', result.data_id, sep='')
