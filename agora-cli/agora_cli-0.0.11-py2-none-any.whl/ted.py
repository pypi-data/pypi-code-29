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

import click
from rdflib import Graph, URIRef, RDF

from agora_cli.root import cli
from agora_cli.show import show_ted, show_td, show_thing

__author__ = 'Fernando Serena'


@cli.group()
@click.pass_context
def ted(ctx):
    pass


@ted.command()
@click.pass_context
@click.option('--turtle', default=False, is_flag=True)
def show(ctx, turtle):
    ted = ctx.obj['gw'].ted
    show_ted(ted, format='text/turtle' if turtle else 'application/ld+json')


@ted.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('--return-turtle', default=False, is_flag=True)
@click.pass_context
def describe(ctx, file, return_turtle):
    with open(file, 'r') as f:
        g = Graph().parse(f, format='turtle')
    ted = ctx.obj['gw'].add_description(g)
    show_ted(ted, format='text/turtle' if return_turtle else 'application/ld+json')


@ted.command('get-td')
@click.argument('id', type=unicode)
@click.option('--return-turtle', default=False, is_flag=True)
@click.pass_context
def get_td(ctx, id, return_turtle):
    td = ctx.obj['gw'].get_description(id)
    show_td(td, format='text/turtle' if return_turtle else 'application/ld+json')


@ted.command('get-thing')
@click.argument('id', type=unicode)
@click.option('--return-turtle', default=False, is_flag=True)
@click.pass_context
def get_thing(ctx, id, return_turtle):
    g = ctx.obj['gw'].get_thing(id).to_graph()
    show_thing(g, format='text/turtle' if return_turtle else 'application/ld+json')
