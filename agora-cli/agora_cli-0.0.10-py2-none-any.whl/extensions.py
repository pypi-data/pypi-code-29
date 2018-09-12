#!/usr/bin/env python
"""
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
  Copyright (C) 2018 Fernando Serena
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

            http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
"""

import json

import click
from rdflib import Graph

from agora_cli.root import cli

__author__ = 'Fernando Serena'


@cli.group()
@click.pass_context
def extensions(ctx):
    pass


@extensions.command('list')
@click.pass_context
def list_extensions(ctx):
    gw = ctx.obj['gw']
    print json.dumps(gw.extensions)


@extensions.command()
@click.pass_context
@click.argument('extension')
def get(ctx, extension):
    gw = ctx.obj['gw']
    g = gw.get_extension(extension)
    print g.serialize(format='turtle')


@extensions.command()
@click.pass_context
@click.argument('extension')
@click.argument('file', type=click.Path(exists=True))
def register(ctx, extension, file):
    gw = ctx.obj['gw']
    with open(file, 'r') as f:
        g = Graph().parse(f, format='turtle')
    gw.add_extension(extension, g)


@extensions.command()
@click.pass_context
@click.argument('extension')
def unregister(ctx, extension):
    gw = ctx.obj['gw']
    gw.delete_extension(extension)
