# -*- coding: utf-8 -*-

"""Console script for adstxt."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for adstxt."""
    click.echo("https://adstxt.readthedocs.io")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
