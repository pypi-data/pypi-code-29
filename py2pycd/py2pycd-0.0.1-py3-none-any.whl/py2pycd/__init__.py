"""py2pycd - transform py to pyc or pyd
Usage:
 py2pycd [options] <file>

Arguments:
 <file>             Source file or directory.

Options:
 -o FILE            Output file or directory.
 -d                 Transform py to pyd.

Examples:
 py2pycd a.py -d
 py2pycd a.py
"""
import os
import sys
import shutil
import py_compile
import subprocess

from docopt import docopt


class py2pycd(object):
    def __init__(self):
        self._base_prefix = sys.base_prefix
        self._include_path = os.path.join(self._base_prefix, 'include')
        self._libs_path = os.path.join(self._base_prefix, 'libs')
        self._lib_name = 'python{}{}'.format(sys.version_info[0], sys.version_info[1])

    def pyc(self, src_path, out_path):
        self._compile(src_path, out_path, False)

    def pyd(self, src_path, out_path):
        self._compile(src_path, out_path, True)

    def _compile(self, src_path, out_path, pyd):
        if os.path.isfile(src_path):
            if pyd:
                self._pyd_compile(src_path, out_path)
            else:
                self._pyc_compile(src_path, out_path)

        elif os.path.isdir(src_path):
            if out_path is None:
                if pyd:
                    out_path = os.path.join('.', 'dist', 'pyd')
                else:
                    out_path = os.path.join('.', 'dist', 'pyc')

            if os.path.exists(out_path):
                shutil.rmtree(out_path)

            shutil.copytree(src_path, out_path)

            for root, dirs, files in os.walk(out_path):
                for file in files:
                    file = os.path.join(root, file)
                    if pyd:
                        self._pyd_compile(file)
                    else:
                        self._pyc_compile(file)
            self._clear_py(out_path)
        else:
            raise FileNotFoundError('[-]{}'.format(src_path))

    def _clear_py(self, path):
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                if dir == '__pycache__':
                    shutil.rmtree(os.path.join(root, dir))

            for file in files:
                if file.endswith('.py') or file.endswith('.pyx'):
                    os.remove(os.path.join(root, file))

    def _pyc_compile(self, src_path, out_path=None):
        if src_path.endswith('.py'):
            if out_path is None:
                out_path = "{}c".format(src_path)
            py_compile.compile(src_path, out_path)

    def _pyd_compile(self, src_path, out_path=None):
        if src_path.endswith('.py') or src_path.endswith('.pyx'):
            if out_path is None:
                out_path = '{}d'.format(src_path)

            src_c_name = '{}.c'.format(src_path)

            cmd = 'cython "{}" -o "{}"'.format(src_path, src_c_name)
            print('[*]Run: {}'.format(cmd))
            if subprocess.call(cmd):
                raise Exception('[-]Cython error.')

            cmd = 'gcc "{}" -o "{}"'.format(src_c_name, out_path)
            cmd = '{} -I"{}" -L"{}" -l{}'.format(cmd, self._include_path, self._libs_path, self._lib_name)
            cmd = '{} -s -shared -O2 -pthread'.format(cmd)

            print('[*]Run: {}'.format(cmd))

            if subprocess.call(cmd):
                raise Exception('[-]gcc error.')

            os.remove(src_c_name)


def main():
    args = docopt(__doc__)
    src_path = args['<file>']
    out_path = args['-o']

    if args['-d']:
        py2pycd().pyd(src_path, out_path)
    else:
        py2pycd().pyc(src_path, out_path)


if __name__ == '__main__':
    main()
