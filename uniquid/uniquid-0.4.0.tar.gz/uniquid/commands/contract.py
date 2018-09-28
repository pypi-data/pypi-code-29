# Copyright (c) 2018 UniquID

import click
import json
from uniquid.core.login_manager import LoginManager
from uniquid.core.cli_console import CliConsole
from uniquid.core.contracts import Contracts
import uniquid.core.constants as constants
import uniquid.commands.common as common


@click.command(name='create-contracts')
@click.option('--input-json',
              default=None,
              type=click.STRING,
              help=('JSON object describing the contract.'),
              required=False)
@click.option('--input-json-file',
              default=None,
              type=click.File(mode='r'),
              help=('Path to file containing a list of JSON'
                    ' contract objects.'),
              required=False)
def create_contracts(input_json, input_json_file):
    """Create a new contract."""
    if (input_json is None) == (input_json_file is None):
        raise click.ClickException(constants.ERR_SINGLE_OPTION)
    cc = CliConsole(click.echo, common.print_error,
                    constants.FORMAT_TEXT, click.ClickException,
                    click.confirm, click.prompt)
    lm = LoginManager(cc)
    contracts = Contracts(cc, lm)
    json_string = input_json
    if input_json_file:
        json_string = input_json_file.read()
    contracts.create_contracts(json_string)


@click.command(name='list-contracts')
@click.option('--output',
              default=constants.FORMAT_TEXT,
              type=click.Choice(constants.FORMAT_ALL),
              help=('Format used to print data to the console. Valid options'
                    ' are: ') + str(constants.FORMAT_ALL),
              required=False)
def list_contracts(output):
    """Show a list of all the contracts."""
    cc = CliConsole(click.echo, common.print_error,
                    output, click.ClickException,
                    click.confirm, click.prompt)
    lm = LoginManager(cc)
    contracts = Contracts(cc, lm)
    contracts.list_contracts()


@click.command(name='show-contract')
@click.argument('txid', nargs=1)
@click.option('--output',
              default=constants.FORMAT_TEXT,
              type=click.Choice(constants.FORMAT_ALL),
              help=('Format used to print data to the console. Valid options'
                    ' are: ') + str(constants.FORMAT_ALL),
              required=False)
def show_contract(txid, output):
    """Show a single contract, identified by transaction TXID."""
    cc = CliConsole(click.echo, common.print_error,
                    output, click.ClickException,
                    click.confirm, click.prompt)
    lm = LoginManager(cc)
    contracts = Contracts(cc, lm)
    contracts.show_contract(txid)


@click.command(name='delete-contracts')
@click.argument('txids', nargs=-1)  # variadic
@click.option('--input-json',
              default=None,
              type=click.STRING,
              help=('JSON array with TXIDs of contracts to be deleted.'),
              required=False)
@click.option('--input-json-file',
              default=None,
              type=click.File(mode='r'),
              help=('Path to file containing a JSON array of the TXIDs'
                    ' of the contracts to be deleted.'),
              required=False)
def delete_contracts(txids, input_json, input_json_file):
    """Delete all of the contracts which are identified by their
        transaction IDs being in the argument list TXIDS."""
    if ((input_json is None) == (input_json_file is None) and
            (txids is None or len(txids) == 0)):
        raise click.ClickException(constants.ERR_SINGLE_OPTION)
    cc = CliConsole(click.echo, common.print_error,
                    constants.FORMAT_TEXT, click.ClickException,
                    click.confirm, click.prompt)
    lm = LoginManager(cc)
    contracts = Contracts(cc, lm)
    json_string = input_json
    if input_json_file:
        json_string = input_json_file.read()
    # if user passed one+ arguments, these take priority over a JSON array.
    if(len(txids) > 0):
        txid_list = list()
        for txid in txids:
            txid_list.append(str(txid))
        json_string = json.dumps(txid_list)
    contracts.delete_contract(json_string)
