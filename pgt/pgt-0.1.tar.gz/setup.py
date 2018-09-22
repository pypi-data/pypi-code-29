from setuptools import setup, find_packages

setup(
    name='pgt',
    version='0.1',
    description=(
        'A pages generate tool.'
    ),
    author='Maintainer1',
    author_email='ltaoist@163.com',
    license='PEP License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/Maintainer1/python-pgt',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Console',
		'Environment :: Web Environment',
        'Intended Audience :: Developers'
    ],
	entry_points={
        'console_scripts': [
            'pgt = pgt.cli:main'
        ]
    }
)
