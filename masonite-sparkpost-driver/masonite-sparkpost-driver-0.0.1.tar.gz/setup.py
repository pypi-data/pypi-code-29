from setuptools import setup

setup(
    name="masonite-sparkpost-driver",
    packages=[
        'masonite.contrib.sparkpost',
        'masonite.contrib.sparkpost.drivers',
        'masonite.contrib.sparkpost.providers',
    ],
    version='0.0.1',
    install_requires=[
        'sparkpost',
    ],
    classifiers=[],
    author='Bjorn Theart',
    author_email='bjorntheart@gmail.com',
    url='https://github.com/bjorntheart/masonite-sparkpost-driver',
    description='Sparkpost mail driver for the Masonite framework',
    keywords=['python web framework', 'python3', 'masonite', 'sparkpost'],
    include_package_data=True,
)
