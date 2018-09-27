from setuptools import setup, find_packages

NAME = 'eroepub'
PACKAGES = [NAME] + ["{}.{}".format(NAME, i) for i in find_packages(NAME)]

config = {
    'description': 'Transform EroManga from dir to epub.',
    'author': 'Pandaria',
    # 'url': 'URL to get it at.',
    # 'download_url': 'https://example.com/eropub.zip',
    'author_email': 'pandaria98f@gmail.com',
    'version': '0.3',
    'install_requires': ['Pillow'],
    'packages': PACKAGES,
    'scripts': [],
    'entry_points': {
        'console_scripts': [
            'EroManga2Epub=eroepub.main:main',
        ]
    },
    'name': 'EroManga2Epub',
}

setup(**config)
