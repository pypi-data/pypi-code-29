from distutils.core import setup

setup(
    name='ADLoginValidation',
    version='0.1',
    packages=['adloginvalidation',],
    license='MIT',
    author='Igor Bichara',
    author_email='igorbacoutinho@gmail.com',
    keywords='microsoft adfs login token validation',
    url='https://gitlab.com/ibichara/adloginvalidation',
    install_requires=['flask'],
    python_requires='>=3',
    long_description=open('README.txt').read(),
)
