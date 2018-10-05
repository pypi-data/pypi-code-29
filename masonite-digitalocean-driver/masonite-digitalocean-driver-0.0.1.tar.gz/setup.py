from setuptools import setup

setup(
    name="masonite-digitalocean-driver",
    packages=[
        'masonite.contrib.digitalocean',
        'masonite.contrib.digitalocean.drivers',
        'masonite.contrib.digitalocean.providers',
    ],
    version='0.0.1',
    install_requires=[
        'boto3',
    ],
    classifiers=[],
    author='Bjorn Theart',
    author_email='bjorntheart@gmail.com',
    url='https://github.com/bjorntheart/masonite-digitalocean-driver',
    description='DigitalOcean upload driver for the Masonite framework',
    keywords=['python web framework', 'python3', 'masonite', 'digitalocean'],
    include_package_data=True,
)
