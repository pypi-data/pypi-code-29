import click
import os
import pytest
import vgstash
import vgstash_cli

from click.testing import CliRunner

verbose = True

def test_init():
    runner = CliRunner()
    result = runner.invoke(vgstash_cli.cli, ['init'])
    if verbose:
        print(result.output)
    assert result.exit_code == 0
    assert result.output == "Initializing the database...\nSchema created.\n"

def test_add_minimum():
    runner = CliRunner()
    result = runner.invoke(vgstash_cli.cli, ['add', 'Super Mario Bros.', 'NES'])
    if verbose:
        print(result.output)
    assert result.exit_code == 0
    assert result.output == "Added Super Mario Bros. for NES. You physically own it and are playing it.\n"

def test_add_ownership():
    runner = CliRunner()
    result = runner.invoke(vgstash_cli.cli, ['add', 'The Legend of Zelda', 'NES', 'd'])
    if verbose:
        print(result.output)
    assert result.exit_code == 0
    assert result.output == "Added The Legend of Zelda for NES. You digitally own it and are playing it.\n"

def test_add_typical():
    runner = CliRunner()
    result = runner.invoke(vgstash_cli.cli, ['add', 'Sonic the Hedgehog 2', 'Genesis', '0', '3'])
    if verbose:
        print(result.output)
    assert result.exit_code == 0
    assert result.output == "Added Sonic the Hedgehog 2 for Genesis. You do not own it and have beaten it.\n"

def test_add_full():
    runner = CliRunner()
    result = runner.invoke(vgstash_cli.cli, ['add', 'Vectorman', 'Genesis', 'u', 'b', 'beep'])
    if verbose:
        print(result.output)
    assert result.exit_code == 0
    assert result.output == "Added Vectorman for Genesis. You do not own it and have beaten it. It also has notes.\n"

def test_add_full_note_with_newline():
    runner = CliRunner()
    result = runner.invoke(vgstash_cli.cli, ['add', 'Vectorman 2', 'Genesis', 'p', 'p', 'beep\nboop'])
    if verbose:
        print(result.output)
    assert result.exit_code == 0
    assert result.output == "Added Vectorman 2 for Genesis. You physically own it and are playing it. It also has notes.\n"

def test_list():
    runner = CliRunner()
    result = runner.invoke(vgstash_cli.list_games, ['--raw'])
    if verbose:
        print(result.output)
    assert result.exit_code == 0
    assert result.output == '\n'.join((
        'Sonic the Hedgehog 2|Genesis|0|3|',
        'Vectorman|Genesis|0|3|beep',
        'Vectorman 2|Genesis|1|2|beep\\nboop',
        'Super Mario Bros.|NES|1|2|',
        'The Legend of Zelda|NES|2|2|\n',
    ))

def test_list_filter():
    runner = CliRunner()
    result = runner.invoke(vgstash_cli.cli, ['list', '-r', 'playlog'])
    if verbose:
        print(result.output)
    assert result.exit_code == 0
    assert result.output == '\n'.join((
        'Vectorman 2|Genesis|1|2|beep\\nboop',
        'Super Mario Bros.|NES|1|2|',
        'The Legend of Zelda|NES|2|2|\n',
    ))

def test_list_pretty():
    runner = CliRunner()
    result = runner.invoke(vgstash_cli.cli, ['list', '-w', '80'])
    if verbose:
        print(result.output)
    assert result.exit_code == 0
    assert result.output == '\n'.join((
        ' ID  | Title                                         | System   | Own | Status ',
        '--------------------------------------------------------------------------------',
        '   3 | Sonic the Hedgehog 2                          | Genesis  |     |       C',
        '   4 | Vectorman                                     | Genesis  |     |       C',
        '   5 | Vectorman 2                                   | Genesis  | P   |     B  ',
        '   1 | Super Mario Bros.                             |   NES    | P   |     B  ',
        '   2 | The Legend of Zelda                           |   NES    |   D |     B  \n'
    ))

def test_list_pretty_smaller():
    runner = CliRunner()
    result = runner.invoke(vgstash_cli.cli, ['list', '-w', '60'])
    if verbose:
        print(result.output)
    assert result.exit_code == 0
    assert result.output == '\n'.join((
        ' ID  | Title                     | System   | Own | Status ',
        '------------------------------------------------------------',
        '   3 | Sonic the Hedgehog 2      | Genesis  |     |       C',
        '   4 | Vectorman                 | Genesis  |     |       C',
        '   5 | Vectorman 2               | Genesis  | P   |     B  ',
        '   1 | Super Mario Bros.         |   NES    | P   |     B  ',
        '   2 | The Legend of Zelda       |   NES    |   D |     B  \n'
    ))

def test_list_pretty_tiny():
    runner = CliRunner()
    result = runner.invoke(vgstash_cli.cli, ['list', '-w', '50'])
    if verbose:
        print(result.output)
    assert result.exit_code == 0
    assert result.output == '\n'.join((
        ' ID  | Title           | System   | Own | Status ',
        '--------------------------------------------------',
        '   3 | Sonic the Hedge | Genesis  |     |       C',
        '   4 | Vectorman       | Genesis  |     |       C',
        '   5 | Vectorman 2     | Genesis  | P   |     B  ',
        '   1 | Super Mario Bro |   NES    | P   |     B  ',
        '   2 | The Legend of Z |   NES    |   D |     B  \n'
    ))
