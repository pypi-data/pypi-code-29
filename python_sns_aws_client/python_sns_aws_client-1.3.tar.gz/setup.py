import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()
setuptools.setup(
    name='python_sns_aws_client',
    packages=setuptools.find_packages(),
    version='1.3',
    description='use boto3 for send and receive sns-topic',
    author='Zinobe',
    author_email='udgottschalk@gmail.com',
    url='https://gitlab.com/Udalbert/python-sns-aws-python',
    download_url='https://gitlab.com/Udalbert/python-sns-aws-python/tags/1.3',
    keywords=['boto3-python', 'sns-topic', 'aws-sns'],
    classifiers=[
        "Programming Language :: Python",
    ],
)
