#!python
# -*- coding: utf-8 -*-

import argparse
import cachelite

if __name__ == '__main__':

    arg_parse = argparse.ArgumentParser(add_help=True)
    arg_parse.add_argument("-c","--cmd",dest="command", help="command to cachelite", choices=["get","set","delete"] ,required=True)
    arg_parse.add_argument("-d", "--dir", dest="dir", help="kvs dir", required=True)
    arg_parse.add_argument("-k", "--key", dest="key", help="key")
    arg_parse.add_argument("-v", "--verbose",action="store_true",  dest="verbose", help="verbose")
    arg_parse.add_argument("--value-file", dest="value_strm", type=argparse.FileType("r"), help="input key")
    arg_parse.add_argument("--value", dest="value", help="input key")

    args = arg_parse.parse_args()

    if args.verbose:
        debug = True
    else:
        debug = False

    if args.command == "get":
        cachelite = cachelite.CacheLite(args.dir, raise_write_error=debug, raise_read_error=True)
        if debug:
            print("file:" + str(cachelite._key_to_file_path(args.key)) )
        print( cachelite[args.key] )

    elif args.command == "set":
        cachelite = cachelite.CacheLite(args.dir, raise_write_error=debug, raise_read_error=True)
        if debug:
            print("file:" + str(cachelite._key_to_file_path(args.key)) )
        if argparse.value_strm:
            data = argparse.value_strm.read()
            cachelite[args.key] = data
        else:
            cachelite[args.key] = args.value

    elif args.command == "delete":
        cachelite = cachelite.CacheLite(args.dir, raise_write_error=debug, raise_read_error=True)
        if debug:
            print("file:" + str(cachelite._key_to_file_path(args.key)) )
        del cachelite[args.key]
    else:
        raise cachelite.CacheLiteError("unknown command:%s" % args.cmd)



