#!/usr/bin/env python3
"""
depth_stat.py

Copyright (c) 2017-2018 Guanliang Meng <mengguanliang@foxmail.com>.

This file is part of MitoZ.

MitoZ is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

MitoZ is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with MitoZ.  If not, see <http://www.gnu.org/licenses/>.

"""

import sys
import collections
from itertools import groupby
import matplotlib
matplotlib.use('Cairo')
# This call to matplotlib.use() has no effect because the backend has already
# been chosen; matplotlib.use() must be called *before* pylab,
# matplotlib.pyplot, or matplotlib.backends is imported for the first time.
# see https://matplotlib.org/faq/usage_faq.html#what-is-a-backend
# for more backends

import matplotlib.pyplot as plt
# if matplotlib.use('agg') doesn't work, try:
# plt.switch_backend('agg')

import seaborn as sns
import argparse


def get_para():
    desc = '''To extract the sequence depth from depthfile.

The depthfile content format:
seqid1 depth1 depth2 depth3 ...
seqid2 depth1 depth2 depth3 ...


This script is part of the MitoZ project, by Guanliang MENG.
See https://github.com/linzhi2013/depth_stat.
    '''

    parser = argparse.ArgumentParser(description=desc,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-i', dest='depthfile', metavar='<file>',
        required=True, help='input depthfile')

    parser.add_argument('-q', dest='seqid', metavar='<str>', required=False,
        help='sequence id')

    parser.add_argument('-a', dest='seqstart', type=int, metavar='<int>',
        default=-1,
        required=False, help='the start position, Python-style (0-leftmost)')

    parser.add_argument('-b', dest='seqend', type=int, metavar='<int>',
        default=-1,
        required=False, help='the end position, Python-style for slicing')

    parser.add_argument('-f', dest='queryfile', metavar='<file>',
        required=False, help="a file of 'seqid start end' list on each line")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()
    if not args.queryfile and not args.seqid:
        sys.exit('you must input "-f" or "-q -a -b"!')

    if args.seqstart < 0 or args.seqend < 0:
        sys.exit('-a and -b must all be >= 0!')

    return args


def get_seqid_start_end(queryfile=None):
    '''
    return a list of tuples of (seqid, start, end)
    '''
    seqid_start_end = []
    with open(queryfile, 'r') as fh:
        for i in fh:
            i = i.strip()
            seqid, start, end = i.split()[0:3]
            start, end = [int(j) for j in (start, end)]
            seqid_start_end.append((seqid, start, end))

    return seqid_start_end


class SeqDepth(object):
    """docstring for ClassName"""

    def __init__(self, depthfile):
        #super(SeqDepth, self).__init__()
        self.depthfile = depthfile

        self.seqid_depth = self.__read_depth__(self.depthfile)


    def __read_depth__(self, depthfile=None):
        '''
        The depthfile content format:

        seqid1 depth1 depth2 depth3 ...
        seqid2 depth1 depth2 depth3 ...

        return:

        A dictionary, seqids are the keys and depths as a list.

        '''
        seqid_depth = collections.defaultdict(list)
        with open(depthfile, 'r') as fh:
            for i in fh:
                i = i.strip()
                line = i.split()
                seqid = line[0]
                depths = [int(j) for j in line[1:]]
                seqid_depth[seqid].extend(depths)

        return seqid_depth


    def extract_range_depth(self, seqid=None, start=None, end=None):
        '''
        return a list of depths from start to end.

        Note: the start and end must be Python-style for slicing.

        '''
        if seqid not in self.seqid_depth:
            raise KeyError('{0} not in {1}'.format(seqid, self.depthfile))

        return self.seqid_depth[seqid][start:end]


    def range_depth_stat(self, seqid=None, start=None, end=None):
        '''
        return a tuple of (seqid, start, end, min_depth, mean_depth, max_depth)
        '''
        depths = self.extract_range_depth(seqid=seqid, start=start, end=end)

        min_depth = min(depths)
        mean_depth = round(sum(depths) / len(depths), 2)
        max_depth = max(depths)

        return seqid, start, end, min_depth, mean_depth, max_depth


    def range_depth_freq(self, seqid=None, start=None, end=None, outfile=None):
        '''
        get the frequency distribution of depths from `start` to `end`.

        and get a pdf file of depth ~ frequencey histogram in current directory
        or you can set the `outfile`.

        Return:
            [(depth1, count1), (depth2, count2), ...]
        '''
        depths = self.extract_range_depth(seqid=seqid, start=start, end=end)
        depths = sorted(depths)

        depths_freq = [(key, len(list(group))) for key, group in groupby(depths)]

        depth_series = [i[0] for i in depths_freq]
        depth_count = [i[1] for i in depths_freq]

        height = 18 * len(depth_series) / 100
        if height < 18:
            height = 18

        fig = plt.figure(figsize=(15,height))
        ax = sns.countplot(y=depths, order=depth_series[::-1])
        ax.set_ylabel('Sequencing depth (X)')

        if outfile:
            fig.savefig(outfile)
        else:
            fig.savefig('{0}_{1}_{2}_freq_count.pdf'.format(seqid, start, end))

        return depths_freq


def main():
    args = get_para()
    seqd_obj = SeqDepth(args.depthfile)

    if args.queryfile:
        seqid_start_end = get_seqid_start_end(queryfile=None)
    else:
        seqid_start_end = [(args.seqid, args.seqstart, args.seqend)]

    for seqid, start, end in seqid_start_end:
        seqid, start, end, min_depth, mean_depth, max_depth = seqd_obj.range_depth_stat(seqid=seqid, start=start, end=end)
        print('seqid:', seqid)
        print('start:', start)
        print('end:', end)
        print('min_depth:', min_depth)
        print('mean_depth:', mean_depth)
        print('max_depth:', max_depth)

        depths_freq = seqd_obj.range_depth_freq(seqid=seqid, start=start, end=end)
        print(depths_freq)


if __name__ == '__main__':
    main()

