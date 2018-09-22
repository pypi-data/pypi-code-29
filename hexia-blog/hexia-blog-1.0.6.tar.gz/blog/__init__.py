__version__ = (1, 0 , 6)

def get_version():
    return '.'.join(map(str, __version__))

default_app_config = 'blog.config.BlogConfig'