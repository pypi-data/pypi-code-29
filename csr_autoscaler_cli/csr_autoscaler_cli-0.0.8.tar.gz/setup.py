from distutils.core import setup
project_name = 'csr_autoscaler_cli'
project_ver = '0.0.8'
setup(
    name=project_name,
    packages=["csr_as_cloud"],
    version=project_ver,
    description='A CLI helper for CSR1000v autoscaler on AWS',
    author='Christopher Reder',
    author_email='creder@cisco.com',
    scripts=["bin/csr_autoscaler"],
    # use the URL to the github repo
    url='https://github4-chn.cisco.com/csr1000v-cloud/autoscaler-cli.git',
    download_url='https://github4-chn.cisco.com/csr1000v-cloud/autoscaler-cli.git',
    keywords=['cisco', 'csr', 'autoscaler'],
    classifiers=[],
    license="MIT",
    install_requires=[
        'docopt'
    ],
)
