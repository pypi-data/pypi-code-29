import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# Add external dependencies using"
# install_requires
# specify version
# package>=#.#
	
setuptools.setup(
	name='sciMove',
	version='0.0.1',
	author='Becca Robins',
	author_email='becca.k.robins@gmail.com',
	description='A package for analyzing whole-body movement in humans.',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/beccarobins/sciMove',
	packages=setuptools.find_packages(),
	classifiers=[
	'Programming Language :: Python :: 3', 
	'License :: OSI Approved :: MIT License', 
	'Operating System :: OS Independent',
	'Intended Audience :: Science/Research', 
	'Development Status :: 1 - Planning'],
)


#	license="MIT"
#install_requires=['']
#packages=['eyeMove'])
#include_package_data=True,
#zip_safe=False)
