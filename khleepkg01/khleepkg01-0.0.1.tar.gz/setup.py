import io
from setuptools import setup, find_packages

version = "0.0.1"

with io.open('./README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name            = "khleepkg01",
    version         = version,
    description     = "SSL-Seminar-test repository:: Topic - Package Test and Deployment",
    long_description= readme,
    long_description_content_type="text/markdown",
    author          = "Keon-Hee Lee",
    author_email    = "beta1360@naver.com",
    url             = "https://github.com/KeonHeeLee/ssl-lab-test",
    download_url    = "https://github.com/KeonHeeLee/ssl-lab-test/archive/v1.0.0.tar.gz",
    install_requires= [],
    packages        = find_packages(exclude=['test*']),
    keywords        = ['Test', 'TDD', 'Deployment', 'Seminar'],
    python_requires = '>=3',
    zip_safe        = False,
    license         = 'MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License'
    ]
)