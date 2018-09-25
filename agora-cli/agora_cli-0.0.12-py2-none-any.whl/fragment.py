#!/usr/bin/env python
# coding=utf-8
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
from Queue import Empty, Queue
from datetime import datetime
from threading import Thread

import click
from agora import RedisCache
from agora.engine.utils import Semaphore
from rdflib import URIRef, BNode

from agora_cli.root import cli
from agora_cli.utils import split_arg

__author__ = 'Fernando Serena'


def gen_thread(status, queue, fragment):
    try:
        gen = fragment['generator']
        plan = fragment['plan']
        prefixes = fragment['prefixes']
        first = True
        best_mime = 'text/turtle'   #''application/agora-quad'
        min_quads = '-min' in best_mime
        if best_mime.startswith('application/agora-quad'):
            for c, s, p, o in gen:
                if min_quads:
                    quad = u'{}·{}·{}·{}\n'.format(c, s.n3(plan.namespace_manager),
                                                   p.n3(plan.namespace_manager), o.n3(plan.namespace_manager))
                else:
                    quad = u'{}·{}·{}·{}\n'.format(c, s.n3(), p.n3(), o.n3())

                queue.put(quad)
        else:
            if first:
                for prefix, uri in prefixes.items():
                    queue.put('@prefix {}: <{}> .\n'.format(prefix, uri))
                queue.put('\n')
            for c, s, p, o in gen:
                triple = u'{} {} {} .\n'.format(s.n3(plan.namespace_manager),
                                                p.n3(plan.namespace_manager), o.n3(plan.namespace_manager))

                queue.put(triple)
    except Exception as e:
        status['exception'] = e

    status['completed'] = True


def gen_queue(status, stop_event, queue):
    with stop_event:
        while not status['completed'] or not queue.empty():
            status['last'] = datetime.now()
            try:
                for chunk in queue.get(timeout=1.0):
                    yield chunk
            except Empty:
                if not status['completed']:
                    pass
                elif status['exception']:
                    raise Exception(status['exception'].message)


@cli.command()
@click.argument('q')
@click.option('--arg', multiple=True)
@click.option('--cache-file')
@click.pass_context
def fragment(ctx, q, arg, cache_file):
    args = dict(map(lambda a: split_arg(a), arg))
    if cache_file:
        cache = RedisCache(redis_file=cache_file)
    else:
        cache = None
    stop = Semaphore()
    queue = Queue()
    gen = ctx.obj['gw'].fragment(q, stop_event=stop, cache=cache, **args)

    request_status = {
        'completed': False,
        'exception': None
    }
    stream_th = Thread(target=gen_thread, args=(request_status, queue, gen))
    stream_th.daemon = False
    stream_th.start()

    for chunk in gen_queue(request_status, stop, queue):
        click.echo(chunk, nl=False)
