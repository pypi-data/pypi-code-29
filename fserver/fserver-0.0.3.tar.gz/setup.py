from setuptools import setup

setup(
    name='fserver',
    version='0.0.3',
    description='a simple http.server implement by flask',
    url='https://github.com/Carrotor116/fserver',
    author='Nonu',
    author_email='1162365377@qq.com',
    license='MIT',
    packages=['fserver'],
    install_requires=['Flask >= 1.0.2'],
    package_data={
    	'': ['templates/*.html', 'LICENSE', 'README.md']
    },
    entry_points={
        'console_scripts': [
            'fserver=fserver:run'
        ]
    }
)