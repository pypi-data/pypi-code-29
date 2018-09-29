#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Cat Python pickle file(s) onto standard output, especially DataFrames.

More concretely, display one or more pickle files on standard output
allowing a host of simple transformations along the way.  Intended for
when you're grooving on the command line and want to avoid firing
up Jupyter/IPython.  Or maybe you like pipelines.  Or maybe you hate
pipelines but Knuth-vs-McIlroy 1986 lives large in your memory."""
import operator
import os
import sys
import typing

import click
import pandas

# TODO Maintain uniform output structure on empty DataFrames
# TODO Handle non-DataFrame pickles
# TODO Consider providing a describe summarizer
# TODO Consider providing a quantiles summarizer


# What types of paths can we hope to load successfully?
PicklePath = click.Path(exists=True, file_okay=True, dir_okay=False,
                        writable=False, readable=True, resolve_path=False,
                        allow_dash=False, path_type=None)

# What defaults are selected for configurable display parameters?
DEFAULT_PRECISION = 17


@click.command()
@click.argument('file', nargs=-1, type=PicklePath)
@click.option('--append-index', '-a', type=str, multiple=True,
              help='Append named column to the index.')
@click.option('--csv', '-c', is_flag=True,
              help='Emit CSV instead of formatted table.')
@click.option('--location', '-l', is_flag=True,
              help='Prefix each row with the location of the file')
@click.option('--multi-sparse', '-m', is_flag=True,
              help='Sparsify any MultiIndex display.')
@click.option('--no-index', '-n', is_flag=True,
              help='Do not display the index.')
@click.option('--precision', '-p', type=click.IntRange(min=1, max=None),
              show_default=True, metavar='DIGITS', default=DEFAULT_PRECISION,
              help='Change precision for floating point.')
@click.option('--query', '-q', type=str, metavar='QUERY',
              help='Show only rows satisfying a query.')
@click.option('--reset-index', '-r', type=str, multiple=True,
              help='Remove named column from the index.')
@click.option('--sort-index', '-s', is_flag=True,
              help='Sort according to the index.')
@click.option('--types', '-t', is_flag=True,
              help='Show the type, not the value, of each datum.')
def main(
        file: typing.List[str],
        *,
        append_index: typing.Sequence[str] = None,
        csv: typing.Optional[bool] = None,
        no_index: typing.Optional[bool] = None,
        location: typing.Optional[bool] = None,
        multi_sparse: typing.Optional[bool] = None,
        precision: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        reset_index: typing.Sequence[str] = None,
        sort_index: typing.Optional[bool] = None,
        types: typing.Optional[bool] = None
):
    """Cat Python pickle file(s) onto standard output, especially DataFrames."""
    with kid_gloves_off(multi_sparse=multi_sparse, precision=precision):
        for f in file:
            # Load the pickle into a DataFrame
            df = pandas.read_pickle(f)
            if isinstance(df, pandas.Series):
                df = df.to_frame()

            # Possibly transform the data
            if query is not None:
                df = df.query(query)
            if types:
                df = (df.applymap(type)
                      .applymap(operator.attrgetter('__name__')))
            if location:
                df.insert(loc=0, column='location', value=f)

            # Possibly transform the index
            if append_index:
                df = df.set_index(keys=list(append_index),
                                  append=not naturally_indexed(df))
            for r in reset_index:
                df = df.reset_index(level=r, drop=False)
            if sort_index:
                df = df.sort_index(axis=0, kind='mergesort')

            # Emit output in the desired format
            if csv:
                df.to_csv(sys.stdout, index=not no_index)
            else:
                df.to_string(sys.stdout, index=not no_index)
                if not df.empty:
                    sys.stdout.write(os.linesep)


def kid_gloves_off(
        multi_sparse: typing.Optional[bool] = None,
        precision: typing.Optional[int] = None,
) -> pandas.option_context:
    """Like, seriously, Pandas just give me the entirety of my data."""
    return pandas.option_context(
        'display.date_yearfirst', True,
        'display.expand_frame_repr', True,
        'display.max_categories', 1024,
        'display.max_columns', None,
        'display.max_colwidth', 1024,
        'display.max_rows', None,
        'display.max_seq_items', None,
        'display.multi_sparse', bool(multi_sparse),
        'display.precision', (precision if precision is not None
                              else DEFAULT_PRECISION),
        'display.show_dimensions', False,
        'display.width', None,
    )


# Surely there must be a better way...?
def naturally_indexed(df: pandas.DataFrame) -> bool:
    "Is the DataFrame index indistinguishable from just numbering the rows?"""
    return (df.index == pandas.RangeIndex(start=0, stop=len(df))).all()


if __name__ == '__main__':
    main()
