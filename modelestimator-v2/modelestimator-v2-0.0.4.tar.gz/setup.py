import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()
	
setuptools.setup(
	name='modelestimator-v2',
	version='0.0.4',
	author='Ruben Ridderström',
	author_email='ruben.ridderstrom@gmail.com',
	description='Program for estimating amino acid replacement rates',
	long_description=long_description,
	long_description_content_type="text/plain; charset=UTF-8",
	url='https://github.com/RubenRidderstrom/modelestimator',
	license='GPLv3',
	packages = setuptools.find_packages(),
	entry_points={
		'console_scripts':[
			'modelestimator = modelestimator.main:main'
		]
	},
	install_requires=[
	"scipy",
	"numpy",
	"biopython"
	],
	setup_requires=['pytest-runner'],
	tests_require=['pytest']
	)