#!/usr/bin/env python
# Copyright (c) 2018, Julien Seguinot <seguinot@vaw.baug.ethz.ch>
# GNU General Public License v3.0+ (https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Plot recent earthquakes in Japan by region.
"""

import os
import re
import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd


def freqlabel(freq):
    """Convert frequency string to English label."""
    units = dict(H='hour', D='day', M='minute')
    for unit, name in units.items():
        freq = freq.replace('1'+unit, name).replace(unit, ' '+name+'s')
    return freq


def download(region='', csv_file=None):
    """Download latest JMA earthquakes into csv file."""

    # read latest earthquakes list matching region
    url = 'https://www.jma.go.jp/en/quake/quake_singendo_index.html'
    kwa = dict(header=0, index_col=0, parse_dates=True)
    new = pd.read_html(url, **kwa)[3].astype('str')
    new = new[new['Region Name'].str.contains(region, flags=re.IGNORECASE)]

    # filename if none provided
    # FIXME handle empty data
    csv_file = csv_file or '{year}-{region}-aftershocks.csv'.format(
        year=new.index.min().strftime('%Y'), region=region.lower() or 'japan')

    # append to csv
    if os.path.isfile(csv_file):
        old = pd.read_csv(csv_file, dtype='str', **kwa)
        new = new.append(old).drop_duplicates()
    new.to_csv(csv_file)

    # return csv file name
    return csv_file


def plot(csv_file, freq='1D', out_file=None, title=None):
    """Plot earthquake magnitude and frequency from csv file."""

    # load earthquake data
    mag = pd.read_csv(csv_file, index_col=0, parse_dates=True)

    # get magnitude and count
    mag = mag.Magnitude.str[1:].astype('float32')
    mag = mag.tz_localize('UTC').tz_convert('Asia/Tokyo')
    cnt = mag.resample(freq).count().rename('Earthquakes per '+freqlabel(freq))

    # init figure
    fig, ax = plt.subplots()

    # plot counts
    ax.bar(cnt.index, cnt, align='edge', alpha=0.75, color='C1',
           width=0.8*pd.to_timedelta(freq)/pd.to_timedelta('1D'))
    ax.set_ylabel(cnt.name, color='C1')
    ax.locator_params(axis='y', nbins=6)
    ax.tick_params(axis='y', colors='C1')

    # add x label based on mid date
    min_date = mag.index.min()
    max_date = mag.index.max()
    mid_date = min_date + 0.5*(max_date-min_date)
    ax.set_xlabel(mid_date.strftime('%B %Y'))

    # plot magnitude
    ax = ax.twinx()
    ax.plot(mag.index, mag, linestyle='', marker='o', alpha=0.75, color='C0')
    ax.set_ylabel(mag.name, color='C0')
    ax.locator_params(axis='y', nbins=6)
    ax.tick_params(axis='y', colors='C0')
    ax.grid(axis='y')

    # mark strongest earthquake
    ax.text(mag.idxmax(), mag.max(), '  M{:.1f}'.format(mag.max()), color='C0',
            ha='left', va='center')

    # pretty time ticks
    timezone = mag.index.tz
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(tz=timezone))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d', tz=timezone))
    ax.xaxis.set_minor_locator(mdates.AutoDateLocator(
        tz=timezone, minticks=20, maxticks=40, interval_multiples=True))

    # add current time
    now = datetime.datetime.now(tz=timezone)
    ax.axvline(now, linestyle='--', color='C3')
    ax.text(now, mag.max(), 'updated ' + now.strftime('%H:%M'), color='C3',
            ha='right', va='top', rotation=90)

    # infer title if None provided
    title = title or ' '.join(csv_file.split('-')[:2]).title()
    ax.set_title(title + ' earthquake and aftershocks\n'
                 'Source: Japan Meteorological Agency (www.jma.go.jp)',
                 pad=10.0)

    # save
    out_file = out_file or os.path.splitext(csv_file)[0]
    fig.savefig(out_file)


def main():
    """Main program for command-line execution."""

    import argparse

    # parse arguments(future args: from lang)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-a', '--at', default='', metavar='NAME',
                        help='filter by region name (default: Japan)')
    parser.add_argument('-b', '--bin', default='1D', metavar='FREQ',
                        help='frequency bin width (default: 1D)')
    parser.add_argument('-o', '--out', default='', metavar='FILE',
                        help='output figure file name (default: auto)')
    args = parser.parse_args()

    # load data and plot
    csv_file = (os.path.splitext(args.out)[0] + '.csv' if args.out else None)
    csv_file = download(region=args.at, csv_file=csv_file)
    plot(csv_file, freq=args.bin, out_file=args.out)


if __name__ == '__main__':
    main()
