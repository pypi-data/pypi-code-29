#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Cat Python pickle file(s) onto standard output, especially DataFrames.

More concretely, display one or more pickle files on standard output allowing
a host of simple transformations along the way.  Intended for when you're
grooving in the $SHELL  and want to avoid firing up Jupyter/IPython."""
import operator
import os
import sys
import typing

import click
import numpy
import pandas

# What types of paths can we hope to load successfully?
PicklePath = click.Path(exists=True, file_okay=True, dir_okay=False,
                        writable=False, readable=True, resolve_path=False,
                        allow_dash=False, path_type=None)

# What defaults are selected for configurable display parameters?
DEFAULT_PRECISION = 17


@click.command()
@click.argument('file', nargs=-1, type=PicklePath)
@click.option('--append-index', '-a', type=str, multiple=True,
              metavar='COLUMN', help='Append named column to the index.')
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
              help='Set precision for floating point.')
@click.option('--query', '-q', type=str, metavar='QUERY',
              help='Show only rows satisfying a query.')
@click.option('--reset-index', '-r', type=str, multiple=True,
              metavar='LEVEL', help='Remove named level from the index.')
@click.option('--sort-index', '-s', is_flag=True,
              help='Sort according to the index.')
@click.option('--types', '-t', is_flag=True,
              help='Show the type, not the value, of each datum.')
def main(
        file: typing.List[str],
        *,
        append_index: typing.Sequence[str] = None,
        buffer: typing.Any = None,  # Not a click.option
        csv: typing.Optional[bool] = None,
        no_index: typing.Optional[bool] = None,
        location: typing.Optional[bool] = None,
        multi_sparse: typing.Optional[bool] = None,
        precision: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        reset_index: typing.Sequence[str] = None,
        sort_index: typing.Optional[bool] = None,
        types: typing.Optional[bool] = None
) -> None:
    """Cat Python pickle file(s) onto standard output, especially DataFrames."""
    for f in file:
        o = pandas.read_pickle(f)
        df = coerce_to_df(o)
        df = transform_data(df, query=query, types=types)
        if location:
            df.insert(loc=0, column='location', value=f)
        df = transform_index(df,
                             append_index=append_index,
                             reset_index=reset_index,
                             sort_index=sort_index)
        emit_output(df,
                    buffer=buffer,
                    csv=csv,
                    no_index=no_index,
                    multi_sparse=multi_sparse,
                    precision=precision)


def coerce_to_df(o: typing.Any) -> pandas.DataFrame:
    """Coerce anything sensible into a DataFrame or else die trying."""
    # Degenerate
    if o is None:
        return pandas.DataFrame()

    # Identity
    if isinstance(o, pandas.DataFrame):
        return o

    # Upgrade
    if isinstance(o, pandas.Series):
        return o.to_frame()

    # Coerce by applying a sequence of transformations
    type_incoming = type(o).__name__
    try:
        # Coerce dict-likes into 2D lists-of-tuples
        try:
            o = list(o.items())
        except AttributeError:
            pass

        # Coerce anything into a NumPy array
        o = numpy.asanyarray(o)

        # NumPy arrays turn nicely into DataFrames
        return pandas.DataFrame(o)
    except:
        raise RuntimeError("Failed to coerce type '{}'".format(type_incoming))

    assert False, "Unreachable"


def transform_data(
        df: pandas.DataFrame,
        *,
        query: typing.Optional[str] = None,
        types: typing.Optional[bool] = None
) -> pandas.DataFrame:
    """Apply possible sequence of data transformations."""
    if query is not None:
        df = df.query(query)
    if types:
        df = (df.applymap(type)
              .applymap(operator.attrgetter('__name__')))
    return df


def transform_index(
        df: pandas.DataFrame,
        *,
        append_index: typing.Sequence[str] = None,
        reset_index: typing.Sequence[str] = None,
        sort_index: typing.Optional[bool] = None
) -> pandas.DataFrame:
    """Apply possible sequence of index transformations."""
    # append_index and reset_index contain strings from the CLI arguments
    # but the DataFrame may include numeric column names.  Make all strings.
    df.columns = [str(c) for c in df.columns]

    for r in reset_index:
        df = df.reset_index(level=r, drop=False)
    if append_index:
        df = df.set_index(keys=list(append_index),
                          append=not naturally_indexed(df))
    if sort_index:
        df = df.sort_index(axis=0, kind='mergesort')

    return df


# Surely there must be a better way...?
def naturally_indexed(df: pandas.DataFrame) -> bool:
    "Is the DataFrame index indistinguishable from just numbering the rows?"""
    return ((not df.index.name) and
            (df.index == pandas.RangeIndex(start=0, stop=len(df))).all())


def emit_output(
        df: pandas.DataFrame,
        *,
        buffer: typing.Any = None,
        csv: typing.Optional[bool] = None,
        no_index: typing.Optional[bool] = None,
        multi_sparse: typing.Optional[bool] = None,
        precision: typing.Optional[int] = None
) -> None:
    """Output the DataFrame to the specified buffer with desired formatting.."""
    buffer = sys.stdout if buffer is None else buffer

    with kid_gloves_off(multi_sparse=multi_sparse, precision=precision):
        index = not (no_index or naturally_indexed(df))

        if csv:  # Properly handles many edge cases
            df.to_csv(buffer, index=index)

        elif df.empty:  # Avoid "Empty DataFrame..." message from to_string(...)
            header = []
            header.extend(df.index.names if index else ())
            header.extend(df.columns)
            print(*header, sep=' ', end=os.linesep, file=buffer)

        else:  # Default to_string(...) lacks a trailing newline w/ buffer
            df.to_string(buffer, index=index)
            buffer.write(os.linesep)


def kid_gloves_off(
        multi_sparse: typing.Optional[bool] = None,
        precision: typing.Optional[int] = None,
) -> pandas.option_context:
    """Like, seriously, Pandas just give me the entirety of my data."""
    return pandas.option_context(
        'display.date_yearfirst', True,
        'display.expand_frame_repr', True,
        'display.max_categories', 65536,
        'display.max_columns', None,
        'display.max_colwidth', 65536,
        'display.max_rows', None,
        'display.max_seq_items', None,
        'display.multi_sparse', bool(multi_sparse),
        'display.precision', (precision if precision is not None
                              else DEFAULT_PRECISION),
        'display.show_dimensions', False,
        'display.width', None,
    )


if __name__ == '__main__':
    main()
