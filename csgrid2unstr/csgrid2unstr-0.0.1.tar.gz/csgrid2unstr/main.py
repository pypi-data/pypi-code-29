"""Main executable
"""

# subset of meshio supports
output_filetypes = [
    'vtk',
    'vtu',
    'gmsh',
    'off',
    'exodus',
    'xdmf',
    'dolfin-xml',
    'stl',
]
exts = {
    'vtk': '.vtk',
    'vtu': '.vtu',
    'exodus': '.exo',
    'gmsh': '.msh',
    'dolfin-xml': '.xml',
    'stl': '.stl',
    'xdmf': '.xdmf',
    'off': '.off',
}


def get_parser():
    import argparse

    parser = argparse.ArgumentParser(description=('write CSGrid to unstr'))
    parser.add_argument(
        '-n',
        '--size',
        type=int,
        help='Number of intervals of a square face',
    )
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        help='Output file name, w/o extension',
    )
    parser.add_argument(
        '-r',
        '--refine',
        type=int,
        help='Level of refinements, default is 1',
        default=1,
    )
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        choices=output_filetypes,
        help='Output file format, default is VTK',
        default='vtk',
    )
    parser.add_argument(
        '-b',
        '--binary',
        help='Use BINARY. Notice that this flag is ignored for some formats',
        action='store_true',
        default=False,
    )
    parser.add_argument(
        '-V',
        '--verbose',
        help='Verbose output',
        action='store_true',
        default=False,
    )
    parser.add_argument(
        '-v',
        '--version',
        help='Check version',
        action='store_true',
        default=False,
    )

    return parser


def main(argv=None):
    import os
    import sys
    import time
    from csgrid2unstr.cubed_sphere import CSGrid
    from csgrid2unstr.unstr import Unstr
    from meshio.helpers import write_points_cells
    args = get_parser().parse_args(argv)
    if args.version:
        import csgrid2unstr
        print(csgrid2unstr.__version__)
        sys.exit(0)
    assert args.refine > 0, 'Invalid refinement {}'.format(args.refine)
    assert args.size > 0, 'Invalid number of intervals {}'.format(args.size)
    args.format = args.format.lower()
    assert args.format in output_filetypes, 'Unknown output format in %r' % output_filetypes
    if args.output is None:
        args.output = argv[0].split(os.sep)[-1]
    if args.refine > 1:
        args.output += '%i' + exts[args.format]

        def get_fname(i=None): return args.output % i
    else:
        args.output += exts[args.format]

        def get_fname(i=None): return args.output
    if args.format == 'gmsh':
        args.format += '4'
    if args.format in ['vtk', 'vtu', 'gmsh4']:
        if args.binary:
            args.format += '-binary'
        else:
            args.format += '-ascii'

    for r in range(args.refine):
        fname = get_fname(r)
        N = args.size * 2**r

        if args.verbose:
            sys.stdout.write('\nCreating CSGrid of size {}...\n'.format(N))
            if args.refine > 1:
                sys.stdout.write('refine level is 2^{}\n'.format(r))
            try:
                sys.stdout.flush()
            except:
                pass
        t = time.time()
        cs = CSGrid(N)
        t = time.time()-t

        if args.verbose:
            sys.stdout.write('time: %.2es\n' % t)

        if args.verbose:
            sys.stdout.write('\nConverting CSGrid to Unstr...\n\n')
            try:
                sys.stdout.flush()
            except:
                pass
        t = time.time()
        unstr = Unstr(cs)
        t = time.time()-t

        if args.verbose:
            sys.stdout.write('time: %.2es\n' % t)

        if args.verbose:
            sys.stdout.write('\nUnstructured mesh, points:{}, cells:{}\n'.format(
                unstr.points.shape[0], unstr.cells.shape[0]))
            sys.stdout.write(
                'output format: {}, output filename: {}\n'.format(args.format, fname))
            sys.stdout.write('\nCalling MESHIO...\n')
            try:
                sys.stdout.flush()
            except:
                pass

        t = time.time()
        write_points_cells(fname, unstr.points, {
                           'quad': unstr.cells}, file_format=args.format)
        t = time.time()-t

        if args.verbose:
            sys.stdout.write('time: %.2es\n' % t)
