import click
from click_plugins import with_plugins
from pkg_resources import iter_entry_points


@with_plugins(iter_entry_points('mli.plugins'))
@click.group()
def mli():
    pass


if __name__ == '__main__':
    mli()
