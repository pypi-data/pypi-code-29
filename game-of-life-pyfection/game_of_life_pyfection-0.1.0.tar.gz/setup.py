from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')


setup(
    name='game_of_life_pyfection',
    version='0.1.0',
    description=readme,
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    author="Michael Livshits",
    author_email='livsmichael@gmail.com',
    url='https://github.com/Michaelliv/game_of_life_pyfection',
    packages=['game_of_life_pyfection'],
    package_dir={'game_of_life_pyfection':
                 'game_of_life_pyfection'},
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='game_of_life_pyfection',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
)
