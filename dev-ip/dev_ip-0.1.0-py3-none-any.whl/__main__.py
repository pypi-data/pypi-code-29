import click
from devip import get_ip_addresses


@click.command()
@click.option('--all', '-a', is_flag=True, help='List all IP addresses.')
@click.option('--reverse', '-r', is_flag=True, help='List in reverse order.')
@click.option('--loopback', '-l', is_flag=True, help='Include loopback.')
def devip(all, reverse, loopback):
    """
    Find a suitable IP host to access local network-based applications.
    """
    addresses = get_ip_addresses(loopback)
    if not addresses:
        click.echo('No IP addresses where found.', err=True)
        return 1
    if reverse:
        addresses = reversed(addresses)
    if all:
        click.echo('\n'.join(addresses))
    else:
        click.echo(addresses[0])


if __name__ == '__main__':
    devip()
