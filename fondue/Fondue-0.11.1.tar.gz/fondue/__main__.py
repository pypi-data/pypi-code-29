import os
import asyncio
import argparse

import uvloop

from fondue.protocol import main as protocol_main
from fondue.tap import Tap
from fondue.api import send_to_endpoint

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

loop = asyncio.get_event_loop()

parser = argparse.ArgumentParser('fondue')
parser.add_argument('-p', type=int, default=3333, help='The port to bind to', metavar='port', dest='port')
subparsers = parser.add_subparsers(dest='subcommand')
parser_serve = subparsers.add_parser('serve')
parser_install = subparsers.add_parser('install')
parser_install.add_argument('id', type=int, help='The user id to give the tap device to')
parser_view = subparsers.add_parser('view')
parser_add = subparsers.add_parser('add')
parser_add.add_argument('addr', type=str, help='The address of the peer to add', metavar='address')


def main():
    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    if args.subcommand == 'serve':
        loop.run_until_complete(protocol_main(loop, parser, args))
    elif args.subcommand == 'install':
        tap = Tap(name='fond%s' % args.port)
        tap.make_persistent(args.id)
    else:
        loop.run_until_complete(send_to_endpoint(loop, args))

if __name__ == '__main__':
    main()
