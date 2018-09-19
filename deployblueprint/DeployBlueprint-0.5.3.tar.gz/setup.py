from setuptools import *

with open('requirements.txt') as f_required:
    required = f_required.read().splitlines()
with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
	name='DeployBlueprint',
	version='0.5.3',
	py_modules=['DeployBlueprint'],
	packages=find_packages(),
	install_requires=required,
	long_description=long_description,
    long_description_content_type="text/markdown",
	author="graboskyc",
	author_email="chris@grabosky.net",
	description="A small and basic package to create AWS instances and Atlas clusters with basic task management.",
    url="https://github.com/graboskyc/DeployBlueprint",
	entry_points='''
		[console_scripts]
		DeployBlueprint=DeployBlueprint:cli
	''',
)