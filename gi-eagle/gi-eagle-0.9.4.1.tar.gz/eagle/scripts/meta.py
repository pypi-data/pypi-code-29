#Access the meta information

import sys
import argparse
import numpy as np
import h5py

def contains(f, name):
    if not f.attrs.__contains__(name):
        print("variable \"", name, "\" not found in meta information", sep ="", file=sys.stderr)
        return False
    return True


def read(f, name):
    if contains(f, name):
        return f.attrs.get(name)


def delete(f, name):
    if contains(f, name):
        f.attrs.__delitem__(name)


def write(f, name, value):
    f.attrs.create(name, value.encode())


def show_all(f):
    for key in f.attrs.keys():
        print(key, read(f, key).decode(), sep="\t")


def main(args):
    args.path = "/"

    f = h5py.File(args.input)[args.path] #open the hdf5 file

    if args.storelist:
        for line in open(args.storelist):
            g = f
            name, value = line.strip().split()

            split = name.rsplit("/",1)
            if len(split) > 1:
                path, name = split
                if path not in f:
                    print("path", path, "not in file", file=sys.stderr)
                    continue
                g = f[path]
            write(g, name, value)
        return

    # no list

    name = args.name

    if name == None:
        show_all(f)
        return

    split = args.name.rsplit("/",1)
    if len(split) > 1:
        path, name = split
        if path not in f:
            print("path", path, "not in file", file=sys.stderr)
            return
        f = f[path]

    if args.delete:
        delete(f, name)
        return

    if args.s == None:
        print(read(f, name).decode())
        return

    write(f, name, args.s)


def create_parser(parser):
    parser.add_argument('input', help='the eagle-data-file')
    parser.add_argument('name', nargs='?', help='the name of the meta information')
    parser.add_argument('-s', default=None, help='write this value as meta information')
    parser.add_argument('--delete', default=False, action='store_true', help='delete the meta information')
    parser.add_argument('--storelist', nargs='?', help='a list containing key value pairs to store')
    parser.set_defaults(func=main)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    create_parser(parser)
    args = parser.parse_args()

    main(args)
