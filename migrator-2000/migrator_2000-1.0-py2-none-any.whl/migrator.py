import glob
import logging
import uuid
from pathlib import Path

import click

from entities.table import Table
from libs.database import *
from libs.servers import *
from libs.utils import comment

logging.basicConfig(format='%(levelname)s | %(message)s', level=logging.INFO)


def dump_tables(database, tables, output, ssh=None):
    comment('DUMPING TABLES')
    for table in tables:
        logging.info('Dumping table ' + table.name + '...')
        if ssh is not None:
            dump_table_ssh(ssh, database, table, output)
        else:
            dump_table(database, table, output)


def import_files(database, files_directory, ssh=None):
    comment('IMPORTING TABLES')
    files = glob.glob(files_directory + '/*.sql.gz')
    for gz in files:
        logging.info('Importing file ' + gz + '...')
        if ssh is not None:
            import_sql_ssh(ssh, database, gz, files_directory)
        else:
            import_sql(database, gz, files_directory)


@click.command()
@click.option('--mysql/--ssh', default=False, help="Method for dumping and importing datas.")
@click.argument('servera', type=click.Path(exists=True))
@click.argument('serverb', type=click.Path(exists=True))
@click.argument('structure', type=click.Path(exists=True))
def command(servera, serverb, structure, mysql):
    output_path = 'tmp/' + str(uuid.uuid1())
    Path(output_path).mkdir(parents=True)

    structure = get_config(structure)

    table_list = []
    for tables_json in structure:
        for table_str in tables_json['name'].split(' '):
            table_list.append(Table(table_str, tables_json['where']))

    if mysql:
        dump_tables(get_server(servera).database, table_list, output_path)
        import_files(get_server(serverb).database, output_path)
    else:
        dump_tables(get_server(servera).database, table_list, output_path, get_server(servera).ssh)
        import_files(get_server(serverb).database, output_path, get_server(serverb).ssh)


if __name__ == '__main__':
    command()
