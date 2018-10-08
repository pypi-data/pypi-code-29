#!/usr/bin/env python

# Usage: benchmark_plot.py <plot file>
# <plot file> is the path of a file containing one timing per line, in the
# HH:mm:ss.S format. The timings are cumulative.

import sys

from glob import glob

import arrow

from matplotlib import pyplot as plt


ptn = sys.argv[1]

files = glob(ptn)
print(f'Files collected: {files} from {ptn}')
for fname in files:

    ta = arrow.get('00:00:00.0000', 'HH:mm:ss.S')
    px = []
    py = []

    i = 0
    print(f'Analyzing {fname}')
    with open(fname, 'r') as fh:
        for line in fh:
            tb = arrow.get(line.strip(), 'HH:mm:ss.S')
            tdelta = tb - ta

            px.append(i)
            # Divide by 1000 for µs → ms, by further 10 because samples are per
            # 10 requests.
            py.append(tdelta.microseconds // 10000)

            ta = tb
            i += 10

    plt.plot(px, py, label=fname)

plt.xlabel('Requests')
plt.ylabel('ms per request')
plt.title('Lakesuperior & FCREPO/Modeshape Benchmarks')
plt.legend()
plt.show()
