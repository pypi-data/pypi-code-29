class tree:
    def __init__(self):
        import os

        '''Создание основного дерева проекта'''

        full_dir = os.getcwd()
        full_dir_splitted = full_dir.split('\\')
        name = full_dir_splitted[len(full_dir_splitted)-1]
        dir_list = ['scripts', 'docs', name, 'tests']
        for folder in dir_list:
            os.mkdir(folder)

        file = open('README.md', 'w')
        file.close()

        file = open('LICENSE.txt', 'w')
        file.close()

        '''Создание файла setup.py с шаблоном'''

        file = open('setup.py', 'w')
        file.write('import setuptools\n'
                   '\n'
                   'with open("README", 'r') as f:'
                   '\n    long_description = f.read()\n'
                   '\n'
                   'setuptools.setup(\n'
                   f'    name=\'{name}\',\n'
                   '    version=\'1.0\',\n'
                   '    description=\' D E S C R I P T I O N\',\n'
                   '    license="MIT",\n'
                   '    long_description=long_description,\n'
                   f'    author=\'Man {name}\',\n'
                   f'    author_email=\'{name}mail@{name}.com\',\n'
                   f'    url="http://www.{name}package.com/",\n'
                   f'    packages=[\'{name}\'],  #same as name\n'
                   '    install_requires=["setuptools"], #external packages as dependencies\n'
                   '    scripts=[]  #\'scripts/cool\',\n'
                   ')\n'
                   )
        file.close()

        os.chdir(f'{full_dir}\\{name}')
        file = open('__init__.py', 'w')
        file.write(f'name = {name}')
        file.close()

        os.chdir(f'{full_dir}\\tests')
        file = open('__init__.py', 'w')
        file_temp = open(f'{name}_tests.py', 'w')
        file.close()
        file_temp.close()
        print(f'{name}/\n'
              f'    ├──{name}/\n'
              '    │  └──__init__.py\n'
              '    ├──docs/\n'
              '    ├──scripts/\n'
              '    ├──tests/\n'
              '    │  ├──__init__.py\n'
              f'    │  └──{name}_tests.py\n'
              '    ├──README.md\n'
              '    ├──MANIFEST.in\n'
              '    ├──LICENSE.txt\n'
              '    └──setup.py\n')

