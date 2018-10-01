# coding: utf-8

"""This module has the parser for miRBase."""

import gzip
from typing import Dict, List

from tqdm import tqdm

from pybel import BELGraph
from pybel.constants import NAMESPACE_DOMAIN_GENE
from pybel.dsl import mirna
from pybel.resources import write_namespace


def parse_mirbase(path: str) -> List[Dict]:
    """Parse miRNA data from filepath and convert it to dictionary.

    The structure of dictionary is {ID:[AC,DE,[[miRNA],[miRNA]]]}

    :param path: The path to the miRBase file
    :rtype: list[dict]
    """
    with gzip.open(path, 'r') as file:
        groups = []

        for line in file:
            line = line.decode('utf-8')

            if line.startswith('ID'):
                listnew = []
                groups.append(listnew)

            groups[-1].append(line)

        # print(groups[0][0][5:18])
        result = []
        for group in tqdm(groups, desc='parsing'):
            name = group[0][5:23].strip()
            identifier = group[2][3:-2].strip()
            description = group[4][3:-1].strip()

            entry_data = {
                'name': name,
                'description': description,
                'identifier': identifier
            }

            mature_mirna_lines = [
                i
                for i, element in enumerate(group)
                if 'FT   miRNA    ' in element
            ]

            entry_data['products'] = [
                {
                    'location': group[index][10:-1].strip(),
                    'accession': group[index + 1][33:-2],
                    'product': group[index + 2][31:-2],
                }
                for index in mature_mirna_lines
            ]

            entry_data['xrefs'] = [
                {
                    'database': '',
                    'identifier': '',
                }
            ]  # TODO @lingling93

            result.append(entry_data)

    return result


def make_bel_namespace(mirbase_list: List[Dict], file=None) -> None:
    """Make a BEL namespace with the information from miRBase."""
    values = [
        entry['name']
        for entry in mirbase_list
    ]

    write_namespace(
        namespace_name='mirbase',
        namespace_keyword='mirbase',
        namespace_domain=NAMESPACE_DOMAIN_GENE,
        author_name='',
        citation_name='',
        functions='GM',
        values=values,
        file=file,
    )


def make_bel(mirbase_list: List[Dict]) -> BELGraph:
    """Make a BEL graph with the equivalences between miRBase and other RNA databases.

    :param mirbase_list: The miRBase dictionary
    """
    result = BELGraph()

    for entry in mirbase_list:

        mirbase_node = mirna(
            namespace='mirbase',
            name=entry['name'],
            identifier=entry['identifier'],
        )

        for xref in entry['xrefs']:
            xref_node = mirna(
                namespace=xref['database'],
                identifier=xref['identifier'],
            )

            result.add_equivalence(mirbase_node, xref_node)

    return result
