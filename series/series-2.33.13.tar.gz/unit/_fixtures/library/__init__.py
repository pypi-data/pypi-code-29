from amino.test import temp_dir, create_temp_file
from golgi import Config
from golgi.config.options import PathListConfigOption


def _filename(name, season, episode):
    return '{}_{}x{}.mkv'.format(name, season, episode)


def create_episodes(collection_names, filenames):
    base = temp_dir('library', 'collections')
    collections = [temp_dir(base, name) for name in collection_names]
    templ = '{name}/{season}/{name}_{season}x{episode}.{ext}'
    Config.override('library', collection_paths=PathListConfigOption(collections),
                    path_template=templ)
    episodes = [create_temp_file(collections[i], name, str(season),
                                 _filename(name, season, episode))
                for name, season, episode, i in filenames]
    return collections, episodes


def create_movies(collection_name, filenames):
    collection = temp_dir('library', 'collections', collection_name)
    Config.override('library', movie_collection_paths=[collection])
    movies = [create_temp_file(collection, _file) for _file in filenames]
    return collection, movies

__all__ = ['create_episodes', 'create_movies']
