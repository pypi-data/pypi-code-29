# -*- coding: utf-8 -*-

"""
Console script for blind_files.

nounlist from http://www.desiquintans.com/downloads/nounlist/nounlist.txt

"""

import csv
import sys
from itertools import permutations
from pathlib import Path

import click

from blind_files.aho_corasick_path_generator import AhoCorasickPathGenerator
from blind_files.delimiter_path_generator import DelimiterPathGenerator
from blind_files.identifier_mapper import IdentifierMapper


@click.command()
@click.option(
    '--key',
    '-k',
    default='key',
)
@click.option(
    "--input-dir",
    '-i',
    type=click.Path(exists=True, file_okay=False),
    required=True,
)
@click.option(
    "--output-dir",
    '-o',
    type=click.Path(file_okay=False),
    required=True,
)
@click.option(
    "--mapping-dir",
    '-m',
    type=click.Path(file_okay=False),
    required=True,
)
@click.option(
    '--mode',
    '-x',
    required=True,
    type=click.Choice(['identifiers', 'delimiter']),
    help=(
        "Whether to recursively replace a fixed set of identifiers, or to "
        "replace all text before some delimiter in a flat set of files."
    )
)
@click.option(
    '--delimiter',
    '-d',
    default=None,
)
@click.option(
    '--identifiers',
    '-t',
    type=click.File('r'),
    default='-',
)
def main(key,
         input_dir,
         output_dir,
         mapping_dir,
         mode,
         delimiter,
         identifiers):
    """Generate a bash script and mapping to blind files."""
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    mapping_dir = Path(mapping_dir)
    mapping_dir.mkdir(parents=True, exist_ok=True)

    if mode == 'identifiers':
        identifiers = [identifier.strip() for identifier in identifiers]

        for identifier1, identifier2 in permutations(identifiers, 2):
            if identifier1 in identifier2:
                raise click.UsageException(
                    f"{identifier1} is a substring of {identifier2}"
                )

    elif mode == 'delimiter':
        if not delimiter:
            raise click.UsageException("Must specify a delimiter")

    mapping_path = mapping_dir / 'mapping.csv'
    if mapping_path.exists():
        with open(mapping_path) as mapping_file:
            mapping_reader = csv.reader(mapping_file)
            next(mapping_reader)
            mapping = {
                original: mapped
                for original, mapped in mapping_reader
            }
    else:
        mapping = {}

    identifier_mapper = IdentifierMapper(key)

    reverse_mapping = {
        mapped: original
        for original, mapped in mapping.items()
    }

    blind_script = ''
    unblind_script = ''

    if mode == 'delimiter':
        path_generator = DelimiterPathGenerator(identifier_mapper, delimiter)
    else:
        path_generator = AhoCorasickPathGenerator(
            identifier_mapper,
            identifiers
        )

    for source_path, dest_path in path_generator(input_dir, output_dir):
        blind_script += f'mv "{source_path}" "{dest_path}"\n'
        unblind_script += f'mv "{dest_path}" "{source_path}"\n'

    for identifier in path_generator.identifiers:
        mapped = identifier_mapper(identifier)
        if reverse_mapping.setdefault(mapped, identifier) != identifier:
            raise Exception(
                f"Hash collision from '{identifier}' and "
                f"'{reverse_mapping[mapped]}' to '{mapped}'"
            )
        if mapping.setdefault(identifier, mapped) != mapped:
            raise Exception(
                f"Inconsistent hash from '{identifier}' to '{mapped}' and "
                f"'{mapping[identifier]}'"
            )

    with open(mapping_dir / 'blind.sh', 'a') as out:
        out.write(path_generator.init_lines)
        out.write(blind_script)
    with open(mapping_dir / 'unblind.sh', 'a') as out:
        out.write(unblind_script)

    with open(mapping_dir / 'mapping.csv', 'w') as mapping_file:
        mapping_writer = csv.writer(mapping_file)
        mapping_writer.writerow(['original', 'blinded'])

        for identifier, mapped in sorted(mapping.items()):
            mapping_writer.writerow([
                identifier,
                mapped
            ])


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
