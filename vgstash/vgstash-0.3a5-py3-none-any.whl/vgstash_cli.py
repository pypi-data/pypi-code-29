import vgstash
import sqlite3
import click
import os
import sys

from shutil import get_terminal_size

def get_db():
    """Fetch a vgstash DB object from the default location.

    Change DEFAULT_CONFIG['db_location'] before calling this function
    to alter behavior."""
    return vgstash.DB(vgstash.DEFAULT_CONFIG['db_location'])


@click.group('vgstash')
def cli():
    pass


@cli.command()
def init():
    db = get_db()
    click.echo("Initializing the database...")
    if db.create_schema():
        click.echo("Schema created.")
    else:
        raise sqlite3.OperationalError("Cannot create schema.")

def row_format(row, width, header):
    """
    TODO
    """
    # There's another way to do this, involving gathering the entire results and
    # *then* formatting them. That is incredibly wasteful of resources imo, so
    # it may need some testing to see if it's better.  Ideally, we'd only make
    # the table as wide as needed; that can't happen unless we know the longest
    # title's length...

    twidth = int(width) - 35
    if header == True:
        click.echo("{:^4s} | {:<{w}s} | {:<8s} | {:^3s} | {:<7s}".format(
            "ID",
            "Title",
            "System",
            "Own",
            "Status",
            w=twidth)
        )
        click.echo("-" * int(width))

    gidstr = "{: >4d}".format(row['rowid'])
    titlestr = "{: <{w}s}".format(row['title'][:twidth], w=twidth)
    systemstr = "{: ^8s}".format(row['system'][:8])
    # unowned, physical, digital, both
    ownltr = [' ', 'P', '  D', 'P D']
    ownstr = "{: <3s}".format(ownltr[row['ownership']])
    statltr = {
        -1: 'U',
        0: 'N',
        1: 'P',
        2: 'B',
        3: 'C'
    }
    statstr = "{: <7s}".format((" " * row['progress'] * 2) + statltr[row['progress']])
    print(" | ".join((gidstr, titlestr, systemstr, ownstr, statstr)))

@cli.command('add')
@click.argument('title', type=str)
@click.argument('system', type=str)
@click.argument('ownership', type=str, required=False, default=vgstash.DEFAULT_CONFIG['ownership'])
@click.argument('progress', type=str, required=False, default=vgstash.DEFAULT_CONFIG['progress'])
@click.argument('notes', type=str, required=False, default="")
def add(title, system, ownership, progress, notes):
    db = get_db()
    game = vgstash.Game(title, system, ownership, progress, notes)
    try:
        db.add_game(game, update=False)
        own_clause = (
            "do not own",
            "physically own",
            "digitally own",
            "digitally and physically own",
        )
        progress_clause = (
            "cannot beat",
            "haven't started",
            "are playing",
            "have beaten",
            "have completed",
        )
        note_clause = "" if len(game.notes) == 0 else " It also has notes."
        click.echo("Added {} for {}. You {} it and {} it.{}".format(
            game.title,
            game.system,
            own_clause[game.ownership],
            progress_clause[game.progress],
            note_clause,
        ))
    except sqlite3.IntegrityError as e:
        print(e)
        click.echo("Couldn't add game.")


@cli.command('list')
@click.argument('filter', required=False, default="allgames")
@click.option('--raw', '-r', is_flag=True, show_default=True, default=False, help="Output raw, pipe-delimited lines")
@click.option('--width', '-w', type=str, required=False, default=get_terminal_size(fallback=(80,24)).columns, help="The width of the table to output, in characters.")
def list_games(filter, raw, width):
    db = get_db()
    res = db.list_games(filter)
    first_pass = True
    for r in res:
        if 'notes' in r.keys() and len(r['notes']) > 0:
            notes = r['notes'].replace('\n', '\\n')
            notes = notes.replace('\r', '\\r')
        else:
            notes = ''

        if raw:
            click.echo("|".join((
                r['title'],
                r['system'],
                str(r['ownership']),
                str(r['progress']),
                notes
            ))
            )
        else:
            row_format(r, width, first_pass)
            first_pass = False
