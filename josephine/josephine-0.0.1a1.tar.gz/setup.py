
import os
import sys
from setuptools import setup, find_packages


# (
#    (Major, Minor, [Micros]),
#    [(releaselevel, serial)],
# )
#__version_info__ = ((1, 0, 0),)
#__version_info__ = ((1, 0, 0),(rc,))
#__version_info__ = ((1, 0, 0),(rc,1))
__version_info__ = ((0, 0, 1), ('a', 1))


readme = os.path.normpath(os.path.join(__file__, '..', 'README.md'))
with open(readme, 'r') as fh:
    long_description = fh.read()

# long_description += '\n\n'
# changelog = os.path.normpath(os.path.join(__file__, '..', 'CHANGELOG.md'))
# with open(changelog, 'r') as fh:
#     long_description += fh.read()


def get_version():
    global __version_info__
    return (
        '.'.join(str(x) for x in __version_info__[0])
        + ''.join(str(x) for x in __version_info__[1])
    )


setup(
    name='josephine',
    version=get_version(),
    description='Maya Animation Studio Pipeline',
    long_description=long_description,
    url='https://gitlab.com/kabaretstudio/kabaret.josephine',
    author='Damien "dee" Coureau',
    author_email='dee909@gmail.com',
    license='LGPLv3+',
    classifiers=[
        'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',

        'Topic :: Desktop Environment :: File Managers',
        'Topic :: Multimedia :: Graphics',

        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 2.7',

        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
    ],
    keywords='maya animation pipeline dataflow workflow asset manager',
    install_requires=[
        'kabaret',
    ],
    python_requires='~=2.7',
    packages=find_packages('python'),
    package_dir={'': 'python'},
    package_data={
        '': ['*.css', '*.png', '*.svg', '*.gif'],
    },
)
