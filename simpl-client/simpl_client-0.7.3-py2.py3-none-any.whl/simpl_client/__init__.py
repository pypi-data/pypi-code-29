_version = "0.7.3"
__version__ = VERSION = tuple(map(int, _version.split('.')))


from .games_client import GamesAPIClient  # noqa
