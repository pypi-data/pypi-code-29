from setuptools import setup, find_packages
from codecs import open as c_open
import versioneer
import os
import sys

with c_open('README.rst', 'r') as f:
    long_description = f.read()

with c_open('requirements.txt', 'r') as f:
    requires = f.read()

with c_open('LICENSE.txt', 'r') as f:
    license = f.read()

setup(
        name='epic-code',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),

        description='Another MCMC sampler for Cosmology',
        long_description=long_description,

        url='https://epic-code.readthedocs.io',
        license=license, # new BSD with clause for arXiv citation

        author='Rafael Marcondes',
        author_email='rafael.marcondes@outlook.com',

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            ],
        install_requires=requires.split(),
        packages=find_packages(),
        include_package_data=True,
        )


import shutil

root = 'EPIC'
user_folder = os.environ.get('EPIC_USER_PATH',
        os.path.join(os.path.expanduser('~'), 'EPIC'))

if not os.path.isdir(user_folder):
    os.mkdir(user_folder)
    for ini in os.listdir(root):
        if ini.endswith('.ini'):
            shutil.copy2(os.path.join(root, ini), user_folder)
    shutil.copytree(os.path.join(root, 'modifications'),
            os.path.join(user_folder, 'modifications'))

if os.name == 'posix':
    env = os.path.abspath(
            os.path.join(sys.executable, '..')
            )
    if env in os.environ['PATH'].split(os.pathsep):
        if os.environ.get('PYENV_VIRTUAL_ENV') == os.path.realpath(sys.exec_prefix):
            shutil.copy2(os.path.join(root, 'epic.py'), user_folder)
        else:
            with open(os.path.join(root, 'epic.py'), 'r') as f: 
                code = f.readlines()
            if code[0].startswith('#!'):
                code.pop(0)
            code.insert(0, '#!' + sys.executable + '\n')
            script_path = os.path.join(env, 'epic.py')
            with open(script_path, 'w') as f:
                f.write(''.join(code))
            os.chmod(script_path, 0o744)
elif sys.platform == 'win32' or os.name == 'nt':
    shutil.copy2(os.path.join(root, 'epic.py'), user_folder)

